---
id: task-040
title: "Testes para a task-013 (Tratamento de Erros no Backend)"
type: test
status: backlog
priority: medium
dependencies: ["task-013"]
parent_plan_objective_id: "10" # Matches parent task-013's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
tags: ["backend", "test", "error-handling", "fastapi"]
description: |
  Validar o tratamento de erros implementado na task-013.
  Isto envolve:
  1. Criar cenários de teste que provoquem diferentes tipos de exceções:
      - Uma `OrchestratorError` (simulada ou induzida dentro de um endpoint de teste).
      - Uma `GeminiAPIError` (simulada ou induzida, por exemplo, mockando uma função no orquestrador para levantar esta exceção quando chamada por um endpoint).
      - Uma `google_exceptions.PermissionDenied` (simulada/mockada de forma similar).
      - Uma `HTTPException` padrão do FastAPI (ex: chamar um endpoint deliberadamente inexistente ou um que levante HTTPException).
      - Uma exceção genérica `Exception` num endpoint de teste dedicado a levantar exceções.
      - Uma `RequestValidationError` (enviando dados inválidos para um endpoint existente que use modelos Pydantic para o corpo da requisição).
  2. Para cada cenário, verificar se:
      - A resposta HTTP tem o status code correto esperado para aquele tipo de erro.
      - O corpo da resposta é JSON e contém os campos `detail` e `error_code` (quando aplicável) conforme definido nos handlers.
      - O log do servidor (stdout/stderr do container se rodando via Docker, ou capturado durante testes se possível) contém a mensagem de erro logada pelo handler correspondente. A verificação de log pode ser um "nice-to-have" se for complexa de implementar no ambiente de teste.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Actual time will be filled by execution platform
# end_time: YYYY-MM-DDTHH:MM:SSZ # Actual time will be filled by execution platform
# duration_minutes: 0 # Actual duration will be filled by execution platform
# files_modified: ["backend/tests/test_error_handling.py", "pytest.ini"]
# reference_documents_consulted: ["jules-flow/done/task-013.md", "jules-flow/docs/reference/fastapi_research.md", "https://fastapi.tiangolo.com/tutorial/testing/", "https://fastapi.tiangolo.com/advanced/testing-events/"]
# execution_details: |
#   1. Created `backend/tests/test_error_handling.py` with test cases for all specified error types:
#      - `OrchestratorError`
#      - `GeminiAPIError`
#      - `google_exceptions.PermissionDenied` (mocked)
#      - `google_exceptions.GoogleAPIError` (mocked, added for completeness based on task-013)
#      - `HTTPException` (from FastAPI)
#      - Generic `Exception`
#      - `RequestValidationError`
#      - Non-existent route (for 404 coverage)
#   2. Installed necessary dependencies: `pytest`, `google-api-core`, `fastapi`, `uvicorn`, `pydantic`, `httpx`, `pytest-anyio`, `trio`.
#   3. Modified test functions to be `async def` and marked with `@pytest.mark.anyio` for compatibility with `pytest-anyio`.
#   4. Created `pytest.ini` and configured it initially with `anyio_backend = asyncio`. This caused a warning.
#   5. Debugged test failures related to `pytest-anyio` setup:
#      - The `test_handle_generic_exception` was failing.
#      - `ModuleNotFoundError: No module named 'trio'` occurred because `pytest-anyio` attempts to run tests on multiple backends by default. Installed `trio`.
#      - The warning `Unknown config option: anyio_backend` persisted. Removed the option from `pytest.ini` as `pytest-anyio` (v0.0.0) might infer it or have other defaults. The warning disappeared.
#      - The `test_handle_generic_exception` still failed. Traced this to `TestClient`'s default behavior of `raise_server_exceptions=True`, which re-raises generic exceptions instead of allowing the app's handler to return a JSON response.
#   6. Fixed the final test failure by initializing `TestClient(app, raise_server_exceptions=False)`.
#   7. All tests passed successfully, covering status codes, JSON response bodies (`detail`, `error_code`), and different exception types. Log verification was not implemented as it was optional.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (entrada, para referência e para o TestClient interagir)
* `backend/orchestrator.py` (entrada, pode ser necessário mockar partes dele)
* `tests/test_error_handling.py` (saída, novo arquivo de teste a ser criado, ou adicionar a um existente como `backend/tests/test_main_api.py`)

## Critérios de Aceitação
1. Um novo arquivo de teste (ex: `backend/tests/test_error_handling.py`) é criado ou testes são adicionados a um arquivo existente.
2. Testes unitários/de integração usando `TestClient` são implementados para cobrir os cenários de exceção listados na descrição.
3. Cada teste afirma (asserts) o status code HTTP correto da resposta.
4. Cada teste afirma o formato JSON da resposta e a presença/conteúdo dos campos `detail` e `error_code` (quando esperado).
5. (Opcional, se viável) Testes tentam capturar e verificar mensagens de log específicas.

## Observações Adicionais
- Usar o `TestClient` do FastAPI é a abordagem padrão.
- A biblioteca `unittest.mock` (ou `pytest-mock`) será essencial para simular ("mock") as condições que levantam exceções específicas, especialmente para aquelas originadas de chamadas externas (como a API do Gemini) ou de partes profundas do código (como o Orchestrator).
- Para testar o handler de `RequestValidationError`, envie uma requisição com corpo inválido para um endpoint que espere um modelo Pydantic.
- Para testar o handler de `HTTPException`, pode-se criar um endpoint de teste simples que diretamente levante uma `HTTPException`, ou testar um endpoint que já faz isso (como o `/generate_files` se a sessão não estiver no estado DEVOPS).
- Para testar o handler de `Exception` genérica, crie um endpoint de teste que simplesmente faça `raise Exception("Erro de teste genérico")`.
- Os `error_code`s definidos nos handlers devem ser verificados nas respostas.
