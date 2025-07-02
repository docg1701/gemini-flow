---
id: task-P5-DEV-01
title: "WP5: Implementar criação de diretório de saída e salvamento de arquivos"
type: development
status: backlog
priority: high
dependencies: ["task-P4-DEV-01", "task-P4-DEV-02", "task-P4-DEV-03", "task-P4-DEV-04"]
parent_plan_objective_id: "5"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:15:00Z # Novo timestamp
updated_at: 2024-07-31T14:15:00Z
tags: ["development", "file-io", "output"]
description: |
  Implementar lógica de saída de arquivos (em `app/services/orchestrator.py` ou `app/main.py`).
  1. Obter nome do projeto de `user_data['project_name']`.
  2. Criar diretório `output/<project_name>/`.
     - Sanitize nome do projeto para nome de diretório válido.
     - Lidar com diretório existente (inicialmente, pode sobrescrever ou falhar).
  3. Escrever conteúdo gerado (Dockerfile, .gitignore, etc.) nos arquivos correspondentes.
  4. Retornar caminho do diretório de saída.

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
#   - app/services/orchestrator.py  # Ou app/main.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/services/orchestrator.py`
* `app/main.py`
* `output/`

## Critérios de Aceitação
1. Diretório `output/<project_name>/` criado.
2. Arquivos gerados salvos corretamente.
3. Função retorna caminho do diretório de saída.
4. Nome do projeto sanitizado.

## Observações Adicionais
Usar `pathlib`.
---
