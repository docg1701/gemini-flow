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

echo "Bootstrap script concluído."
