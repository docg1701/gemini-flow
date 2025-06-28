---
id: task-009
title: "Implementar máquina de estados e orquestrador do backend"
type: development
status: backlog # This status in the file header is not changed by Jules. task-index.md tracks current status.
priority: high
dependencies: ["task-007", "task-008", "task-005"] # Depende da config, init backend e prompts
parent_plan_objective_id: "6"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:08:00Z
updated_at: 2024-07-30T11:00:00Z # Reflecting last update
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
# outcome: failure
# outcome_reason: "A verificação da tarefa (execução do script backend/orchestrator.py) falhou devido à ausência da variável de ambiente GEMINI_API_KEY. O script jules_bootstrap.sh foi atualizado para criar um backend/.env com uma chave placeholder. A tarefa foi pausada para aguardar o reinício da VM com o bootstrap atualizado."
# start_time: 2024-07-30T10:00:00Z
# end_time: 2024-07-30T11:00:00Z # Updated time
# duration_minutes: 60 # Updated duration
# files_modified:
#   - backend/orchestrator.py
#   - jules_bootstrap.sh # Added this modification
# reference_documents_consulted:
#   - "jules-flow/docs/reference/fastapi_research.md"
# execution_details: |
#   - Criado o arquivo `backend/orchestrator.py` (recriado após uma falha inicial na verificação de sua existência).
#   - Definida a Enum `AppStates` (PLANNING, ISSUES, DEVOPS).
#   - Implementada a classe `SessionManager` (estado, nome do projeto, histórico, carregamento de prompts).
#   - Implementada a classe `Orchestrator` (gerencia SessionManager, métodos de API simulados).
#   - Interação LLM simulada.
#   - Bloco de teste `if __name__ == "__main__":` adicionado.
#   - Durante a etapa de verificação:
#     - `backend/orchestrator.py` inicialmente não encontrado, recriado.
#     - `ModuleNotFoundError: No module named 'decouple'` resolvido instalando dependências com `poetry install` em `backend/`.
#     - `decouple.UndefinedValueError: GEMINI_API_KEY not found` ocorreu.
#     - Identificado que `jules_bootstrap.sh` não criava o `backend/.env` com `GEMINI_API_KEY`.
#     - `jules_bootstrap.sh` foi atualizado para criar `backend/.env` com uma chave placeholder.
#   - A tarefa não pode ser totalmente validada até que o ambiente seja reiniciado com o `jules_bootstrap.sh` atualizado para fornecer a `GEMINI_API_KEY`.
#   - A tarefa será movida para `paused_environment`.
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
