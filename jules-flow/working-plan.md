Com certeza, Galvani.

Aqui está o conteúdo completo para o arquivo `working-plan.md`, formatado em Markdown como solicitado.

```markdown
---
# Plano de Trabalho para Jules
## Objetivo Geral
Migrar o projeto "gemini-flow" de sua arquitetura atual (FastAPI + React/TypeScript) para uma aplicação monolítica em Python, utilizando o framework **NiceGUI** para a interface do usuário e o **LangChain** para orquestrar a lógica de negócio. O objetivo final do novo `gemini-flow` é atuar como um assistente de bootstrapping inteligente, que gera uma estrutura de projeto completa e um arquivo de contexto `GEMINI.md` robusto, preparando o ambiente para o uso subsequente da ferramenta `gemini-cli`.

## Passo a Passo da Execução para Jules
1.  **Configuração Inicial e Estrutura do Projeto:**
    * Crie uma nova estrutura de diretórios para o projeto unificado, por exemplo, um diretório `app/` na raiz.
    * Remova os diretórios existentes `/frontend` e `/backend`.
    * Atualize o arquivo `requirements.txt` para incluir `nicegui`, `langchain`, `langchain-google-genai` e quaisquer outras dependências necessárias. Remova `fastapi` e dependências relacionadas ao frontend antigo.
    * Crie o arquivo de entrada principal, `app/main.py`, que será responsável por inicializar e executar a aplicação NiceGUI.

2.  **Implementar Prova de Conceito (PoC) da Integração:**
    * No `app/main.py`, crie uma página NiceGUI mínima (um "Olá, Mundo") para garantir que o servidor está a funcionar corretamente.
    * Crie um módulo de orquestração `app/services/orchestrator.py`.
    * Implemente uma função simples no orquestrador que use LangChain para fazer uma chamada básica ao modelo Gemini.
    * Adicione um botão na página NiceGUI que chame essa função do orquestrador e exiba o resultado na interface. Isto validará a integração `NiceGUI <-> LangChain`.

3.  **Desenvolver a Interface do Wizard com NiceGUI:**
    * Projete e implemente uma interface de usuário no formato de um wizard passo a passo usando NiceGUI.
    * Crie módulos de UI separados dentro de um diretório `app/ui/` para cada etapa do wizard (ex: `ui/visao_geral.py`, `ui/pilha_tecnologica.py`, etc.).
    * A interface deve coletar de forma interativa todas as informações necessárias para o bootstrapping do projeto do usuário (nome do projeto, tecnologias, padrões, etc.).

4.  **Implementar o Orquestrador de Geração de Arquivos com LangChain:**
    * Desenvolva a lógica principal no `app/services/orchestrator.py`.
    * Crie "chains" no LangChain que recebam os dados coletados do wizard do NiceGUI como entrada.
    * Implemente a lógica para processar essas entradas e gerar o conteúdo de vários arquivos de configuração (ex: `Dockerfile`, `.gitignore`, `requirements.txt`).
    * Preste atenção especial à lógica de geração do `GEMINI.md`, que deve ser dinamicamente construído com base nas escolhas do usuário para refletir a arquitetura, os padrões de código e os fluxos de trabalho do projeto.

5.  **Gerar a Saída e Finalizar:**
    * Implemente a funcionalidade que, ao final do wizard, cria um diretório de saída (ex: `/output/nome-do-projeto-do-usuario`).
    * Escreva todos os arquivos gerados pelo orquestrador LangChain nesse diretório.
    * Adicione uma tela final no wizard do NiceGUI que informe o usuário que o projeto foi gerado com sucesso e indique o caminho para os arquivos.

6.  **Testes e Documentação:**
    * Crie testes unitários para a lógica no `app/services/orchestrator.py` para garantir que a geração de arquivos está correta.
    * Atualize o `README.md` principal do projeto para refletir a nova arquitetura, o propósito e como executar a aplicação NiceGUI.
    * Remova toda a documentação antiga relacionada à arquitetura FastAPI + React.
---
```
