from app.core.config import settings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Use ChatGoogleGenerativeAI for direct Gemini API usage
from langchain_google_genai import ChatGoogleGenerativeAI

class OrchestratorService:
    def __init__(self):
        # Initialize the LLM with the API key from settings
        # Ensure GEMINI_API_KEY is set in your .env file or environment
        if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
            # This is a fallback or error for when the key isn't properly set.
            # In a real scenario, you might raise an error or use a mock/dummy for local dev
            # if no key is available and you want the app to run without full LLM functionality.
            print("Warning: GEMINI_API_KEY not configured. LLM functionality will be limited/mocked.")
            self.llm = None # Or a mock LLM
        else:
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-pro", # Or another compatible Gemini model
                google_api_key=settings.GEMINI_API_KEY,
                temperature=0.7, # Example: Adjust creativity
                # convert_system_message_to_human=True # If using SystemMessage with a model that prefers HumanMessage for system-like prompts
            )

        # Define the prompt template for the greeting
        self.greeting_prompt = PromptTemplate.from_template(
            "Crie uma saudação curta, criativa e amigável para {name}."
        )

        # Define the chain for generating greetings
        if self.llm:
            self.greeting_chain = self.greeting_prompt | self.llm | StrOutputParser()
        else:
            # Fallback chain if LLM is not configured
            self.greeting_chain = self.greeting_prompt | (lambda x: f"Olá, {x['name']}! (LLM não configurado)") | StrOutputParser()


    def get_gemini_greeting(self, name: str) -> str:
        """
        Generates a personalized greeting using LangChain and Gemini.
        """
        if not name:
            return "Olá! Por favor, me diga seu nome."
        try:
            response = self.greeting_chain.invoke({"name": name})
            return response
        except Exception as e:
            # Log the error e
            print(f"Error calling LLM: {e}")
            return f"Olá, {name}! Tive um problema ao gerar sua saudação personalizada."

# Example of how to use it (for testing purposes, not part of the class)
if __name__ == "__main__":
    # This part would require a .env file with GEMINI_API_KEY in the project root
    # or the environment variable to be set.
    # For direct execution, ensure your PYTHONPATH is set up correctly if running from outside `app`
    # Ex: export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"
    # then: python app/services/orchestrator.py

    # A simple way to test if settings are loaded (requires .env or env var)
    print(f"Testing configuration. API Key Loaded: {'Yes' if settings.GEMINI_API_KEY != 'YOUR_GEMINI_API_KEY_HERE' and settings.GEMINI_API_KEY else 'No (Using Default/Placeholder)'}")

    orchestrator = OrchestratorService()

    # Test without a properly configured API key (will use fallback)
    if orchestrator.llm is None:
        print("\n--- Teste com LLM não configurado ---")
        greeting_no_key = orchestrator.get_gemini_greeting("Usuário Teste")
        print(f"Saudação (LLM não configurado): {greeting_no_key}")

    # To test with a real API key, ensure your .env is set up
    # Note: This direct execution might not work as intended without proper context
    # or if the API key is not available.
    # It's better to test this through an entry point that initializes NiceGUI or via unit tests.
    print("\n--- Tentativa de teste com LLM (requer API Key configurada) ---")
    # This will only work if GEMINI_API_KEY is correctly set in .env or environment
    if settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE":
        try:
            greeting_real = orchestrator.get_gemini_greeting("Galvani")
            print(f"Saudação (LLM real): {greeting_real}")
        except Exception as e:
            print(f"Erro durante teste com LLM real: {e}")
    else:
        print("Pular teste com LLM real: GEMINI_API_KEY não configurada.")

    greeting_empty_name = orchestrator.get_gemini_greeting("")
    print(f"Saudação (nome vazio): {greeting_empty_name}")

```
