---
id: task-REF-003
title: "Refatorar lógica de aprovação e mensagem inicial de nova fase em `backend/main.py`"
type: refactor
status: backlog
priority: medium
dependencies: []
parent_plan_objective_id: ""
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-01T10:15:00Z
updated_at: 2024-07-01T10:15:00Z
tags: ["refactor", "backend", "api"]
description: |
  Refactor the `/approve` endpoint in `backend/main.py`.
  The current implementation calls `orchestrator.process_user_message` with a hardcoded message like `"Ok, aprovei a fase anterior. O que faremos em {next_state_enum.value}?"` to get the initial message for the new phase.
  This is somewhat artificial. Explore options such as:
  1. Modifying `orchestrator.change_phase` to return an initial system message for the new phase.
  2. Having the frontend simply display the new phase's prompt/initial state based on the new state information, without needing a canned AI message to kickstart the new phase display.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
outcome: success
outcome_reason: ""
start_time: 2024-07-01T11:00:00Z
end_time: 2024-07-01T11:10:00Z
duration_minutes: 10
files_modified:
  - backend/orchestrator.py
  - backend/main.py
reference_documents_consulted: []
execution_details: |
  - Modified `backend/orchestrator.py`:
    - The `SessionManager.change_state` method now returns a string, which is the first line of the newly loaded prompt template, prefixed with a message indicating the new prompt is loaded.
    - The `Orchestrator.change_phase` method now uses this returned string as the "message" in its response dictionary.
  - Modified `backend/main.py`:
    - The `/approve` endpoint now directly uses the `message` returned by `orchestrator.change_phase`.
    - Removed the artificial call to `orchestrator.process_user_message` that was previously used to generate an initial message for the new phase.
  - Verified that the frontend's `ApiApproveResponse` interface and its usage in `App.tsx` are already expecting a `message` field, so no direct frontend changes were needed for this specific refactoring. The frontend will now display the more direct initial prompt message.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py`
* `backend/orchestrator.py` (Potencialmente)
* `frontend/src/App.tsx` (Potencialmente, dependendo da abordagem)
* `frontend/src/services/api.ts` (Potencialmente, dependendo da abordagem)

## Critérios de Aceitação
1. The artificial call to `process_user_message` with a hardcoded approval message in the `/approve` endpoint is removed.
2. The frontend correctly displays the initial context or prompt for the new phase after approval.
3. The transition between phases remains smooth for the user.

## Observações Adicionais
  Favor a abordagem que modifica `orchestrator.change_phase` para incluir ou fornecer o "prompt inicial" ou mensagem de sistema da nova fase, que pode então ser retornada diretamente pela API `/approve`.
