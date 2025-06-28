#!/bin/bash
# Script de bootstrap para o ambiente de Jules
# Adicione aqui os comandos para instalar dependências de sistema

# Exemplo:
# sudo apt-get update
# sudo apt-get install -y curl git python3-pip
sudo apt-get update
sudo apt-get install -y nodejs npm
sudo npm install -g npx
sudo apt-get install -y python3-pip

# Criar o arquivo .env no diretório backend se não existir
BACKEND_ENV_FILE="backend/.env"
if [ ! -f "$BACKEND_ENV_FILE" ]; then
  echo "Criando arquivo de ambiente em $BACKEND_ENV_FILE..."
  # Certifique-se de que o diretório backend existe
  mkdir -p backend
  echo "GEMINI_API_KEY='SUA_CHAVE_API_AQUI_POR_FAVOR_ATUALIZE'" > "$BACKEND_ENV_FILE"
  echo "Arquivo $BACKEND_ENV_FILE criado com uma chave GEMINI_API_KEY placeholder."
else
  # Se o arquivo existe, verificar se GEMINI_API_KEY está presente
  if ! grep -q "GEMINI_API_KEY" "$BACKEND_ENV_FILE"; then
    echo "Adicionando GEMINI_API_KEY placeholder ao arquivo $BACKEND_ENV_FILE existente..."
    echo "GEMINI_API_KEY='SUA_CHAVE_API_AQUI_POR_FAVOR_ATUALIZE'" >> "$BACKEND_ENV_FILE"
  else
    echo "GEMINI_API_KEY já parece estar configurada em $BACKEND_ENV_FILE."
  fi
fi

echo "Bootstrap script concluído."
