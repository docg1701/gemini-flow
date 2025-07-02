---
id: task-P2-DEV-01
title: "WP2: Criar app/services/orchestrator.py com função básica LangChain/Gemini"
type: development
status: backlog
priority: high
dependencies: ["task-P1-DEV-03"]
parent_plan_objective_id: "2"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:04:00Z # Novo timestamp
updated_at: 2024-07-31T14:04:00Z
tags: ["development", "langchain", "gemini", "poc", "backend"]
description: |
  1. Criar o diretório `app/services/`.
  2. Adicionar um arquivo `app/services/__init__.py`.
  3. Criar o arquivo `app/services/orchestrator.py`.
  4. Neste arquivo, implementar uma classe `OrchestratorService` (ou similar).
  5. Adicionar um método simples ao serviço (ex: `get_gemini_greeting(name: str) -> str`).
  6. Este método deve usar LangChain com um modelo Gemini para gerar uma saudação personalizada.
     Exemplo de prompt: "Crie uma saudação curta e amigável para {name}."
  7. A função deve retornar a saudação gerada.
  8. Configurar o acesso à API Gemini (uso de chave de API via `app/core/config.py`).

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
#   - app/services/__init__.py
#   - app/services/orchestrator.py
#   - app/core/config.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/langchain_research.md
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/services/__init__.py`
* `app/services/orchestrator.py`
* `app/core/config.py`

## Critérios de Aceitação
1. `app/services/orchestrator.py` existe com a função de saudação.
2. A função usa LangChain e Gemini.
3. A função retorna uma saudação string.
4. Uso seguro da chave API.

## Observações Adicionais
Primeira integração com LangChain/Gemini.
---
