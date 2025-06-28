# Pesquisa sobre FastAPI

## Documentação Oficial
- FastAPI Main Page: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Tutorial - User Guide: [https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)
- Advanced User Guide: [https://fastapi.tiangolo.com/advanced/](https://fastapi.tiangolo.com/advanced/)

## Conceitos Chave para o Projeto "Planejador Gemini-Flow"

### 1. Criação de Endpoints
- Usar decoradores como `@app.get("/")`, `@app.post("/items/")`.
- Definir parâmetros de path, query, e body.
- Exemplo:
  ```python
  from fastapi import FastAPI
  app = FastAPI()
  @app.get("/items/{item_id}")
  async def read_item(item_id: int, q: str | None = None):
      return {"item_id": item_id, "q": q}
  ```

### 2. Validação de Dados com Pydantic
- Definir modelos Pydantic para request e response bodies.
- FastAPI usa esses modelos para validação automática e serialização/deserialização de dados.
- Exemplo:
  ```python
  from pydantic import BaseModel
  class Item(BaseModel):
      name: str
      description: str | None = None
      price: float
      tax: float | None = None
  @app.post("/items/")
  async def create_item(item: Item):
      return item
  ```

### 3. Gerenciamento de Configuração
- Pode ser feito com `python-decouple` (conforme planejado no `working-plan.md`) ou `pydantic-settings`.
- Carregar variáveis de ambiente (ex: API keys) de forma segura.
- Exemplo com `pydantic-settings`:
  ```python
  from pydantic_settings import BaseSettings
  class Settings(BaseSettings):
      GEMINI_API_KEY: str
      # ... outras configurações
      class Config:
          env_file = ".env"
  settings = Settings()
  # Usar settings.GEMINI_API_KEY
  ```

### 4. Middlewares para Tratamento de Erros
- FastAPI permite adicionar middlewares para processar requests e responses globalmente.
- Útil para capturar exceções e retornar respostas HTTP padronizadas.
- Exemplo:
  ```python
  from fastapi import FastAPI, Request
  from fastapi.responses import JSONResponse
  app = FastAPI()
  class MyCustomException(Exception):
      pass
  @app.exception_handler(MyCustomException)
  async def my_custom_exception_handler(request: Request, exc: MyCustomException):
      return JSONResponse(
          status_code=418,
          content={"message": f"Oops! {exc} did something. It's a teapot problem."},
      )
  @app.get("/custom-exception/")
  async def custom_exception_route():
      raise MyCustomException("Something broke")
  ```
- Para exceções HTTP padrão, usar `HTTPException` do FastAPI.

### 5. Estrutura do Projeto e Módulos
- Organizar o código em múltiplos arquivos/módulos (ex: `main.py`, `orchestrator.py`, `config.py`).
- Usar `APIRouter` para dividir endpoints em diferentes módulos.
  ```python
  # In items.py
  from fastapi import APIRouter
  router = APIRouter()
  @router.get("/items/")
  async def read_items():
      return [{"name": "Item Foo"}, {"name": "Item Bar"}]

  # In main.py
  from fastapi import FastAPI
  from .routers import items # Supondo que items.py está em ./routers/
  app = FastAPI()
  app.include_router(items.router)
  ```

### 6. Langchain e Integração com Gemini
- `langchain` e `langchain-google-genai` serão usados para a lógica de conversação.
- A API key será carregada via configuração.
- O `orchestrator.py` provavelmente conterá a lógica de carregar prompts e interagir com o modelo Gemini através do Langchain.

## Endpoints Planejados
- `/start` (POST): Iniciar uma nova sessão de planejamento. Receber nome do projeto.
- `/chat` (POST): Enviar mensagem do usuário e receber resposta da IA. Incluir `is_approval_step`.
- `/approve` (POST): Sinalizar aprovação de uma fase pelo usuário.
- `/generate_files` (GET/POST): Gerar a estrutura de projeto final.

## Considerações Adicionais
- **Async/Await**: FastAPI é construído sobre `asyncio`. Usar `async def` para os endpoints e operações I/O-bound.
- **Dependências**: Gerenciar com `pyproject.toml` e `poetry` ou `pip`.
- **Testes**: FastAPI tem bom suporte para testes com `pytest` e `TestClient`.

Este resumo cobre os pontos principais para iniciar o desenvolvimento do backend conforme o `working-plan.md`.
