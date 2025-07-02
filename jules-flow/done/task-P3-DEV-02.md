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
# outcome: success
# outcome_reason: Successfully created and integrated modular UI components for wizard steps, including data binding.
# start_time: 2024-08-01T21:30:00Z # Approximate
# end_time: 2024-08-01T21:45:00Z # Approximate
# duration_minutes: 15
# files_modified:
#   - app/ui/wizard_steps/__init__.py
#   - app/ui/wizard_steps/step_project_details.py
#   - app/ui/wizard_steps/step_tech_stack.py
#   - app/main.py # For integration and storage initialization
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/nicegui_research.md
#   - VISION.md
#   - task-P3-DEV-02.md (self)
# execution_details: |
#   1. Created `app/ui/wizard_steps/__init__.py` to make the directory a package.
#   2. Created `app/ui/wizard_steps/step_project_details.py` containing `create_project_details_ui()` function:
#      - Implemented `ui.input` for 'Nome do Projeto', bound to `app.storage.user['wizard_data']['project_name']` with not-empty validation.
#      - Implemented `ui.textarea` for 'Descrição do Projeto', bound to `app.storage.user['wizard_data']['project_description']`.
#   3. Created `app/ui/wizard_steps/step_tech_stack.py` containing `create_tech_stack_ui()` function:
#      - Implemented `ui.select` for 'Tecnologia Principal' (Python, JS, Java, Outra), bound to `app.storage.user['wizard_data']['main_technology']`.
#      - Implemented `ui.checkbox` elements for 'Recursos Adicionais' (Docker, CI/CD, Testes), bound to `app.storage.user['wizard_data']['additional_features']` (dictionary of booleans).
#   4. Modified `app/main.py`:
#      - Added `init_wizard_storage()` function to robustly initialize `app.storage.user['wizard_data']` and its nested structures ('additional_features', default values for inputs) before UI elements are created. This function is called in `main_page()`.
#      - Imported `create_project_details_ui` and `create_tech_stack_ui`.
#      - Called these functions within the 'Detalhes do Projeto' and 'Pilha Tecnológica' steps of the `ui.stepper`, replacing placeholders.
#   5. Verified the application by running `sudo PYTHONPATH="<path>" /opt/app-venv/bin/python app/main.py`.
#   6. The application started successfully; `app_server.log` showed no Python errors. Server was responsive.
#   7. UI elements for data collection are now in place within a modular structure.
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
