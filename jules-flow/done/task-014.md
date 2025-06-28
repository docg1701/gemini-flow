---
id: task-014
title: "Inicializar aplicação frontend React com TypeScript"
type: development
status: backlog
priority: high
dependencies: ["task-002", "task-004"] # Depende da pesquisa React/TS e da criação do diretório frontend
parent_plan_objective_id: "11"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:13:00Z
updated_at: 2024-07-29T10:13:00Z
tags: ["frontend", "react", "typescript", "setup", "cra"]
description: |
  No diretório `frontend/`, inicializar uma nova aplicação React com TypeScript usando o comando:
  `npx create-react-app frontend --template typescript`
  Atenção: O comando `create-react-app` cria um subdiretório. A task deve ser executada na raiz e o conteúdo gerado movido para `frontend/`, ou o comando adaptado para gerar diretamente em `frontend/` se possível, ou o diretório `frontend` ser criado pelo CRA e depois renomeado/movido se necessário para se adequar à estrutura `frontend/` já criada pela task-004.
  A forma mais simples é:
  1. `npx create-react-app temp_frontend --template typescript` (na raiz do projeto ou em /tmp)
  2. Mover o conteúdo de `temp_frontend/*` para `frontend/`
  3. Remover `temp_frontend`

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
#   - frontend/ # Entire directory was (re)created and populated by CRA
# reference_documents_consulted: ["react_typescript_research.md"]
# execution_details: |
#   1. Executado `rm -rf frontend/` para remover o diretório placeholder existente.
#   2. Executado `npx create-react-app frontend --template typescript` na raiz do projeto.
#      Este comando recriou o diretório `frontend/` e o populou com uma aplicação React com TypeScript.
#      A saída do comando indicou sucesso.
#   3. Verificado se um sub-repositório Git (`frontend/.git`) foi criado. Não foi encontrado.
#   A aplicação React com TypeScript foi inicializada com sucesso no diretório `frontend/`.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/` (saída, diretório será populado pelo CRA)
* `frontend/package.json` (saída)
* `frontend/src/App.tsx` (saída)
* `frontend/tsconfig.json` (saída)

## Critérios de Aceitação
1. O diretório `frontend/` contém uma estrutura de projeto React válida.
2. O projeto React está configurado para usar TypeScript (`tsconfig.json` presente, arquivos `.tsx`).
3. O comando `npm start` (ou `yarn start`) dentro do diretório `frontend/` inicia o servidor de desenvolvimento React com sucesso.

## Observações Adicionais
O `npx` precisa estar instalado no ambiente de execução (adicionado ao `jules_bootstrap.sh`).
O nome do projeto dentro do `package.json` do frontend será "frontend" por padrão se o comando for `npx create-react-app frontend ...`. Se a task-004 já criou `frontend/`, o CRA pode reclamar. A estratégia de criar em `temp_frontend` e mover é mais robusta. Ou, executar `cd frontend && npx create-react-app . --template typescript` se o diretório `frontend` já existir e estiver vazio. No entanto, `create-react-app .` pode ter restrições.
Melhor abordagem: `npx create-react-app temp-app --template typescript && mv temp-app/* frontend/ && rm -rf temp-app` (assumindo que `frontend/` já existe e está vazio, ou limpar `frontend/` antes). Se `frontend/` não existir, `npx create-react-app frontend --template typescript` é direto. Dado que task-004 cria `frontend/`, a abordagem de mover é melhor.
Ainda mais simples: `rm -rf frontend && npx create-react-app frontend --template typescript` (recria o diretório `frontend` com o CRA).
