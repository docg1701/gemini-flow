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

echo "Instalando Node.js, npm, Python pip, venv e curl..."
sudo apt-get -y -q install nodejs npm curl
# sudo npm install -g npx # Removido conforme plano
sudo apt-get -y -q install python3-pip python3-venv

# Criar ambiente virtual e instalar dependências do requirements.txt
VENV_PATH="/opt/app-venv"
echo "Criando ambiente virtual Python em $VENV_PATH..."
sudo python3 -m venv $VENV_PATH
# O chown abaixo pode ser necessário se o script ou o usuário que executa a app não for root
# sudo chown -R $(whoami):$(whoami) $VENV_PATH 
# Por enquanto, vamos assumir que o bootstrap e a execução da app ocorrem com privilégios suficientes
# ou que o usuário padrão da VM tem acesso a /opt ou que o Docker lida com isso.

if [ -f "requirements.txt" ]; then
  echo "Instalando dependências de requirements.txt no ambiente virtual $VENV_PATH..."
  sudo $VENV_PATH/bin/python -m pip install --no-cache-dir -r requirements.txt
else
  echo "AVISO: requirements.txt não encontrado na raiz. Pulando instalação de dependências."
fi

# Instalar Poetry (gerenciador de dependências Python)
# Se Poetry for usado para gerenciar o projeto principal no futuro,
# ele deve ser configurado para usar este venv ou criar o seu próprio dentro do projeto.
# Por agora, a instalação de Poetry é mantida, mas não é usada para o requirements.txt principal.
echo "Instalando Poetry..."
export POETRY_HOME="/opt/poetry"
curl -sSL https://install.python-poetry.org | sudo python3 -
export PATH="$POETRY_HOME/bin:$PATH"

# Configurar Poetry para não criar virtualenvs ou modificar o projeto
# Essas configurações são mais relevantes para o Docker, mas podem ser setadas aqui para consistência
# poetry config virtualenvs.create false # Removido - pode não ser desejável/necessário no bootstrap geral
# poetry config virtualenvs.in-project false # Removido
# poetry config virtualenvs.path null # Removido
# poetry env use system # Removido - poetry decidirá ou usará o venv atual

# A dependência 'multidict' e sua restrição de versão (<6.6.0) são gerenciadas
# diretamente no arquivo backend/pyproject.toml.
# O comando `poetry install` abaixo cuidará de sua instalação conforme definido.
# Remover a tentativa explícita de 'poetry add multidict' daqui para evitar redundância.

# Instalar dependências do backend com Poetry
if [ -f "backend/pyproject.toml" ]; then
  echo "Instalando dependências do backend definidas em backend/pyproject.toml..."
  poetry -C backend install --no-root # Usando poetry diretamente
else
  echo "AVISO: backend/pyproject.toml não encontrado. Pulando instalação de dependências do backend."
fi

# Instalar dependências do frontend
if [ -f "frontend/package.json" ]; then
  echo "Instalando dependências do frontend definidas em frontend/package.json..."
  npm install --prefix frontend
else
  echo "AVISO: frontend/package.json não encontrado. Pulando instalação de dependências do frontend."
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
