# Planejador Gemini-Flow

O **Planejador Gemini-Flow** é uma aplicação web interativa projetada para auxiliar na arquitetura de software. Utilizando uma interface de chat, ele guia os usuários através de um diálogo colaborativo com uma IA (potencializada pelo Google Gemini) para transformar um objetivo de alto nível em uma estrutura de projeto completa, incluindo artefatos como planos de trabalho, scripts de criação de issues e configurações de ambiente.

## Arquitetura

A aplicação é construída com a seguinte stack:

*   **Frontend:** React com TypeScript, fornecendo uma interface de usuário dinâmica e responsiva.
*   **Backend:** Python com o framework FastAPI, gerenciando a lógica de negócios, o estado da conversa e a comunicação com a API do Gemini.
*   **Orquestração de IA:** A biblioteca LangChain (versão Python) é usada no backend para gerenciar as interações com o modelo Gemini.
*   **Containerização:** Docker e Docker Compose são utilizados para garantir um ambiente de desenvolvimento e execução consistente e fácil de configurar.

## Pré-requisitos

Antes de executar a aplicação, certifique-se de que você tem o seguinte software instalado:

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/) (geralmente incluído nas instalações mais recentes do Docker Desktop)

## Configuração do Ambiente

Antes de executar a aplicação, você precisa configurar as variáveis de ambiente. O projeto utiliza um arquivo `.env` na raiz para gerenciar essas configurações.

1.  **Criar o arquivo `.env`:**
    Copie o arquivo de exemplo `.env.example` (localizado na raiz do projeto) para um novo arquivo chamado `.env`:
    ```bash
    cp .env.example .env
    ```

2.  **Configurar Variáveis no `.env`:**
    Abra o arquivo `.env` recém-criado com um editor de texto. **Consulte o arquivo `.env.example` original para uma lista completa de todas as variáveis de ambiente disponíveis e seus propósitos detalhados**, que abrangem configurações para o backend, frontend e o processo de build do Docker. O `.env.example` é a fonte da verdade para estas configurações.

    *   **Variável Obrigatória Principal:**
        *   `GEMINI_API_KEY`: Você **deve** fornecer sua chave da API do Google Gemini. Conforme descrito no `.env.example`, obtenha sua chave em [Google AI Studio](https://aistudio.google.com/app/apikey) e defina-a no seu arquivo `.env`:
          ```
          GEMINI_API_KEY="SUA_CHAVE_API_REAL_AQUI"
          ```

    *   **Outras Variáveis (Opcionais/Padrões):**
        *   Revise todas as outras variáveis no `.env.example` e copie/ajuste as que necessitar para o seu arquivo `.env`. Muitas delas têm valores padrão (ou estão comentadas no `.env.example`) que são adequados para desenvolvimento local (ex: `BACKEND_HOST_PORT=8000`, `FRONTEND_HOST_PORT=3000`).
        *   Ajuste as portas ou outras configurações no seu `.env` conforme necessário para o seu ambiente.
        *   Variáveis como `DOCKER_NODE_VERSION`, `DOCKER_PYTHON_VERSION` (definidas no `.env.example` e usadas no `docker-compose.yml`) controlam as versões das imagens base usadas na construção dos containers Docker.

## Como Executar a Aplicação

Com o Docker e o Docker Compose instalados e o arquivo `.env` configurado:

1.  **Construir e Iniciar os Containers:**
    Navegue até o diretório raiz do projeto no seu terminal e execute o seguinte comando:
    ```bash
    sudo docker compose up --build
    ```
    Este comando irá construir as imagens Docker para o frontend e o backend (se ainda não estiverem construídas ou se houver alterações) e, em seguida, iniciará os serviços. O `sudo` pode ser necessário dependendo da configuração do seu Docker.

2.  **Acessar a Aplicação:**
    *   O **Frontend** estará acessível em: `http://localhost:3000`. As chamadas da API do frontend para o backend (ex: `/api/start`) são automaticamente roteadas pelo Nginx para o serviço de backend.
    *   O **Backend API** (para acesso direto ou via ferramentas como curl/Postman) estará acessível em: `http://localhost:8000`. A documentação interativa da API (Swagger UI) está disponível em `http://localhost:8000/docs`.

    *Nota sobre Nomes dos Containers:* Os containers Docker terão nomes como `geminiflow-backend-1` e `geminiflow-frontend-1`. O nome base (`geminiflow`) pode ser customizado através da variável `PROJECT_NAME` no seu arquivo `.env`.

    *Nota sobre Builds da Imagem:* O `Dockerfile` agora inclui labels OCI (Open Container Initiative) para metadados. Se você estiver modificando o Dockerfile e construindo imagens para distribuição, por favor, atualize os valores de placeholder nas labels (ex: autor, URL do repositório).

3.  **Parar a Aplicação:**
    Para parar os containers, pressione `Ctrl+C` no terminal onde o `docker compose up` está rodando. Para remover os containers (e redes), você pode usar:
    ```bash
    sudo docker compose down
    ```

## Fluxo da Aplicação (Resumo)

1.  **Início:** O usuário fornece um nome para o projeto a ser planejado.
2.  **Fases Guiadas:** A aplicação guia o usuário por três fases principais através de um chat com a IA:
    *   Planejamento do Projeto
    *   Definição de Issues
    *   Configuração do Ambiente
3.  **Aprovação do Usuário:** Cada fase requer a aprovação explícita do usuário antes de prosseguir.
4.  **Geração de Artefatos:** Ao final, a aplicação gera os documentos e scripts de planejamento em um diretório de saída.

## Contribuições

Este projeto é um componente dentro do repositório maior "Projeto Gemini Workflow". Contribuições para o "Planejador Gemini-Flow" devem seguir as diretrizes gerais do repositório.
