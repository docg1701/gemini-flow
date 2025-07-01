---
id: task-P4-DEV-03
title: "WP4: Implementar chain LangChain para gerar novo requirements.txt"
type: development
status: backlog
priority: medium
dependencies: ["task-P1-DEV-02", "task-P2-DEV-01"] # P1-DEV-02 já lida com o requirements.txt inicial, esta é para gerar um dinâmico se necessário.
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T12:22:00Z
updated_at: 2024-07-31T12:22:00Z
tags: ["development", "langchain", "dependencies", "python"]
description: |
  No arquivo `app/services/orchestrator.py`:
  1. Definir uma função (ex: `generate_requirements_content(user_data: dict) -> str`).
  2. A função recebe `user_data` (dados do wizard, especialmente as tecnologias e bibliotecas Python escolhidas).
  3. Construir uma chain LangChain (`PromptTemplate | LLM | StrOutputParser`).
     - O `PromptTemplate` instrui o Gemini a listar as dependências Python (`requirements.txt` ou formato similar) com base nas escolhas do usuário.
     - Deve incluir `nicegui`, `langchain`, `langchain-google-genai` como base, mais quaisquer outras bibliotecas especificadas (ex: para um tipo de banco de dados, uma biblioteca de data science, etc.).
  4. Invocar a chain e retornar o conteúdo do `requirements.txt` gerado.
  5. Alternativamente, em vez de usar LLM para *gerar* o conteúdo, esta função pode *construir* o `requirements.txt` programaticamente com base nas escolhas do usuário, adicionando dependências fixas e condicionais. O LLM poderia ser usado para sugerir versões ou dependências adicionais com base em uma descrição de alto nível, se essa complexidade for desejada. Por ora, focar em uma lista baseada nas escolhas diretas do wizard.

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
1. Uma função para gerar/construir o conteúdo do `requirements.txt` existe no `orchestrator.py`.
2. A função inclui dependências base (`nicegui`, `langchain`, `langchain-google-genai`).
3. A função adiciona dependências com base nas escolhas do usuário no wizard.
4. A função retorna uma string formatada corretamente para um arquivo `requirements.txt`.

## Observações Adicionais
A task `task-P1-DEV-02` já atualiza o `requirements.txt` principal do projeto `gemini-flow`. Esta task (`P4-DEV-03`) refere-se à geração de um `requirements.txt` para o *projeto do usuário* que está sendo bootstrapped. É importante distinguir isso. A abordagem programática para construir o `requirements.txt` do projeto do usuário pode ser mais confiável do que depender de um LLM para listar dependências corretamente com versões.
---
