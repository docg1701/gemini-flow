---
id: task-036
title: "Testes para a task-022 (docker-compose.yml)"
type: test
status: backlog
priority: high
dependencies: ["task-022"]
parent_plan_objective_id: "19" # Corresponds to task-022's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
tags: ["docker", "docker-compose", "test", "orchestration"]
description: |
  Validar o `docker-compose.yml` e a capacidade de orquestrar os serviços definidos na task-022.
  O objetivo é garantir que os containers `frontend` e `backend` podem ser construídos e iniciados corretamente usando o Docker Compose.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: failure
# outcome_reason: "Backend container fails to start due to ModuleNotFoundError: No module named 'backend'. Imports in backend/main.py are structured as 'from backend.module' but the Dockerfile copies contents of the 'backend' directory directly into '/app', meaning modules are at the root of the Python path within the container, not under a 'backend' namespace."
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# duration_minutes: 0 # Placeholder
# files_modified: [".env"]
# reference_documents_consulted: ["Dockerfile", "backend/main.py", "docker-compose.yml"]
# execution_details: |
#   1. Created .env file with GEMINI_API_KEY=TEST_KEY_VALID_FORMAT.
#   2. Ran `sudo docker compose -f docker-compose.yml up --build -d`. Command executed, images built, containers started.
#   3. Ran `sudo docker compose ps`. Output showed both backend and frontend containers running.
#   4. Ran `sudo docker compose logs backend`. Log revealed:
#      Traceback (most recent call last):
#        ...
#        File "/app/main.py", line 5, in <module>
#          from backend.orchestrator import Orchestrator, AppStates
#      ModuleNotFoundError: No module named 'backend'
#   5. Test failed due to backend container error. `sudo docker compose down` will be run as part of cleanup.
#   6. `.env` file created for the test will be removed as part of cleanup.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `docker-compose.yml` (entrada)
* `Dockerfile` (entrada)
* `.env.example` (entrada, para referência, mas um `.env` real seria necessário para `docker compose up`)
* `frontend/` (entrada, para contexto de build)
* `backend/` (entrada, para contexto de build)
* `nginx.conf` (entrada, para contexto de build)

## Critérios de Aceitação
1. Criar um arquivo `.env` na raiz do projeto a partir do `.env.example`, preenchendo `GEMINI_API_KEY` com um valor de teste (ex: "TEST_KEY_VALID_FORMAT").
2. Executar `sudo docker compose -f docker-compose.yml up --build -d` com sucesso. (Usar `-f` é mais explícito, mas `sudo docker compose up --build -d` também funciona se o arquivo for nomeado `docker-compose.yml`).
3. Verificar se os containers `backend` e `frontend` estão rodando (ex: usando `sudo docker compose ps`).
4. Verificar logs básicos dos containers `backend` e `frontend` para sinais de inicialização bem-sucedida (ex: `sudo docker compose logs backend` e `sudo docker compose logs frontend`). O backend deve mostrar Uvicorn rodando e o frontend deve mostrar Nginx iniciando.
5. Executar `sudo docker compose down` com sucesso para parar e remover os containers e a rede.
6. Remover o arquivo `.env` de teste criado no passo 1.

## Observações Adicionais
O `GEMINI_API_KEY` no `.env` de teste não precisa ser uma chave real, apenas um valor que satisfaça o formato esperado se a aplicação tentar lê-lo na inicialização. O foco é a orquestração dos containers.
Usar `sudo docker compose` conforme as instruções gerais.
O `created_at` e `updated_at` serão preenchidos pela plataforma.
Lembre-se que o nome padrão do arquivo é `docker-compose.yml`, então `-f docker-compose.yml` é opcional se esse for o nome do arquivo.
O comando `docker compose` (sem hífen) é a sintaxe moderna.
As instruções especificam "sudo docker compose", então usaremos isso.
