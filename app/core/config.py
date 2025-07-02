from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Gemini-Flow Bootstrapper"
    GEMINI_API_KEY: str = "YOUR_GEMINI_API_KEY_HERE"  # Default, expecting override from .env

    # Para carregar de um arquivo .env na raiz do projeto
    # O .env não deve ser commitado se contiver chaves reais.
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8', extra='ignore')

settings = Settings()

# Adicionar um .env.example para guiar o usuário
# Este .env.example DEVE ser commitado.
# O .env real NÃO DEVE.
# Esta lógica de criar o .env.example aqui é apenas para garantir que ele exista
# para esta task. Idealmente, seria um arquivo já existente no repo.
# Conteúdo para .env.example:
# GEMINI_API_KEY=SUA_CHAVE_API_AQUI
