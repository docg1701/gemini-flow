---
id: task-P3-DEV-02
title: "WP3: Criar módulos de UI para cada passo do wizard e coletar dados"
type: development
status: backlog
priority: high
dependencies: ["task-P3-DEV-01"]
parent_plan_objective_id: "3"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:08:00Z # Novo timestamp
updated_at: 2024-07-31T14:08:00Z
tags: ["development", "nicegui", "ui", "wizard", "form"]
description: |
  Para cada passo no `ui.stepper`:
  1. Criar módulo Python em `app/ui/wizard_steps/` (ex: `step_project_details.py`).
  2. Cada módulo com função (ex: `create_project_details_step_ui()`) que define elementos NiceGUI (`ui.input`, `ui.select`) para coletar informações.
  3. Usar `app.storage.user['wizard_data']` para armazenar dados, com `.bind_value()`.
  4. Importar e chamar funções nos respectivos `ui.step`.

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
#   - app/ui/wizard_steps/__init__.py
#   - app/ui/wizard_steps/step_project_details.py
#   # ... (outros arquivos de step)
#   - app/main.py # (para integrar)
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/nicegui_research.md
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/ui/wizard_steps/`
* `app/main.py`

## Critérios de Aceitação
1. Módulos para passos do wizard criados.
2. Cada módulo implementa UI para coleta de dados.
3. Dados armazenados (ex: em `app.storage.user['wizard_data']`).
4. Módulos integrados ao stepper principal.

## Observações Adicionais
Passo de revisão deve exibir dados de `app.storage.user['wizard_data']`.
---
