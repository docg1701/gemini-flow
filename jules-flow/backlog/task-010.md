---
id: task-010
title: "Criar API principal do backend com FastAPI"
type: development
status: backlog
priority: high
dependencies: ["task-009"] # Depende do orquestrador
parent_plan_objective_id: "7"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:09:00Z
updated_at: 2024-07-29T10:09:00Z
tags: ["backend", "fastapi", "api", "endpoints"]
description: |
  Criar/Atualizar o arquivo `backend/main.py`.
  Implementar os seguintes endpoints FastAPI:
  - `POST /start`: Recebe o nome do projeto, inicializa a sessão no orquestrador (fase PLANNING), e retorna uma mensagem de boas-vindas e o primeiro prompt do assistente.
  - `POST /chat`: Recebe a mensagem do usuário, passa para o orquestrador, e retorna a resposta da IA e o indicador `is_approval_step`.
  - `POST /approve`: Notifica o orquestrador que o usuário aprovou a fase atual. O orquestrador avança para a próxima fase (ou para a geração de arquivos se for a última fase) e retorna a mensagem/prompt inicial da nova fase.
  - `GET /generate_files` (ou POST): Aciona a lógica no orquestrador para gerar a estrutura de projeto final e o script `bootstrap.sh`. Retorna uma confirmação ou os arquivos (a ser definido).

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
#   - backend/main.py
# reference_documents_consulted: ["fastapi_research.md"]
# execution_details: |
#   Arquivo backend/main.py criado/atualizado com os schematics dos endpoints /start, /chat, /approve, e /generate_files.
#   A lógica de cada endpoint irá interagir com o backend/orchestrator.py.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (saída)
* `backend/orchestrator.py` (entrada)
* `backend/config.py` (entrada)

## Critérios de Aceitação
1. O arquivo `backend/main.py` contém uma instância FastAPI.
2. O endpoint `POST /start` está implementado e interage com o orquestrador.
3. O endpoint `POST /chat` está implementado e interage com o orquestrador.
4. O endpoint `POST /approve` está implementado e interage com o orquestrador.
5. O endpoint `/generate_files` (GET ou POST) está definido e interage com o orquestrador.
6. Os modelos Pydantic para os corpos de requisição e resposta são definidos e utilizados.

## Observações Adicionais
A resposta do `/generate_files` pode ser um JSON indicando sucesso e o caminho onde os arquivos foram gerados (dentro do container, a ser copiado ou montado via volume). Para uma V1, gerar em um subdiretório `output/` dentro do container pode ser o mais simples.
