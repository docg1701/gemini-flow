---
id: task-043
title: "Correção Agrupada: Falhas em Testes Frontend (App.test.tsx) e Inicialização do Backend (Docker)"
type: fix
status: backlog # Atualizado para backlog ao mover
priority: high
dependencies: ["task-034", "task-036", "task-038", "task-042"] # Referencing the failed tasks
parent_plan_objective_id: null # This is a corrective task for multiple issues
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T17:00:00Z # Placeholder time
updated_at: # Será atualizado pela plataforma ou por Jules ao retomar
tags: ["frontend", "backend", "test", "fix", "docker", "react", "python"]
description: |
  Esta tarefa visa corrigir duas categorias principais de falhas identificadas:
  1.  **Problemas nos Testes do Frontend (`frontend/src/App.test.tsx`):**
      As tarefas `task-034`, `task-037`, `task-038`, e `task-042` falharam devido a problemas persistentes nos testes de `frontend/src/App.test.tsx`.
      Especificamente, os testes que verificam a renderização condicional após o início da sessão (ocultar `ProjectNameInput`, mostrar `ChatInterfacePlaceholder`) falham, acompanhados por avisos de `act(...)`.
      A `task-038` tentou corrigir isso sem sucesso.
      **Plano de Ação para Frontend:**
      - Revisar a lógica de `App.tsx` e `ProjectNameInput.tsx` relacionada ao estado da sessão e renderização condicional.
      - Investigar profundamente os avisos de `act(...)`. Pode ser necessário refatorar os testes para usar `waitFor` ou outras utilidades do RTL de forma mais eficaz, ou ajustar como o estado é atualizado/mockado.
      - Considerar se o problema está no mock de `startSession` ou na interação entre componentes.
      - Se as tentativas anteriores de `act` e `waitFor` não funcionaram, pode ser necessário simplificar os cenários de teste ou investigar interações mais profundas com o JSDOM/React.

  2.  **Falha na Inicialização do Container Backend (`task-036`):**
      A `task-036` falhou devido a um `ModuleNotFoundError: No module named 'backend'` no container do backend.
      Isso indica que a estrutura de imports do Python (`from backend.module`) não corresponde à forma como os arquivos estão organizados ou como o `PYTHONPATH` está configurado no Dockerfile do backend.
      **Plano de Ação para Backend:**
      - Revisar o `Dockerfile` do backend para garantir que os arquivos sejam copiados de uma maneira que preserve a estrutura de diretório `backend/` no `WORKDIR /app`, ou ajustar o `PYTHONPATH` dentro do container.
      - Uma solução comum é garantir que o diretório pai do diretório `backend` (se o código estiver em `backend/backend/...`) esteja no `PYTHONPATH`, ou que os imports sejam relativos à raiz da aplicação no container (ex: `from .module` se `main.py` estiver em `/app/backend/` e os módulos também, ou ajustar os `COPY` e `WORKDIR` para que `/app` seja o diretório `backend` original).
      - Alternativamente, se a intenção é ter todos os arquivos do diretório `backend` (do repositório) diretamente em `/app` no container, então os imports em `main.py` e outros arquivos Python deveriam ser `from orchestrator import ...` em vez de `from backend.orchestrator import ...`.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: # pending, in_progress, success, failure
# outcome_reason: # Se failure, descreva o motivo.
# start_time: # YYYY-MM-DDTHH:MM:SSZ
# end_time: # YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: # Em minutos
# files_modified:
#   - # Lista de arquivos modificados, criados ou deletados
# reference_documents_consulted:
#   - jules-flow/failed/task-034.md
#   - jules-flow/failed/task-036.md
#   - jules-flow/failed/task-038.md
#   - jules-flow/failed/task-042.md
#   - frontend/src/App.tsx
#   - frontend/src/App.test.tsx
#   - frontend/src/components/ProjectNameInput.tsx
#   - Dockerfile
#   - backend/main.py
# execution_details: |
#   # Log detalhado das ações tomadas, decisões, e resultados parciais.
#   # Tarefa pausada para priorizar task-044 (Revisão de Configuração de Containerização).
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
### Para Correção do Frontend:
* `frontend/src/App.tsx`
* `frontend/src/App.test.tsx`
* `frontend/src/components/ProjectNameInput.tsx`
* `frontend/src/services/api.ts` (para mocks)
* `frontend/src/setupTests.ts` (se aplicável)

### Para Correção do Backend:
* `Dockerfile` (principalmente a seção do backend)
* `backend/main.py` (e outros arquivos Python com imports `from backend...`)
* `docker-compose.yml` (para testar a inicialização)

## Critérios de Aceitação
1.  **Frontend:**
    *   Todos os testes em `frontend/src/App.test.tsx` passam.
    *   Não há mais avisos de `act(...)` durante a execução dos testes do frontend.
    *   O conjunto completo de testes do frontend (`npm test --prefix frontend`) passa.
2.  **Backend:**
    *   O comando `sudo docker compose up --build backend` (ou `... up --build` para todos os serviços) inicia o container do backend sem erros de `ModuleNotFoundError`.
    *   Os logs do container backend (`sudo docker compose logs backend`) indicam que a aplicação FastAPI iniciou corretamente.
3.  As tarefas originais `task-034`, `task-036`, `task-038`, `task-042` (ou pelo menos seus objetivos) podem ser consideradas resolvidas por esta tarefa de correção. (Isso será verificado re-executando os testes relevantes ou validando os cenários).

## Observações Adicionais
Esta tarefa combina duas áreas problemáticas distintas para eficiência. Se uma área se provar significativamente mais complexa, pode ser necessário dividi-la posteriormente.
Priorizar a correção do backend primeiro pode ser benéfico se os testes de frontend dependerem de um backend funcional em algum cenário de teste de integração (embora os problemas atuais do frontend pareçam ser com testes unitários/mockados).
Para o backend, a solução mais simples pode ser ajustar os caminhos de import no código Python para refletir a estrutura de arquivos dentro do container, ou ajustar o Dockerfile `COPY` para criar um subdiretório `backend` dentro de `/app` se essa for a estrutura de importação desejada.
Para o frontend, uma revisão sistemática das interações assíncronas e do estado nos testes de `App.test.tsx` é necessária.
---
