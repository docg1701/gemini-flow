# Plano de Trabalho - Branch: jules-20250627135500

## Objetivo Geral

Desenvolver uma aplicação web stand-alone e containerizada chamada **"Planejador Gemini-Flow"**. A aplicação consistirá em um frontend **React (com TypeScript)** e um backend **Python (com FastAPI)**. Ela funcionará como um assistente de IA conversacional que guiará o usuário através de três fases de planejamento de projeto, controladas por um botão "Aprovar". A lógica da IA será alimentada dinamicamente por prompts armazenados no diretório `/prompts`. O resultado final será a geração de uma estrutura de projeto em um diretório de saída com timestamp, contendo um script `bootstrap.sh` interativo que solicitará ao usuário o caminho de instalação. Todo o sistema será executado via **Docker Compose**.

## Passo a Passo da Execução para Jules

### Seção 1: Estrutura e Configuração do Projeto

1.  Crie uma task do tipo `development` para estabelecer a estrutura de diretórios inicial. Na raiz do projeto, crie os diretórios `backend`, `frontend`, e `prompts`.
2.  Crie uma task do tipo `development` para mover os arquivos de prompt existentes (`gemini-gem-*.md`) para o novo diretório `prompts`.
3.  Crie uma task do tipo `documentation` para criar o arquivo `VISION.md` na raiz do projeto e preenchê-lo com a versão final e detalhada que foi consolidada.
4.  Crie uma task do tipo `development` para inicializar o backend Python no diretório `backend`. Crie um arquivo `pyproject.toml` definindo as dependências: `fastapi`, `uvicorn[standard]`, `langchain`, `langchain-google-genai`, e `python-decouple`.
5.  Crie uma task do tipo `development` para criar um módulo de configuração central no backend. Crie o arquivo `backend/config.py` que usará `python-decouple` para carregar variáveis de ambiente, como a `GEMINI_API_KEY`.

### Seção 2: Lógica do Backend

6.  Crie uma task do tipo `development` para implementar a máquina de estados e o orquestrador no `backend/orchestrator.py`. Este módulo deve definir os estados (`PLANNING`, `ISSUES`, `DEVOPS`), gerenciar o estado da sessão e carregar o prompt correspondente à fase ativa.
7.  Crie uma task do tipo `development` para criar a API principal no `backend/main.py` com os endpoints `/start`, `/chat`, `/approve` e `/generate_files`.
8.  Crie uma task do tipo `development` para refinar a comunicação entre backend e frontend. A resposta do endpoint `/chat` deve incluir um booleano `is_approval_step` para notificar o frontend quando o botão "Aprovar" deve ser habilitado.
9.  Crie uma task do tipo `development` para implementar a lógica do script de bootstrap interativo. A função no backend que gera o `bootstrap.sh` deve criar um script que use `read -p` para solicitar ao usuário o caminho de instalação.
10. Crie uma task do tipo `development` para implementar o tratamento de erros no backend. Adicione um middleware ao FastAPI em `main.py` para capturar exceções (ex: falha na API do Gemini) e retornar respostas de erro HTTP padronizadas.

### Seção 3: Interface e Experiência do Usuário (Frontend)

11. Crie uma task do tipo `development` para inicializar a aplicação frontend no diretório `frontend` usando `npx create-react-app frontend --template typescript`.
12. Crie uma task do tipo `development` para criar o fluxo de inicialização da sessão. Crie um componente no frontend que primeiro peça o "Nome do Projeto" e, após o envio, chame o endpoint `/start` e renderize a interface principal do chat.
13. Crie uma task do tipo `development` para construir a interface principal do chat em `frontend/src/App.tsx`, contendo o indicador de fase, a janela de chat e o botão "Aprovar".
14. Crie uma task do tipo `development` para gerenciar o estado do frontend (hooks do React) para o histórico do chat, a fase atual e o estado do botão "Aprovar", que será controlado pelo flag `is_approval_step` vindo do backend.
15. Crie uma task do tipo `development` para implementar as funções de comunicação com a API no frontend, garantindo que todas as chamadas para os endpoints (`/start`, `/chat`, etc.) sejam tratadas.
16. Crie uma task do tipo `development` para implementar o tratamento de erros no frontend. A lógica de comunicação com a API deve ser capaz de tratar as respostas de erro do backend e exibir uma mensagem amigável para o usuário na interface.
17. Crie uma task do tipo `development` para aplicar um estilo visual básico e limpo à aplicação. Adicione um arquivo CSS global para garantir que a interface seja organizada e legível, sem a necessidade de um framework complexo.

### Seção 4: Containerização e Documentação Final

18. Crie uma task do tipo `development` para criar um `Dockerfile` multi-stage na raiz do projeto, conforme definido na visão.
19. Crie uma task do tipo `development` para criar o arquivo `docker-compose.yml` na raiz para orquestrar o serviço, mapear portas e gerenciar variáveis de ambiente via `.env`.
20. Crie uma task do tipo `documentation` para reescrever completamente o `README.md` principal. Ele deve explicar o propósito do "Planejador Gemini-Flow", sua arquitetura e como executá-lo com o comando `docker-compose up`.
