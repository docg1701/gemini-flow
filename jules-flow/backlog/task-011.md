---
id: task-011
title: "Refinar Comunicação Backend-Frontend (Flag de Aprovação)"
epic: "Seção 2: Lógica do Backend"
type: "development"
status: backlog
priority: medium
dependencies: ["task-010"]
assignee: Jules
---

### Descrição

Refinar a comunicação entre o backend e o frontend. Especificamente, a resposta do endpoint `/chat` no backend (`backend/main.py`) deve incluir um campo booleano `is_approval_step`. Este campo indicará ao frontend se o botão "Aprovar" deve ser habilitado, sinalizando que o assistente de IA está aguardando a aprovação do usuário para concluir a fase atual.

### Critérios de Aceitação

- [ ] A resposta JSON do endpoint `/chat` em `backend/main.py` contém um campo `is_approval_step` (booleano).
- [ ] A lógica no `backend/orchestrator.py` (ou `main.py`) define corretamente o valor de `is_approval_step` com base no estado atual da conversa e da máquina de estados.

### Arquivos Relevantes

* `backend/main.py`
* `backend/orchestrator.py`

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**: `task-002` (Pesquisa FastAPI)
* **Resultado**:
* **Observações**:
---
