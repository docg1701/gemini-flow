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
created_at: 2024-07-31T14:11:00Z # Novo timestamp
updated_at: 2024-07-31T14:11:00Z
tags: ["development", "langchain", "gitignore", "code-generation"]
description: |
  Em `app/services/orchestrator.py`:
  1. Definir `generate_gitignore_content(user_data: dict) -> str`.
  2. Receber `user_data`.
  3. Construir chain LangChain (`PromptTemplate | LLM | StrOutputParser`).
     - `PromptTemplate` para gerar `.gitignore` para tecnologias escolhidas.
  4. Invocar chain e retornar conteúdo do `.gitignore`.

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
1. Função para gerar `.gitignore` existe.
2. Usa LangChain e Gemini.
3. Prompt parametrizado.
4. Retorna string do `.gitignore`.

## Observações Adicionais
Referenciar templates comuns de `.gitignore` no prompt.
---
