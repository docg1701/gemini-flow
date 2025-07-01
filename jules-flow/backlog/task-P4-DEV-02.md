---
id: task-P4-DEV-02
title: "WP4: Implementar chain LangChain para gerar .gitignore"
type: development
status: backlog
priority: medium
dependencies: ["task-P2-DEV-01"]
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T12:21:00Z
updated_at: 2024-07-31T12:21:00Z
tags: ["development", "langchain", "gitignore", "code-generation"]
description: |
  No arquivo `app/services/orchestrator.py`:
  1. Definir uma função (ex: `generate_gitignore_content(user_data: dict) -> str`).
  2. A função recebe `user_data` (dados do wizard).
  3. Construir uma chain LangChain (`PromptTemplate | LLM | StrOutputParser`).
     - O `PromptTemplate` instrui o Gemini a gerar um `.gitignore` apropriado para as tecnologias escolhidas pelo usuário (ex: Python, Node.js, arquivos de IDE comuns, arquivos de SO).
  4. Invocar a chain e retornar o conteúdo do `.gitignore` gerado.

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
#   - app/services/orchestrator.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/langchain_research.md
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/services/orchestrator.py`

## Critérios de Aceitação
1. Uma função para gerar conteúdo do `.gitignore` existe no `orchestrator.py`.
2. A função usa LangChain e Gemini.
3. O prompt é parametrizado com as tecnologias do projeto.
4. A função retorna uma string contendo as regras do `.gitignore`.

## Observações Adicionais
Pode-se referenciar templates de `.gitignore` comuns (ex: do GitHub) no prompt para guiar o LLM.
---
