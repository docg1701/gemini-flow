from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, Optional

from backend.orchestrator import Orchestrator, AppStates

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

        is_approval_step = False # Placeholder: Logic to determine this should be in Orchestrator
        # Example: if orchestrator.session.requires_approval_now(): is_approval_step = True

        return ChatResponse(
            user_message=response_data["user_message"],
            ai_response=response_data["ai_response"],
            current_state=response_data["current_state"],
            history_length=response_data["history_length"],
            is_approval_step=is_approval_step
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
        # This logic ideally belongs in the orchestrator.
        # orchestrator.prepare_for_generation() / orchestrator.generate_files()
        if orchestrator.session.current_state == AppStates.DEVOPS: # Simplified check
            # Actual file generation logic is missing in Orchestrator.py
            # For now, returning a success message.
            # project_files_data = orchestrator.generate_files_content() # Imaginary method
            return GenerateFilesResponse(
                status="files_generated_successfully_simulated",
                message=f"Arquivos do projeto '{orchestrator.session.project_name}' foram gerados (simulação)."
            )
        else:
            return GenerateFilesResponse(
                status="not_ready_for_generation",
                message="O projeto não está na fase final de aprovação para gerar arquivos."
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar arquivos: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": app.version}
