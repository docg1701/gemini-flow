---
id: task-018
title: "Implementar funções de comunicação com API no frontend"
type: development
status: backlog
priority: high
dependencies: ["task-014", "task-010"] # Depende da init do frontend e da API backend definida
parent_plan_objective_id: "15"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:17:00Z
updated_at: 2024-07-29T10:17:00Z
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
# outcome: success | failure
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ
# end_time: YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: 0
# files_modified:
#   - frontend/src/services/api.ts
#   # (ou similar)
# reference_documents_consulted: ["react_typescript_research.md", "fastapi_research.md"]
# execution_details: |
#   Funções para chamar os endpoints /start, /chat, /approve, /generate_files implementadas em frontend/src/services/api.ts.
#   Tipos de payload e resposta definidos.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/services/api.ts` (ou similar, ex: `frontend/src/apiClient.ts`) (saída)
* Componentes que utilizam essas funções (entrada/saída para integração).

## Critérios de Aceitação
1. Um módulo (ex: `api.ts`) é criado para encapsular as chamadas à API.
2. Funções para chamar `POST /start`, `POST /chat`, `POST /approve`, e `GET /generate_files` são implementadas.
3. As funções enviam os payloads corretos e tratam as respostas (incluindo o `is_approval_step` de `/chat`).
4. Tipos TypeScript são usados para payloads e respostas.
5. As funções lidam com a URL base da API (ex: `http://localhost:8000` em desenvolvimento).

## Observações Adicionais
Lembrar de configurar o proxy no `package.json` do frontend (`"proxy": "http://localhost:8000"`) para o desenvolvimento local, para que chamadas a `/start` (relativas) sejam direcionadas ao backend FastAPI. Ou usar URLs completas.
O tratamento de erro detalhado será feito na task-019, mas estas funções devem pelo menos propagar os erros.
