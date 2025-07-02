from nicegui import ui, app

def create_project_details_ui():
    """Creates UI elements for the 'Project Details' step."""
    ui.label('Forneça os detalhes básicos do seu projeto.')

    # Project Name
    ui.input(
        label='Nome do Projeto',
        placeholder='Ex: MeuSuperAppInovador',
        validation={'O nome do projeto não pode estar vazio.': lambda value: bool(value and value.strip())}
    ).bind_value(app.storage.user['wizard_data'], 'project_name').classes('w-full')

    # Project Description
    ui.textarea(
        label='Descrição do Projeto',
        placeholder='Descreva brevemente o objetivo e as funcionalidades principais do seu projeto.'
    ).bind_value(app.storage.user['wizard_data'], 'project_description').classes('w-full')

    # You can add more fields here as needed, for example:
    # ui.input(label='Versão Inicial', value='0.1.0').bind_value(app.storage.user['wizard_data'], 'project_version').classes('w-1/2')

    # Ensure default keys exist if not already present from main_page initialization
    if 'project_name' not in app.storage.user['wizard_data']:
        app.storage.user['wizard_data']['project_name'] = ''
    if 'project_description' not in app.storage.user['wizard_data']:
        app.storage.user['wizard_data']['project_description'] = ''

    # ui.label('Mais campos aqui em breve...') # Removed as we are adding actual fields
