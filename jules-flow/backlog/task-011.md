---
id: task-011
title: "Refinar comunicação backend-frontend (/chat endpoint)"
type: development
status: backlog
priority: low
dependencies: ["task-010", "task-999"] # Depende da API principal
parent_plan_objective_id: "8"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:10:00Z
updated_at: 2024-07-29T10:10:00Z
tags: ["backend", "fastapi", "api", "frontend-integration"]
description: |
  No `backend/main.py`, garantir que a resposta do endpoint `POST /chat` inclua um campo booleano `is_approval_step`.
  Este campo deve ser `true` quando a conversa da fase atual atingiu um ponto onde o usuário deve usar o botão "Aprovar" para prosseguir. Caso contrário, deve ser `false`.
  A lógica para determinar `is_approval_step` residirá no `backend/orchestrator.py`.

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
#   - backend/main.py
#   - backend/orchestrator.py
# reference_documents_consulted: ["fastapi_research.md"]
# execution_details: |
#   Atualizada a resposta do endpoint /chat em backend/main.py e a lógica correspondente em backend/orchestrator.py para incluir o campo is_approval_step.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (entrada/saída)
* `backend/orchestrator.py` (entrada/saída)

## Critérios de Aceitação
1. O modelo de resposta Pydantic para o endpoint `/chat` inclui o campo `is_approval_step: bool`.
2. O `backend/orchestrator.py` possui lógica para determinar quando `is_approval_step` deve ser `true` (ex: após o Gemini indicar que coletou todas as informações para a fase atual).
3. O endpoint `/chat` em `backend/main.py` retorna corretamente este campo.

## Observações Adicionais
Isso é crucial para a UX, pois o frontend usará este flag para habilitar/desabilitar o botão "Aprovar". A IA (Gemini) precisará ser instruída (via prompt) a indicar quando é um ponto de aprovação.
