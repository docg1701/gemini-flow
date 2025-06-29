---
id: task-039
title: "Testes para a task-012 (Geração de bootstrap.sh)"
type: test
status: backlog
priority: medium
dependencies: ["task-012"]
parent_plan_objective_id: "9" # Matches parent task-012's objective
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
updated_at: YYYY-MM-DDTHH:MM:SSZ # Placeholder
tags: ["backend", "test", "generation", "shellscript"]
description: |
  Validar a funcionalidade de geração do script bootstrap.sh implementada na task-012.
  Isto envolve:
  1. Chamar o endpoint `/generate_files` (após garantir que a sessão está no estado AppStates.DEVOPS).
     - Para isso, será necessário simular o fluxo: /start, depois várias chamadas a /approve até atingir DEVOPS.
  2. Verificar se um diretório de output é criado em `output/` com um nome esperado (ex: `projectname_timestamp`).
  3. Verificar se `bootstrap.sh` existe dentro deste diretório.
  4. Verificar se `bootstrap.sh` é executável (permissões).
  5. Verificar o conteúdo de `bootstrap.sh` para garantir que:
      - Inclui o shebang `#!/bin/bash`.
      - Inclui o `read -p` para `install_path`.
      - Inclui comandos como `mkdir -p "$install_path/{project_name}"`.
      - Inclui a criação do `README.md` com `cat << EOF`.
  (O teste não precisa executar o `bootstrap.sh` interativamente, apenas validar sua criação e conteúdo estático).

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder, to be filled by execution environment
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder, to be filled by execution environment
# duration_minutes: 0 # Placeholder, to be filled by execution environment
# files_modified:
#   - backend/tests/test_file_generation.py
#   - backend/file_generator.py # Minor change to allow testable output directory
# reference_documents_consulted:
#   - "jules-flow/done/task-012.md"
#   - "backend/main.py"
#   - "backend/file_generator.py"
#   - "backend/orchestrator.py"
# execution_details: |
#   1.  **Created Test File**: `backend/tests/test_file_generation.py`.
#   2.  **Imports and Setup**: Added necessary imports (`pytest`, `shutil`, `os`, `stat`, `TestClient`, `AppStates`, `Optional`) and initialized `TestClient(app)`.
#   3.  **Test Output Directory Fixture**:
#       - Created a module-scoped pytest fixture `test_output_dir` in `backend/tests/test_file_generation.py`.
#       - This fixture creates a directory `backend/tests/test_output_gen_files/` before module tests run and removes it after they complete.
#   4.  **Made `file_generator.py` Testable**:
#       - Added a global variable `BASE_OUTPUT_DIR_FOR_TESTS: Optional[str] = None` to `backend/file_generator.py`.
#       - Modified `create_project_structure_and_files` in `backend/file_generator.py` to use `BASE_OUTPUT_DIR_FOR_TESTS` if set, otherwise defaulting to its original `base_output_dir="output"`. This allows tests to redirect output.
#   5.  **Implemented `test_generate_files_endpoint_success`**:
#       - Monkeypatches `backend.file_generator.BASE_OUTPUT_DIR_FOR_TESTS` to the path from `test_output_dir` fixture.
#       - Simulates API calls: `/start` -> `/approve` -> `/approve` to reach `DEVOPS` state.
#       - Calls `/generate_files`.
#       - Asserts HTTP 200 status and success message.
#       - Verifies that the output directory and `bootstrap.sh` are created within the fixture-managed test output directory.
#       - Cleanup is handled by the `test_output_dir` fixture.
#   6.  **Implemented `test_bootstrap_script_content_and_permissions`**:
#       - Similar flow to reach `DEVOPS` state and generate files into the test output directory.
#       - Verifies execute permissions (`S_IXUSR`, `S_IXGRP`, `S_IXOTH`) of the generated `bootstrap.sh` using `os.stat()`.
#       - Verifies key content in `bootstrap.sh`: shebang, `read -p` for project name, `mkdir -p` with project name, `cat << EOF` for README.
#   7.  **Implemented `test_generate_files_endpoint_not_in_devops_state`**:
#       - Tests calling `/generate_files` when the application is in `PLANNING` and `ISSUES` states.
#       - Asserts HTTP 200 status but with "not_ready_for_generation" status in the JSON response.
#       - Verifies that no project-specific output directory is created in the test output directory.
#   8.  **Implemented `test_generate_files_no_active_session`**:
#       - Simulates no active session by temporarily setting `global_main_orchestrator.session = None` (from `backend.main`).
#       - Calls `/generate_files`.
#       - Asserts HTTP 400 status and the expected error message "Nenhuma sessão de projeto ativa."
#       - Restores the original orchestrator session in a `finally` block.
#   9.  **Cleanup Logic**: Confirmed that the module-scoped `test_output_dir` fixture correctly manages the lifecycle of the test output directory, making individual test cleanup of generated project subfolders unnecessary if they are within this managed directory.
#   10. **Helper Function**: Added `_extract_output_dir_from_message` to parse the output directory from API responses.
#   11. **Test Execution**:
#       - Added `pytest`, `httpx`, `python-decouple` to `requirements-dev.txt` and installed them.
#       - Ran `python -m pytest backend/tests/test_file_generation.py`.
#       - All 4 tests passed successfully.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/main.py` (entrada, para interagir com o endpoint)
* `backend/file_generator.py` (entrada, para referência da lógica)
* `output/` (saída, onde os arquivos são gerados e verificados)
* `tests/test_file_generation.py` (ou similar, onde o teste será implementado - pode ser necessário criar este arquivo de teste)

## Critérios de Aceitação
1. O endpoint `/generate_files`, quando chamado no estado DEVOPS, retorna uma resposta de sucesso HTTP 200 e uma mensagem indicando o caminho do diretório de output.
2. O diretório de output especificado na resposta existe dentro da pasta `output/` do projeto.
3. O diretório de output contém um arquivo chamado `bootstrap.sh`.
4. O arquivo `bootstrap.sh` possui permissões de execução.
5. O conteúdo do arquivo `bootstrap.sh` contém as seções esperadas (shebang, `read -p`, `mkdir -p`, `cat << EOF`).
6. O diretório de output criado durante o teste é removido após a conclusão do teste (limpeza).

## Observações Adicionais
Os testes para este endpoint podem ser testes de integração que chamam a API HTTP.
Será preciso garantir que o estado da aplicação (Orchestrator.session) esteja em `AppStates.DEVOPS` antes de chamar `/generate_files`. Isso pode envolver chamadas sequenciais a `/start` e `/approve` nos testes.
A verificação do conteúdo do script pode ser feita lendo o arquivo e procurando por substrings chave.
O diretório `output/` deve ser criado na raiz do projeto se não existir, e deve ser limpável após os testes.
Lembrar que os testes não devem depender da execução real do `bootstrap.sh`, apenas de sua correta geração.
A importação `from backend.file_generator import ...` em `main.py` pode ser um problema em ambiente Dockerizado, o teste deve ser robusto a isso ou o problema de import deve ser resolvido antes. (Nota: este é um teste da funcionalidade da task-012, não do problema de import em si).
