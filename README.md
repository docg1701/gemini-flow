# Projeto Gemini Workflow: Padrões para Desenvolvimento Assistido por IA

## Visão Geral

Este repositório centraliza os "Gems" (prompts estruturados) que nossa equipe utiliza para padronizar o ciclo de vida do desenvolvimento de software com a assistência do Gemini. O objetivo é garantir consistência, qualidade e eficiência em todos os nossos projetos, desde o planejamento inicial até a configuração do ambiente e a criação de tarefas.

## Ferramenta Principal: `gemini-cli`

Todo o desenvolvimento assistido por IA e a interação com os modelos Gemini devem ser realizados através da ferramenta de linha de comando `gemini-cli`. Ela nos permite um controle granular sobre as ações da IA, incluindo a revisão de código, o uso de ferramentas e um fluxo de trabalho seguro e reprodutível.

## O Fluxo de Trabalho Padrão

Nosso processo de desenvolvimento para cada novo projeto é dividido em três fases principais, cada uma guiada por um Gem específico.

---

### **Fase 1: Planejamento Estratégico do Projeto**

O primeiro passo é traduzir as ideias e requisitos de negócio em um plano de trabalho técnico e estruturado.

1.  **Gem a ser utilizado:** `Arquiteto de Projetos`
2.  **Arquivo de Instruções:** `gemini-gem-arquiteto-de-projetos.md`
3.  **Processo:**
    - Crie um novo Gem no Gemini Advanced utilizando o conteúdo do arquivo `gemini-gem-arquiteto-de-projetos.md`.
    - Inicie uma conversa com este Gem. Ele irá guiá-lo interativamente para criar o plano do projeto.
4.  **Resultado Esperado:**
    - O Gem fornecerá o conteúdo completo para o arquivo `working-plan.md`. Este arquivo deve ser salvo na raiz do repositório do projeto e comitado no Git.

---

### **Fase 2: Criação e Rastreamento de Tarefas**

Com o plano definido, automatizamos a criação de tarefas rastreáveis no GitHub.

1.  **Gem a ser utilizado:** `Gerente de Issues`
2.  **Arquivo de Instruções:** `gemini-gem-gerador-de-issues.md`
3.  **Processo:**
    - Crie um Gem com o conteúdo do arquivo `gemini-gem-gerador-de-issues.md`.
    - Inicie uma conversa e forneça a ele o conteúdo do `working-plan.md` (da Fase 1) e a URL do seu repositório GitHub.
4.  **Resultado Esperado:**
    - O Gem irá gerar um **script shell** (`create_issues.sh`). Salve e execute este script no seu terminal (requer o GitHub CLI instalado) para criar todas as tarefas do plano como Issues no GitHub de uma só vez.

---

### **Fase 3: Configuração do Ambiente de Desenvolvimento**

Com as tarefas criadas, preparamos o ambiente local para que o `gemini-cli` atue de forma otimizada e alinhada ao plano.

1.  **Gem a ser utilizado:** `Arquiteto de Soluções DevOps & AI`
2.  **Arquivo de Instruções:** `gemini-gem-super-devops.md`
3.  **Processo:**
    - Crie um Gem com o conteúdo do arquivo `gemini-gem-super-devops.md`.
    - Inicie uma conversa e forneça a ele o conteúdo do `working-plan.md` para análise.
    - O Gem fará uma consultoria para gerar os arquivos de configuração.
4.  **Resultado Esperado:**
    - O Gem fornecerá o conteúdo para três arquivos essenciais:
        - `settings.json`: Configuração global da ferramenta (salvar em `~/.gemini/`).
        - `.env`: Segredos do projeto (salvar na raiz do projeto e **adicionar ao `.gitignore`**).
        - `GEMINI.md`: O "cérebro" do projeto com as instruções para a IA (salvar na raiz do projeto).

## Como Começar

1.  Clone este repositório para ter acesso local aos arquivos dos Gems.
2.  Acesse sua conta do Gemini Advanced.
3.  Crie os três Gems descritos acima, nomeando-os de forma clara.
4.  Para cada novo projeto da equipe, siga rigorosamente o fluxo de trabalho de três fases.

## Contribuições

Melhorias nos prompts e no fluxo de trabalho são bem-vindas. Por favor, abra uma issue para discutir as mudanças e envie um Pull Request para revisão.

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
