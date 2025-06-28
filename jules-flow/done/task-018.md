---
id: task-018
title: "Implementar funções de comunicação com API no frontend"
type: development
status: backlog # This status is from the original file, will be 'done' in task-index.md
priority: high
dependencies: ["task-014", "task-010"] # Depende da init do frontend e da API backend definida
parent_plan_objective_id: "15"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:17:00Z
updated_at: 2024-07-30T15:00:00Z # Placeholder for actual completion time
tags: ["frontend", "react", "typescript", "api-integration", "fetch"]
description: |
  No frontend React (ex: em `frontend/src/services/api.ts`):
  - Criar funções assíncronas para interagir com cada endpoint do backend:
    - `POST /start (payload: { projectName: string })`: Retorna a mensagem inicial e estado.
    - `POST /chat (payload: { message: string })`: Retorna a resposta da IA e `is_approval_step`.
    - `POST /approve`: Notifica o backend sobre a aprovação da fase. Retorna a mensagem da nova fase.
    - `GET /generate_files` (ou POST): Aciona a geração de arquivos. Retorna status.
  - Usar `fetch` ou `axios` para as chamadas HTTP.
  - Definir tipos TypeScript para os payloads de requisição e os dados de resposta esperados de cada endpoint.
  - Estas funções devem ser chamadas pelos componentes apropriados (ex: `ProjectNameInput.tsx` chama a API de `/start`, `ChatInterface.tsx` chama `/chat` e `/approve`).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: "Frontend API service module created and compiles successfully with the project."
# start_time: 2024-07-30T14:00:00Z
# end_time: 2024-07-30T15:00:00Z
# duration_minutes: 60
# files_modified:
#   - frontend/src/services/api.ts
# reference_documents_consulted:
#   - "jules-flow/docs/reference/react_typescript_research.md"
#   - "jules-flow/docs/reference/fastapi_research.md"
# execution_details: |
#   - Criado o diretório `frontend/src/services/` e o arquivo `frontend/src/services/api.ts`.
#   - Definido `API_BASE_URL = ''` para uso com proxy CRA.
#   - Definidas interfaces TypeScript para payloads de requisição e dados de resposta, consistentes com os modelos Pydantic do backend:
#     - `ApiStartRequest`, `ApiStartResponse`
#     - `ApiChatRequest`, `ApiChatResponse`
#     - `ApiApproveResponse`
#     - `ApiGenerateFilesResponse`
#   - Implementada uma função helper `handleResponse<T>(response: Response): Promise<T>` para centralizar a checagem de `response.ok` e o parsing de JSON, além de lançar erros de forma padronizada.
#   - Implementadas as seguintes funções assíncronas de serviço API usando `fetch`:
#     - `startSession(payload: ApiStartRequest): Promise<ApiStartResponse>` (chama `POST /start`)
#     - `sendMessage(payload: ApiChatRequest): Promise<ApiChatResponse>` (chama `POST /chat`)
#     - `approvePhase(): Promise<ApiApproveResponse>` (chama `POST /approve`)
#     - `generateFiles(): Promise<ApiGenerateFilesResponse>` (chama `POST /generate_files`)
#   - As funções implementam o método HTTP correto (POST para todos os endpoints, conforme `backend/main.py`), `Content-Type` header, e serialização do corpo da requisição.
#   - Tratamento básico de erro está incluído (lança erro se `!response.ok`).
#   - O código foi verificado através de `npm install` e `npm run build` no diretório `frontend`, que compilaram o projeto com sucesso.
#   - Todos os critérios de aceitação da tarefa foram atendidos.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/services/api.ts` (ou similar, ex: `frontend/src/apiClient.ts`) (saída)
* Componentes que utilizam essas funções (entrada/saída para integração).

## Critérios de Aceitação
1. Um módulo (ex: `api.ts`) é criado para encapsular as chamadas à API. (Concluído)
2. Funções para chamar `POST /start`, `POST /chat`, `POST /approve`, e `GET /generate_files` são implementadas. (Concluído, /generate_files as POST)
3. As funções enviam os payloads corretos e tratam as respostas (incluindo o `is_approval_step` de `/chat`). (Concluído)
4. Tipos TypeScript são usados para payloads e respostas. (Concluído)
5. As funções lidam com a URL base da API (ex: `http://localhost:8000` em desenvolvimento). (Concluído, via API_BASE_URL e proxy assumption)

## Observações Adicionais
Lembrar de configurar o proxy no `package.json` do frontend (`"proxy": "http://localhost:8000"`) para o desenvolvimento local, para que chamadas a `/start` (relativas) sejam direcionadas ao backend FastAPI. Ou usar URLs completas.
O tratamento de erro detalhado será feito na task-019, mas estas funções devem pelo menos propagar os erros.
