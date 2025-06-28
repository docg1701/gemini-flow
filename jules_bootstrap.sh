#!/bin/bash
set -e
# set -o pipefail # Removed as it may not be supported in all sh environments

export DEBIAN_FRONTEND=noninteractive

# Script de bootstrap para o ambiente de Jules
# Adicione aqui os comandos para instalar dependências de sistema

# Exemplo:
# sudo apt-get -y -q update
# sudo apt-get -y -q install curl git python3-pip

echo "Atualizando lista de pacotes e fazendo upgrade do sistema..."
sudo apt-get -y -q update
sudo apt-get -y -q full-upgrade

echo "Instalando Node.js, npm, Python pip e venv..."
sudo apt-get -y -q install nodejs npm
# sudo npm install -g npx # Removido conforme plano
sudo apt-get -y -q install python3-pip python3-venv

# Instalar Poetry (gerenciador de dependências Python)
echo "Instalando Poetry..."
# python3 -m pip install --user poetry # Será substituído pelo método oficial
curl -sSL https://install.python-poetry.org | python3 -

# Adicionar/atualizar multidict para uma versão segura antes de instalar todas as dependências
if [ -f "backend/pyproject.toml" ]; then
  echo "Garantindo que multidict seja uma versão segura (<6.6.0)..."
  ~/.local/bin/poetry -C backend add "multidict<6.6.0"
fi

# Instalar dependências do backend com Poetry
if [ -f "backend/pyproject.toml" ]; then
  echo "Instalando dependências do backend definidas em backend/pyproject.toml..."
  # Executar poetry install de dentro do diretório backend
  # ou usar -C para especificar o diretório do projeto Poetry
  ~/.local/bin/poetry -C backend install --no-root # --no-root para não instalar o próprio projeto backend como editável, apenas deps
  # Se o comando acima falhar por permissão, pode ser necessário configurar Poetry para criar venvs no projeto
  # ou garantir que o usuário Jules tenha permissão para ~/.cache/pypoetry
  # Exemplo alternativo se poetry global não for desejado:
  # python3 -m pip install poetry
  # python3 -m poetry -C backend install --no-root
else
  echo "AVISO: backend/pyproject.toml não encontrado. Pulando instalação de dependências do backend."
fi

# Criar backend/.env com placeholder para GEMINI_API_KEY se não existir
BACKEND_ENV_FILE="backend/.env"
if [ ! -f "$BACKEND_ENV_FILE" ]; then
  echo "Criando arquivo $BACKEND_ENV_FILE com placeholder para GEMINI_API_KEY..."
  # Certifique-se de que o diretório backend exista
  mkdir -p backend
  echo "GEMINI_API_KEY=YOUR_API_KEY_HERE" > "$BACKEND_ENV_FILE"
  echo "OPENAI_API_KEY=YOUR_OPENAI_KEY_HERE" >> "$BACKEND_ENV_FILE" # Exemplo se outra chave for necessária
else
  # Garantir que GEMINI_API_KEY esteja no arquivo se o arquivo já existir mas a chave não
  if ! grep -q "GEMINI_API_KEY" "$BACKEND_ENV_FILE"; then
    echo "Adicionando GEMINI_API_KEY placeholder ao $BACKEND_ENV_FILE existente..."
    echo "" >> "$BACKEND_ENV_FILE" # Nova linha para segurança
    echo "GEMINI_API_KEY=YOUR_API_KEY_HERE" >> "$BACKEND_ENV_FILE"
  fi
fi

echo "Removendo pacotes não mais necessários..."
sudo apt-get -y -q autoremove
echo "Bootstrap script concluído."
