---
id: task-015
title: "Criar Fluxo de Inicialização da Sessão no Frontend"
epic: "Seção 3: Interface e Experiência do Usuário (Frontend)"
type: "development"
status: backlog
priority: medium
dependencies: ["task-014", "task-010"]
assignee: Jules
---

### Descrição

Criar o fluxo de inicialização da sessão no frontend. Implementar um componente React (ex: `SessionInitializer.tsx` ou dentro de `App.tsx`) que:
1.  Primeiro solicita ao usuário o "Nome do Projeto" através de um campo de input.
2.  Após o usuário submeter o nome, este componente faz uma chamada ao endpoint `/start` do backend, enviando o nome do projeto.
3.  Após a chamada bem-sucedida ao `/start`, renderiza a interface principal do chat.

### Critérios de Aceitação

- [ ] Um componente React é criado para lidar com a inicialização da sessão.
- [ ] O componente possui um campo de input para "Nome do Projeto" e um botão de submissão.
- [ ] Ao submeter, uma chamada POST é feita para o endpoint `/api/start` (ou o prefixo configurado) do backend com o nome do projeto.
- [ ] A interface principal do chat é exibida somente após a conclusão bem-sucedida desta etapa.

### Arquivos Relevantes

* `frontend/src/App.tsx`
* `frontend/src/components/SessionInitializer.tsx` (ou similar)
* `frontend/src/services/api.ts` (ou similar, para a chamada à API)

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**: `task-001` (Pesquisa React)
* **Resultado**:
* **Observações**:
---
