---
id: task-016
title: "Construir Interface Principal do Chat no Frontend"
epic: "Seção 3: Interface e Experiência do Usuário (Frontend)"
type: "development"
status: backlog
priority: high
dependencies: ["task-015"]
assignee: Jules
---

### Descrição

Construir a interface principal do chat no frontend, preferencialmente no arquivo `frontend/src/App.tsx` ou em componentes dedicados. A interface deve conter:
- Um indicador da fase atual do planejamento (ex: "Fase 1: Planejamento", "Fase 2: Issues").
- Uma janela de chat para exibir o histórico da conversa entre o usuário e o assistente de IA.
- Uma área de input para o usuário digitar suas mensagens.
- Um botão "Enviar Mensagem".
- Um botão "Aprovar", que será habilitado/desabilitado conforme o estado da conversa (controlado pelo flag `is_approval_step` do backend).

### Critérios de Aceitação

- [ ] O componente principal (`App.tsx` ou similar) renderiza os elementos da interface do chat.
- [ ] Há um display para a fase atual do planejamento.
- [ ] A janela de chat exibe corretamente as mensagens trocadas.
- [ ] O input de mensagem e o botão "Enviar Mensagem" são funcionais.
- [ ] O botão "Aprovar" está presente e sua visibilidade/estado habilitado é controlado dinamicamente.

### Arquivos Relevantes

* `frontend/src/App.tsx`
* `frontend/src/components/ChatWindow.tsx` (ou similar)
* `frontend/src/components/MessageInput.tsx` (ou similar)

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**: `task-001` (Pesquisa React)
* **Resultado**:
* **Observações**:
---
