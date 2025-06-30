---
id: task-012
title: "Implementar lógica do script bootstrap.sh interativo no backend"
type: development
status: backlog
priority: medium
dependencies: ["task-010"] # Depende do orquestrador e da API
parent_plan_objective_id: "9"
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-29T10:11:00Z
updated_at: 2024-07-29T10:11:00Z
tags: ["backend", "generation", "shellscript"]
description: |
  No `backend/orchestrator.py` (ou um novo módulo `backend/file_generator.py` chamado pelo orquestrador), implementar uma função que gera o conteúdo de um script `bootstrap.sh`.
  Este script shell deve:
  - Ser interativo, usando `read -p "Por favor, forneça o caminho de instalação: " install_path` para solicitar ao usuário o caminho de instalação.
  - Incluir lógica básica para criar um diretório de exemplo ou copiar arquivos para o `install_path` fornecido.
  - O endpoint `/generate_files` em `backend/main.py` deve chamar esta função e salvar o `bootstrap.sh` como parte da estrutura de projeto gerada.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# end_time: YYYY-MM-DDTHH:MM:SSZ # Placeholder
# duration_minutes: 0 # Placeholder
# files_modified:
#   - backend/file_generator.py
#   - backend/main.py
# reference_documents_consulted: []
# execution_details: |
#   1. Created `backend/file_generator.py` with two functions:
#      - `generate_bootstrap_script(project_name: str) -> str`: Generates the content of an interactive bootstrap.sh script. The script prompts for an installation path and creates a sample README.md there.
#      - `create_project_structure_and_files(project_name: str, base_output_dir: str = "output") -> str`: Creates a timestamped project directory under `base_output_dir`, generates the bootstrap.sh script using the first function, saves it into the project directory, and makes it executable. Returns the path to the created project directory.
#   2. Modified `backend/main.py`:
#      - Added import: `from backend.file_generator import create_project_structure_and_files`.
#      - Updated the `/generate_files` endpoint:
#        - It now checks if a session and project name exist.
#        - If the current state is `AppStates.DEVOPS`, it calls `create_project_structure_and_files` with the project name.
#        - Returns a success message including the path to the generated output directory (which contains `bootstrap.sh`).
#        - Added more specific error handling and status messages.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `backend/orchestrator.py` (ou `backend/file_generator.py`) (entrada/saída)
* `backend/main.py` (entrada/saída)
* `output/{timestamp}/bootstrap.sh` (saída esperada pela aplicação, não diretamente por esta task)

## Critérios de Aceitação
1. Existe uma função no backend que retorna uma string contendo um script shell válido.
2. O script shell gerado usa `read -p` para solicitar um caminho de instalação.
3. O script shell gerado contém comandos básicos para usar o caminho fornecido (ex: `mkdir -p "$install_path/meu_projeto"`).
4. O endpoint `/generate_files` salva este script como `bootstrap.sh` no diretório de saída da estrutura do projeto.

## Observações Adicionais
A estrutura de projeto gerada (e o `bootstrap.sh`) será colocada em um diretório com timestamp, por exemplo, `output/planejador_gemini_flow_20240729101100/bootstrap.sh`. A lógica de criação deste diretório de saída também faz parte da funcionalidade de `/generate_files`.
