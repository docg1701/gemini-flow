---
id: task-P1-DEV-02
title: "WP1: Atualizar requirements.txt para NiceGUI e LangChain"
type: development
status: backlog
priority: high
dependencies: ["task-P1-DEV-01"]
parent_plan_objective_id: "1"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:01:00Z # Novo timestamp
updated_at: 2024-07-31T14:01:00Z
tags: ["dependencies", "python", "nicegui", "langchain"]
description: |
  Atualizar o arquivo `requirements.txt` na raiz do projeto para refletir a nova pilha tecnológica:
  1. Adicionar `nicegui`.
  2. Adicionar `langchain`.
  3. Adicionar `langchain-google-genai` (para integração com Gemini).
  4. Adicionar `python-dotenv` (para carregar configurações de .env, se a estratégia de config usar).
  5. Adicionar `pydantic` e `pydantic-settings` (se for usar para config ou modelos de dados).
  6. Remover `fastapi` e `uvicorn` (e outras dependências específicas do backend FastAPI antigo, como `python-decouple` se substituído).
  7. Remover quaisquer dependências que eram exclusivamente para o frontend React/TypeScript antigo (se por acaso estivessem listadas no `requirements.txt` principal, o que é incomum mas deve ser verificado).
  8. Garantir que `pytest` (se já presente) seja mantido para testes. `httpx` também pode ser útil.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: 2024-07-31T14:45:00Z # Estimado
# end_time: 2024-07-31T14:50:00Z # Estimado
# duration_minutes: 5 # Estimado
# files_modified:
#   - requirements.txt
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - VISION.md
#   - jules-flow/docs/reference/nicegui_research.md
#   - jules-flow/docs/reference/langchain_research.md
# execution_details: |
#   1. Lido o arquivo `requirements.txt` existente.
#   2. Identificadas dependências a remover: `fastapi`, `uvicorn`, `python-decouple`.
#   3. Identificadas dependências a adicionar: `nicegui`, `langchain`, `langchain-google-genai`, `python-dotenv`, `pydantic`, `pydantic-settings`.
#   4. Dependências `pytest` e `httpx` foram mantidas.
#   5. O arquivo `requirements.txt` foi sobrescrito com a nova lista de dependências, uma por linha.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `requirements.txt`

## Critérios de Aceitação
1. `requirements.txt` contém `nicegui`.
2. `requirements.txt` contém `langchain`.
3. `requirements.txt` contém `langchain-google-genai`.
4. `requirements.txt` contém `python-dotenv` e/ou `pydantic`, `pydantic-settings` conforme decidido para a estratégia de configuração e modelagem.
5. `requirements.txt` NÃO contém `fastapi` ou `uvicorn`.
6. O arquivo está formatado corretamente (uma dependência por linha).

## Observações Adicionais
Consultar a documentação do NiceGUI e LangChain para versões específicas recomendadas. O `requirements.txt` atual contém: `pytest`, `fastapi`, `uvicorn`, `httpx`, `python-decouple`.
---
