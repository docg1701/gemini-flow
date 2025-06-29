---
id: task-039
title: "Testes para a task-012 (Geração de bootstrap.sh)"
type: test
status: backlog
priority: medium
dependencies: ["task-012"]
parent_plan_objective_id: "9" # Matches parent task-012's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
tags: ["backend", "test", "generation", "shellscript"]
description: |
  Validar a funcionalidade de geração do script bootstrap.sh implementada na task-012.
  Isto envolve:
  1. Chamar o endpoint `/generate_files` (após garantir que a sessão está no estado AppStates.DEVOPS).
     - Para isso, será necessário simular o fluxo: /start, depois várias chamadas a /approve até atingir DEVOPS.
  2. Verificar se um diretório de output é criado em `output/` com um nome esperado (ex: `projectname_timestamp`).
  3. Verificar se `bootstrap.sh` existe dentro deste diretório.
  4. Verificar se `bootstrap.sh` é executável (permissões).
  5. Verificar o conteúdo de `bootstrap.sh` para garantir que:
      - Inclui o shebang `#!/bin/bash`.
      - Inclui o `read -p` para `install_path`.
      - Inclui comandos como `mkdir -p "$install_path/{project_name}"`.
      - Inclui a criação do `README.md` com `cat << EOF`.
  (O teste não precisa executar o `bootstrap.sh` interativamente, apenas validar sua criação e conteúdo estático).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success | failure
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ
# end_time: YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: 0
# files_modified: [] # Testes não devem modificar código fonte da aplicação
# reference_documents_consulted: ["jules-flow/done/task-012.md"]
# execution_details: |
#   Detalhes da execução dos testes para a geração do bootstrap.sh.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (entrada, para interagir com o endpoint)
* `backend/file_generator.py` (entrada, para referência da lógica)
* `output/` (saída, onde os arquivos são gerados e verificados)
* `tests/test_file_generation.py` (ou similar, onde o teste será implementado - pode ser necessário criar este arquivo de teste)

## Critérios de Aceitação
1. O endpoint `/generate_files`, quando chamado no estado DEVOPS, retorna uma resposta de sucesso HTTP 200 e uma mensagem indicando o caminho do diretório de output.
2. O diretório de output especificado na resposta existe dentro da pasta `output/` do projeto.
3. O diretório de output contém um arquivo chamado `bootstrap.sh`.
4. O arquivo `bootstrap.sh` possui permissões de execução.
5. O conteúdo do arquivo `bootstrap.sh` contém as seções esperadas (shebang, `read -p`, `mkdir -p`, `cat << EOF`).
6. O diretório de output criado durante o teste é removido após a conclusão do teste (limpeza).

## Observações Adicionais
Os testes para este endpoint podem ser testes de integração que chamam a API HTTP.
Será preciso garantir que o estado da aplicação (Orchestrator.session) esteja em `AppStates.DEVOPS` antes de chamar `/generate_files`. Isso pode envolver chamadas sequenciais a `/start` e `/approve` nos testes.
A verificação do conteúdo do script pode ser feita lendo o arquivo e procurando por substrings chave.
O diretório `output/` deve ser criado na raiz do projeto se não existir, e deve ser limpável após os testes.
Lembrar que os testes não devem depender da execução real do `bootstrap.sh`, apenas de sua correta geração.
A importação `from backend.file_generator import ...` em `main.py` pode ser um problema em ambiente Dockerizado, o teste deve ser robusto a isso ou o problema de import deve ser resolvido antes. (Nota: este é um teste da funcionalidade da task-012, não do problema de import em si).
