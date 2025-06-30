---
id: task-024
title: "Testes para a task-004"
type: test
status: backlog
priority: high
dependencies: ["task-004"]
parent_plan_objective_id: "1" # Corresponds to objective 1 in working-plan.md
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder, to be filled by platform
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder, to be filled by platform
tags: ["test", "estrutura"]
description: |
  Validar a estrutura de diretórios criada pela task-004.
  Esta tarefa deve verificar se os diretórios `backend/`, `frontend/`, e `prompts/` existem na raiz do projeto.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# duration_minutes: 0 # Placeholder
# files_modified: []
# reference_documents_consulted: [] # None needed
# execution_details: |
#   Teste para verificar a existência dos diretórios base do projeto.
#   Critérios de Aceitação:
#   1. O diretório `backend` existe na raiz do projeto.
#   2. O diretório `frontend` existe na raiz do projeto.
#   3. O diretório `prompts` existe na raiz do projeto.
#
#   Comandos executados e resultados:
#   1. `ls -d backend/`
#      Output: `backend/`
#      Status: Sucesso (diretório existe)
#
#   2. `ls -d frontend/`
#      Output: `frontend/`
#      Status: Sucesso (diretório existe)
#
#   3. `ls -d prompts/`
#      Output: `prompts/`
#      Status: Sucesso (diretório existe)
#
#   Conclusão: Todos os diretórios especificados existem. A tarefa `task-004` foi implementada corretamente em relação à criação destes diretórios.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/`
* `frontend/`
* `prompts/`

## Critérios de Aceitação
1. O diretório `backend` existe na raiz do projeto.
2. O diretório `frontend` existe na raiz do projeto.
3. O diretório `prompts` existe na raiz do projeto.
4. A tarefa deve ser concluída com sucesso se todos os diretórios existirem.

## Observações Adicionais
Esta tarefa de teste é gerada automaticamente após a conclusão de `task-004` (development).
Os testes podem ser simples verificações de existência de diretórios.
