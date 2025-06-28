---
id: task-009
title: "Implementar máquina de estados e orquestrador do backend"
type: development
status: backlog
priority: high
dependencies: ["task-007", "task-008", "task-005"] # Depende da config, init backend e prompts
parent_plan_objective_id: "6"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:08:00Z
updated_at: 2024-07-29T10:08:00Z
tags: ["backend", "fastapi", "langchain", "orchestrator", "statemachine"]
description: |
  Criar o arquivo `backend/orchestrator.py`.
  Este módulo deve:
  - Definir os estados da aplicação (ex: `PLANNING`, `ISSUES`, `DEVOPS`).
  - Gerenciar o estado da sessão do usuário (fase atual, histórico da conversa, nome do projeto).
  - Carregar dinamicamente o prompt correspondente à fase ativa do diretório `prompts/`.
  - Interagir com o modelo Gemini (via Langchain e `langchain-google-genai`) usando a `GEMINI_API_KEY` da configuração.
  - Manter o histórico da conversa para fornecer contexto ao modelo.

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
#   - backend/orchestrator.py
# reference_documents_consulted: ["fastapi_research.md"]
# execution_details: |
#   Arquivo backend/orchestrator.py criado com a lógica inicial da máquina de estados e carregamento de prompts.
#   A implementação da interação com Langchain e Gemini será o núcleo deste módulo.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/orchestrator.py` (saída)
* `prompts/gemini-gem-arquiteto-de-projetos.md` (entrada)
* `prompts/gemini-gem-gerente-de-issues.md` (entrada)
* `prompts/gemini-gem-super-devops.md` (entrada)
* `backend/config.py` (entrada)

## Critérios de Aceitação
1. O arquivo `backend/orchestrator.py` existe.
2. O módulo define e gerencia os estados (`PLANNING`, `ISSUES`, `DEVOPS`).
3. O módulo consegue carregar arquivos de prompt do diretório `prompts/` com base no estado atual.
4. O módulo possui uma função para processar a mensagem do usuário, interagir com o modelo Gemini (simulado inicialmente se necessário) e retornar a resposta da IA.
5. O estado da sessão (fase, histórico) é mantido (em memória por enquanto, ou considerar uma forma simples de persistência se escopo permitir).

## Observações Adicionais
Este é um componente central da lógica do backend. A gestão de sessão pode ser simples (ex: um dicionário em memória por ID de sessão, se múltiplas sessões simultâneas forem consideradas no futuro, ou um único estado global para uma sessão única). Para a V1, uma sessão única pode ser suficiente. Os prompts são: `gemini-gem-arquiteto-de-projetos.md` (PLANNING), `gemini-gem-gerente-de-issues.md` (ISSUES), `gemini-gem-super-devops.md` (DEVOPS).
