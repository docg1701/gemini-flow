---
id: task-P4-DEV-01
title: "WP4: Implementar chain LangChain em orchestrator.py para gerar Dockerfile"
type: development
status: backlog
priority: high
dependencies: ["task-P2-DEV-01"]
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:10:00Z # Novo timestamp
updated_at: 2024-07-31T14:10:00Z
tags: ["development", "langchain", "dockerfile", "code-generation"]
description: |
  Em `app/services/orchestrator.py`:
  1. Definir `generate_dockerfile_content(user_data: dict) -> str`.
  2. Receber `user_data` do wizard.
  3. Construir chain LangChain (`PromptTemplate | LLM | StrOutputParser`).
     - `PromptTemplate` para instruir Gemini a gerar Dockerfile.
     - Usar variáveis de `user_data` (linguagem, framework, porta, etc.).
  4. Invocar chain e retornar conteúdo do Dockerfile.

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
1. Função para gerar Dockerfile existe no orquestrador.
2. Usa LangChain e Gemini.
3. Prompt parametrizado com dados do usuário.
4. Retorna string do Dockerfile.

## Observações Adicionais
Qualidade do Dockerfile depende do prompt.
---
