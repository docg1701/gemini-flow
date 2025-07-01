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
created_at: 2024-07-31T12:27:00Z
updated_at: 2024-07-31T12:27:00Z
tags: ["test", "integration", "e2e"]
description: |
  Realizar um teste de integração de ponta a ponta (end-to-end) do fluxo principal da aplicação:
  1. Iniciar a aplicação NiceGUI.
  2. Interagir com o wizard, preenchendo todos os campos com dados de teste válidos.
  3. Prosseguir por todos os passos até acionar a geração do projeto.
  4. Verificar se o orquestrador LangChain é chamado (pode envolver logs ou mocks parciais se o LLM real for custoso/lento para testes repetidos).
  5. Verificar se um diretório de projeto é criado corretamente na pasta `output/` com o nome esperado.
  6. Verificar se todos os arquivos esperados (Dockerfile, .gitignore, requirements.txt, GEMINI.md) são criados dentro deste diretório.
  7. Verificar (superficialmente) se o conteúdo dos arquivos gerados parece razoável e reflete as entradas do wizard. (Testes unitários em P4-TEST-01 cobrem a lógica de conteúdo mais a fundo).
  8. Verificar se a tela final do wizard exibe a mensagem de sucesso e o caminho correto para os arquivos gerados.

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
#   # Nenhum arquivo de código do produto
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - Todas as tasks DEV dos Passos 1 a 5.
# execution_details: |
#   Detalhes da execução...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* Aplicação completa (`app/main.py` e seus módulos).
* Diretório `output/`.

## Critérios de Aceitação
1. O fluxo completo, desde o início do wizard até a geração dos arquivos e feedback final, é executado sem erros críticos.
2. O diretório do projeto e os arquivos esperados são criados em `output/`.
3. O conteúdo dos arquivos gerados é consistente (em nível básico) com as entradas do wizard.
4. A UI finaliza no passo de conclusão com as informações corretas.

## Observações Adicionais
Este é o teste mais abrangente, simulando o uso real da aplicação. Para testes repetidos, pode ser útil ter uma forma de mockar as chamadas LLM para acelerar o processo, focando na integração dos componentes.
---
