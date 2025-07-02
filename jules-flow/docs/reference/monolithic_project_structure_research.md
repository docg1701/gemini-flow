# Pesquisa sobre Estrutura de Projeto Python Monolítico com NiceGUI (task-R04)

Data da Compilação: 2024-07-31

## Fontes Consultadas
* `jules-flow/docs/reference/nicegui_research.md` (Manual do NiceGUI fornecido pelo usuário, especificamente Capítulo 15.1 sobre Modularização)
* Conhecimento geral sobre arquitetura de software e boas práticas em projetos Python.
* Requisitos do `jules-flow/working-plan.md` (migração para monolítico NiceGUI + LangChain).

## Estrutura Recomendada para Aplicação Monolítica NiceGUI + LangChain

O objetivo é criar uma estrutura clara, manutenível e escalável para a nova versão do `gemini-flow`.

### 1. Estrutura de Diretórios Proposta

Baseado nos requisitos do `working-plan.md` (criar `app/` e remover `/frontend` e `/backend`), e nas práticas de modularização:

```
gemini-flow/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada da aplicação NiceGUI, define páginas/rotas principais
│   │
│   ├── core/                   # Configurações centrais, logging, etc.
│   │   ├── __init__.py
│   │   └── config.py           # Gerenciamento de configurações (ex: chaves de API, paths)
│   │
│   ├── ui/                     # Módulos relacionados à interface do usuário NiceGUI
│   │   ├── __init__.py
│   │   ├── wizard_steps/       # Componentes para cada passo do wizard
│   │   │   ├── __init__.py
│   │   │   ├── step_introduction.py
│   │   │   ├── step_project_details.py
│   │   │   └── ... (outros passos do wizard)
│   │   ├── shared_components/  # Componentes de UI reutilizáveis (ex: cabeçalho customizado)
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   └── main_layout.py      # Layout principal da página (header, footer, drawers) se aplicável globalmente
│   │
│   ├── services/               # Lógica de negócio, interações com LangChain
│   │   ├── __init__.py
│   │   ├── orchestrator.py     # Orquestra a lógica de LangChain para geração de arquivos
│   │   └── file_templates/     # (Opcional) Pode conter templates de prompt ou snippets
│   │       ├── __init__.py
│   │       ├── dockerfile_prompts.py
│   │       └── ...
│   │
│   └── models/                 # (Opcional) Modelos de dados Pydantic, se necessário para LangChain ou estado da UI
│       ├── __init__.py
│       └── project_config_model.py
│
├── tests/                      # Testes unitários e de integração
│   ├── __init__.py
│   ├── test_orchestrator.py
│   └── ui/
│       ├── __init__.py
│       └── test_wizard_steps.py
│
├── output/                     # Diretório onde os projetos gerados pelo usuário serão salvos
│   └── .gitkeep
│
├── jules-flow/                 # Diretório existente para o fluxo de trabalho de Jules
│   └── ...
│
├── .gitignore
├── jules_bootstrap.sh
├── LICENSE
├── README.md                   # A ser atualizado para refletir a nova arquitetura
├── requirements.txt            # A ser atualizado com `nicegui`, `langchain`, etc.
└── VISION.md                   # A ser gerado/atualizado
```

**Justificativa da Estrutura:**

*   **`app/`**: Contém todo o código da aplicação, conforme solicitado pelo `working-plan.md`.
*   **`app/main.py`**: Ponto de entrada claro. Inicializa `ui.run()` e define as páginas principais (provavelmente o wizard).
*   **`app/core/config.py`**: Centraliza configurações, como chaves de API para Gemini, caminhos padrão, etc. Pode usar bibliotecas como `python-decouple` ou Pydantic's `BaseSettings`.
*   **`app/ui/`**: Separa a lógica da interface.
    *   `wizard_steps/`: Cada passo do wizard como um módulo Python separado. Cada módulo define os elementos NiceGUI para aquele passo e pode interagir com `app.storage.user` para coletar dados.
    *   `shared_components/`: Para componentes de UI que são usados em múltiplos lugares.
    *   `main_layout.py`: Se houver um layout comum (header/footer) para todas as páginas do wizard, ele pode ser definido aqui e importado em `main.py`.
*   **`app/services/`**: Lógica de backend desacoplada da UI.
    *   `orchestrator.py`: Responsável por receber os dados coletados pelo wizard e usar LangChain para gerar os arquivos. Contém as chains, prompts (ou importa de `file_templates`).
    *   `file_templates/` (opcional): Se os prompts forem muito longos ou reutilizáveis, podem ser organizados aqui.
*   **`app/models/`** (opcional): Se a aplicação usar modelos de dados complexos (ex: Pydantic models para validar entradas do wizard ou para estruturar a saída do LangChain antes da geração final), eles podem residir aqui. O manual do NiceGUI sugere `@binding.bindable_dataclass` para modelos de dados vinculados à UI.
*   **`tests/`**: Estrutura de testes espelhando a estrutura de `app/`.
*   **`output/`**: Diretório de saída para os projetos gerados, conforme `working-plan.md`.

### 2. Gerenciamento de Configurações (`app/core/config.py`)

*   Usar variáveis de ambiente para dados sensíveis (API Keys).
*   Bibliotecas como `python-decouple` ou Pydantic (`BaseSettings`) podem facilitar o carregamento de configurações de arquivos `.env` e do ambiente.
    ```python
    # Exemplo app/core/config.py com Pydantic
    from pydantic_settings import BaseSettings, SettingsConfigDict

    class Settings(BaseSettings):
        APP_NAME: str = "Gemini-Flow Bootstrapper"
        GEMINI_API_KEY: str = "YOUR_API_KEY_HERE" # Default, mas deve vir do .env
        OUTPUT_DIR: str = "output"

        # Para carregar de um arquivo .env
        model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')

    settings = Settings()

    # Em outros módulos:
    # from app.core.config import settings
    # api_key = settings.GEMINI_API_KEY
    ```
    O `.env` estaria na raiz do projeto e adicionado ao `.gitignore`.

### 3. Padrões para Importação de Módulos e Evitar Dependências Circulares

*   **Importações Absolutas**: Usar importações absolutas relativas à raiz do pacote `app` (ex: `from app.ui.wizard_steps import step_introduction`).
*   **Injeção de Dependência (Implícita ou Explícita)**:
    *   Módulos de UI não devem importar diretamente módulos de serviço de forma pesada, se possível. `main.py` pode instanciar o orquestrador e passá-lo para os handlers de UI que precisam dele, ou os handlers podem importar e usar o orquestrador diretamente se for um singleton ou tiver estado global gerenciado.
    *   Exemplo: O handler do botão "Gerar" em `main.py` chamaria uma função em `app.services.orchestrator`.
*   **Sinais/Eventos ou Callbacks Simples**: Para comunicação UI -> Serviço, os handlers de evento do NiceGUI são o mecanismo natural. Para Serviço -> UI (atualizações), usar `ui.notify`, atualizar labels/markdowns diretamente, ou usar `app.storage.user` com `bind_...` para reatividade.
*   **Evitar Importações no Nível do Módulo que Criam Ciclos**: Se o módulo A importa B e B importa A no nível superior, isso cria um ciclo. Tentar adiar importações para dentro de funções/métodos se necessário, ou refatorar para que um módulo dependa de uma abstração em vez de uma implementação concreta que causa o ciclo.
*   **Modelo de Dados Compartilhado**: Se UI e serviços precisam compartilhar estruturas de dados, defini-las em `app/models/` e ambos importarem de lá pode ajudar.

### 4. Considerações para Testes

*   **Testes Unitários (`app/services/orchestrator.py`)**:
    *   Testar a lógica de LangChain (formatação de prompt, invocação de chain, parsing de saída) com LLMs mockados ou "fake" LLMs (`FakeLLM` do LangChain) para evitar chamadas reais à API e garantir testes rápidos e determinísticos.
    *   Verificar se os prompts são gerados corretamente com base em diferentes entradas do usuário.
    *   Verificar se o conteúdo do arquivo gerado (mockado) corresponde ao esperado.
*   **Testes de UI (NiceGUI)**:
    *   NiceGUI tem alguma capacidade de teste para interações de UI (ver documentação do NiceGUI para `nicegui.testing`). Pode-se simular cliques de botão, entrada de usuário e verificar se a UI reage como esperado (ex: se notificações aparecem, se elementos são atualizados).
    *   Testar a lógica de navegação do wizard.
    *   Testar a coleta de dados em `app.storage.user`.
*   **Testes de Integração**:
    *   Testar o fluxo completo: entrada do usuário no wizard -> coleta de dados -> chamada ao orquestrador -> (mock) geração de conteúdo de arquivo.

### Exemplo de Fluxo de Importação (Simplificado)

```python
# app/main.py
from nicegui import ui, app
from app.core.config import settings
from app.ui.wizard_steps import step_introduction, step_project_details # e outros
from app.services.orchestrator import ProjectOrchestrator

orchestrator = ProjectOrchestrator(api_key=settings.GEMINI_API_KEY)

@ui.page('/')
def show_wizard():
    # Configuração do ui.stepper
    with ui.stepper() as stepper:
        with ui.step('Intro'):
            step_introduction.create_ui() # step_introduction.py pode usar app.storage.user
            ui.stepper_navigation()
        with ui.step('Detalhes'):
            step_project_details.create_ui() # step_project_details.py usa app.storage.user
            ui.stepper_navigation()
        # ... outros passos
        with ui.step('Gerar'):
            async def handle_generate():
                user_data = app.storage.user.get('wizard_data', {})
                ui.notify("Gerando projeto...")
                try:
                    # Idealmente, orchestrator.generate_all_files seria async
                    # ou chamado com run.io_bound
                    file_contents = await run.io_bound(orchestrator.generate_all_files, user_data)
                    # Lógica para salvar arquivos em settings.OUTPUT_DIR / user_data['project_name']
                    # ...
                    ui.notify("Projeto gerado com sucesso!", type='positive')
                except Exception as e:
                    ui.notify(f"Erro: {e}", type='negative')
            ui.button("Gerar Projeto", on_click=handle_generate)
            ui.stepper_navigation()

# ui.run(storage_secret=settings.STORAGE_SECRET_KEY_IF_ANY) # Adicionar secret para app.storage
```

```python
# app/services/orchestrator.py
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_google_vertexai import ChatVertexAI # ou similar

class ProjectOrchestrator:
    def __init__(self, api_key: str):
        # self.llm = ChatVertexAI(model_name="gemini-1.0-pro", project=...) # Configurar LLM
        # Exemplo de chain
        # self.dockerfile_prompt = PromptTemplate.from_template("Gerar Dockerfile para {tech}...")
        # self.dockerfile_chain = self.dockerfile_prompt | self.llm | StrOutputParser()
        pass

    def generate_dockerfile(self, user_data: dict) -> str:
        # tech = user_data.get('main_technology')
        # return self.dockerfile_chain.invoke({"tech": tech})
        return f"# Dockerfile para {user_data.get('project_name')}\nFROM {user_data.get('main_technology', 'python')}:latest" # Mock

    def generate_gemini_md(self, user_data: dict) -> str:
        # Lógica mais complexa aqui, possivelmente múltiplas chains
        return f"# GEMINI.md para {user_data.get('project_name')}\nConteúdo principal..." # Mock

    def generate_all_files(self, user_data: dict) -> dict:
        # Este método seria chamado pelo handler do NiceGUI
        files = {}
        files["Dockerfile"] = self.generate_dockerfile(user_data)
        files["GEMINI.md"] = self.generate_gemini_md(user_data)
        # ... gerar outros arquivos
        return files
```

Esta estrutura promove a separação de preocupações (UI vs. Lógica de Negócio), facilita os testes e deve ser manutenível à medida que o projeto cresce.
---
