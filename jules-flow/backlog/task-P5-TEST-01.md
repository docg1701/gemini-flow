---
id: task-P5-TEST-01
title: "WP5: Teste de integração do fluxo completo de geração e saída"
type: test
status: backlog
priority: medium
dependencies: ["task-P3-TEST-01", "task-P4-TEST-01", "task-P5-DEV-01", "task-P5-DEV-02"]
parent_plan_objective_id: "5"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:17:00Z # Novo timestamp
updated_at: 2024-07-31T14:17:00Z
tags: ["test", "integration", "e2e"]
description: |
  Teste de integração end-to-end:
  1. Iniciar aplicação.
  2. Preencher wizard com dados de teste.
  3. Acionar geração do projeto.
  4. Verificar chamada ao orquestrador LangChain (logs/mocks).
  5. Verificar criação de diretório em `output/`.
  6. Verificar criação de todos os arquivos esperados.
  7. Verificar superficialmente conteúdo dos arquivos.
  8. Verificar tela final do wizard (sucesso, caminho).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO
# ---------------------------------------------------------------
# outcome:
# outcome_reason:
# start_time:
# end_time:
# duration_minutes:
# files_modified:
# reference_documents_consulted:
#   - jules-flow/working-plan.md
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* Aplicação completa (`app/main.py` e módulos).
* Diretório `output/`.

## Critérios de Aceitação
1. Fluxo completo sem erros críticos.
2. Diretório e arquivos criados em `output/`.
3. Conteúdo básico dos arquivos consistente.
4. UI finaliza no passo de conclusão com infos corretas.

## Observações Adicionais
Teste abrangente. Mockar LLMs para testes repetidos.
---
