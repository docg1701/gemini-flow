# Projeto Gemini Workflow: Linha de Produção para Desenvolvimento Assistido por IA

## Visão Geral

Este repositório centraliza a nossa "Linha de Produção de Software", um conjunto de "Gems" (prompts estruturados) que orquestram o ciclo de vida do desenvolvimento com a assistência do Gemini. O objetivo é transformar um plano inicial numa base de projeto totalmente configurada, garantindo consistência, qualidade e máxima automação.

## Ferramenta Principal: `gemini-cli`

Todo o desenvolvimento assistido por IA e a interação com os modelos Gemini **devem** ser realizados através da ferramenta de linha de comando `gemini-cli`. Ela permite um controlo granular sobre as ações da IA, incluindo a revisão de código, o uso de ferramentas e um fluxo de trabalho seguro e reprodutível.

## O Pipeline de Automação (Fase 1 ➡️ Fase 2 ➡️ Fase 3)

O nosso processo para cada novo projeto segue um pipeline de três fases, onde o resultado de uma fase é a entrada da seguinte. Cada fase é guiada por um Gem especialista.

### Fase 1: Orquestração do Plano Mestre

O primeiro passo é transformar os requisitos de negócio numa "partitura" técnica que guiará toda a automação subsequente.

* **Gem a ser utilizado:** **Maestro de Projetos** (o antigo "Arquiteto de Projetos")
* **Ficheiro de Instruções:** `gemini-gem-maestro-de-projetos.md`
* **Processo:**
    1.  Crie um novo Gem no Gemini Advanced utilizando o conteúdo do ficheiro de instruções.
    2.  Inicie uma conversa com o "Maestro". Ele irá guiá-lo interativamente para criar o plano do projeto, recolhendo todos os detalhes necessários para as fases seguintes.
* **Resultado Esperado:**
    * O Gem fornecerá o conteúdo completo para o ficheiro `working-plan.md`. Este documento é a **única fonte da verdade** e deve ser salvo na raiz do repositório do projeto e commitado no Git.

### Fase 2: Geração Automatizada de Issues

Com o plano definido, processamo-lo para criar tarefas rastreáveis no GitHub de forma automática.

* **Gem a ser utilizado:** **Gerente de Issues**
* **Ficheiro de Instruções:** `gemini-gem-gerador-de-issues.md`
* **Processo:**
    1.  Crie um Gem com o conteúdo do ficheiro de instruções.
    2.  Inicie uma conversa e forneça a ele **apenas o conteúdo do `working-plan.md`**. O Gem irá extrair de forma inteligente a URL do repositório, os títulos, corpos, responsáveis (`@`) e etiquetas (`#`) diretamente do plano.
* **Resultado Esperado:**
    * O Gem irá gerar um script shell (ex: `create_issues.sh`). Salve e execute este script para criar todas as tarefas como Issues no GitHub de uma só vez (requer o [GitHub CLI](https://cli.github.com/) instalado e autenticado).

### Fase 3: Arquitetura do Ambiente de Desenvolvimento

Com o projeto planeado e as tarefas criadas, arquitetamos o ambiente local para que o `gemini-cli` atue de forma otimizada.

* **Gem a ser utilizado:** **Arquiteto de Soluções DevOps & AI**
* **Ficheiro de Instruções:** `gemini-gem-super-devops.md`
* **Processo:**
    1.  Crie um Gem com o conteúdo do ficheiro de instruções.
    2.  Inicie uma conversa e forneça a ele o conteúdo do `working-plan.md`.
    3.  O Gem irá analisar o plano e **propor uma arquitetura de configuração completa** para sua validação, em vez de fazer uma consultoria longa.
* **Resultado Esperado:**
    * O Gem fornecerá o conteúdo para três ficheiros essenciais:
        * `settings.json`: Configuração global da ferramenta (salvar em `~/.gemini/`).
        * `.env.example`: **Template seguro** para segredos do projeto.
        * `GEMINI.md`: A "constituição" do projeto com as instruções para a IA (salvar na raiz do projeto).

## Como Começar

1.  Clone este repositório para ter acesso local aos ficheiros dos Gems.
2.  Acesse sua conta do Gemini Advanced.
3.  Crie os três Gems descritos acima, nomeando-os de forma clara (ex: "Maestro de Projetos").
4.  Para cada novo projeto da equipe, siga rigorosamente o pipeline de três fases.

## Contribuições

Melhorias nos prompts e no pipeline são bem-vindas. Por favor, abra uma issue para discutir as mudanças e envie um Pull Request para revisão.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o ficheiro `LICENSE` para mais detalhes.
