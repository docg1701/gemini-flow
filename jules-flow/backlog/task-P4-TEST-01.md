---
id: task-P4-TEST-01
title: "WP4: Testes unitários para as chains de geração de arquivos no orquestrador"
type: test
status: backlog
priority: medium
dependencies: ["task-P4-DEV-01", "task-P4-DEV-02", "task-P4-DEV-03", "task-P4-DEV-04"]
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:14:00Z # Novo timestamp
updated_at: 2024-07-31T14:14:00Z
tags: ["test", "unittest", "langchain", "code-generation"]
description: |
  Criar testes unitários para `app/services/orchestrator.py`.
  1. Para cada função de geração (Dockerfile, .gitignore, requirements.txt, GEMINI.md):
     - Mockar chamada LLM (`FakeLLM` ou `unittest.mock.patch`).
     - Fornecer `user_data` de exemplo.
     - Verificar formatação do `PromptTemplate`.
     - Verificar se função retorna conteúdo esperado (mockado).
     - Testar lógica de construção programática (ex: para `requirements.txt`).
  2. Testes em `tests/test_orchestrator.py`.
  3. Testes rápidos, sem chamadas reais à API LLM.

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
#   - tests/test_orchestrator.py
# reference_documents_consulted:
#   - app/services/orchestrator.py
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `tests/test_orchestrator.py`
* `app/services/orchestrator.py`

## Critérios de Aceitação
1. Testes unitários para cada função de geração.
2. Chamadas LLM mockadas.
3. Verificam prompts e/ou lógica de saída.
4. Testes passam (`pytest`).

## Observações Adicionais
Crucial para confiabilidade da geração de arquivos.
---
