---
id: task-P2-DEV-01
title: "WP2: Criar app/services/orchestrator.py com função básica LangChain/Gemini"
type: development
status: backlog
priority: high
dependencies: ["task-P1-DEV-03"]
parent_plan_objective_id: "2"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:04:00Z # Novo timestamp
updated_at: 2024-07-31T14:04:00Z
tags: ["development", "langchain", "gemini", "poc", "backend"]
description: |
  1. Criar o diretório `app/services/`.
  2. Adicionar um arquivo `app/services/__init__.py`.
  3. Criar o arquivo `app/services/orchestrator.py`.
  4. Neste arquivo, implementar uma classe `OrchestratorService` (ou similar).
  5. Adicionar um método simples ao serviço (ex: `get_gemini_greeting(name: str) -> str`).
  6. Este método deve usar LangChain com um modelo Gemini para gerar uma saudação personalizada.
     Exemplo de prompt: "Crie uma saudação curta e amigável para {name}."
  7. A função deve retornar a saudação gerada.
  8. Configurar o acesso à API Gemini (uso de chave de API via `app/core/config.py`).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: 2024-07-31T15:25:00Z # Estimado
# end_time: 2024-07-31T15:40:00Z # Estimado
# duration_minutes: 15 # Estimado
# files_modified:
#   - app/core/__init__.py
#   - app/core/config.py
#   - app/services/__init__.py
#   - app/services/orchestrator.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/langchain_research.md
#   - jules-flow/docs/reference/monolithic_project_structure_research.md
#   - VISION.md
# execution_details: |
#   1. Criado o diretório `app/core/` e o arquivo `app/core/__init__.py`.
#   2. Criado o arquivo `app/core/config.py` com uma classe `Settings` (usando Pydantic `BaseSettings`) para carregar `GEMINI_API_KEY` de um arquivo `.env`. Inclui um valor padrão/placeholder.
#   3. Verificado que `.env.example` já existe e é adequado.
#   4. Criado o diretório `app/services/` (implicitamente pela criação do `__init__.py`).
#   5. Criado o arquivo `app/services/__init__.py`.
#   6. Criado o arquivo `app/services/orchestrator.py`.
#   7. Implementada a classe `OrchestratorService` em `orchestrator.py`.
#      - O construtor `__init__` inicializa `ChatGoogleGenerativeAI` com o modelo "gemini-pro", usando a `GEMINI_API_KEY` de `app.core.config.settings`.
#      - Inclui um fallback para o caso da API key não estar configurada, permitindo que a aplicação rode com funcionalidade LLM mockada/limitada.
#      - Define um `PromptTemplate` para a saudação.
#      - Define uma `greeting_chain` combinando o prompt, o LLM e um `StrOutputParser`.
#   8. Implementado o método `get_gemini_greeting(self, name: str) -> str` na classe:
#      - Recebe um nome.
#      - Invoca a `greeting_chain` com o nome.
#      - Inclui tratamento básico de erro e um retorno de saudação padrão em caso de falha na chamada LLM.
#      - Retorna uma saudação padrão se o nome estiver vazio.
#   9. Adicionado um bloco `if __name__ == \"__main__\":` em `orchestrator.py` para testes básicos (principalmente para verificar o carregamento da config e o fallback do LLM).
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/services/__init__.py`
* `app/services/orchestrator.py`
* `app/core/config.py`

## Critérios de Aceitação
1. `app/services/orchestrator.py` existe com a função de saudação.
2. A função usa LangChain e Gemini.
3. A função retorna uma saudação string.
4. Uso seguro da chave API.

## Observações Adicionais
Primeira integração com LangChain/Gemini.
---
