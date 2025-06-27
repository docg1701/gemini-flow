---
id: task-009
title: "Implementar Máquina de Estados e Orquestrador no Backend"
epic: "Seção 2: Lógica do Backend"
type: "development"
status: backlog
priority: high
dependencies: ["task-008"]
assignee: Jules
---

### Descrição

Implementar a máquina de estados e o orquestrador da lógica de planejamento no backend. Criar o arquivo `backend/orchestrator.py`. Este módulo deve:
- Definir os estados do processo de planejamento (ex: `PLANNING`, `ISSUES`, `DEVOPS`).
- Gerenciar o estado da sessão do usuário (qual fase está ativa).
- Carregar dinamicamente o prompt correspondente à fase ativa do diretório `prompts/`.

### Critérios de Aceitação

- [ ] Arquivo `backend/orchestrator.py` criado.
- [ ] Módulo define e gerencia os estados (`PLANNING`, `ISSUES`, `DEVOPS`).
- [ ] Módulo contém lógica para carregar arquivos de prompt de `prompts/` com base no estado atual.
- [ ] Módulo gerencia a sessão do usuário, mantendo o controle da fase atual e do histórico da conversa.

### Arquivos Relevantes

* `backend/orchestrator.py`
* `prompts/` (para leitura dos arquivos de prompt)

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**: `task-002` (Pesquisa FastAPI), `task-005` (para saber onde estarão os prompts)
* **Resultado**:
* **Observações**:
---
