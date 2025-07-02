---
id: task-P2-DEV-02
title: "WP2: Adicionar botão em app/main.py para chamar orquestrador e exibir resultado"
type: development
status: backlog
priority: high
dependencies: ["task-P1-DEV-03", "task-P2-DEV-01"]
parent_plan_objective_id: "2"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:05:00Z # Novo timestamp
updated_at: 2024-07-31T14:05:00Z
tags: ["development", "nicegui", "ui", "integration", "poc"]
description: |
  Modificar `app/main.py` para:
  1. Importar o serviço de orquestração de `app/services/orchestrator.py`.
  2. Instanciar o serviço.
  3. Adicionar um `ui.input` para o usuário digitar um nome.
  4. Adicionar um `ui.button` "Chamar Gemini".
  5. No `on_click`, chamar a função de saudação do orquestrador.
  6. Exibir o resultado em um `ui.label` ou `ui.markdown`.
  7. Garantir chamada assíncrona (`async def`, `await run.io_bound`).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: 2024-07-31T15:45:00Z # Estimado
# end_time: 2024-07-31T15:55:00Z # Estimado
# duration_minutes: 10 # Estimado
# files_modified:
#   - app/main.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/nicegui_research.md
#   - jules-flow/docs/reference/nicegui_langchain_integration_research.md
#   - jules-flow/docs/reference/langchain_research.md
#   - task-P2-DEV-01.md (relatório)
#   - VISION.md
# execution_details: |
#   1. Modificado o arquivo `app/main.py`.
#   2. Adicionadas importações para `run` de `nicegui` e `OrchestratorService` de `app.services.orchestrator`.
#   3. Instanciado `OrchestratorService` globalmente no módulo.
#   4. A função `main_page` foi convertida para `async def`.
#   5. Adicionado um `ui.input` para o nome do usuário e um `ui.markdown()` para exibir a saudação.
#   6. Adicionado um `ui.button("Gerar Saudação Gemini!")`.
#   7. Implementado um handler `async def on_generate_greeting_click()` para o botão:
#      - Obtém o valor do input de nome.
#      - Fornece feedback inicial na área de output ("Gerando saudação...").
#      - Chama `orchestrator.get_gemini_greeting(user_name)` usando `await run.io_bound()` para garantir que a chamada não bloqueie a UI.
#      - Exibe a saudação resultante ou uma mensagem de erro na área de output.
#      - Usa `ui.notify` para feedback rápido de sucesso ou erro.
#      - Loga erros no console do servidor.
#   8. Mantido o `ui.label('Olá, Mundo NiceGUI!')` original para compatibilidade com o teste P1-TEST-01.
#   9. Adicionado `storage_secret` à chamada `ui.run()` como boa prática, embora não estritamente usado por esta PoC.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/main.py`
* `app/services/orchestrator.py`

## Critérios de Aceitação
1. `app/main.py` tem input e botão.
2. Clique no botão chama orquestrador.
3. Resultado do LLM é exibido.
4. UI responsiva.

## Observações Adicionais
Completa a PoC NiceGUI <-> LangChain.
---
