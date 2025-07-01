---
id: task-P4-TEST-01
title: "WP4: Testes unitários para as chains de geração de arquivos no orquestrador"
type: test
status: backlog
priority: medium
dependencies: ["task-P4-DEV-01", "task-P4-DEV-02", "task-P4-DEV-03", "task-P4-DEV-04"]
parent_plan_objective_id: "4" # Também cobre parte do Passo 6 do working-plan
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T12:24:00Z
updated_at: 2024-07-31T12:24:00Z
tags: ["test", "unittest", "langchain", "code-generation"]
description: |
  Criar testes unitários para as funções de geração de conteúdo de arquivo em `app/services/orchestrator.py`.
  1. Para cada função de geração (Dockerfile, .gitignore, requirements.txt, GEMINI.md):
     - Mockar a chamada ao LLM (ex: usando `FakeLLM` do LangChain ou `unittest.mock.patch` para o método `.invoke()` do LLM).
     - Fornecer dados de entrada (`user_data`) de exemplo.
     - Verificar se o `PromptTemplate` é formatado corretamente com os dados de entrada.
     - Se o LLM é mockado para retornar um conteúdo específico, verificar se a função do orquestrador retorna esse conteúdo (ou o processa corretamente).
     - Para a geração programática de `requirements.txt` (se essa abordagem for escolhida sobre LLM), testar a lógica de construção da lista de dependências.
  2. Os testes devem ser colocados em `tests/test_orchestrator.py` (ou similar).
  3. Garantir que os testes sejam rápidos e não façam chamadas reais à API do LLM.

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
#   - tests/__init__.py (se não existir)
#   - tests/test_orchestrator.py (para criação/atualização)
# reference_documents_consulted:
#   - app/services/orchestrator.py
#   - jules-flow/docs/reference/langchain_research.md
#   - jules-flow/docs/reference/monolithic_project_structure_research.md (para estrutura de testes)
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `tests/test_orchestrator.py`
* `app/services/orchestrator.py` (para referência)

## Critérios de Aceitação
1. Testes unitários são criados para cada função de geração de arquivo no orquestrador.
2. Os testes mockam chamadas a LLMs.
3. Os testes verificam a formatação correta dos prompts e/ou a lógica de processamento de saída.
4. Os testes passam quando executados (ex: via `pytest`).

## Observações Adicionais
Estes testes são cruciais para garantir a confiabilidade da lógica de geração de arquivos.
---
