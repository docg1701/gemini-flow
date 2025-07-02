---
id: task-P4-DEV-04
title: "WP4: Implementar chain LangChain para gerar GEMINI.md"
type: development
status: backlog
priority: high
dependencies: ["task-P2-DEV-01"]
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:13:00Z # Novo timestamp
updated_at: 2024-07-31T14:13:00Z
tags: ["development", "langchain", "documentation", "gemini", "ai-pair-programming"]
description: |
  Em `app/services/orchestrator.py`:
  1. Definir `generate_gemini_md_content(user_data: dict) -> str`.
  2. Receber `user_data` (todos os dados do wizard).
  3. Implementar chain(s) LangChain para gerar `GEMINI.md`.
  4. `GEMINI.md` deve refletir dinamicamente arquitetura, padrões, fluxos do projeto.
     - Seções: Visão Geral, Arquitetura, Tecnologias, Estrutura, Setup, etc.
  5. Prompt(s) serão extensos; considerar modularização ou chain of thought.
  6. Invocar chain(s) e retornar conteúdo do `GEMINI.md`.

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
1. Função para gerar `GEMINI.md` existe.
2. Usa LangChain e Gemini.
3. Prompt(s) abrangente e parametrizado.
4. Retorna string Markdown bem formatada para `gemini-cli`.

## Observações Adicionais
Task central. Qualidade do `GEMINI.md` é crucial.
---
