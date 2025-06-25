# Sistema Gemini-Flow

## Propósito do Sistema

Gemini-Flow é um sistema de gerenciamento de microtarefas projetado para ser operado pelo agente de IA, Gemini, sob a supervisão de um Desenvolvedor humano. O sistema é inteiramente baseado em arquivos Markdown e visa estruturar, rastrear e executar o trabalho de desenvolvimento de forma transparente, documentada e com alta qualidade, utilizando o poder do `gemini-cli` para a execução das tarefas.

## Integração e Gerenciamento com Git

A integração do Gemini-Flow ao seu projeto deve ser feita utilizando **Git Submodules**.

### 1. Adicionando o Gemini-Flow ao seu Projeto

```bash
# Adicione o submódulo
git submodule add [https://github.com/SEU_USUARIO/gemini-flow.git](https://github.com/SEU_USUARIO/gemini-flow.git) gemini-flow

# Comite a integração
git add gemini-flow .gitmodules
git commit -m "feat: Integra o sistema Gemini-Flow como submódulo"
```

### 2. Clonando um Projeto que já usa o Gemini-Flow
```bash
# Opção A: Clonar o repositório e o submódulo de uma só vez
git clone --recurse-submodules [https://github.com/SEU_USUARIO/SEU_PROJETO.git](https://github.com/SEU_USUARIO/SEU_PROJETO.git)

# Opção B: Se você já clonou o projeto sem o submódulo
git submodule init
git submodule update
```

### 3. Atualizando o Gemini-Flow
```bash
cd gemini-flow
git pull origin main
cd ..
git add gemini-flow
git commit -m "chore: Atualiza o submódulo Gemini-Flow para a versão mais recente"
```

## O Fluxo de Trabalho Orientado a Tarefas

O trabalho com o Gemini é organizado em um ciclo de vida que ocorre em seu próprio branch. O processo é guiado por um plano mestre (`working-plan.md`) e executado através de tarefas atômicas gerenciadas pelo agente.

### Fase 1: Planejamento (Humano + IA)

O desenvolvedor, atuando como arquiteto, colabora com a IA para analisar o código e discutir a implementação. Esta fase culmina na geração de um arquivo `working-plan.md`, que contém o roteiro detalhado para o agente Gemini.

### Fase 2: Execução (Agente Gemini)

Em um novo branch, o agente Gemini é acionado. Ele lê o `working-plan.md`, prepara o ambiente e decompõe o plano em `task`s atômicas no diretório `/tasks/backlog/`. A partir daí, ele executa as tarefas seguindo a lógica definida no `GEMINI.md`, utilizando o `gemini-cli` para interagir com o sistema de arquivos, realizar pesquisas e gerar código.

### Fase 3: Finalização e Relatório (Agente Gemini)

Após todas as `task`s serem concluídas, Gemini consolida os relatórios de execução em um único relatório final, arquivado em `/final-reports/`, e limpa o ambiente de trabalho, deixando o branch pronto para a revisão.

## Guia de Prompts Essenciais

Este guia contém os prompts necessários para interagir com o Gemini durante o ciclo de vida de desenvolvimento.

**Prompt 1: Início dos Trabalhos no Branch**
```markdown
Olá, Gemini. Estamos iniciando o trabalho em um novo branch. Sua missão é preparar o ambiente e iniciar o ciclo de trabalho.

Execute as **Fases 1 e 2** do arquivo `GEMINI.md` sequencialmente para colocar o projeto em estado de pronto para a execução das tarefas.
```

**Prompt 2: Continuar Trabalho**
```markdown
Olá, Gemini. É hora de retomar seu trabalho.

Execute a **Fase 3** do arquivo `GEMINI.md` para processar a próxima tarefa disponível no backlog.
```

**Prompt 3: Finalizar e Limpar o Branch**
```markdown
Olá, Gemini. O trabalho de desenvolvimento neste branch foi concluído.

Execute a **Fase 4** do arquivo `GEMINI.md` para gerar o relatório final e limpar o ambiente de trabalho.
```

**Prompt 4: Atualizar a Documentação**
```markdown

Olá, Gemini. Com base no trabalho concluído, sua missão agora é atualizar a documentação do projeto.

Execute a **Fase 5** do arquivo `GEMINI.md`.
```

**Prompt 5: Revisar o Trabalho do Branch**
```markdown
Olá, Gemini. O desenvolvimento principal neste branch foi concluído.

Execute a **Fase 6** do arquivo `GEMINI.md` para realizar uma revisão de qualidade no código produzido e identificar possíveis melhorias.
```
## Estrutura de Diretórios

* `/gemini-flow/`: Diretório raiz do sistema.
    * `/docs/`: Contém documentação gerada pelo Gemini-Flow.
        * `/reference/`: Arquivos de referência criados durante a fase de pesquisa.
    * `/tasks/`: Contém todos os artefatos de tarefas.
        * `/backlog/`: Tarefas pendentes.
        * `/in_progress/`: Tarefa em execução.
        * `/done/`: Tarefas concluídas.
        * `/failed/`: Tarefas com falha.
        * `/archive/`: Arquivo de tarefas antigas (opcional).
        * `/templates/`: Contém o `task_template.md`.
        * `index.md`: Índice e status de todas as tarefas.
    * `GEMINI.md`: Instruções operacionais para o agente Gemini.
    * `README.md`: Este arquivo.
    * `working-plan.md`: O plano de trabalho mestre para o branch atual.

## Licença

Este projeto está licenciado sob os termos da Licença MIT.
