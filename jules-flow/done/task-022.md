---
id: task-022
title: "Criar arquivo docker-compose.yml"
type: development
status: backlog
priority: high
dependencies: ["task-021"] # Depende do Dockerfile
parent_plan_objective_id: "19"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:21:00Z
updated_at: 2024-07-29T10:21:00Z
tags: ["docker", "docker-compose", "devops", "orchestration"]
description: |
  Criar um arquivo `docker-compose.yml` na raiz do projeto.
  Este arquivo deve definir e orquestrar os serviços `frontend` e `backend`:
  - **Serviço `backend`**:
    - `build`: context `.` e target `backend` do `Dockerfile` principal.
    - `ports`: mapear porta do container (ex: 8000) para uma porta do host (ex: 8000).
    - `env_file`: referenciar um arquivo `.env` para carregar variáveis de ambiente (como `GEMINI_API_KEY`).
    - `command`: (opcional, se não definido no Dockerfile) comando para iniciar Uvicorn.
    - `volumes`: (para desenvolvimento) mapear `./backend:/app` para hot-reloading.
  - **Serviço `frontend`**:
    - `build`: context `.` e target `frontend` do `Dockerfile` principal.
    - `ports`: mapear porta do container Nginx (ex: 80) para uma porta do host (ex: 3000).
    - `depends_on`: `backend` (para indicar dependência de inicialização, não de prontidão).
    - `volumes`: (para desenvolvimento com dev server) mapear `./frontend:/app`. Se servindo build estático, não é estritamente necessário para código, mas pode ser para config Nginx.
  Criar também um arquivo `.env.example` na raiz para documentar as variáveis de ambiente necessárias (ex: `GEMINI_API_KEY=SUA_CHAVE_AQUI`).

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
#   - docker-compose.yml
#   - .env.example
# reference_documents_consulted: ["jules-flow/docs/reference/docker_research.md"]
# execution_details: |
#   1. Criado o arquivo `.env.example` na raiz do projeto, incluindo `GEMINI_API_KEY` e placeholders para outras possíveis configurações.
#   2. Criado o arquivo `docker-compose.yml` versão '3.8' na raiz do projeto.
#   3. Definido o serviço `backend`:
#      - `build`: context `.`, `Dockerfile`, target `backend`.
#      - `ports`: "8000:8000".
#      - `env_file`: `['.env']`.
#      - `volumes`: `./backend:/app` para hot-reloading.
#      - `command`: `poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload`.
#      - `networks`: `['app-network']`.
#   4. Definido o serviço `frontend`:
#      - `build`: context `.`, `Dockerfile`, target `frontend`.
#      - `ports`: "3000:80".
#      - `depends_on`: `['backend']`.
#      - `networks`: `['app-network']`.
#      - Volumes para código não foram incluídos pois o Nginx serve o build estático da imagem.
#   5. Definida uma rede customizada `app-network` do tipo `bridge`.
#   6. A configuração segue as orientações da task e do `docker_research.md`.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `docker-compose.yml` (saída)
* `Dockerfile` (entrada)
* `.env.example` (saída)

## Critérios de Aceitação
1. O arquivo `docker-compose.yml` existe na raiz do projeto.
2. Define um serviço `backend` que usa o target `backend` do `Dockerfile`.
3. O serviço `backend` mapeia a porta 8000 e usa um `env_file`.
4. Define um serviço `frontend` que usa o target `frontend` do `Dockerfile`.
5. O serviço `frontend` mapeia uma porta (ex: 80 para 3000) e depende do `backend`.
6. O arquivo `.env.example` existe e lista `GEMINI_API_KEY`.
7. `docker-compose up --build` (após as tasks de código serem concluídas) deve construir e iniciar os containers (teoricamente).

## Observações Adicionais
Os volumes para hot-reloading são mais para um ambiente de desenvolvimento. Para uma "build final", o código já estaria nas imagens. O `working-plan.md` foca na aplicação final, então os volumes podem ser omitidos no `docker-compose.yml` principal se a intenção for apenas rodar a versão buildada. No entanto, para desenvolvimento iterativo por Jules, volumes podem ser úteis. Vamos incluir volumes para desenvolvimento, pois é uma prática comum.
A comunicação entre frontend e backend dentro da rede Docker (se o Nginx fizer proxy) usaria `http://backend:8000`. Se o frontend (React no browser) chama diretamente, usa `http://localhost:8000` (assumindo que a porta 8000 do backend está exposta no host). Para o Nginx servir o frontend e também fazer proxy para o backend, a configuração do Nginx precisaria ser mais elaborada. Para este escopo, o React chamará `localhost:8000`.
