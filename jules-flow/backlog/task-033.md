---
id: task-033
title: "Testes para a task-018 (Funções de Comunicação API Frontend)"
type: test
status: backlog
priority: high
dependencies: ["task-018"]
parent_plan_objective_id: "15" # Corresponds to task-018's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-30T15:00:00Z # Placeholder time
updated_at: 2024-07-30T15:00:00Z # Placeholder time
tags: ["frontend", "test", "api-integration", "jest", "mocking"]
description: |
  Esta tarefa visa criar e executar testes unitários para o módulo `frontend/src/services/api.ts` implementado na `task-018`.
  Os testes devem cobrir:
  - Mocking da função `fetch` global.
  - Para cada função de serviço API (`startSession`, `sendMessage`, `approvePhase`, `generateFiles`):
    - Verificar se a URL correta é chamada com o método HTTP correto.
    - Verificar se os headers corretos (ex: `Content-Type`) são enviados.
    - Verificar se o payload da requisição (body) é serializado corretamente.
    - Simular respostas de sucesso do `fetch` e verificar se a função de serviço parseia e retorna os dados corretamente.
    - Simular respostas de erro do `fetch` (ex: `response.ok = false`, status 4xx, 5xx) e verificar se a função de serviço lança ou propaga o erro adequadamente.
  - Verificar a corretude dos tipos TypeScript usados para requests e responses.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success | failure
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ
# end_time: YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: 0
# files_modified:
#   - frontend/src/services/__tests__/api.test.ts # Exemplo
# reference_documents_consulted: []
# execution_details: |
#   Detalhes da execução dos testes...
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `frontend/src/services/api.ts` (entrada, para ser testado)
* `frontend/src/services/__tests__/api.test.ts` (saída, arquivo de teste a ser criado)
* `frontend/package.json` (para verificar dependências de teste como `jest`, `@testing-library/react`, `msw` ou similar para mocking de API)
* `frontend/src/setupTests.ts` (pode ser usado para configurar mocks globais se necessário)

## Critérios de Aceitação
1. Um novo arquivo de teste (ex: `frontend/src/services/__tests__/api.test.ts`) é criado.
2. Testes unitários são implementados para cada função em `api.ts`.
3. A função `fetch` é mockada (ex: usando `jest.fn()`, `jest.spyOn(global, 'fetch')`, ou bibliotecas como `msw`).
4. Os testes verificam chamadas corretas (URL, method, headers, body) e tratamento de respostas (sucesso e erro).
5. Os testes passam com sucesso (`npm test` no diretório `frontend`).

## Observações Adicionais
Create React App (CRA) já vem com Jest configurado.
Considerar o uso de `msw` (Mock Service Worker) para um mocking de API mais robusto e declarativo, se a complexidade justificar. Para testes unitários das funções de serviço, mockar `fetch` diretamente com Jest pode ser suficiente.
Garantir que os mocks de `fetch` retornem objetos `Response` com um método `.json()` que retorna uma Promise, para simular o comportamento real do `fetch`.
A `task-014` (Init frontend) deveria ter configurado o ambiente de teste Jest básico.
Se houver problemas ao executar `npm test` devido ao ambiente (similar aos problemas com `run_in_bash_session` em outras tasks), isso deve ser investigado e resolvido primeiro.
