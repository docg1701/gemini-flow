from nicegui import ui, app

def create_tech_stack_ui():
    """Creates UI elements for the 'Tech Stack' step."""
    ui.label('Selecione as tecnologias principais e recursos para o seu projeto.')

    # Main Technology
    tech_options = ['Python', 'JavaScript (Node.js)', 'Java', 'Outra']
    ui.select(
        options=tech_options,
        label='Tecnologia Principal',
        value='Python' # Default value
    ).bind_value(app.storage.user['wizard_data'], 'main_technology').classes('w-full')

    ui.separator().classes('my-4')
    ui.label('Recursos Adicionais:').classes('text-subtitle1')

    # Additional Features - using individual checkboxes for clarity in binding
    # Ensure 'additional_features' dict is initialized in app.storage.user['wizard_data']
    # This initialization is better done once in main_page or wizard_data setup.
    # For safety here, ensure keys exist before binding if not using a more robust init pattern.

    features_storage = app.storage.user['wizard_data'].setdefault('additional_features', {})

    ui.checkbox('Incluir Dockerfile?', on_change=lambda e: features_storage.update({'docker': e.value})).bind_value_from(features_storage, 'docker')
    ui.checkbox('Configurar Pipeline CI/CD (básico)?', on_change=lambda e: features_storage.update({'cicd': e.value})).bind_value_from(features_storage, 'cicd')
    ui.checkbox('Incluir Estrutura de Testes Automatizados?', on_change=lambda e: features_storage.update({'tests': e.value})).bind_value_from(features_storage, 'tests')

    # Initialize default values if not present for these specific features
    if 'main_technology' not in app.storage.user['wizard_data']:
        app.storage.user['wizard_data']['main_technology'] = 'Python' # Default
    if 'docker' not in features_storage:
        features_storage['docker'] = False
    if 'cicd' not in features_storage:
        features_storage['cicd'] = False
    if 'tests' not in features_storage:
        features_storage['tests'] = False
