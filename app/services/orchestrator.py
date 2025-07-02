from app.core.config import settings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Use ChatGoogleGenerativeAI for direct Gemini API usage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda # Import RunnableLambda

class OrchestratorService:
    def __init__(self):
        if not settings.GEMINI_API_KEY or settings.GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
            print("Warning: GEMINI_API_KEY not configured. LLM functionality will be limited/mocked.")
            self.llm = None
        else:
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-pro",
                google_api_key=settings.GEMINI_API_KEY,
                temperature=0.7,
            )

        self.greeting_prompt = PromptTemplate.from_template(
            "Crie uma saudação curta, criativa e amigável para {name}."
        )
        if self.llm:
            self.greeting_chain = self.greeting_prompt | self.llm | StrOutputParser()
        else:
            self.greeting_chain = RunnableLambda(
                lambda input_dict: f"Olá, {input_dict.get('name', 'convidado')}! (LLM não configurado)"
            )

        # # Define the prompt template for Dockerfile generation - COMMENTED OUT
        # self.dockerfile_prompt_template = PromptTemplate.from_template(
        #     "Dockerfile para {project_name} usando {main_technology}."
        # )
        # if self.llm:
        #     self.dockerfile_chain = self.dockerfile_prompt_template | self.llm | StrOutputParser()
        # else:
        #     self.dockerfile_chain = RunnableLambda(
        #         lambda input_dict: f"# Dockerfile para {input_dict.get('project_name', 'projeto_desconhecido')}\n"
        #                              f"# Gerado com {input_dict.get('main_technology', 'tecnologia_desconhecida')}\n"
        #                              f"# LLM não configurado. (SIMPLIFICADO)"
        #     ) # This was the extra parenthesis from the commented block

        # Define the prompt template for Dockerfile generation - SIMPLIFIED (but was working)
        self.dockerfile_prompt_template = PromptTemplate.from_template(
            "Dockerfile para {project_name} usando {main_technology}."
        )
        if self.llm:
            self.dockerfile_chain = self.dockerfile_prompt_template | self.llm | StrOutputParser()
        else:
            self.dockerfile_chain = RunnableLambda(
                lambda input_dict: f"# Dockerfile para {input_dict.get('project_name', 'projeto_desconhecido')}\n"
                                     f"# Gerado com {input_dict.get('main_technology', 'tecnologia_desconhecida')}\n"
                                     f"# LLM não configurado. (SIMPLIFICADO)"
            )
        # self.dockerfile_chain = None # Ensure attribute exists - No, this is now defined

        # # Define the prompt template for GEMINI.md generation - COMMENTED OUT
        # self.gemini_md_prompt_template = PromptTemplate.from_template(
        #     "GEMINI.md para {project_name}. Descrição: {project_description}. Tech: {main_technology}."
        # )
        # if self.llm:
        #     self.gemini_md_chain = self.gemini_md_prompt_template | self.llm | StrOutputParser()
        # else:
        #     self.gemini_md_chain = RunnableLambda(
        #         lambda input_dict: f"# GEMINI.md para {input_dict.get('project_name', 'projeto_desconhecido')}\n"
        #                              f"## (LLM não configurado - Este é um placeholder SIMPLIFICADO)\n"
        #                              f"**Tecnologia Principal:** {input_dict.get('main_technology', 'N/A')}"
        #     ) # Correctly removing this extra parenthesis

        # Define the prompt template for GEMINI.md generation - USING ULTRA-SIMPLIFIED WORKING VERSION
        self.gemini_md_prompt_template = PromptTemplate.from_template(
            "GEMINI.md para {project_name}. Descrição: {project_description}. Tech: {main_technology}. Docker: {docker_enabled}. CI/CD: {cicd_enabled}. Tests: {tests_enabled}."
        ) # This uses all placeholders that the generate_gemini_md_content method prepares.

        if self.llm:
            self.gemini_md_chain = self.gemini_md_prompt_template | self.llm | StrOutputParser()
        else:
            self.gemini_md_chain = RunnableLambda(
                lambda input_dict: f"# GEMINI.md para {input_dict.get('project_name', 'projeto_desconhecido')}\n"
                                     f"## (LLM não configurado - Este é um placeholder)\n" # Restored placeholder
                                     f"**Tecnologia Principal:** {input_dict.get('main_technology', 'N/A')}\n"
                                     f"**Descrição:** {input_dict.get('project_description', 'N/A')}\n"
                                     f"**Docker:** {input_dict.get('docker_enabled', 'N/A')}\n"
                                     f"**CI/CD:** {input_dict.get('cicd_enabled', 'N/A')}\n"
                                     f"**Testes:** {input_dict.get('tests_enabled', 'N/A')}\n"
                                     f"\n(Conteúdo completo do GEMINI.md seria gerado aqui pelo LLM.)"
            )
        # self.gemini_md_chain = None # Ensure attribute exists - No, this is now defined


    def get_gemini_greeting(self, name: str) -> str:
        if not name:
            return "Olá! Por favor, me diga seu nome."
        try:
            response = self.greeting_chain.invoke({"name": name})
            return response
        except Exception as e:
            print(f"Error calling LLM for greeting: {e}")
            return f"Olá, {name}! Tive um problema ao gerar sua saudação personalizada."

    def generate_dockerfile_content(self, project_details: dict) -> str:
        if not self.dockerfile_chain:
            return "# Erro: Funcionalidade Dockerfile desabilitada para teste."
        if not project_details.get('project_name') or not project_details.get('main_technology'):
            return "# Erro: Nome do projeto e tecnologia principal são obrigatórios para gerar o Dockerfile."
        prompt_input = {
            'project_name': project_details.get('project_name'),
            'main_technology': project_details.get('main_technology'),
            'app_port': project_details.get('app_port', 8000)
        }
        try:
            response = self.dockerfile_chain.invoke(prompt_input)
            return response
        except Exception as e:
            print(f"Error calling LLM for Dockerfile generation: {e}")
            return f"# Erro ao gerar Dockerfile para {project_details.get('project_name', 'projeto_desconhecido')}: {e}"

    def generate_gemini_md_content(self, project_details: dict) -> str:
        if not self.gemini_md_chain:
            return "# Erro: Funcionalidade GEMINI.md desabilitada para teste."
        if not project_details.get('project_name'):
            return "# Erro: Nome do projeto é obrigatório para gerar o GEMINI.md."
        additional_features = project_details.get('additional_features', {})
        prompt_input = {
            'project_name': project_details.get('project_name', 'N/A'),
            'project_description': project_details.get('project_description', 'N/A'),
            'main_technology': project_details.get('main_technology', 'N/A'),
            'docker_enabled': "Sim" if additional_features.get('docker') else "Não",
            'cicd_enabled': "Sim" if additional_features.get('cicd') else "Não",
            'tests_enabled': "Sim" if additional_features.get('tests') else "Não",
            'docker_enabled_text': "Habilitado" if additional_features.get('docker') else "Não habilitado",
            'cicd_enabled_text': "Solicitada" if additional_features.get('cicd') else "Não solicitado",
            'tests_enabled_text': "Solicitada" if additional_features.get('tests') else "Não solicitado",
        }
        try:
            response = self.gemini_md_chain.invoke(prompt_input)
            return response
        except Exception as e:
            print(f"Error calling LLM for GEMINI.md generation: {e}")
            return f"# Erro ao gerar GEMINI.md para {project_details.get('project_name', 'projeto_desconhecido')}: {e}"

if __name__ == "__main__":
    print(f"Testing configuration. API Key Loaded: {'Yes' if settings.GEMINI_API_KEY != 'YOUR_GEMINI_API_KEY_HERE' and settings.GEMINI_API_KEY else 'No (Using Default/Placeholder)'}")
    orchestrator = OrchestratorService()

    if orchestrator.llm is None:
        print("\n--- Teste com LLM não configurado (Saudação) ---")
        greeting_no_key = orchestrator.get_gemini_greeting("Usuário Teste")
        print(f"Saudação (LLM não configurado): {greeting_no_key}")
    
    sample_project_details = {
        'project_name': 'MeuAppTeste',
        'main_technology': 'Python',
        'project_description': 'Descrição teste.',
        'additional_features': {'docker': True, 'cicd': False, 'tests': True},
        'app_port': 8000
    }
    print("\n--- Teste de Geração de Dockerfile (funcionalidade desabilitada) ---")
    dockerfile_content = orchestrator.generate_dockerfile_content(sample_project_details)
    print(dockerfile_content)

    print("\n--- Teste de Geração de GEMINI.md (funcionalidade desabilitada) ---")
    gemini_md_content = orchestrator.generate_gemini_md_content(sample_project_details)
    print(gemini_md_content)
