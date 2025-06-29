---
id: task-035
title: "Testes para a task-021 (Dockerfile multi-stage)"
type: test
status: backlog # Will be updated in task-index.md
priority: high
dependencies: ["task-021"]
parent_plan_objective_id: "18" # Corresponds to task-021's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
tags: ["docker", "test", "dockerfile"]
description: |
  Validar o Dockerfile multi-stage criado na task-021.
  O objetivo principal é garantir que os diferentes stages do Dockerfile podem ser construídos com sucesso.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder - to be filled by platform
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder - to be filled by platform
# duration_minutes: 5 # Approximate
# files_modified: []
# reference_documents_consulted: ["jules-flow/docs/reference/docker_research.md"]
# execution_details: |
#   1. Executed `sudo docker build --target frontend-builder -t test-frontend-builder .` - Success.
#   2. Executed `sudo docker build --target backend -t test-backend .` - Success.
#   3. Executed `sudo docker build --target frontend -t test-frontend .` - Success.
#   4. Verified image creation using `sudo docker images | grep -E "test-frontend-builder|test-backend|test-frontend"`. All images were present.
#   5. Cleaned up test images using `sudo docker rmi test-frontend-builder test-backend test-frontend`. All images were removed.
#   All acceptance criteria met.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `Dockerfile` (entrada)
* `frontend/` (entrada, para contexto de build)
* `backend/` (entrada, para contexto de build)
* `nginx.conf` (entrada, para contexto de build)

## Critérios de Aceitação
1. O comando `sudo docker build --target frontend-builder -t test-frontend-builder .` é executado com sucesso.
2. O comando `sudo docker build --target backend -t test-backend .` é executado com sucesso.
3. O comando `sudo docker build --target frontend -t test-frontend .` é executado com sucesso.
4. (Opcional) Verificar se as imagens de teste (`test-frontend-builder`, `test-backend`, `test-frontend`) são listadas por `sudo docker images`.
5. Limpar as imagens de teste criadas (`sudo docker rmi test-frontend-builder test-backend test-frontend`).

## Observações Adicionais
Estes testes focam na capacidade de construir as imagens a partir do Dockerfile. Testes de funcionalidade dos containers (ex: se o Nginx serve corretamente, se o backend FastAPI responde) serão parte dos testes da task-022 (docker-compose.yml) ou tarefas subsequentes.
Usar `sudo docker` para os comandos de build, conforme especificado nas instruções gerais, a menos que o ambiente já esteja configurado para Docker sem sudo.
O `created_at` e `updated_at` serão preenchidos pela plataforma.
