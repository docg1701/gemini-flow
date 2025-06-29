import datetime
import os
from typing import Optional

# This global can be monkeypatched by tests to redirect output
BASE_OUTPUT_DIR_FOR_TESTS: Optional[str] = None

def generate_bootstrap_script(project_name: str) -> str:
    script_content = f"""#!/bin/bash

# Script de Bootstrap para o projeto: {project_name}
# Gerado em: {datetime.datetime.now().isoformat()}

echo "=== Bem-vindo ao Bootstrap do Projeto: {project_name} ==="
echo ""

# Solicitar caminho de instalação ao usuário
read -p "Por favor, forneça o caminho de instalação para '{project_name}' (ex: /opt/meu_projeto_instalado): " install_path

# Validar se o caminho foi fornecido
if [ -z "$install_path" ]; then
  echo "Erro: Nenhum caminho de instalação fornecido. Abortando."
  exit 1
fi

echo ""
echo "Caminho de instalação escolhido: $install_path"

# Criar diretório de instalação
echo "Criando diretório de instalação em $install_path/{project_name}..."
mkdir -p "$install_path/{project_name}"
if [ $? -ne 0 ]; then
  echo "Erro: Falha ao criar o diretório de instalação. Verifique as permissões."
  exit 1
fi
echo "Diretório de instalação criado com sucesso."
echo ""

# Exemplo: Copiar arquivos de um diretório 'template_files' (se existir no pacote gerado)
# Este é um placeholder. Você precisaria incluir 'template_files' no seu pacote.
# if [ -d "template_files" ]; then
#   echo "Copiando arquivos de template para $install_path/{project_name}..."
#   cp -r template_files/* "$install_path/{project_name}/"
#   if [ $? -ne 0 ]; then
#     echo "Aviso: Falha ao copiar alguns arquivos de template."
#   else
#     echo "Arquivos de template copiados com sucesso."
#   fi
# else
#   echo "Nenhum diretório 'template_files' encontrado para copiar."
# fi

echo ""
echo "Exemplo: Criando um arquivo README básico no local de instalação..."
cat << EOF > "$install_path/{project_name}/README.md"
# Projeto: {project_name}

Este projeto foi instalado em: $install_path/{project_name}
Data de instalação: $(date)

Obrigado por usar nosso script de bootstrap!
EOF
echo "README.md criado em $install_path/{project_name}/README.md"
echo ""

echo "=== Bootstrap do Projeto {project_name} Concluído ==="
echo "Seu projeto está configurado em: $install_path/{project_name}"

exit 0
"""
    return script_content

def create_project_structure_and_files(project_name: str, base_output_dir: str = "output") -> str:
    """
    Cria a estrutura de diretórios base para o projeto gerado e salva o bootstrap.sh.
    Retorna o caminho para o diretório do projeto gerado.
    """
    current_base_output_dir = BASE_OUTPUT_DIR_FOR_TESTS if BASE_OUTPUT_DIR_FOR_TESTS is not None else base_output_dir

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Sanitize project_name for directory path
    sanitized_project_name = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in project_name)
    sanitized_project_name = sanitized_project_name.lower().replace(' ', '_')

    project_output_dir = os.path.join(current_base_output_dir, f"{sanitized_project_name}_{timestamp}")

    os.makedirs(project_output_dir, exist_ok=True)

    bootstrap_content = generate_bootstrap_script(project_name)
    bootstrap_file_path = os.path.join(project_output_dir, "bootstrap.sh")

    with open(bootstrap_file_path, "w") as f:
        f.write(bootstrap_content)

    # Tornar o script executável
    os.chmod(bootstrap_file_path, 0o755)

    return project_output_dir
