from enum import Enum
import os
from typing import List, Dict, Any
# from langchain_google_genai import ChatGoogleGenerativeAI # Will be uncommented when used
# from langchain.schema import HumanMessage, AIMessage, SystemMessage # Will be uncommented when used
from backend.config import settings

# Define os estados da aplicação
class AppStates(Enum):
    PLANNING = "PLANNING"
    ISSUES = "ISSUES"
    DEVOPS = "DEVOPS"

# Mapeamento de estados para arquivos de prompt
PROMPT_FILES = {
    AppStates.PLANNING: "gemini-gem-arquiteto-de-projetos.md",
    AppStates.ISSUES: "gemini-gem-gerente-de-issues.md",
    AppStates.DEVOPS: "gemini-gem-super-devops.md",
}

# PROMPTS_DIR is relative to the project root directory (where run_tests.sh is, or where main.py is effectively run from)
# When orchestrator.py is run as `python -m backend.orchestrator` from project root, CWD is project root.
# When main.py (FastAPI app) runs, and imports orchestrator, PROMPTS_DIR needs to be correct from project root.
# For tests, if CWD is backend/, then ../prompts is needed.
# Making it robust by being relative to this file's location.
_orchestrator_dir = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.normpath(os.path.join(_orchestrator_dir, "..", "prompts"))


class SessionManager:
    def __init__(self, project_name: str = "Meu Projeto"):
        self.project_name: str = project_name
        self.current_state: AppStates = AppStates.PLANNING
        self.conversation_history: List[Dict[str, str]] = [] # e.g., [{"role": "user", "content": "Hi"}, {"role": "assistant", "content": "Hello"}]
        self.current_prompt_template: str = ""
        self._load_prompt_for_state()

    def _load_prompt_for_state(self):
        """Carrega o template de prompt para o estado atual."""
        prompt_filename = PROMPT_FILES.get(self.current_state)
        if not prompt_filename:
            prompt_filename = PROMPT_FILES[AppStates.PLANNING]

        try:
            filepath = os.path.join(PROMPTS_DIR, prompt_filename)
            # abs_filepath = os.path.abspath(filepath) # Debug line
            # print(f"[DEBUG orchestrator._load_prompt_for_state] Trying to load prompt from: {filepath} (abs: {abs_filepath}, CWD: {os.getcwd()})") # Debug line
            with open(filepath, 'r', encoding='utf-8') as f: # Corrected encoding
                self.current_prompt_template = f.read()
        except FileNotFoundError:
            self.current_prompt_template = "Erro: Template de prompt não encontrado."
        except Exception as e:
            self.current_prompt_template = f"Erro ao carregar prompt: {str(e)}"

    def change_state(self, new_state: AppStates):
        """Muda o estado da aplicação e carrega o novo prompt."""
        if new_state in AppStates:
            self.current_state = new_state
            self._load_prompt_for_state()
            self.conversation_history.append({
                "role": "system",
                "content": f"Estado da aplicação alterado para: {self.current_state.value}. Novo prompt carregado."
            })
        # Return the introductory part of the prompt or a specific system message
        # For now, returning a generic message related to the new prompt template.
        # This could be the prompt template itself, or a predefined intro message.
        return f"Novo prompt para {self.current_state.value} carregado. {self.current_prompt_template.splitlines()[0]}"


    def add_message_to_history(self, role: str, content: str):
        """Adiciona uma mensagem ao histórico da conversa."""
        self.conversation_history.append({"role": role, "content": content})

    def get_formatted_history_for_llm(self) -> List[Any]: # Langchain messages
        # messages = [SystemMessage(content=self.current_prompt_template)]
        # for msg in self.conversation_history:
        #     if msg["role"] == "user":
        #         messages.append(HumanMessage(content=msg["content"]))
        #     elif msg["role"] == "assistant":
        #         messages.append(AIMessage(content=msg["content"]))
        # return messages
        return self.conversation_history

    def set_project_name(self, project_name: str):
        self.project_name = project_name
        self.add_message_to_history("system", f"Nome do projeto definido como: {project_name}")

    def requires_approval(self) -> bool:
        """
        Determina se a fase atual da conversa exige uma etapa de aprovação do usuário.
        Placeholder: Esta lógica precisará ser refinada.
        Por exemplo, pode verificar se a última mensagem da IA contém um marcador específico
        ou se um certo número de interações ocorreu na fase atual.
        """
        # Exemplo simples: sempre requer aprovação no estado DEVOPS após algumas mensagens
        if self.current_state == AppStates.DEVOPS and len(self.conversation_history) > 5:
            return True
        # Exemplo: requer aprovação se a última mensagem da IA contiver "[APROVAR AGORA]"
        if self.conversation_history:
            last_ai_message = next((msg["content"] for msg in reversed(self.conversation_history) if msg["role"] == "assistant"), None)
            if last_ai_message and "[APROVAR AGORA]" in last_ai_message:
                return True
        return False


class Orchestrator:
    def __init__(self):
        self.session = SessionManager()
        # self.llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=settings.GEMINI_API_KEY) # Uncomment when ready

    def start_new_session(self, project_name: str):
        """Inicia uma nova sessão de planejamento."""
        self.session = SessionManager(project_name=project_name)
        initial_message = f"Nova sessão iniciada para o projeto '{project_name}'. Estado inicial: {self.session.current_state.value}."
        return {"status": "session_started", "project_name": project_name, "current_state": self.session.current_state.value, "message": initial_message}

    def process_user_message(self, user_message: str) -> Dict[str, Any]:
        """Processa a mensagem do usuário, interage com o LLM e retorna a resposta."""
        self.session.add_message_to_history("user", user_message)

        response_content = (
            f"Mensagem recebida: '{user_message}'. "
            f"Estado atual: {self.session.current_state.value}. "
            f"Prompt ativo: {PROMPT_FILES.get(self.session.current_state)}. "
            f"Histórico contém {len(self.session.conversation_history)} mensagens. (Resposta simulada)"
        )

        self.session.add_message_to_history("assistant", response_content)
        is_approval_step = self.session.requires_approval()

        return {
            "user_message": user_message,
            "ai_response": response_content,
            "current_state": self.session.current_state.value,
            "history_length": len(self.session.conversation_history),
            "is_approval_step": is_approval_step
        }

    def change_phase(self, new_phase_name: str) -> Dict[str, Any]:
        """Muda a fase (estado) da aplicação e retorna a mensagem inicial da nova fase."""
        try:
            new_state_enum = AppStates[new_phase_name.upper()]
            initial_message_for_new_phase = self.session.change_state(new_state_enum) # change_state now returns a message

            # Simulate an initial AI response for the new phase based on its loaded prompt
            # This is a placeholder; a real LLM call would be better.
            # For now, we use the message returned by session.change_state directly or a derivative.
            # Let's assume the initial_message_for_new_phase is suitable as the first "AI" message.

            # We might also want to add this initial message to history as a system or AI message.
            # For now, let's make the returned 'message' be this initial prompt/message.
            # The frontend will display this as the first message from the AI in the new phase.

            return {
                "status": "state_changed",
                "new_state": self.session.current_state.value,
                "message": initial_message_for_new_phase # This is the key change
            }
        except KeyError:
            return {
                "status": "error",
                "message": f"Fase '{new_phase_name}' desconhecida. Estados válidos: {[s.name for s in AppStates]}."
            }

if __name__ == "__main__":
    orchestrator = Orchestrator()
    print(orchestrator.start_new_session(project_name="Super Projeto X"))

    print("\n--- Enviando mensagem ---")
    response = orchestrator.process_user_message("Olá, vamos começar o planejamento.")
    print(response)

    print("\n--- Mudando de estado para ISSUES ---")
    change_response = orchestrator.change_phase("ISSUES")
    print(change_response)

    print("\n--- Enviando outra mensagem ---")
    response = orchestrator.process_user_message("Preciso reportar um bug.")
    print(response)

    print("\n--- Tentando mudar para estado inválido ---")
    change_response = orchestrator.change_phase("TESTING")
    print(change_response)

    print("\n--- Verificando o Gemini API Key (da config) ---")
    if hasattr(settings, 'GEMINI_API_KEY') and settings.GEMINI_API_KEY:
        print(f"Chave GEMINI_API_KEY carregada: {settings.GEMINI_API_KEY[:5]}... (ocultado por segurança)")
    elif hasattr(settings, 'GEMINI_API_KEY'):
        print("GEMINI_API_KEY está presente nas configurações, mas vazia.")
    else:
        print("GEMINI_API_KEY não encontrada nas configurações.")

    print("\n--- Testando carregamento de prompts ---")
    for state in AppStates:
        print(f"Testando estado: {state.name}")
        orchestrator.change_phase(state.name)
        if "Erro:" in orchestrator.session.current_prompt_template:
             print(f"!!! Problema ao carregar prompt para {state.name}: {orchestrator.session.current_prompt_template}")
        else:
             print(f"Prompt para {state.name} carregado, início: '{orchestrator.session.current_prompt_template[:70].replace('\n', ' ')}...'")


    print("\n--- Verificando arquivos de prompt fisicamente ---")
    all_prompts_found = True
    for state, filename in PROMPT_FILES.items():
        filepath = os.path.join(PROMPTS_DIR, filename)
        if os.path.exists(filepath):
            print(f"Arquivo de prompt para {state.name} ({filename}) ENCONTRADO em {filepath}.")
        else:
            print(f"ATENÇÃO: Arquivo de prompt para {state.name} ({filename}) NÃO encontrado em {filepath}.")
            all_prompts_found = False
    if all_prompts_found:
        print("Todos os arquivos de prompt referenciados foram encontrados.")
    else:
        print("!!! ALERTA: Um ou mais arquivos de prompt não foram encontrados. Verifique os caminhos e a existência dos arquivos.")

    print("\n--- Teste de funcionalidade básica concluído ---")
    if not all_prompts_found:
        print("ALERTA: Testes de prompt falharam devido a arquivos ausentes.")
        # Em um CI, isso poderia sair com um código de erro.
        # exit(1)
    if not hasattr(settings, 'GEMINI_API_KEY') or not settings.GEMINI_API_KEY:
        print("ALERTA: GEMINI_API_KEY não configurada corretamente.")
        # exit(1)

    # Adicionando uma verificação final para o nome do projeto
    orchestrator.session.set_project_name("Projeto Y Teste")
    if orchestrator.session.project_name == "Projeto Y Teste":
        print("Teste de set_project_name: SUCESSO")
    else:
        print(f"Teste de set_project_name: FALHA (esperado 'Projeto Y Teste', obteve '{orchestrator.session.project_name}')")

    print("--- Fim dos testes ---")
