from nicegui import ui, run, app
from app.services.orchestrator import OrchestratorService
# Import UI modules for wizard steps
from app.ui.wizard_steps import step_project_details, step_tech_stack

# Instanciar o serviço de orquestração
orchestrator = OrchestratorService()

def init_wizard_storage():
    """Initializes the wizard_data structure in app.storage.user if not present."""
    if 'wizard_data' not in app.storage.user:
        app.storage.user['wizard_data'] = {}

    # Initialize default keys for project details if they don't exist
    app.storage.user['wizard_data'].setdefault('project_name', '')
    app.storage.user['wizard_data'].setdefault('project_description', '')

    # Initialize default keys for tech stack if they don't exist
    app.storage.user['wizard_data'].setdefault('main_technology', 'Python') # Default value

    # Initialize additional_features dictionary and its keys
    additional_features_storage = app.storage.user['wizard_data'].setdefault('additional_features', {})
    additional_features_storage.setdefault('docker', False)
    additional_features_storage.setdefault('cicd', False)
    additional_features_storage.setdefault('tests', False)

# Define a página raiz da aplicação
@ui.page('/')
async def main_page():
    # Ensure wizard_data and its nested dictionaries are initialized
    init_wizard_storage()

    # Main page layout
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label('Gemini-Flow Project Bootstrapper').classes('text-h5')

    # Wizard Stepper Implementation
    with ui.stepper().props('vertical').classes('w-full') as stepper:
        with ui.step('Introdução'):
            ui.label('Bem-vindo ao Gemini-Flow Project Bootstrapper!')
            ui.markdown('Este wizard irá guiá-lo na configuração inicial do seu novo projeto.')
            with ui.stepper_navigation():
                ui.button('Avançar', on_click=stepper.next)

        with ui.step('Detalhes do Projeto'):
            # Call the UI creation function from the imported module
            step_project_details.create_project_details_ui()
            with ui.stepper_navigation():
                ui.button('Voltar', on_click=stepper.previous).props('flat')
                ui.button('Avançar', on_click=stepper.next)

        with ui.step('Pilha Tecnológica'):
            # Call the UI creation function from the imported module
            step_tech_stack.create_tech_stack_ui()
            with ui.stepper_navigation():
                ui.button('Voltar', on_click=stepper.previous).props('flat')
                ui.button('Avançar', on_click=stepper.next)

        with ui.step('Geração de Arquivos'):
            ui.label('Pronto para gerar os arquivos do projeto.')
            ui.label('Resumo das escolhas e botão de geração aqui em breve...')
            # TODO: Display summary of app.storage.user['wizard_data'] here
            with ui.stepper_navigation():
                ui.button('Voltar', on_click=stepper.previous).props('flat')
                ui.button('Gerar Projeto (placeholder)')

    ui.separator().classes('my-4')

    # --- PoC Greeting Section (Kept for now, can be removed later) ---
    with ui.expansion('PoC: Teste de Saudação Gemini (Legado)', icon='contact_support').classes('w-full'):
        ui.label('Prova de Conceito: NiceGUI + LangChain (Gemini)')
        name_input = ui.input(label="Qual o seu nome?", placeholder="Digite seu nome aqui")
        greeting_output_area = ui.markdown()

        async def on_generate_greeting_click():
            user_name = name_input.value
            if not user_name:
                ui.notify("Por favor, insira um nome.", type='warning')
                greeting_output_area.set_content("")
                return

            greeting_output_area.set_content(f"*Gerando saudação para {user_name}...*")
            try:
                greeting = await run.io_bound(orchestrator.get_gemini_greeting, user_name)
                greeting_output_area.set_content(f"**Saudação Gerada:**\n\n{greeting}")
                ui.notify("Saudação gerada com sucesso!", type='positive')
            except Exception as e:
                error_message = f"Erro ao gerar saudação: {e}"
                greeting_output_area.set_content(f"**Erro:**\n\n`{error_message}`")
                ui.notify(error_message, type='negative')
                print(f"Detalhes do erro no backend: {e}") # Logar erro no console do servidor

        ui.button("Gerar Saudação Gemini!", on_click=on_generate_greeting_click)
        ui.label('Olá, Mundo NiceGUI! (Base)')
    # --- End PoC Greeting Section ---


# Inicia o servidor e a aplicação
# Para desenvolvimento, reload=True é útil.
# O título da aplicação também pode ser definido aqui.
# storage_secret é necessário se app.storage for usado
ui.run(title="Gemini-Flow Bootstrapper", reload=True, storage_secret="SUPER_SECRET_KEY_FOR_GEMINI_FLOW_WIZARD")
