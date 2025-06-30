---
id: task-008
title: "Criar módulo de configuração do backend"
type: development
status: backlog
priority: high
dependencies: ["task-007"] # Depende da inicialização do backend
parent_plan_objective_id: "5"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:07:00Z
updated_at: 2024-07-29T10:07:00Z
tags: ["backend", "config", "python-decouple", "fastapi"]
description: |
  Criar o arquivo `backend/config.py`.
  Este módulo deve usar `python-decouple` para carregar variáveis de ambiente, como `GEMINI_API_KEY`.
  Definir uma função ou classe para acessar as configurações.

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
#   - backend/config.py
#   - backend/.env.example
#   - .gitignore
# reference_documents_consulted: ["fastapi_research.md"]
# execution_details: |
#   1. Criado o arquivo `backend/config.py` que utiliza `python-decouple` para carregar a variável de ambiente `GEMINI_API_KEY`.
#   2. Criado o arquivo `backend/.env.example` com um modelo para a `GEMINI_API_KEY`.
#   3. Atualizado o arquivo `.gitignore` na raiz do projeto para incluir `backend/.env` e outros padrões comuns de arquivos a serem ignorados (Python, IDEs, etc.).
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/config.py` (saída)
* `.env.example` (sugerido, para documentar variáveis de ambiente)

## Critérios de Aceitação
1. O arquivo `backend/config.py` existe.
2. O módulo `config.py` utiliza `decouple.config` para carregar a variável `GEMINI_API_KEY`.
3. A variável `GEMINI_API_KEY` pode ser importada e utilizada por outros módulos do backend.
4. Um arquivo `.env.example` é criado na raiz do projeto (ou no diretório `backend/`) para listar as variáveis esperadas.

## Observações Adicionais
O `.env` real contendo a chave não deve ser commitado. `python-decouple` procura por um arquivo `.env` na raiz do projeto ou no diretório onde o script é executado.
