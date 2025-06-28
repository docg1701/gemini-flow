#!/bin/bash
# Script de bootstrap para o ambiente de Jules
# Adicione aqui os comandos para instalar dependências de sistema

# Exemplo:
# sudo apt-get update
# sudo apt-get install -y curl git python3-pip
# sudo apt-get update
sudo apt -y update
sudo apt -y full-upgrade
sudo apt-get install -y nodejs npm
sudo npm install -g npx
sudo apt-get install -y python3-pip

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

sudo apt -y autoremove
echo "Bootstrap script concluído."
