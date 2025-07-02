# Visão do Projeto: Gemini-Flow (NiceGUI Monolithic Edition)

## 1. Objetivo Geral do Projeto

O projeto "gemini-flow" está sendo migrado de sua arquitetura anterior (FastAPI + React/TypeScript) para uma **aplicação monolítica em Python**, utilizando o framework **NiceGUI** para a interface do usuário e **LangChain** para orquestrar a lógica de negócio.

O objetivo final do novo `gemini-flow` é atuar como um **assistente de bootstrapping inteligente**. Através de uma interface de wizard interativa construída com NiceGUI, o usuário fornecerá informações sobre o projeto que deseja iniciar. Com base nessas entradas, a aplicação, orquestrada pelo LangChain e utilizando o poder do modelo Gemini, gerará:

1.  Uma **estrutura de projeto completa** e customizada para o usuário.
2.  Um arquivo de contexto `GEMINI.md` robusto, detalhando a arquitetura, tecnologias, padrões de código e fluxos de trabalho do projeto gerado.

Este output visa preparar o ambiente para o uso subsequente da ferramenta `gemini-cli` ou para desenvolvimento manual, acelerando significativamente o início de novos projetos de software.

## 2. Arquitetura Principal Pretendida

A nova arquitetura será um monólito Python, simplificando o desenvolvimento e o deploy em comparação com a abordagem anterior de microsserviços.

*   **Interface do Usuário (Frontend)**:
    *   Totalmente construída com **NiceGUI**.
    *   Apresentará um wizard passo a passo para coletar as especificações do projeto do usuário.
    *   Será servida diretamente pela aplicação Python.
*   **Lógica de Negócio e Orquestração (Backend)**:
    *   Implementada em Python.
    *   **LangChain** será usado para:
        *   Gerenciar interações com o modelo de linguagem (Google Gemini).
        *   Construir "chains" que processam as entradas do usuário.
        *   Orquestrar a geração do conteúdo dos arquivos do projeto.
    *   Um módulo de serviço (ex: `app/services/orchestrator.py`) centralizará essa lógica.
*   **Ponto de Entrada da Aplicação**:
    *   Um único script Python (ex: `app/main.py`) inicializará e executará a aplicação NiceGUI.
*   **Estrutura de Diretórios**:
    *   Todo o código da aplicação residirá dentro de um diretório principal `app/`.
    *   Subdiretórios como `app/ui/` (para módulos do wizard NiceGUI) e `app/services/` (para a lógica LangChain) organizarão o código.
    *   Os diretórios `/frontend` e `/backend` da arquitetura antiga serão removidos.

## 3. Principais Funcionalidades ou Módulos

Conforme o `jules-flow/working-plan.md`, as funcionalidades chave são:

1.  **Wizard Interativo (NiceGUI)**:
    *   Coleta de dados do usuário em múltiplos passos (nome do projeto, descrição, tecnologias, padrões, etc.).
    *   Interface amigável e guiada.
2.  **Orquestrador de Geração de Arquivos (LangChain & Gemini)**:
    *   Recebe os dados do wizard.
    *   Utiliza chains LangChain e prompts para o modelo Gemini para gerar o conteúdo de:
        *   `Dockerfile`
        *   `.gitignore`
        *   `requirements.txt` (ou equivalente, baseado nas tecnologias)
        *   `GEMINI.md` (documento de contexto detalhado)
        *   Outros arquivos de configuração básicos, conforme aplicável.
3.  **Geração da Estrutura do Projeto**:
    *   Criação de um diretório de saída (ex: `output/nome-do-projeto/`).
    *   Escrita dos arquivos gerados na estrutura de diretórios apropriada dentro do diretório de saída.
4.  **Feedback ao Usuário**:
    *   Tela final no wizard NiceGUI indicando sucesso e o caminho para os arquivos gerados.

## 4. Princípios de Design e Tecnologias Chave

*   **Backend-First com NiceGUI**: Foco na lógica Python, com NiceGUI gerenciando a complexidade do frontend.
*   **Orquestração Inteligente com LangChain**: Uso de chains e prompts para interagir com o LLM (Gemini) e gerar conteúdo de forma estruturada.
*   **Monólito Python**: Simplificação da arquitetura para facilitar desenvolvimento e manutenção.
*   **Geração Dinâmica e Customizada**: O output (estrutura de projeto e `GEMINI.md`) deve ser altamente customizado com base nas entradas do usuário.
*   **Tecnologias Principais**:
    *   Python
    *   NiceGUI (para UI)
    *   LangChain (para orquestração LLM)
    *   Google Gemini (como o LLM)

## 5. Principais Fluxos de Interação ou Dados

1.  **Coleta de Dados**:
    *   Usuário inicia a aplicação NiceGUI.
    *   Usuário navega pelo wizard, inserindo informações sobre o projeto desejado em cada passo.
    *   NiceGUI armazena os dados coletados (provavelmente em `app.storage.user`).
2.  **Processamento e Geração**:
    *   Ao final do wizard, o usuário aciona a geração do projeto.
    *   A aplicação NiceGUI passa os dados coletados para o módulo orquestrador (`app/services/orchestrator.py`).
    *   O orquestrador utiliza chains LangChain (com prompts parametrizados pelos dados do usuário) para interagir com o modelo Gemini.
    *   Gemini retorna o conteúdo para cada arquivo a ser gerado.
3.  **Criação do Output**:
    *   O orquestrador (ou uma função chamada por ele) cria a estrutura de diretórios do novo projeto em `output/nome-do-projeto/`.
    *   Os conteúdos de arquivo gerados são escritos nos locais corretos dentro desta estrutura.
4.  **Feedback**:
    *   A interface NiceGUI exibe uma mensagem de sucesso e o caminho para o projeto gerado.

Este `VISION.md` reflete a transição para uma aplicação monolítica focada na geração de projetos via um wizard NiceGUI e lógica LangChain, conforme o plano de trabalho atual.
---
