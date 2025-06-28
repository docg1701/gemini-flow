---
id: task-032
title: "Testes para a task-010 (API Principal FastAPI)"
type: test
status: backlog
priority: high
dependencies: ["task-010"]
parent_plan_objective_id: "7" # Corresponds to task-010's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-30T13:00:00Z # Placeholder time
updated_at: 2024-07-30T13:00:00Z # Placeholder time
tags: ["backend", "test", "fastapi", "api"]
description: |
  Esta tarefa visa criar e executar testes de integração para a API FastAPI implementada em `backend/main.py` (task-010).
  Os testes devem cobrir:
  - Interação com o endpoint `POST /start`: verificar resposta, inicialização de sessão.
  - Interação com o endpoint `POST /chat`: verificar envio de mensagem, recebimento de resposta (simulada do LLM), e estrutura da resposta.
  - Interação com o endpoint `POST /approve`: verificar mudança de estado no orquestrador e resposta da API.
  - Interação com o endpoint `POST /generate_files`: verificar resposta (mesmo que simulada a geração).
  - Interação com o endpoint `GET /health`: verificar status de saúde.
  - Validação de modelos Pydantic para requests e responses (FastAPI TestClient lida com isso em parte).
  - Tratamento de erros básicos (ex: request malformado, se aplicável).

  Crucialmente, esta tarefa DEVE tentar resolver ou encontrar um workaround para os problemas de execução do servidor Uvicorn e acesso ao arquivo `.env` que foram encontrados durante a `task-010`. Sem um servidor FastAPI funcional no ambiente de teste, estes testes não podem ser executados.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success | failure
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ
# end_time: YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: 0
# files_modified:
#   - backend/tests/test_main_api.py # Exemplo de arquivo de teste
# reference_documents_consulted: []
# execution_details: |
#   Detalhes da execução dos testes...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (entrada, para ser testado)
* `backend/orchestrator.py` (entrada, usado por main.py)
* `backend/config.py` (entrada, usado por orchestrator.py)
* `backend/tests/test_main_api.py` (saída, arquivo de teste a ser criado)
* `backend/pyproject.toml` (para garantir que `pytest` e `httpx` ou `requests` estejam como dependências de dev)
* `backend/.env` (necessário para o Orchestrator carregar a config)

## Critérios de Aceitação
1. Um novo arquivo de teste (ex: `backend/tests/test_main_api.py`) é criado.
2. Os testes utilizam o `TestClient` do FastAPI ou uma ferramenta similar (ex: `httpx`) para fazer requisições HTTP aos endpoints.
3. Os testes cobrem os endpoints `/start`, `/chat`, `/approve`, `/generate_files`, e `/health`.
4. Os testes verificam os códigos de status HTTP esperados e a estrutura básica das respostas JSON.
5. Os testes passam com sucesso.
6. **IMPRESCINDÍVEL**: O ambiente de execução de testes permite que o servidor FastAPI (`backend/main.py`) seja iniciado corretamente, incluindo o carregamento da configuração do `backend/.env`.

## Observações Adicionais
Revisar `fastapi_research.md` para informações sobre `TestClient`.
Se `httpx` for usado para testes assíncronos, adicionar ao `pyproject.toml`. (FastAPI's TestClient usa `httpx` por baixo dos panos).
O problema com `os.path.exists('/app/backend/.env')` retornando `False` no contexto do Uvicorn (observado na task-010) precisa ser a primeira coisa a ser investigada e resolvida. Se não for resolvido, esta tarefa não pode ser concluída com sucesso.
Considerar mockar o `Orchestrator` ou suas chamadas LLM para testes mais isolados e rápidos da API, se necessário, embora o objetivo primário seja testar a integração da API com o orquestrador (com LLM simulado).
A `task-009` já verificou que `pytest` está listado como dev dependency em `backend/pyproject.toml`.
O arquivo `backend/.env` com `GEMINI_API_KEY=PLACEHOLDER_API_KEY_FOR_TESTING` foi criado na `task-009`.
Os debug prints em `backend/config.py` devem ser removidos após a resolução do problema de carregamento do `.env`.
