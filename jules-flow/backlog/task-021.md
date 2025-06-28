---
id: task-021
title: "Criar Dockerfile multi-stage"
type: development
status: backlog
priority: high
dependencies: ["task-003", "task-007", "task-014"] # Depende da pesquisa Docker, init backend, init frontend
parent_plan_objective_id: "18"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:20:00Z
updated_at: 2024-07-29T10:20:00Z
tags: ["docker", "container", "devops", "dockerfile"]
description: |
  Criar um arquivo `Dockerfile` na raiz do projeto.
  Este Dockerfile deve ser multi-stage para construir e servir tanto o frontend React quanto o backend FastAPI.
  - **Frontend Stages**:
    1. `frontend-builder`: Baseado em Node, instala dependências do frontend (`frontend/package.json`) e executa `npm run build`.
    2. `frontend`: Baseado em Nginx, copia os artefatos de build do `frontend-builder` e serve-os. Pode precisar de uma configuração Nginx customizada simples para roteamento client-side.
  - **Backend Stage**:
    1. `backend`: Baseado em Python, instala dependências do backend (`backend/pyproject.toml` ou `backend/requirements.txt`), copia o código do backend e define o CMD para rodar Uvicorn.

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
#   - Dockerfile
#   - nginx.conf (opcional, se customizado para o frontend)
# reference_documents_consulted: ["docker_research.md"]
# execution_details: |
#   Dockerfile multi-stage criado na raiz do projeto com stages para frontend-builder, frontend (nginx), e backend (python/uvicorn).
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `Dockerfile` (saída)
* `frontend/` (entrada, código fonte e `package.json`)
* `backend/` (entrada, código fonte e `pyproject.toml`/`requirements.txt`)
* `nginx.conf` (opcional, se um Nginx customizado for necessário para o stage `frontend`) (saída)

## Critérios de Aceitação
1. O arquivo `Dockerfile` existe na raiz do projeto.
2. O Dockerfile contém um stage alias `frontend-builder` que constrói a aplicação React.
3. O Dockerfile contém um stage alias `frontend` (baseado em Nginx) que serve o build do React.
4. O Dockerfile contém um stage alias `backend` (baseado em Python) que prepara e pode rodar a aplicação FastAPI.
5. O Dockerfile é otimizado para tamanho de imagem e cache de layers (ex: copiar arquivos de manifesto e instalar dependências antes de copiar o resto do código).

## Observações Adicionais
O `docker-compose.yml` (task-022) usará os `target` stages deste Dockerfile para construir as imagens finais para cada serviço.
Uma configuração Nginx simples para o frontend pode ser necessária para garantir que todas as rotas do React (client-side routing) sejam direcionadas para `index.html`.
Exemplo `nginx.conf` para React Router:
```nginx
server {
  listen 80;
  root /usr/share/nginx/html;
  index index.html index.htm;

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```
Este arquivo `nginx.conf` seria copiado para o stage `frontend` do Dockerfile.
