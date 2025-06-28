# --- Frontend Build Stage ---
FROM node:20-slim AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
# Use npm ci for installing dependencies from lock file
RUN npm ci
COPY frontend/ ./
RUN npm run build

# --- Backend Stage ---
FROM python:3.10-slim AS backend
WORKDIR /app
# Copy poetry files first for dependency caching
COPY backend/pyproject.toml backend/poetry.lock* ./
# Install poetry and dependencies
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --only main
# Copy the rest of the backend application code
COPY backend/ ./
# The CMD will be specified in docker-compose.yml or can be added here if preferred
# Example: CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# --- Frontend Runtime Stage ---
FROM nginx:1.25-alpine AS frontend
# Copy built frontend assets from the frontend-builder stage
COPY --from=frontend-builder /app/frontend/build /usr/share/nginx/html
# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Expose port 80 for Nginx
EXPOSE 80
# Nginx will be started by default when the container runs
