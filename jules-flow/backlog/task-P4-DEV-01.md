---
id: task-P4-DEV-01
title: "WP4: Implementar chain LangChain em orchestrator.py para gerar Dockerfile"
type: development
status: backlog
priority: high
dependencies: ["task-P2-DEV-01"] # Depende do orchestrator.py básico
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T12:20:00Z
updated_at: 2024-07-31T12:20:00Z
tags: ["development", "langchain", "dockerfile", "code-generation"]
description: |
  No arquivo `app/services/orchestrator.py`:
  1. Definir uma função (ex: `generate_dockerfile_content(user_data: dict) -> str`).
  2. Esta função deve receber os dados coletados do wizard (`user_data`) como entrada.
  3. Construir uma chain LangChain (usando LCEL: `PromptTemplate | LLM | StrOutputParser`).
     - O `PromptTemplate` deve ser projetado para instruir o modelo Gemini a gerar o conteúdo de um `Dockerfile`.
     - O prompt deve usar variáveis de `user_data` (ex: linguagem principal, framework, porta da aplicação, se precisa de banco de dados, etc.) para personalizar o Dockerfile.
  4. Invocar a chain com os dados do usuário.
  5. Retornar o conteúdo do Dockerfile gerado como uma string.

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
#   - app/services/file_templates/dockerfile_prompts.py (opcional, se os prompts forem externalizados)
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/langchain_research.md
#   - jules-flow/docs/reference/nicegui_langchain_integration_research.md
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/services/orchestrator.py`
* `app/services/file_templates/dockerfile_prompts.py` (se prompts forem separados)

## Critérios de Aceitação
1. Uma função para gerar conteúdo do Dockerfile existe no `orchestrator.py`.
2. A função usa LangChain e um modelo Gemini.
3. O prompt para o LLM é parametrizado com dados do usuário.
4. A função retorna uma string que representa o conteúdo de um Dockerfile.

## Observações Adicionais
A qualidade do Dockerfile gerado dependerá muito da qualidade do prompt. Pode ser necessário iterar no design do prompt.
---
