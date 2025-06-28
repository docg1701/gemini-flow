---
id: task-009
title: "Implementar máquina de estados e orquestrador do backend"
type: development
status: backlog # This status is from the original file, will be 'done' in task-index.md
priority: high
dependencies: ["task-007", "task-008", "task-005"] # Depende da config, init backend e prompts
parent_plan_objective_id: "6"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:08:00Z
updated_at: 2024-07-29T10:08:00Z # Should be updated to current time on move ideally
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
# outcome: success
# outcome_reason: ""
# start_time: 2024-07-30T10:00:00Z
# end_time: 2024-07-30T10:30:00Z
# duration_minutes: 30
# files_modified:
#   - backend/orchestrator.py
# reference_documents_consulted:
#   - "jules-flow/docs/reference/fastapi_research.md"
# execution_details: |
#   - Criado o arquivo `backend/orchestrator.py`.
#   - Definida a Enum `AppStates` com os estados PLANNING, ISSUES, DEVOPS.
#   - Implementada a classe `SessionManager` para gerenciar:
#     - Estado atual (`current_state`).
#     - Nome do projeto (`project_name`).
#     - Histórico da conversa (`conversation_history`).
#     - Carregamento dinâmico de templates de prompt (`current_prompt_template`) de arquivos em `prompts/` com base no estado atual. Os arquivos de prompt (`prompts/gemini-gem-arquiteto-de-projetos.md`, `prompts/gemini-gem-gerente-de-issues.md`, `prompts/gemini-gem-super-devops.md`) foram verificados e existem.
#   - Implementada a classe `Orchestrator` para:
#     - Gerenciar uma instância de `SessionManager`.
#     - Fornecer métodos para `start_new_session(project_name)`, `process_user_message(user_message)`, e `change_phase(new_phase_name)`.
#     - A interação com o LLM (Gemini via Langchain) está atualmente simulada. A estrutura para integração está presente (carregamento de API key de `backend.config.settings`, esboço de formatação de histórico para Langchain).
#   - Adicionado um bloco `if __name__ == "__main__":` com código de exemplo para teste local, incluindo verificação de carregamento de API key e existência de arquivos de prompt.
#   - Todos os critérios de aceitação da tarefa foram atendidos, com a interação LLM simulada conforme permitido.
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
