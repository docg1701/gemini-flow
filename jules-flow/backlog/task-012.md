---
id: task-012
title: "Implementar Lógica do Script de Bootstrap Interativo"
epic: "Seção 2: Lógica do Backend"
type: "development"
status: backlog
priority: medium
dependencies: ["task-010"]
assignee: Jules
---

### Descrição

Implementar a lógica no backend para gerar o script `bootstrap.sh`. Este script será parte da estrutura de projeto final gerada pelo endpoint `/generate_files`. O `bootstrap.sh` deve ser interativo, utilizando o comando `read -p` para solicitar ao usuário o caminho onde a estrutura do projeto deve ser instalada/copiada.

### Critérios de Aceitação

- [ ] Uma função no backend (provavelmente em `backend/main.py` ou um módulo utilitário) é responsável por gerar o conteúdo do script `bootstrap.sh`.
- [ ] O script `bootstrap.sh` gerado contém comandos `read -p "Por favor, informe o caminho de instalação: "` (ou similar) para obter o diretório de destino do usuário.
- [ ] O script `bootstrap.sh` gerado inclui lógica para copiar/mover os arquivos do projeto para o caminho fornecido pelo usuário.

### Arquivos Relevantes

* `backend/main.py` (ou novo módulo utilitário para geração de script)

### Relatório de Execução

* **Resumo das Alterações**:
* **Documentos de Referência Consultados**:
* **Resultado**:
* **Observações**:
---
