import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict, Optional

# Assuming google-generativeai might raise specific exceptions
# We'll create a placeholder for now, actual exception type might differ
try:
    from google.api_core import exceptions as google_exceptions
except ImportError:
    # Placeholder if the exact exception isn't critical for this task's structure
    class google_exceptions:
        PermissionDenied = type("PermissionDenied", (Exception,), {})
        GoogleAPIError = type("GoogleAPIError", (Exception,), {})


from orchestrator import Orchestrator, AppStates
from file_generator import create_project_structure_and_files # Added for bootstrap generation

# --- Setup Logging ---
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO) # Configure basic logging

# --- Custom Exceptions ---
class OrchestratorError(Exception):
    """Custom exception for orchestrator specific errors."""
    def __init__(self, message: str, error_code: str = "ORCHESTRATOR_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

class GeminiAPIError(Exception):
    """Custom exception for Gemini API related errors."""
    def __init__(self, message: str, error_code: str = "GEMINI_API_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

# --- Pydantic Models ---

class StartRequest(BaseModel):
    project_name: str

class StartResponse(BaseModel):
    status: str
    project_name: str
    current_state: str
    message: str

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    user_message: str
    ai_response: str
    current_state: str
    history_length: int
    is_approval_step: bool = False

class ApproveResponse(BaseModel):
    status: str
    new_state: str
    message: str

class GenerateFilesResponse(BaseModel):
    status: str
    message: str

# --- FastAPI App Instance ---
app = FastAPI(
    title="Planejador Gemini-Flow API",
    description="API para gerenciar o fluxo de planejamento de projetos com Gemini.",
    version="0.1.0"
)

orchestrator = Orchestrator()

# --- Exception Handlers ---

@app.exception_handler(OrchestratorError)
async def orchestrator_exception_handler(request: Request, exc: OrchestratorError):
    logger.error(f"OrchestratorError: {exc.message} (Code: {exc.error_code})", exc_info=True)
    return JSONResponse(
        status_code=400, # Bad Request, could be 500 depending on the error nature
        content={"detail": exc.message, "error_code": exc.error_code},
    )

@app.exception_handler(GeminiAPIError)
async def gemini_api_exception_handler(request: Request, exc: GeminiAPIError):
    logger.error(f"GeminiAPIError: {exc.message} (Code: {exc.error_code})", exc_info=True)
    return JSONResponse(
        status_code=502, # Bad Gateway, as it's an upstream API error
        content={"detail": exc.message, "error_code": exc.error_code},
    )

@app.exception_handler(google_exceptions.PermissionDenied)
async def google_permission_denied_handler(request: Request, exc: google_exceptions.PermissionDenied):
    logger.error(f"Google API Permission Denied: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=502,
        content={"detail": "Falha de permissão ao acessar a API do Google.", "error_code": "GOOGLE_PERMISSION_DENIED"},
    )

@app.exception_handler(google_exceptions.GoogleAPIError) # Generic Google API error
async def google_api_error_handler(request: Request, exc: google_exceptions.GoogleAPIError):
    logger.error(f"Google API Error: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=502,
        content={"detail": "Erro na comunicação com a API do Google.", "error_code": "GOOGLE_API_ERROR"},
    )

@app.exception_handler(HTTPException)
async def http_exception_handler_custom(request: Request, exc: HTTPException):
    # This will handle FastAPI's own HTTPErrors if not caught by more specific handlers
    # It allows logging them or standardizing the response further if needed.
    # FastAPI's default handler for HTTPException already returns JSON.
    logger.error(f"HTTPException: Status: {exc.status_code}, Detail: {exc.detail}", exc_info=False) # exc_info might be too verbose for standard HTTPExceptions
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "error_code": "HTTP_EXCEPTION"}, # Optionally add a generic error code
        headers=exc.headers
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Ocorreu um erro interno inesperado no servidor.", "error_code": "INTERNAL_SERVER_ERROR"},
    )

# --- API Endpoints ---

@app.post("/start", response_model=StartResponse)
async def start_session(request: StartRequest):
    try:
        session_data = orchestrator.start_new_session(project_name=request.project_name)
        # Get the first AI message by sending a predefined initial prompt
        initial_ai_interaction = orchestrator.process_user_message("Olá! Vamos começar o planejamento do projeto.")

        return StartResponse(
            status=session_data["status"],
            project_name=session_data["project_name"],
            current_state=session_data["current_state"],
            message=initial_ai_interaction["ai_response"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao iniciar sessão: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
async def chat_with_assistant(request: ChatRequest):
    try:
        response_data = orchestrator.process_user_message(user_message=request.user_message)

        return ChatResponse(
            user_message=response_data["user_message"],
            ai_response=response_data["ai_response"],
            current_state=response_data["current_state"],
            history_length=response_data["history_length"],
            is_approval_step=response_data["is_approval_step"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no chat: {str(e)}")

@app.post("/approve", response_model=ApproveResponse)
async def approve_phase():
    try:
        current_state_before_approve = orchestrator.session.current_state
        next_state_map = {
            AppStates.PLANNING: AppStates.ISSUES,
            AppStates.ISSUES: AppStates.DEVOPS,
            AppStates.DEVOPS: None
        }

        next_state_enum = next_state_map.get(current_state_before_approve)

        if next_state_enum:
            change_response = orchestrator.change_phase(next_state_enum.name)
            # Get the first AI message for the new phase
            new_phase_initial_interaction = orchestrator.process_user_message(f"Ok, aprovei a fase anterior. O que faremos em {next_state_enum.value}?")

            return ApproveResponse(
                status=change_response["status"],
                new_state=change_response["new_state"],
                message=new_phase_initial_interaction["ai_response"]
            )
        elif current_state_before_approve == AppStates.DEVOPS:
            return ApproveResponse(
                status="phase_approved_ready_to_generate",
                new_state=current_state_before_approve.value,
                message="Fase DEVOPS aprovada. Você pode agora gerar os arquivos do projeto através do endpoint /generate_files."
            )
        else:
            raise HTTPException(status_code=400, detail="Não há próxima fase definida ou estado atual inválido para aprovação.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao aprovar fase: {str(e)}")

@app.post("/generate_files", response_model=GenerateFilesResponse)
async def generate_project_files():
    try:
        if orchestrator.session is None or not orchestrator.session.project_name:
            raise HTTPException(status_code=400, detail="Nenhuma sessão de projeto ativa. Inicie um projeto primeiro.")

        if orchestrator.session.current_state == AppStates.DEVOPS:
            project_name = orchestrator.session.project_name
            output_dir = create_project_structure_and_files(project_name)

            # Here you would typically add other files to 'output_dir'
            # For example, content from orchestrator.session.phases_data
            # For now, only bootstrap.sh is created by create_project_structure_and_files

            return GenerateFilesResponse(
                status="files_generated_successfully",
                message=f"Arquivos do projeto '{project_name}', incluindo bootstrap.sh, foram gerados em: {output_dir}"
            )
        else:
            return GenerateFilesResponse(
                status="not_ready_for_generation",
                message=f"O projeto não está na fase DEVOPS finalizada para gerar arquivos. Estado atual: {orchestrator.session.current_state.value if orchestrator.session else 'N/A'}"
            )
    except HTTPException as e:
        raise e # Re-raise HTTPException directly
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar arquivos: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": app.version}
