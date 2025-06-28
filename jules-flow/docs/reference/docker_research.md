# Pesquisa sobre Docker e Docker Compose para Containerização

## Documentação Oficial
- Docker: [https://docs.docker.com/](https://docs.docker.com/)
- Dockerfile reference: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
- Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Compose file reference: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)

## Conceitos Chave para o Projeto "Planejador Gemini-Flow"

### 1. Dockerfile Multi-stage
- **Propósito**: Criar imagens Docker otimizadas, separando o ambiente de build do ambiente de runtime. Isso resulta em imagens menores e mais seguras.
- **Para o Frontend (React/TypeScript)**:
    - Stage 1 (build): Usar uma imagem base Node.js (ex: `node:18-alpine` ou `node:20-slim`) para instalar dependências (`npm install`) e construir os arquivos estáticos (`npm run build`).
    - Stage 2 (runtime): Usar uma imagem de servidor web leve (ex: `nginx:alpine`) para servir os arquivos estáticos gerados no stage 1. Copiar os artefatos do build do stage 1 para o diretório apropriado do Nginx.
- **Para o Backend (Python/FastAPI)**:
    - Stage 1 (build/dependencies - opcional, mas bom para gerenciar dependências): Usar uma imagem base Python (ex: `python:3.10-slim`) para instalar dependências (`pip install -r requirements.txt` ou `poetry install`).
    - Stage 2 (runtime): Usar uma imagem Python leve (ex: `python:3.10-slim`). Copiar o código da aplicação e as dependências (se instaladas em um local separado no stage 1) para esta imagem. Definir o `CMD` para rodar a aplicação FastAPI com Uvicorn.
- **Dockerfile Unificado (Multi-stage para ambos)**: Um único `Dockerfile` na raiz do projeto pode construir ambas as imagens ou, mais comumente, o `docker-compose.yml` referencia Dockerfiles separados para cada serviço (`frontend/Dockerfile` e `backend/Dockerfile`). O `working-plan.md` menciona um `Dockerfile` multi-stage na raiz, o que sugere que ele poderia construir o frontend e o backend e, em seguida, o `docker-compose.yml` usaria contextos de build diferentes ou stages específicos desse Dockerfile. Uma abordagem mais clara é ter Dockerfiles separados e um `docker-compose.yml` que os orquestra.
    *Revisando o `working-plan.md` (item 18: "criar um `Dockerfile` multi-stage na raiz do projeto, conforme definido na visão"), a intenção é provavelmente um único Dockerfile que pode construir ambos, e o `docker-compose.yml` especificaria qual `target` stage usar para cada serviço.
    ```dockerfile
    # frontend/Dockerfile (Exemplo)
    # Stage 1: Build React App
    FROM node:20-slim AS build-react
    WORKDIR /app
    COPY frontend/package.json frontend/package-lock.json ./
    RUN npm install
    COPY frontend/ ./
    RUN npm run build

    # Stage 2: Serve React App with Nginx
    FROM nginx:alpine AS serve-react
    COPY --from=build-react /app/build /usr/share/nginx/html
    # COPY nginx.conf /etc/nginx/conf.d/default.conf # Opcional: para configuração customizada do Nginx

    # backend/Dockerfile (Exemplo)
    FROM python:3.10-slim AS python-base
    WORKDIR /app
    COPY backend/pyproject.toml backend/poetry.lock* ./
    # Ou COPY backend/requirements.txt ./
    RUN pip install --no-cache-dir poetry \
        && poetry config virtualenvs.create false \
        && poetry install --no-dev --no-interaction --no-ansi
    # Ou RUN pip install --no-cache-dir -r requirements.txt

    COPY backend/ ./

    # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] # Este será o CMD do serviço backend
    ```
    O `Dockerfile` na raiz pode usar estes como base ou incorporá-los. Se for um único `Dockerfile` na raiz:
    ```dockerfile
    # Dockerfile (raiz)

    # --- Frontend Build Stage ---
    FROM node:20-slim AS frontend-builder
    WORKDIR /app/frontend
    COPY frontend/package.json frontend/package-lock.json* ./
    RUN npm ci
    COPY frontend/ ./
    RUN npm run build

    # --- Backend Build Stage (se necessário para compilação ou assets) ---
    # Normalmente para Python, as dependências são instaladas no runtime stage
    # Mas se houvesse passos de compilação, seria aqui.

    # --- Frontend Runtime Stage ---
    FROM nginx:alpine AS frontend
    COPY --from=frontend-builder /app/frontend/build /usr/share/nginx/html
    # COPY nginx_custom.conf /etc/nginx/conf.d/default.conf # Se precisar de config Nginx

    # --- Backend Runtime Stage ---
    FROM python:3.10-slim AS backend
    WORKDIR /app
    COPY backend/pyproject.toml backend/poetry.lock* ./
    # ou COPY backend/requirements.txt ./
    # Instalar dependências
    RUN pip install --no-cache-dir poetry && \
        poetry config virtualenvs.create false && \
        poetry install --no-interaction --no-ansi --no-root && \
        poetry self add uvicorn # Adicionar uvicorn se não estiver no pyproject.toml principal
    # ou RUN pip install --no-cache-dir -r requirements.txt
    COPY backend/ ./
    # Comando será definido no docker-compose.yml ou aqui
    # CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```

### 2. Configuração de Serviços no `docker-compose.yml`
- Definir serviços para `frontend` e `backend`.
- Especificar `build` context e `dockerfile` para cada serviço. Se usando um único Dockerfile na raiz com múltiplos targets, pode-se usar `target`:
  ```yaml
  version: '3.8'
  services:
    backend:
      build:
        context: .
        dockerfile: Dockerfile # Dockerfile na raiz
        target: backend # Especifica o target stage 'backend'
      ports:
        - "8000:8000"
      env_file:
        - .env
      volumes:
        - ./backend:/app # Para desenvolvimento, para hot-reloading
        # Em produção, o código já estaria na imagem
      command: poetry run uvicorn main:app --host 0.0.0.0 --port 8000 # Exemplo de comando

    frontend:
      build:
        context: .
        dockerfile: Dockerfile # Dockerfile na raiz
        target: frontend # Especifica o target stage 'frontend'
      ports:
        - "3000:80" # Nginx no container roda na 80 por padrão
      depends_on:
        - backend
      # Não precisa de volumes para código se servindo build estático
      # Se usando dev server do React, precisaria de volumes e comando diferente
  ```

### 3. Mapeamento de Portas e Volumes
- **Portas**: Expor as portas dos containers para o host (ex: `frontend` porta 80 do Nginx para porta 3000 do host, `backend` porta 8000 do Uvicorn para porta 8000 do host).
- **Volumes**:
    - Para desenvolvimento: Montar o código fonte local nos containers para permitir hot-reloading (ex: `./backend:/app` para o backend FastAPI, `./frontend/src:/app/src` para o frontend React com dev server).
    - Para produção: Geralmente não se usa volumes para o código da aplicação, pois ele já está copiado para dentro da imagem durante o build. Volumes podem ser usados para dados persistentes (ex: bancos de dados), mas não é o caso aqui.
    - O `working-plan.md` implica uma estrutura de projeto final gerada, então o Docker Compose provavelmente será para execução, não necessariamente para hot-reloading de desenvolvimento, embora possa ser configurado para ambos os cenários (com `docker-compose.override.yml` por exemplo).

### 4. Gerenciamento de Variáveis de Ambiente com Arquivos `.env`
- Criar um arquivo `.env` na raiz do projeto (ao lado do `docker-compose.yml`).
- Listar variáveis de ambiente nele (ex: `GEMINI_API_KEY=xxxx`).
- Referenciar o `.env` no `docker-compose.yml` usando `env_file`.
  ```yaml
  services:
    backend:
      # ...
      env_file:
        - .env
  ```
- O `.env` deve ser adicionado ao `.gitignore`. Um `.env.example` deve ser versionado.

### 5. Orquestração de Múltiplos Containers
- `docker-compose up`: Constrói (se necessário) e inicia todos os serviços definidos no `docker-compose.yml`.
- `docker-compose down`: Para e remove os containers, redes e volumes (opcionalmente).
- **Comunicação entre containers**: Containers na mesma rede Docker (criada por padrão pelo Docker Compose) podem se comunicar usando os nomes dos serviços como hostnames.
    - Ex: O frontend (rodando no browser do usuário, mas o código é servido pelo Nginx container) fará chamadas para o backend usando `http://backend:8000/api/...` se a chamada for feita do container Nginx (ex: em SSR ou se Nginx fizesse proxy).
    - **Importante**: Como o frontend é React (client-side), as chamadas API serão feitas do navegador do usuário para o host da máquina. Portanto, o frontend chamará `http://localhost:8000/api/...` (ou o IP/hostname onde o backend está exposto). Se o Nginx estiver configurado para fazer proxy reverso para o backend, então o React pode chamar o Nginx (ex: `http://localhost:3000/api/...`) e o Nginx encaminha para `http://backend:8000/api/...`. Esta última é uma configuração comum para evitar CORS e simplificar URLs.

### 6. Script `bootstrap.sh`
- O `working-plan.md` menciona um `bootstrap.sh` interativo gerado pela aplicação. Este script não faz parte da configuração Docker em si, mas é um artefato produzido pela aplicação que roda dentro do Docker.

## Considerações Adicionais
- **Rede**: Docker Compose cria uma rede padrão para os serviços.
- **Saúde e Dependências**: Usar `depends_on` para controlar a ordem de inicialização (embora não garanta que o serviço dependente esteja "pronto", apenas que o container iniciou). Para checagens de saúde mais robustas, usar `healthcheck`.
- **Produção vs Desenvolvimento**: Pode-se usar um `docker-compose.override.yml` para configurações específicas de desenvolvimento (como volumes para hot-reload e portas diferentes).

Este resumo cobre os pontos principais para containerizar a aplicação "Planejador Gemini-Flow" usando Docker e Docker Compose, conforme o `working-plan.md`.
