# Gemini Flow: Padrões para Desenvolvimento Assistido por IA

## Visão Geral

Este repositório centraliza os "Gems" (prompts estruturados) que nossa equipe utiliza para padronizar o ciclo de vida do desenvolvimento de software com a assistência do Gemini. O objetivo é garantir consistência, qualidade e eficiência em todos os nossos projetos, desde o planejamento inicial até a configuração do ambiente de desenvolvimento.

## Ferramenta Principal: `gemini-cli`

Todo o desenvolvimento assistido por IA e a interação com os modelos Gemini devem ser realizados através da ferramenta de linha de comando `gemini-cli`. Ela nos permite um controle granular sobre as ações da IA, incluindo a revisão de código, o uso de ferramentas e um fluxo de trabalho seguro e reprodutível.

## O Fluxo de Trabalho Padrão

Nosso processo de desenvolvimento para cada novo projeto é dividido em duas fases principais, cada uma guiada por um Gem específico.

---

### **Fase 1: Planejamento Estratégico do Projeto**

O primeiro passo é traduzir as ideias e requisitos de negócio em um plano de trabalho técnico e estruturado.

1.  **Gem a ser utilizado:** `Arquiteto de Projetos`
2.  **Arquivo de Instruções:** `gemini-gem-arquiteto-de-projetos.md`
3.  **Processo:**
    - Crie um novo Gem no Gemini Advanced utilizando o conteúdo do arquivo `gemini-gem-arquiteto-de-projetos.md`.
    - Inicie uma conversa com este Gem. Ele irá guiá-lo interativamente, fazendo perguntas sobre os objetivos, escopo, tecnologias e cronograma do projeto.
4.  **Resultado Esperado:**
    - Ao final da conversa, o Gem fornecerá o conteúdo completo para o arquivo `working-plan.md`. Este arquivo deve ser salvo na raiz do repositório do projeto e comitado no Git.

---

### **Fase 2: Configuração do Ambiente de Desenvolvimento**

Com o plano de trabalho em mãos, o próximo passo é configurar o ambiente de desenvolvimento para que o `gemini-cli` possa atuar de forma otimizada e alinhada ao plano.

1.  **Gem a ser utilizado:** `Arquiteto de Soluções DevOps & AI`
2.  **Arquivo de Instruções:** `gemini-gem-super-devops.md`
3.  **Processo:**
    - Crie um segundo Gem no Gemini Advanced com o conteúdo do arquivo `gemini-gem-super-devops.md`.
    - Inicie uma conversa com este novo Gem. **Sua primeira ação será fornecer a ele o conteúdo completo do `working-plan.md` gerado na Fase 1.**
    - O Gem analisará o plano e fará uma consultoria para gerar os arquivos de configuração, sugerindo as melhores práticas.
4.  **Resultado Esperado:**
    - O Gem fornecerá o conteúdo para três arquivos essenciais:
        - `settings.json`: Configuração global da ferramenta `gemini-cli` (salvar em `~/.gemini/`).
        - `.env`: Variáveis de ambiente e segredos do projeto (salvar na raiz do projeto e **adicionar ao `.gitignore`**).
        - `GEMINI.md`: O "cérebro" do projeto, com as instruções contextuais para a IA (salvar na raiz do projeto).

## Como Começar

1.  Clone este repositório para ter acesso local aos arquivos dos Gems.
2.  Acesse sua conta do Gemini Advanced.
3.  Crie os dois Gems descritos acima, nomeando-os de forma clara (ex: "Planejador de Projetos" e "Configurador de Ambiente").
4.  Para cada novo projeto da equipe, siga rigorosamente o fluxo de trabalho de duas fases.

## Contribuições

Melhorias nos prompts e no fluxo de trabalho são bem-vindas. Por favor, abra uma issue para discutir as mudanças e envie um Pull Request para revisão.

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
