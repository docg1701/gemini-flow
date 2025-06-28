---
id: task-037
title: "Correção: Re-executar Testes para task-018 (Funções de Comunicação API Frontend)"
type: fix
status: backlog # Will be updated to in_progress in task-index.md
priority: high
dependencies: ["task-033", "task-018"] # Depends on original task and its direct dependency
parent_plan_objective_id: "15" # Corresponds to task-018's objective, same as task-033
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T10:00:00Z # Placeholder time
updated_at: 2024-07-31T10:00:00Z # Placeholder time
tags: ["frontend", "test", "fix", "api-integration", "jest", "mocking"]
description: |
  Esta tarefa é uma correção para a `task-033`, que falhou anteriormente devido a um problema de configuração de ambiente (dependências do frontend não instaladas).
  O script `jules_bootstrap.sh` foi atualizado para incluir `npm install --prefix frontend`.
  Esta tarefa irá re-tentar a execução dos testes para o módulo `frontend/src/services/api.ts` implementado na `task-018`.

  Os testes devem cobrir (copiado de `task-033`):
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
# outcome: failure
# outcome_reason: "Test suite `npm test --prefix frontend` failed. While `src/services/__tests__/api.test.ts` passed, `src/App.test.tsx` had 2 failing tests. Acceptance criterion 'Os testes passam com sucesso (`npm test` no diretório `frontend`)' was not met."
# start_time: 2024-07-31T10:15:00Z # Approximate
# end_time: 2024-07-31T10:16:00Z # Approximate
# duration_minutes: 1 # Approximate
# files_modified:
#   - frontend/test-results.json # Created by the test run
# reference_documents_consulted:
#   - jules-flow/backlog/task-033.md
# execution_details: |
#   1. Verified `frontend/src/services/__tests__/api.test.ts` exists.
#   2. Ran tests using `npm test --prefix frontend -- --watchAll=false --ci --json --outputFile=test-results.json`.
#   3. Test Results:
#      - `src/services/__tests__/api.test.ts`: PASSED (9 tests)
#      - `src/App.test.tsx`: FAILED (2 out of 5 tests failed)
#        - Failing tests:
#          - 'App Component Rendering › After session starts › renders ChatInterfacePlaceholder after starting a session'
#          - 'App Component Rendering › After session starts › ProjectNameInput is no longer visible after session start'
#        - Reason for failures: `Unable to find an element with the text: Chat Interface for: Meu Projeto de Teste.`
#        - Console errors about state updates not wrapped in `act(...)` were also present for `App.test.tsx`.
#   4. Since the overall test suite failed, this task is marked as failed as per acceptance criteria.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa) - Copiado de `task-033`
* `frontend/src/services/api.ts` (entrada, para ser testado)
* `frontend/src/services/__tests__/api.test.ts` (saída, arquivo de teste a ser criado/verificado)
* `frontend/package.json` (para verificar dependências de teste como `jest`, `@testing-library/react`, `msw` ou similar para mocking de API)
* `frontend/src/setupTests.ts` (pode ser usado para configurar mocks globais se necessário)

## Critérios de Aceitação - Copiado de `task-033`
1. O arquivo de teste `frontend/src/services/__tests__/api.test.ts` existe e contém os testes necessários.
2. Testes unitários são implementados para cada função em `api.ts`.
3. A função `fetch` é mockada (ex: usando `jest.fn()`, `jest.spyOn(global, 'fetch')`, ou bibliotecas como `msw`).
4. Os testes verificam chamadas corretas (URL, method, headers, body) e tratamento de respostas (sucesso e erro).
5. Os testes passam com sucesso (`npm test --prefix frontend -- --watchAll=false --ci --json --outputFile=test-results.json`).

## Observações Adicionais - Copiado de `task-033`
Create React App (CRA) já vem com Jest configurado.
Considerar o uso de `msw` (Mock Service Worker) para um mocking de API mais robusto e declarativo, se a complexidade justificar. Para testes unitários das funções de serviço, mockar `fetch` diretamente com Jest pode ser suficiente.
Garantir que os mocks de `fetch` retornem objetos `Response` com um método `.json()` que retorna uma Promise, para simular o comportamento real do `fetch`.
A `task-014` (Init frontend) deveria ter configurado o ambiente de teste Jest básico.
O arquivo `frontend/src/services/__tests__/api.test.ts` já deve existir devido à tentativa anterior em `task-033`. Esta tarefa verificará sua adequação e executará os testes.
A execução dos testes será feita com `npm test --prefix frontend -- --watchAll=false --ci --json --outputFile=test-results.json`.
---
