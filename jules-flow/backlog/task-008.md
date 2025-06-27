---
id: task-008
title: "Criar Módulo de Configuração Central no Backend"
epic: "Seção 1: Estrutura e Configuração do Projeto"
type: "development"
status: backlog
priority: medium
dependencies: ["task-007"]
assignee: Jules
---

### Descrição

Criar um módulo de configuração central para o backend. No diretório `backend/`, criar um arquivo `config.py`. Este módulo deve utilizar a biblioteca `python-decouple` para carregar variáveis de ambiente, como a `GEMINI_API_KEY`.

### Critérios de Aceitação

- [ ] Arquivo `backend/config.py` criado.
- [ ] `backend/config.py` utiliza `python-decouple` para definir e carregar a variável de ambiente `GEMINI_API_KEY`.
- [ ] O arquivo deve prever um valor default ou lançar um erro caso a variável não esteja definida.

### Arquivos Relevantes

* `backend/config.py`

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**: `task-002` (Pesquisa FastAPI)
* **Resultado**:
* **Observações**:
---
