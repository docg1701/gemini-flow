---
id: task-021
title: "Criar Dockerfile Multi-Stage"
epic: "Seção 4: Containerização e Documentação Final"
type: "development"
status: backlog
priority: high
dependencies: ["task-014", "task-007"] # Depende do frontend e backend estarem inicializados
assignee: Jules
---

### Descrição

Criar um `Dockerfile` multi-stage na raiz do projeto. Este Dockerfile deve ser capaz de construir e executar tanto o frontend React quanto o backend Python/FastAPI.
- Estágio de build para o frontend: Instalar dependências, construir os assets estáticos do React.
- Estágio de build/runtime para o backend: Instalar dependências Python, copiar o código do backend.
- Estágio final: Configurar um servidor (ex: Nginx ou Caddy) para servir os assets estáticos do frontend e o Uvicorn para rodar a API FastAPI.

### Critérios de Aceitação

- [ ] Arquivo `Dockerfile` criado na raiz do projeto.
- [ ] O Dockerfile utiliza a técnica multi-stage.
- [ ] Um estágio constrói a aplicação React (`npm run build` ou `yarn build`).
- [ ] Um estágio instala as dependências Python e prepara o backend.
- [ ] O estágio final combina os artefatos do frontend e backend e configura os servidores necessários (ex: Nginx para frontend, Uvicorn para backend).
- [ ] A imagem Docker construída a partir deste Dockerfile é funcional.

### Arquivos Relevantes

* `Dockerfile`
* `frontend/` (para build)
* `backend/` (para build e runtime)

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**: `task-003` (Pesquisa Docker)
* **Resultado**:
* **Observações**:
---
