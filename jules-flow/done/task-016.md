---
id: task-016
title: "Construir interface principal do chat no frontend"
type: development
status: backlog
priority: high
dependencies: ["task-014", "task-017"] # Depende da init do frontend e do gerenciamento de estado
parent_plan_objective_id: "13"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:15:00Z
updated_at: 2024-07-29T10:15:00Z
tags: ["frontend", "react", "typescript", "ui", "chat"]
description: |
  No `frontend/src/App.tsx` ou em um novo componente `ChatInterface.tsx`:
  - Implementar a estrutura visual da interface de chat.
  - Deve conter:
    - Um indicador da fase atual do planejamento (ex: "Fase 1: Planejamento de Alto Nível").
    - Uma janela de chat para exibir o histórico de mensagens (usuário e IA).
    - Um campo de input para o usuário digitar sua mensagem.
    - Um botão "Enviar Mensagem".
    - Um botão "Aprovar Fase" (ou similar), que será habilitado/desabilitado pelo estado gerenciado na task-017.

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
#   - frontend/src/types/index.ts
#   - frontend/src/components/PhaseIndicator.tsx
#   - frontend/src/components/ChatWindow.tsx
#   - frontend/src/components/MessageInputBar.tsx
#   - frontend/src/components/ApproveButtonArea.tsx
#   - frontend/src/App.tsx
#   - frontend/src/App.css
# reference_documents_consulted: ["react_typescript_research.md", "jules-flow/done/task-017.md"]
# execution_details: |
#   1. Criado `frontend/src/types/index.ts` com definições para `Message` e `AppContextType` (baseado na estratégia da task-017).
#   2. Criado o diretório `frontend/src/components/`.
#   3. Implementados os seguintes componentes placeholder com estrutura básica e props tipadas:
#      - `PhaseIndicator.tsx`: Exibe a fase atual.
#      - `ChatWindow.tsx`: Exibe a lista de mensagens.
#      - `MessageInputBar.tsx`: Contém o campo de input e botão de enviar mensagem.
#      - `ApproveButtonArea.tsx`: Contém o botão "Aprovar Fase".
#   4. Atualizado `frontend/src/App.tsx`:
#      - Importa e renderiza os componentes acima.
#      - Inclui `useState` hooks para simular os estados globais definidos na task-017 (ex: `currentPhase`, `chatHistory`, `isApprovalStepEnabled`, `isLoadingChat`, `chatError`, `projectName`).
#      - Inclui funções placeholder para `handleSendMessage` e `handleApprovePhase` que manipulam esses estados simulados.
#      - Estrutura básica para `AppContext` foi referenciada, mas a implementação completa do Provider/Consumer é para tasks futuras.
#   5. Atualizado `frontend/src/App.css` com estilos básicos para suportar a estrutura dos novos componentes e layout geral.
#   A interface principal do chat está estruturada visualmente. A lógica de estado completa e a comunicação com API serão implementadas em tasks subsequentes.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/App.tsx` (ou `frontend/src/components/ChatInterface.tsx`) (saída)
* `frontend/src/components/MessageList.tsx` (sugerido, para a janela de chat)
* `frontend/src/components/MessageInput.tsx` (sugerido, para o input e botão de enviar)

## Critérios de Aceitação
1. A interface exibe um título indicando a fase atual.
2. A interface possui uma área para renderizar mensagens do chat.
3. A interface possui um campo de texto para entrada do usuário e um botão de envio.
4. A interface possui um botão "Aprovar Fase".
5. Os componentes são construídos com React e TypeScript.

## Observações Adicionais
Esta task foca na estrutura visual (JSX e tipos). A lógica de estado (task-017) e comunicação com API (task-018) darão vida a esta interface. A estilização básica virá da task-020.
