---
id: task-FIX-001
title: "Melhorar fallback de mensagem de erro em `frontend/src/services/api.ts`"
type: fix
status: backlog
priority: low
dependencies: []
parent_plan_objective_id: ""
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-01T10:05:00Z
updated_at: 2024-07-01T10:05:00Z
tags: ["fix", "frontend", "error-handling"]
description: |
  Improve the error message fallback in `handleApiResponse` in `frontend/src/services/api.ts`.
  Currently, if `errorJson.detail` and `response.statusText` are both empty, the error message might be too generic (e.g., "HTTP error! Status: 500").
  Ensure a more informative default message is provided in such cases.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
outcome: success
outcome_reason: ""
start_time: 2024-07-01T10:40:00Z
end_time: 2024-07-01T10:45:00Z
duration_minutes: 5
files_modified:
  - frontend/src/services/api.ts
reference_documents_consulted: []
execution_details: |
  - Modified `frontend/src/services/api.ts` in the `handleApiResponse` function.
  - Changed the logic for setting `errorMessage`. It now prioritizes `errorJson.detail`.
  - If `errorJson.detail` is not found (either because `errorJson` is null, `detail` is missing, or JSON parsing failed), it falls back to `response.statusText`.
  - If `response.statusText` is also empty, it now defaults to a more specific message: `An unexpected error occurred (HTTP ${response.status})`.
  - Ensured `errorMessage` is trimmed.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/services/api.ts`

## Critérios de Aceitação
1. The `handleApiResponse` function provides a clear, informative default error message when `errorJson.detail` is not available and `response.statusText` is empty.
2. Error messages still prioritize `errorJson.detail` if available.

## Observações Adicionais
(Nenhuma)
