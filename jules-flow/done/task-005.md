---
id: task-005
title: "Mover arquivos de prompt para o diretório prompts"
type: development
status: backlog
priority: medium
dependencies: ["task-004"]
parent_plan_objective_id: "2"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:04:00Z
updated_at: 2024-07-29T10:04:00Z
tags: ["organização", "prompts"]
description: |
  Mover os arquivos existentes que correspondem ao padrão `gemini-gem-*.md` da raiz do projeto para o diretório `prompts/`.

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
#   - gemini-gem-arquiteto-de-projetos.md # Original path (source of move)
#   - prompts/gemini-gem-arquiteto-de-projetos.md # New path (destination of move)
#   - gemini-gem-gerente-de-issues.md # Original path
#   - prompts/gemini-gem-gerente-de-issues.md # New path
#   - gemini-gem-super-devops.md # Original path
#   - prompts/gemini-gem-super-devops.md # New path
# reference_documents_consulted: []
# execution_details: |
#   Os seguintes arquivos foram movidos da raiz do projeto para o diretório `prompts/`:
#   - `gemini-gem-arquiteto-de-projetos.md` -> `prompts/gemini-gem-arquiteto-de-projetos.md`
#   - `gemini-gem-gerente-de-issues.md` -> `prompts/gemini-gem-gerente-de-issues.md`
#   - `gemini-gem-super-devops.md` -> `prompts/gemini-gem-super-devops.md`
#   A operação foi concluída com sucesso.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `gemini-gem-arquiteto-de-projetos.md` (entrada, a ser movido)
* `gemini-gem-gerente-de-issues.md` (entrada, a ser movido)
* `gemini-gem-super-devops.md` (entrada, a ser movido)
* `prompts/gemini-gem-arquiteto-de-projetos.md` (saída)
* `prompts/gemini-gem-gerente-de-issues.md` (saída)
* `prompts/gemini-gem-super-devops.md` (saída)

## Critérios de Aceitação
1. Os arquivos `gemini-gem-arquiteto-de-projetos.md`, `gemini-gem-gerente-de-issues.md`, e `gemini-gem-super-devops.md` não existem mais na raiz.
2. Os arquivos `gemini-gem-arquiteto-de-projetos.md`, `gemini-gem-gerente-de-issues.md`, e `gemini-gem-super-devops.md` existem no diretório `prompts/`.

## Observações Adicionais
Manter os prompts centralizados.
