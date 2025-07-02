---
id: task-P3-TEST-02 # Assuming this ID is available
title: "Testes para a task-P3-DEV-02 (Coleta de Dados nos Passos do Wizard)"
type: test
status: backlog
priority: medium
dependencies: ["task-P3-DEV-02"] # Depends on the dev task just completed
parent_plan_objective_id: "3" # Part of Work Package 3
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-08-01T22:00:00Z # Approximate current time
updated_at: 2024-08-01T22:00:00Z
tags: ["test", "nicegui", "wizard", "form-input", "data-binding"]
description: |
  Testar a funcionalidade de coleta de dados implementada nos módulos de UI dos passos do wizard, especificamente para os elementos criados em `task-P3-DEV-02`.
  1. Verificar se os campos de entrada (Nome do Projeto, Descrição) no passo "Detalhes do Projeto" são renderizados corretamente.
  2. Testar a validação do campo "Nome do Projeto" (ex: não permitir vazio).
  3. Verificar se os dados inseridos em "Nome do Projeto" e "Descrição do Projeto" são corretamente vinculados e armazenados em `app.storage.user['wizard_data']['project_name']` e `app.storage.user['wizard_data']['project_description']`.
  4. Verificar se os elementos de seleção (`ui.select` para Tecnologia Principal, `ui.checkbox` para Recursos Adicionais) no passo "Pilha Tecnológica" são renderizados.
  5. Verificar se as seleções feitas nestes campos são corretamente vinculadas e armazenadas em `app.storage.user['wizard_data']['main_technology']` and `app.storage.user['wizard_data']['additional_features']`.
  6. (Simulado/Inferido) Assegurar que a estrutura de `app.storage.user['wizard_data']` é corretamente inicializada e atualizada.

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
#   # Potentially test scripts if this were fully automated, or none if manual verification
# reference_documents_consulted:
#   - task-P3-DEV-02.md
#   - app/main.py
#   - app/ui/wizard_steps/step_project_details.py
#   - app/ui/wizard_steps/step_tech_stack.py
# execution_details: |
#   Detalhes da execução do teste...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/main.py` (para executar a UI)
* `app/ui/wizard_steps/step_project_details.py` (para referência dos elementos)
* `app/ui/wizard_steps/step_tech_stack.py` (para referência dos elementos)
* `app.storage.user` (para verificar o armazenamento de dados - indiretamente)

## Critérios de Aceitação
1. Inputs para detalhes do projeto (nome, descrição) funcionam e os dados são armazenados.
2. Validação do nome do projeto funciona.
3. Seletores para pilha tecnológica (tecnologia principal, recursos adicionais) funcionam e os dados são armazenados.
4. Nenhuma regressão ou erro introduzido na navegação básica do stepper.

## Observações Adicionais
Este teste foca nos elementos de UI e na vinculação de dados introduzidos por `task-P3-DEV-02`.
A navegação geral do stepper é coberta mais amplamente por `task-P3-TEST-01` (quando ambas as tasks de desenvolvimento P3 estiverem concluídas).
---
