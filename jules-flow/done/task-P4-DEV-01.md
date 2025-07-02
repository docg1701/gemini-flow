---
id: task-P4-DEV-01
title: "WP4: Implementar chain LangChain em orchestrator.py para gerar Dockerfile"
type: development
status: backlog
priority: high
dependencies: ["task-P2-DEV-01"]
parent_plan_objective_id: "4"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T14:10:00Z # Novo timestamp
updated_at: 2024-07-31T14:10:00Z
tags: ["development", "langchain", "dockerfile", "code-generation"]
description: |
  Em `app/services/orchestrator.py`:
  1. Definir `generate_dockerfile_content(user_data: dict) -> str`.
  2. Receber `user_data` do wizard.
  3. Construir chain LangChain (`PromptTemplate | LLM | StrOutputParser`).
     - `PromptTemplate` para instruir Gemini a gerar Dockerfile.
     - Usar variáveis de `user_data` (linguagem, framework, porta, etc.).
  4. Invocar chain e retornar conteúdo do Dockerfile.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: Successfully implemented and verified the Dockerfile generation chain and its fallback logic in OrchestratorService.
# start_time: 2024-08-02T04:10:00Z # Approximate
# end_time: 2024-08-02T04:45:00Z # Approximate (includes debugging time for fallback)
# duration_minutes: 35
# files_modified:
#   - app/services/orchestrator.py
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - jules-flow/docs/reference/langchain_research.md
#   - VISION.md
#   - task-P4-DEV-01.md (self)
# execution_details: |
#   1. Defined a new method `generate_dockerfile_content(self, project_details: dict) -> str` in `app/services/orchestrator.py`.
#   2. Created `self.dockerfile_prompt_template` with variables for `project_name`, `main_technology`, and `app_port`.
#   3. Created `self.dockerfile_chain` using the prompt, `self.llm` (if available), and `StrOutputParser`.
#   4. Implemented fallback logic for `self.dockerfile_chain` using `RunnableLambda` when `self.llm` is None. This required a couple of iterations to get the lambda input correct (it receives the original input dictionary for the chain).
#   5. The `generate_dockerfile_content` method processes input, invokes the chain, and handles potential errors.
#   6. Added test calls in the `if __name__ == "__main__":` block of `orchestrator.py` for various scenarios:
#      - Python project
#      - Node.js project
#      - Java project (testing default port)
#      - Insufficient data to trigger error message
#   7. Executed `app/services/orchestrator.py` using the venv Python and correct PYTHONPATH.
#   8. The script ran successfully. Fallback Dockerfile content was generated as expected (since GEMINI_API_KEY was not set for the test environment), demonstrating the corrected fallback logic works.
#   9. The test for insufficient data also correctly returned the error message.
#   10. No unexpected Python errors or tracebacks occurred during the verification.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `app/services/orchestrator.py`

## Critérios de Aceitação
1. Função para gerar Dockerfile existe no orquestrador.
2. Usa LangChain e Gemini.
3. Prompt parametrizado com dados do usuário.
4. Retorna string do Dockerfile.

## Observações Adicionais
Qualidade do Dockerfile depende do prompt.
---
