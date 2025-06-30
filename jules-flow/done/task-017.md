---
id: task-017
title: "Gerenciar estado do frontend com React Hooks"
type: development
status: backlog
priority: high
dependencies: ["task-014"] # Depende da init do frontend
parent_plan_objective_id: "14"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:16:00Z
updated_at: 2024-07-29T10:16:00Z
tags: ["frontend", "react", "typescript", "state-management", "hooks"]
description: |
  No frontend React (`frontend/src/App.tsx` ou componentes relevantes):
  - Utilizar React Hooks (`useState`, `useEffect`) para gerenciar:
    - Histórico do chat (array de mensagens, cada uma com remetente e texto).
    - A fase atual do planejamento (string, ex: "PLANNING", "ISSUES", "DEVOPS").
    - O estado do botão "Aprovar" (booleano `isApprovalStepEnabled`, controlado pelo flag `is_approval_step` vindo do backend).
    - Mensagem atual no campo de input.
    - Estado de carregamento (loading) durante chamadas de API.
    - Estado de erro para exibir mensagens de erro da API.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# duration_minutes: 0 # Placeholder
# files_modified: [] # No code files were modified as this task was about defining the strategy.
# reference_documents_consulted: ["react_typescript_research.md"]
# execution_details: |
#   **Estratégia de Gerenciamento de Estado para o Frontend**
#
#   A gestão de estado no frontend React com TypeScript será realizada utilizando uma combinação de Hooks React (`useState`, `useEffect`) para estados locais e a `Context API` para estados globais da aplicação.
#
#   **1. Estados Locais (Gerenciados via `useState` nos respectivos componentes):**
#     - `currentMessageInput` (string): Conteúdo atual do campo de input de mensagem do chat. Gerenciado pelo componente de input.
#     - `isLoadingComponent` (boolean): Estados de carregamento específicos de um componente (ex: enquanto um sub-componente carrega dados próprios).
#     - `componentError` (string | null): Erros específicos de um componente.
#
#   **2. Estados Globais da Aplicação (Gerenciados via `Context API`):**
#     Será criado um `AppContext` (ex: `frontend/src/contexts/AppContext.tsx`) para prover os seguintes estados e suas funções de atualização:
#     - `projectName` (string): Nome do projeto, definido no início da sessão.
#     - `chatHistory` (Message[]): Array de objetos de mensagem. Ex: `{ id: string; sender: 'user' | 'ai'; text: string; timestamp: Date }`.
#     - `currentPhase` (string): Fase atual do planejamento (ex: "PLANNING", "ISSUES", "DEVOPS").
#     - `isApprovalStepEnabled` (boolean): Controla a habilitação do botão "Aprovar", com base no feedback do backend.
#     - `isLoadingChat` (boolean): Estado de carregamento global para interações de chat com o backend (API calls).
#     - `chatError` (string | null): Mensagens de erro globais resultantes de interações de chat com o backend.
#
#   **Estrutura do `AppContext` (Exemplo Conceitual):**
#   ```typescript
#   // Em frontend/src/types/index.ts (ou similar)
#   export interface Message {
#     id: string;
#     sender: 'user' | 'ai';
#     text: string;
#     timestamp: Date;
#   }
#
#   export interface AppContextType {
#     projectName: string;
#     setProjectName: (name: string) => void;
#     chatHistory: Message[];
#     addMessageToHistory: (message: Message) => void;
#     currentPhase: string;
#     setCurrentPhase: (phase: string) => void;
#     isApprovalStepEnabled: boolean;
#     setIsApprovalStepEnabled: (isEnabled: boolean) => void;
#     isLoadingChat: boolean;
#     setIsLoadingChat: (isLoading: boolean) => void;
#     chatError: string | null;
#     setChatError: (error: string | null) => void;
#   }
#
#   // Em frontend/src/contexts/AppContext.tsx
#   // ... implementação do Context Provider usando useState e useMemo para os valores.
#   ```
#
#   **3. Uso de `useEffect`:**
#     - Para realizar chamadas de API quando certos estados ou props mudarem.
#     - Para sincronizar estados ou realizar ações baseadas em mudanças no ciclo de vida dos componentes.
#
#   **4. Tipagem:**
#     - Todos os estados, props e funções de contexto serão devidamente tipados usando TypeScript para garantir a segurança e clareza do código.
#
#   **Justificativa para `Context API`:**
#   Estados como `currentPhase`, `isApprovalStepEnabled`, `chatHistory` e `projectName` são considerados globais porque provavelmente serão necessários em múltiplos componentes (ex: Header para exibir fase, ChatWindow para exibir mensagens, ControlPanel para o botão Aprovar). Usar Context API evitará "prop drilling" excessivo e facilitará a manutenção.
#
#   Esta estratégia será implementada nas tasks subsequentes de desenvolvimento do frontend. Nenhuma modificação de código foi realizada como parte desta task específica, que se concentrou na definição desta abordagem.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/App.tsx` (principalmente)
* Outros componentes que consomem ou modificam esses estados.
* (Opcional) `frontend/src/contexts/ChatContext.tsx` se Context API for usada para estados mais globais.

## Critérios de Aceitação
1. O estado do histórico do chat é definido e pode ser atualizado.
2. O estado da fase atual é definido e pode ser atualizado.
3. O estado de habilitação do botão "Aprovar" é definido e pode ser atualizado.
4. O estado da mensagem de input é gerenciado.
5. Estados de loading e error são definidos para feedback durante chamadas de API.
6. Todos os estados são tipados corretamente com TypeScript.

## Observações Adicionais
Este é o núcleo da lógica de UI do frontend. Considerar se algum estado precisa ser elevado para um contexto (React Context API) se muitos componentes precisarem acessá-lo e a passagem de props se tornar complexa. Para o escopo inicial, `App.tsx` pode gerenciar a maioria dos estados.
