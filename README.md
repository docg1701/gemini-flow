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

## Configuração

1.  **Chave da API do Gemini:**
    Este projeto requer uma chave da API do Google Gemini para interagir com os modelos de linguagem.
    *   Copie o arquivo `.env.example` para um novo arquivo chamado `.env` na raiz do projeto:
        ```bash
        cp .env.example .env
        ```
    *   Abra o arquivo `.env` e substitua `SUA_CHAVE_AQUI` pela sua chave da API do Gemini:
        ```
        GEMINI_API_KEY=SUA_CHAVE_AQUI_REAL
        ```

## Como Executar a Aplicação

Com o Docker e o Docker Compose instalados e o arquivo `.env` configurado:

1.  **Construir e Iniciar os Containers:**
    Navegue até o diretório raiz do projeto no seu terminal e execute o seguinte comando:
    ```bash
    sudo docker compose up --build
    ```
    Este comando irá construir as imagens Docker para o frontend e o backend (se ainda não estiverem construídas ou se houver alterações) e, em seguida, iniciará os serviços. O `sudo` pode ser necessário dependendo da configuração do seu Docker.

2.  **Acessar a Aplicação:**
    *   O **Frontend** estará acessível em: `http://localhost:3000`
    *   O **Backend API** estará acessível em: `http://localhost:8000` (com documentação interativa da API em `http://localhost:8000/docs`)

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
