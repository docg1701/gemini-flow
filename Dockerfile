# Dockerfile para Gemini-Flow

# --- Argumentos Globais ---
ARG NODE_VERSION=22-slim
ARG PYTHON_VERSION=3.12-slim
ARG NGINX_VERSION=1.26-alpine
ARG APP_USER=appuser
ARG APP_GROUP=appgroup

# --- Labels Comuns (Temporariamente Comentadas para Teste) ---
# ARG APP_VERSION=0.1.0 # Example, can be overridden or set in docker-compose build args
# LABEL org.opencontainers.image.title="Gemini-Flow Application"
# LABEL org.opencontainers.image.description="A multi-component application using FastAPI backend and React frontend, orchestrated by Gemini-Flow."
# LABEL org.opencontainers.image.version=${APP_VERSION}
# LABEL org.opencontainers.image.authors="Your Name/Team <your.email@example.com>"
# LABEL org.opencontainers.image.source="https://github.com/your-repo/gemini-flow"
# LABEL org.opencontainers.image.documentation="https://github.com/your-repo/gemini-flow/blob/main/README.md"
# LABEL org.opencontainers.image.vendor="Your Organization"
# TODO: Update placeholder values in the LABELs above with actual maintainer, source repo, documentation, and vendor information.
# LABEL maintainer="team" # Using OCI labels instead
# LABEL description="app" # Using OCI labels instead
# LABEL version=${APP_VERSION} # Using OCI labels instead

# ==============================================================================
# Frontend Build Stage
# ==============================================================================
FROM node:${NODE_VERSION} AS frontend-builder
LABEL stage="frontend-builder"
WORKDIR /app/frontend

COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/public ./public
COPY frontend/src ./src
COPY frontend/tsconfig.json ./

RUN npm run build

# ==============================================================================
# Backend Stage (Renomeado)
# ==============================================================================
FROM python:${PYTHON_VERSION} AS backend_app
LABEL stage="backend_app"

ARG APP_USER
ARG APP_GROUP

WORKDIR /app

# 1. Operações como root: Criar usuário/grupo
RUN groupadd -r ${APP_GROUP} && useradd --no-log-init -r -g ${APP_GROUP} -d /app -s /bin/bash ${APP_USER}

# Copiar arquivos de dependência do Poetry
COPY backend/pyproject.toml backend/poetry.lock ./

# Configurar ENVs do Poetry
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_CACHE_DIR="/app/.cache/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

# Instalar dependências de sistema, Poetry, e configurar Poetry (ainda como root)
RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry config virtualenvs.in-project false \
    && poetry config virtualenvs.path null \
    && poetry env use system \
    && mkdir -p "$POETRY_CACHE_DIR" \
    # Chown inicial para o diretório de trabalho e cache do poetry para appuser
    # Isso é feito antes do poetry install, mas poetry install ainda roda como root nesta versão
    # APP_USER does not need to own POETRY_HOME itself, only execute binaries from it.
    && chown -R ${APP_USER}:${APP_GROUP} /app "$POETRY_CACHE_DIR"

# Instalar dependências do projeto COMO ROOT.
# Poetry vai instalar os pacotes em um local do sistema que o appuser poderá ler.
# Using --without dev to exclude development dependencies for a leaner image.
RUN poetry install --no-interaction --no-ansi --no-root --without dev
# Remover .venv se criado acidentalmente
RUN rm -rf /app/.venv

# Copia o restante dos arquivos da aplicação COMO ROOT
COPY backend/ ./

# Chown final de tudo em /app para appuser, EXECUTADO COMO ROOT
RUN chown -R ${APP_USER}:${APP_GROUP} /app

ENV PYTHONPATH=/app
# Mudar para appuser para a execução do container (final)
USER ${APP_USER}

# O comando no docker-compose.yml (poetry run uvicorn...) será executado como appuser.
# O appuser agora é dono de /app e seu conteúdo.
# As dependências foram instaladas globalmente pelo root, mas são acessíveis.

# ==============================================================================
# Frontend Runtime Stage (Nginx)
# ==============================================================================
FROM nginx:${NGINX_VERSION} AS frontend
LABEL stage="frontend-runtime"

COPY --from=frontend-builder /app/frontend/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
