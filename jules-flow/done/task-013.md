---
id: task-013
title: "Implementar tratamento de erros no backend"
type: development
status: backlog
priority: medium
dependencies: ["task-010"] # Depende da API principal
parent_plan_objective_id: "10"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:12:00Z
updated_at: 2024-07-29T10:12:00Z
tags: ["backend", "fastapi", "error-handling", "middleware"]
description: |
  No `backend/main.py`, adicionar um middleware FastAPI ou handlers de exceção para:
  - Capturar exceções genéricas e exceções específicas (ex: falha ao chamar a API do Gemini, erro de validação Pydantic não pego automaticamente).
  - Retornar respostas de erro HTTP padronizadas em formato JSON (ex: `{"detail": "Mensagem de erro", "error_code": "CODIGO_ERRO"}`).
  - Logar os erros para fins de depuração.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# duration_minutes: 0 # Placeholder
# files_modified:
#   - backend/main.py
# reference_documents_consulted: ["fastapi_research.md", "https://fastapi.tiangolo.com/tutorial/handling-errors/", "https://fastapi.tiangolo.com/advanced/middleware/"]
# execution_details: |
#   1. Imported `logging`, `Request`, `JSONResponse` from FastAPI.
#   2. Added placeholder imports for `google.api_core.exceptions` to define handlers for potential Google API errors.
#   3. Configured basic logging using `logging.basicConfig(level=logging.INFO)`.
#   4. Defined custom exceptions: `OrchestratorError` and `GeminiAPIError`.
#   5. Implemented global exception handlers in `backend/main.py` using `@app.exception_handler`:
#      - `OrchestratorError`: Returns 400 with error code.
#      - `GeminiAPIError`: Returns 502 with error code.
#      - `google_exceptions.PermissionDenied`: Returns 502 with error code.
#      - `google_exceptions.GoogleAPIError`: Returns 502 with error code.
#      - `HTTPException` (FastAPI's own): Custom handler to ensure logging and add a generic "HTTP_EXCEPTION" error_code.
#      - `Exception` (generic fallback): Returns 500 with "INTERNAL_SERVER_ERROR" code.
#   6. All handlers log the error with relevant details.
#   7. Responses are standardized to JSON with `detail` and `error_code` fields.
#   8. Existing try/except blocks in endpoints that raised generic HTTPExceptions will now often be caught by these more specific global handlers or the custom HTTPException handler, ensuring logging and standardized format.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (entrada/saída)

## Critérios de Aceitação
1. Um middleware FastAPI ou `@app.exception_handler` está configurado em `backend/main.py`.
2. O sistema captura exceções comuns (ex: `ValueError`, `HTTPException` customizadas, exceções de `langchain` ou `google-generativeai`).
3. Respostas de erro são formatadas como JSON com um campo `detail`.
4. Os erros são logados no servidor (usando o logger padrão do Python ou um configurado).

## Observações Adicionais
Consultar a documentação do FastAPI sobre "Error Handling" e "Middleware" para as melhores práticas.
O `working-plan.md` menciona especificamente "falha na API do Gemini".
