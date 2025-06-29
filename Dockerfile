# Dockerfile para Gemini-Flow

# --- Argumentos Globais ---
ARG NODE_VERSION=20-slim
ARG PYTHON_VERSION=3.10-slim
ARG NGINX_VERSION=1.25-alpine
ARG APP_USER=appuser
ARG APP_GROUP=appgroup

# --- Labels Comuns ---
#LABEL maintainer="Jules <jules@example.com>"
#LABEL description="Aplicação Gemini-Flow (Backend Python/FastAPI e Frontend React/Nginx)"

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

RUN groupadd -r ${APP_GROUP} && useradd --no-log-init -r -g ${APP_GROUP} ${APP_USER}

COPY backend/pyproject.toml backend/poetry.lock ./

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apt-get update && apt-get install --no-install-recommends -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY backend/ ./
RUN chown -R ${APP_USER}:${APP_GROUP} /app
USER ${APP_USER}

# ==============================================================================
# Frontend Runtime Stage (Nginx)
# ==============================================================================
FROM nginx:${NGINX_VERSION} AS frontend
LABEL stage="frontend-runtime"

COPY --from=frontend-builder /app/frontend/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
