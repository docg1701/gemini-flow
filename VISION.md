# Visão Consolidada do Projeto: Planejador Gemini-Flow

## 1. O Conceito Central

O "Planejador Gemini-Flow" será uma aplicação web stand-alone e containerizada, projetada para atuar como um assistente especialista em arquitetura de software. Através de uma interface de chat, o usuário será guiado por um diálogo colaborativo com uma IA (potencializada pelo Gemini e orquestrada pelo LangChain) para transformar um objetivo de alto nível em uma estrutura de projeto completa e pronta para uso, com todos os artefatos necessários.

## 2. Princípios de Design e Filosofia

* **Inteligência Flexível e Modular:** A "inteligência" da aplicação reside nos arquivos de prompt `.md`, não no código-fonte. Isso nos permite evoluir, adaptar e refinar o comportamento do assistente sem a necessidade de reescrever a lógica da aplicação, tornando-o extremamente flexível.
* **Controle Explícito do Usuário:** Embora a interação seja conversacional, o fluxo do projeto não avança sem a aprovação explícita do usuário. O uso de um botão "Aprovar" em cada fase garante que o usuário final tenha sempre o controle total sobre o processo e as decisões.
* **Experiência de Desenvolvedor (DX) Simplificada:** O uso de Docker e Docker Compose é um pilar fundamental. O objetivo é que qualquer desenvolvedor, em qualquer sistema operacional, possa clonar o repositório e ter todo o ambiente complexo (frontend, backend, dependências) funcionando com um único comando: `docker-compose up`.
* **Foco na Geração de "Scaffolding":** A aplicação é uma ferramenta de "andaime" (scaffolding). Seu propósito é acelerar drasticamente o início de um projeto, automatizando as tarefas repetitivas de planejamento e configuração inicial.

## 3. A Experiência do Usuário (Interface)

A interação do usuário será o foco principal, projetada para ser intuitiva, clara e guiada.

* **Início da Sessão:** Ao abrir a aplicação, a primeira interação do usuário será fornecer um **Nome para o Projeto** que ele deseja planejar. Este nome será usado para nomear a sessão de chat e o diretório de saída final.

* **Interface Principal:** A tela principal será dividida em três componentes chave:
    1.  **Indicador de Fase:** No topo da tela, um indicador visual (como um "stepper" ou um título grande) mostrará de forma inequívoca em qual das três fases o processo se encontra:
        * `FASE 1: Planejamento do Projeto`
        * `FASE 2: Definição de Issues`
        * `FASE 3: Configuração do Ambiente`
    2.  **Janela de Chat:** O corpo principal da interface será uma janela de chat, onde o diálogo entre o usuário e o assistente de IA acontece.
    3.  **Botão de Ação "Aprovar":** Um único botão de ação, rotulado **"Aprovar"**, estará presente. Este botão ficará **desabilitado** na maior parte do tempo, tornando-se ativo apenas quando o assistente de IA indicar que a fase atual da conversa foi concluída e está pronta para a aprovação do usuário.

* **Fluxo da Conversa Guiada:** O diálogo será fluido, mas estruturado. O assistente de IA, operando com a persona da fase atual, conversará com o usuário para refinar os detalhes. Ao final de cada fase, o assistente dirá explicitamente no chat: *"A fase de [Nome da Fase] está concluída. Quando estiver pronto, por favor, clique em 'Aprovar' para avançarmos."* Isso ativará o botão "Aprovar", dando ao usuário o controle explícito para passar para a próxima etapa.

## 4. A Lógica de Orquestração (Backend)

O backend será o cérebro que gerencia o estado, a lógica e a comunicação com a API do Gemini.

* **Máquina de Estados:** O sistema operará como uma máquina de estados finitos. Cada sessão de chat terá um estado atual (`PLANNING`, `ISSUES`, `DEVOPS`). O clique no botão "Aprovar" acionará uma chamada de API que fará a transição do backend para o próximo estado.

* **Personas Dinâmicas (Prompts):** Cada estado corresponderá a uma "persona" específica da IA, definida por um arquivo `.md` no diretório `prompts`.
    * No estado `PLANNING`, o sistema carregará o prompt do "Maestro de Projetos".
    * Ao transicionar para `ISSUES`, ele descartará a persona anterior e carregará o prompt do "Gerente de Issues", injetando o plano de trabalho já aprovado como contexto inicial.
    * A mesma lógica se aplica para a fase `DEVOPS`.

* **Memória de Conversa:** Dentro de cada fase, o LangChain manterá uma memória da conversa para garantir que o assistente tenha contexto sobre o diálogo daquela etapa específica.

## 5. O Resultado Final (Artefatos Gerados)

O objetivo final da aplicação é produzir um conjunto de arquivos concretos e úteis.

* **Geração dos Arquivos:** Após a aprovação da terceira e última fase, o backend irá:
    1.  Criar um diretório de saída único na pasta `output/`, usando o padrão: `<Nome-do-Projeto-do-Usuario>-<timestamp>`.
    2.  Salvar todos os artefatos definidos durante a conversa dentro deste diretório (ex: `working-plan.md`, `README.md`, `create_issues.sh`, arquivos de configuração como `settings.json`, etc.).

* **O Script de Bootstrap Interativo (`bootstrap.sh`):** Este será o principal artefato executável. Ao ser rodado pelo usuário em seu terminal, ele não irá criar o projeto imediatamente. Em vez disso, ele irá primeiro **perguntar ao usuário** onde ele deseja que a estrutura do projeto seja criada, com um prompt claro:
    > `Por favor, insira o caminho completo onde deseja criar o diretório do projeto (ex: /home/usuario/dev):`
    Após o usuário fornecer o caminho, o script procederá com a criação de toda a estrutura de diretórios e arquivos do novo projeto naquele local específico.

## 6. Escopo, Limites e "Anti-Padrões"

Para garantir a clareza do propósito, é fundamental definir o que o projeto **não é** e o que o agente **não deve fazer**.

#### O que o "Planejador Gemini-Flow" NÃO é:
* **NÃO é um IDE ou editor de código:** A aplicação não é um ambiente para desenvolver, compilar ou depurar código. Sua função é estritamente de planejamento e geração de estrutura.
* **NÃO é uma ferramenta de gestão de projetos (como Jira, Trello, etc.):** A aplicação gera um script para criar issues, mas não acompanha seu status, ciclo de vida ou progresso. Sua responsabilidade termina na configuração inicial.
* **NÃO é um chatbot de propósito geral:** O assistente é um especialista focado e não deve ser usado para conversas que fujam do escopo de planejamento de software.

#### O que o Agente de IA NÃO deve fazer:
* **NÃO deve tomar decisões autônomas:** O agente nunca deve avançar para a próxima fase ou finalizar o processo sem o comando explícito do usuário através do botão "Aprovar". Ele sempre sugere e aguarda a confirmação.
* **NÃO deve gerar código de lógica de negócio:** O agente gera configurações, scripts, documentação e boilerplate. Ele não deve, por exemplo, escrever o código da função de login ou de uma regra de negócio específica.
* **NÃO deve misturar suas personas:** O agente deve operar estritamente dentro da sua persona da fase atual. O "Maestro de Projetos" não deve discutir detalhes de configuração de ambiente, e o "Arquiteto DevOps" não deve redefinir o plano de trabalho.

#### O que o Resultado Final NÃO será:
* **NÃO será uma aplicação compilada ou funcional:** O resultado é o **código-fonte** e os **documentos de planejamento** de uma estrutura de projeto, não um binário executável ou um software pronto para uso.
* **NÃO será um ambiente de produção:** O Docker Compose e os scripts gerados são para criar um **ambiente de desenvolvimento local**. A configuração para produção (deploy, CI/CD, etc.) está fora do escopo deste projeto.

## 7. Possíveis Evoluções Futuras

* **Integração com Git:** Adicionar a funcionalidade para que o script de bootstrap, opcionalmente, inicialize um repositório Git, crie um repositório remoto (via APIs do GitHub/GitLab) e faça o primeiro commit.
* **Persistência de Sessão:** Implementar um banco de dados simples (como SQLite) para salvar as sessões de chat, permitindo que o usuário pause um planejamento e o retome mais tarde.
* **Biblioteca de "Gems":** Expandir o número de personas/prompts disponíveis, talvez permitindo que o usuário escolha quais "Gems" (ex: "Gem de Testes", "Gem de Documentação") quer incluir no seu fluxo de planejamento.

## 8. A Pilha de Tecnologia (Stack)

* **Frontend:** React com TypeScript.
* **Backend:** Python com o framework FastAPI.
* **Orquestração de IA:** Biblioteca LangChain (versão Python).
* **Modelo de Linguagem:** API do Google Gemini.
* **Containerização:** Docker e Docker Compose para garantir um setup de desenvolvimento e execução de um único comando (`docker-compose up`).
