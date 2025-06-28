---
id: task-015
title: "Criar fluxo de inicialização da sessão no frontend"
type: development
status: backlog
priority: high
dependencies: ["task-014", "task-018"] # Depende da init do frontend e das funções de API
parent_plan_objective_id: "12"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:14:00Z
updated_at: 2024-07-29T10:14:00Z
tags: ["frontend", "react", "typescript", "ui", "session"]
description: |
  No frontend React (`frontend/src/`):
  - Criar um novo componente (ex: `ProjectNameInput.tsx`).
  - Este componente deve exibir um campo de input para o "Nome do Projeto" e um botão "Iniciar".
  - Ao clicar em "Iniciar", o componente deve:
    1. Chamar o endpoint `POST /start` do backend com o nome do projeto.
    2. Após receber a resposta do backend (mensagem de boas-vindas/primeiro prompt), deve renderizar a interface principal do chat (que será criada na task-016), passando os dados iniciais.
  - O `App.tsx` deve condicionalmente renderizar `ProjectNameInput.tsx` ou a interface principal do chat, com base no estado da sessão (ex: se o nome do projeto já foi enviado).

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
#   - frontend/src/App.tsx
#   - frontend/src/components/ProjectNameInput.tsx
#   # (ou similar)
# reference_documents_consulted: ["react_typescript_research.md"]
# execution_details: |
#   Componente para entrada do nome do projeto e chamada ao /start criada.
#   App.tsx atualizado para renderização condicional.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/App.tsx` (entrada/saída)
* `frontend/src/components/ProjectNameInput.tsx` (ou similar) (saída)
* `frontend/src/services/api.ts` (ou similar, para a chamada ao `/start`) (entrada, será criado na task-018)

## Critérios de Aceitação
1. Um componente é criado para solicitar o nome do projeto.
2. Ao submeter o nome, uma chamada à API `POST /start` é feita.
3. `App.tsx` gerencia o estado para mostrar este componente de input ou a interface de chat.
4. Após a chamada bem-sucedida ao `/start`, a interface principal do chat é exibida (mesmo que seja um placeholder inicialmente).

## Observações Adicionais
A interface principal do chat será desenvolvida na próxima tarefa (task-016), mas este fluxo precisa preparar o terreno para ela.
A comunicação com a API será implementada na task-018; esta task pode mockar a chamada ou focar na UI e estado, assumindo que a função de API estará disponível. A dependência de task-018 é crucial.
