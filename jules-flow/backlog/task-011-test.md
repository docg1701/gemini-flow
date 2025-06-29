---
id: task-011-test
title: "Testes para a task-011 (is_approval_step)"
type: test
status: backlog
priority: medium
dependencies: ["task-011"]
parent_plan_objective_id: "8" # Mesmo da task-011
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T12:01:00Z
updated_at: 2024-07-31T12:01:00Z
tags: ["test", "api", "backend"]
description: |
  Validar a funcionalidade `is_approval_step` implementada na task-011.
  Garantir que o campo seja retornado corretamente na API `/chat` e que seu valor mude para `true` de acordo com a lógica definida no `Orchestrator` (estado DEVOPS e histórico > 5).

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
#   - backend/tests/test_main_api.py
#   - backend/tests/test_orchestrator.py # Opcional
# reference_documents_consulted: []
# execution_details: |
#   Detalhes da execução dos testes serão preenchidos aqui.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/tests/test_main_api.py` (saída - criar/modificar testes aqui)
* `backend/main.py` (entrada - para entender a API)
* `backend/orchestrator.py` (entrada - para entender a lógica a ser testada)
* `backend/tests/test_orchestrator.py` (saída - opcional, para testes unitários da lógica `requires_approval`)

## Critérios de Aceitação
1. Um novo conjunto de testes em `backend/tests/test_main_api.py` é criado para o endpoint `/chat`.
2. Os testes verificam a presença do campo `is_approval_step` na resposta.
3. Os testes simulam o fluxo de conversa: `/start`, múltiplos `/approve` para chegar ao estado `DEVOPS`.
4. Os testes enviam mensagens no estado `DEVOPS` e verificam que `is_approval_step` se torna `true` quando a condição do histórico de conversa é atendida.
5. Os testes verificam que `is_approval_step` permanece `false` em outros estados ou antes da condição ser atendida.
6. (Opcional) Testes unitários em `backend/tests/test_orchestrator.py` validam diretamente a lógica do método `requires_approval` da classe `SessionManager`.
7. Todos os novos testes passam.

## Observações Adicionais
Considerar o uso de fixtures do Pytest para gerenciar o estado da sessão do orquestrador entre as chamadas de API nos testes de integração.
A simulação da IA pode continuar sendo a resposta placeholder atual para fins destes testes de API.
