from nicegui import ui, run
from app.services.orchestrator import OrchestratorService

# Instanciar o serviço de orquestração
# Idealmente, seria injetado ou um singleton se o estado fosse complexo,
# mas para esta PoC, uma instância global simples é suficiente.
orchestrator = OrchestratorService()

# Define a página raiz da aplicação
@ui.page('/')
async def main_page(): # Alterado para async para permitir await no handler
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
            # Chamar o método do orquestrador de forma assíncrona
            # run.io_bound é usado para garantir que chamadas potencialmente bloqueantes
            # (mesmo que a chain seja async, partes dela podem não ser)
            # não congelem a UI do NiceGUI.
            greeting = await run.io_bound(orchestrator.get_gemini_greeting, user_name)
            greeting_output_area.set_content(f"**Saudação Gerada:**\n\n{greeting}")
            ui.notify("Saudação gerada com sucesso!", type='positive')
        except Exception as e:
            error_message = f"Erro ao gerar saudação: {e}"
            greeting_output_area.set_content(f"**Erro:**\n\n`{error_message}`")
            ui.notify(error_message, type='negative')
            print(f"Detalhes do erro no backend: {e}") # Logar erro no console do servidor

    ui.button("Gerar Saudação Gemini!", on_click=on_generate_greeting_click)

    # Adicionando um label "Olá, Mundo" para manter o teste original da P1-DEV-03
    ui.label('Olá, Mundo NiceGUI! (Base)')


# Inicia o servidor e a aplicação
# Para desenvolvimento, reload=True é útil.
# O título da aplicação também pode ser definido aqui.
# storage_secret é necessário se app.storage for usado (não nesta PoC específica, mas boa prática)
ui.run(title="Gemini-Flow Bootstrapper", reload=True, storage_secret="SUPER_SECRET_KEY_FOR_POC")
