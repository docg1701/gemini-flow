---
id: task-030
title: "Testes para a task-005"
type: test
status: in_progress # Will be updated to done in task-index
priority: medium
dependencies: ["task-005"]
parent_plan_objective_id: "2"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:30:00Z
updated_at: 2024-08-01T12:40:00Z
tags: ["test", "prompts", "organização"]
description: |
  Validar que os arquivos de prompt (`gemini-gem-*.md`) foram corretamente movidos da raiz do projeto para o diretório `prompts/`.
  Verificar que os arquivos não existem mais na raiz e existem no novo local.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
outcome: success
outcome_reason: ""
start_time: 2024-08-01T12:35:00Z
end_time: 2024-08-01T12:40:00Z
duration_minutes: 5
files_modified: []
reference_documents_consulted: []
execution_details: |
  Criterion 1: gemini-gem-arquiteto-de-projetos.md not found in root. PASS.
  Criterion 2: gemini-gem-gerente-de-issues.md not found in root. PASS.
  Criterion 3: gemini-gem-super-devops.md not found in root. PASS.
  Criterion 4: prompts/gemini-gem-arquiteto-de-projetos.md found in prompts/. PASS.
  Criterion 5: prompts/gemini-gem-gerente-de-issues.md found in prompts/. PASS.
  Criterion 6: prompts/gemini-gem-super-devops.md found in prompts/. PASS.

  All checks passed. The files were correctly moved to the prompts/ directory and removed from the root directory.
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
