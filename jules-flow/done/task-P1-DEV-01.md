---
id: task-P1-DEV-01
title: "WP1: Criar estrutura app/ e remover /frontend, /backend"
type: development
status: backlog
priority: high
dependencies: [] # task-VIS pode ser uma dependência implícita para contexto
parent_plan_objective_id: "1"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:00:00Z # Novo timestamp
updated_at: 2024-07-31T14:00:00Z
tags: ["setup", "structure", "refactor"]
description: |
  Como parte da migração para uma arquitetura monolítica NiceGUI:
  1. Criar um novo diretório `app/` na raiz do projeto. Este diretório conterá todo o código da nova aplicação.
  2. Adicionar um arquivo `app/__init__.py` para que `app/` seja reconhecido como um pacote Python.
  3. Remover completamente os diretórios existentes `/frontend` e `/backend` e todo o seu conteúdo.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: 2024-07-31T14:36:00Z # Estimado
# end_time: 2024-07-31T14:40:00Z # Estimado
# duration_minutes: 4 # Estimado
# files_modified:
#   - app/__init__.py
# files_deleted:
#   - frontend/
#   - backend/
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/monolithic_project_structure_research.md
#   - VISION.md
# execution_details: |
#   1. Criado o arquivo `app/__init__.py`. A criação deste arquivo também criou o diretório `app/`.
#   2. Verificado com `ls()` que `app/` e `app/__init__.py` foram criados.
#   3. Removido o diretório `frontend/` usando `rm -rf frontend/` na sessão bash.
#   4. Verificado com `ls()` que `frontend/` foi removido.
#   5. Removido o diretório `backend/` usando `rm -rf backend/` na sessão bash.
#   6. Verificado com `ls()` que `backend/` foi removido.
#   A estrutura de diretórios agora está conforme o Passo 1 do working-plan.md.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/` (para criação)
* `app/__init__.py` (para criação)
* `frontend/` (para exclusão)
* `backend/` (para exclusão)

## Critérios de Aceitação
1. O diretório `app/` existe na raiz do projeto.
2. O arquivo `app/__init__.py` existe.
3. Os diretórios `frontend/` e `backend/` não existem mais na raiz do projeto.
4. A remoção dos diretórios não causa problemas com arquivos de configuração de nível superior que possam ter referências (ex: `.gitignore` deve ser verificado/atualizado se necessário, embora isso possa ser uma task separada ou parte de P1-DEV-02).

## Observações Adicionais
Esta é uma alteração estrutural significativa. Verificar se há referências aos diretórios `frontend/` ou `backend/` em outros arquivos na raiz (ex: `Dockerfile`, `docker-compose.yml`, `.gitignore`, `README.md`) que precisarão ser atualizados em tasks subsequentes.
---
