#!/bin/bash

# Script de Bootstrap para o projeto: Generate Test Ready
# Gerado em: 2025-06-29T12:32:10.779350

echo "=== Bem-vindo ao Bootstrap do Projeto: Generate Test Ready ==="
echo ""

# Solicitar caminho de instalação ao usuário
read -p "Por favor, forneça o caminho de instalação para 'Generate Test Ready' (ex: /opt/meu_projeto_instalado): " install_path

# Validar se o caminho foi fornecido
if [ -z "$install_path" ]; then
  echo "Erro: Nenhum caminho de instalação fornecido. Abortando."
  exit 1
fi

echo ""
echo "Caminho de instalação escolhido: $install_path"

# Criar diretório de instalação
echo "Criando diretório de instalação em $install_path/Generate Test Ready..."
mkdir -p "$install_path/Generate Test Ready"
if [ $? -ne 0 ]; then
  echo "Erro: Falha ao criar o diretório de instalação. Verifique as permissões."
  exit 1
fi
echo "Diretório de instalação criado com sucesso."
echo ""

# Exemplo: Copiar arquivos de um diretório 'template_files' (se existir no pacote gerado)
# Este é um placeholder. Você precisaria incluir 'template_files' no seu pacote.
# if [ -d "template_files" ]; then
#   echo "Copiando arquivos de template para $install_path/Generate Test Ready..."
#   cp -r template_files/* "$install_path/Generate Test Ready/"
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
cat << EOF > "$install_path/Generate Test Ready/README.md"
# Projeto: Generate Test Ready

Este projeto foi instalado em: $install_path/Generate Test Ready
Data de instalação: $(date)

Obrigado por usar nosso script de bootstrap!
EOF
echo "README.md criado em $install_path/Generate Test Ready/README.md"
echo ""

echo "=== Bootstrap do Projeto Generate Test Ready Concluído ==="
echo "Seu projeto está configurado em: $install_path/Generate Test Ready"

exit 0
