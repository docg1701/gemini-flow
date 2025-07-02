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
# outcome:
# outcome_reason:
# start_time:
# end_time:
# duration_minutes:
# files_modified:
#   - app/main.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/nicegui_research.md
#   - jules-flow/docs/reference/nicegui_langchain_integration_research.md
# execution_details: |
#   Detalhes da execução...
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
