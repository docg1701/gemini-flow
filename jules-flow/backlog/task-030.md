---
id: task-030
title: "Testes para a task-005"
type: test
status: backlog
priority: medium
dependencies: ["task-005"]
parent_plan_objective_id: "2" # Corresponds to objective 2 in working-plan.md
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
tags: ["test", "prompts", "organização"]
description: |
  Validar que os arquivos de prompt (`gemini-gem-*.md`) foram corretamente movidos da raiz do projeto para o diretório `prompts/`.
  Verificar que os arquivos não existem mais na raiz e existem no novo local.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success | failure
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ
# end_time: YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: 0
# files_modified: []
# reference_documents_consulted: []
# execution_details: |
#   Detalhes da execução dos testes para a movimentação dos arquivos de prompt.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `gemini-gem-arquiteto-de-projetos.md` (verificar ausência na raiz)
* `gemini-gem-gerente-de-issues.md` (verificar ausência na raiz)
* `gemini-gem-super-devops.md` (verificar ausência na raiz)
* `prompts/gemini-gem-arquiteto-de-projetos.md` (verificar presença)
* `prompts/gemini-gem-gerente-de-issues.md` (verificar presença)
* `prompts/gemini-gem-super-devops.md` (verificar presença)
* `prompts/` (diretório)

## Critérios de Aceitação
1. O arquivo `gemini-gem-arquiteto-de-projetos.md` NÃO existe na raiz do projeto.
2. O arquivo `gemini-gem-gerente-de-issues.md` NÃO existe na raiz do projeto.
3. O arquivo `gemini-gem-super-devops.md` NÃO existe na raiz do projeto.
4. O arquivo `prompts/gemini-gem-arquiteto-de-projetos.md` EXISTE.
5. O arquivo `prompts/gemini-gem-gerente-de-issues.md` EXISTE.
6. O arquivo `prompts/gemini-gem-super-devops.md` EXISTE.
7. A tarefa deve ser concluída com sucesso se todos os critérios forem atendidos.

## Observações Adicionais
Esta tarefa de teste é gerada automaticamente.
Os testes envolvem verificações de existência e não existência de arquivos em locais específicos.
Usar `ls` ou similar para verificar.
