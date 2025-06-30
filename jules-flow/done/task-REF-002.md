---
id: task-REF-002
title: "Refatorar configuração de PYTHONPATH em `run_tests.sh`"
type: refactor
status: backlog
priority: low
dependencies: []
parent_plan_objective_id: ""
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-01T10:10:00Z
updated_at: 2024-07-01T10:10:00Z
tags: ["refactor", "testing", "shellscript"]
description: |
  Refactor the `PYTHONPATH` setting in `run_tests.sh`.
  Currently, `PYTHONPATH` is set using `export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH}"` multiple times, which can lead to the project root path being prepended repeatedly.
  A more robust approach is to set it to `export PYTHONPATH="${PROJECT_ROOT}"` or ensure it's added only once if a prior `PYTHONPATH` is essential (which is unlikely for this script's context for backend tests).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
outcome: success
outcome_reason: ""
start_time: 2024-07-01T10:50:00Z
end_time: 2024-07-01T10:55:00Z
duration_minutes: 5
files_modified:
  - run_tests.sh
reference_documents_consulted: []
execution_details: |
  - Modified `run_tests.sh`.
  - Changed instances of `export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH}"` to `export PYTHONPATH="${PROJECT_ROOT}"` in the backend testing sections.
  - This simplifies the `PYTHONPATH` and avoids potential issues with the project root being added multiple times to the path.
  - For commands run via `poetry run` (like `py_compile`), `PYTHONPATH` manipulation is often not strictly necessary as Poetry adjusts `sys.path` for its execution environment. However, explicitly setting `PYTHONPATH="${PROJECT_ROOT}"` for direct `python -m backend.orchestrator` and `uvicorn backend.main:app` calls, and for `pytest` ensures clarity and robustness, especially if the script were run in diverse environments or if Poetry's path handling had subtle differences.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `run_tests.sh`

## Critérios de Aceitação
1. `PYTHONPATH` is set cleanly and correctly in `run_tests.sh` for backend tests, avoiding redundant path additions.
2. Backend tests (especially those involving module imports from the project root) continue to pass after the change.

## Observações Adicionais
  Consider using `export PYTHONPATH="${PROJECT_ROOT}"` as the primary method for the backend test sections.
