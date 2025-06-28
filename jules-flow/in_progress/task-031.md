---
id: task-031
title: "Testes para a task-009 (Máquina de Estados e Orquestrador do Backend)"
type: test
status: backlog
priority: high
dependencies: ["task-009"]
parent_plan_objective_id: "6" # Corresponds to task-009's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-30T11:00:00Z # Placeholder time
updated_at: 2024-07-30T11:00:00Z # Placeholder time
tags: ["backend", "test", "orchestrator", "statemachine"]
description: |
  Esta tarefa visa criar e executar testes unitários e de integração para o módulo `backend/orchestrator.py` implementado na `task-009`.
  Os testes devem cobrir:
  - Inicialização correta do `Orchestrator` e `SessionManager`.
  - Mudança de estados (`AppStates`) e carregamento correto dos respectivos prompts.
  - Adição de mensagens ao histórico de conversa.
  - Simulação (ou execução real se a API key estiver disponível e configurada para teste) da interação com o LLM (Gemini).
  - Verificação da lógica de `start_new_session`.
  - Tratamento de erros (ex: tentativa de mudar para estado inválido, falha no carregamento de prompt se arquivo ausente - embora `task-009` verificou que existem).
  - Garantir que `backend/config.py` é carregado corretamente e `GEMINI_API_KEY` é acessada (mesmo que seja um placeholder para o teste).
  - Se possível, resolver os problemas de execução do script `orchestrator.py` (via `poetry run python orchestrator.py`) que foram encontrados durante a `task-009` devido a problemas de acesso ao diretório `backend/` pela ferramenta `run_in_bash_session`. A capacidade de executar o script de teste é crucial.

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
#   - backend/tests/test_orchestrator.py # Exemplo de arquivo de teste
# reference_documents_consulted: []
# execution_details: |
#   Detalhes da execução dos testes...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/orchestrator.py` (entrada, para ser testado)
* `backend/config.py` (entrada)
* `prompts/*.md` (entrada, para verificar carregamento)
* `backend/tests/test_orchestrator.py` (saída, arquivo de teste a ser criado)
* `backend/pyproject.toml` (para garantir que `pytest` está como dependência de dev)

## Critérios de Aceitação
1. Um novo arquivo de teste (ex: `backend/tests/test_orchestrator.py`) é criado.
2. Os testes cobrem os principais aspectos funcionais do `SessionManager` e `Orchestrator`.
3. Os testes passam com sucesso, incluindo a simulação de interação com LLM.
4. (Idealmente) Os problemas de execução de scripts Python via `poetry run` no diretório `backend/` são resolvidos ou contornados para permitir a execução dos testes.

## Observações Adicionais
Considerar o uso de `pytest`. A `task-007` deveria ter adicionado `pytest` ao `pyproject.toml` nas dependências de desenvolvimento. Se não, adicionar.
A estrutura de diretórios para testes pode ser `backend/tests/`.
Lidar com a `GEMINI_API_KEY` (usar um placeholder seguro para testes, ou mockar a interação com `python-decouple` ou `settings`).
O problema com `run_in_bash_session` e `cd backend` precisa ser investigado; se persistir, pode impedir a execução de `pytest` via `poetry run pytest`.
Se o problema de `cd backend` persistir, deve ser reportado como um impedimento crítico.
A `task-009` já verificou que `python-decouple` está em `backend/pyproject.toml` e foi instalado.
A `task-009` também já verificou que `pytest` está listado como dev dependency em `backend/pyproject.toml`.
`backend/.env` foi criado com `GEMINI_API_KEY=PLACEHOLDER_API_KEY_FOR_TESTING` na task-009.
