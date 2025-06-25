# Instruções Operacionais para Gemini (GEMINI.md)

Este documento detalha o fluxo de trabalho completo que você, Gemini, deve seguir. Sua aderência estrita a estas fases e princípios é crucial para a organização e o sucesso do projeto `gemini-flow`.

---

### Princípios Fundamentais

1.  **Comunicação via Commits**: Cada passo significativo que você toma deve ser registrado através de um commit atômico e bem descrito.
2.  **Gestão de Estado por Arquivos**: O estado do projeto é definido pela localização dos arquivos de tarefa (`task-XXX.md`) nos diretórios `/tasks/backlog/`, `/tasks/in_progress/`, `/tasks/done/` e `/tasks/failed/`.
3.  **Índice Central como Fonte da Verdade**: O arquivo `tasks/index.md` é a única fonte da verdade para o status e o histórico de todas as tarefas. Ele **deve ser atualizado** a cada mudança de estado de uma tarefa.
4.  **Escopo Estrito de Modificação**: Você está estritamente proibido de alterar, mover ou excluir qualquer arquivo que não esteja explicitamente listado na seção "Arquivos Relevantes" da `task` ativa.
5.  **Imutabilidade do Status no Arquivo da Tarefa**: O cabeçalho `status:` dentro do arquivo `.md` de uma tarefa é definido apenas no momento de sua criação e **não deve ser alterado manualmente por você**.

---

### O Fluxo de Trabalho em 6 Fases

#### Fase 1: Descoberta e Pesquisa

* **Objetivo**: Limpar o ambiente de trabalho, identificar o escopo de pesquisa e buscar o conhecimento necessário utilizando as ferramentas do `gemini-cli`.
* **Ação**:
    1.  **Limpeza do Ambiente**: Exclua todos os arquivos dos diretórios de tarefas (`/tasks/backlog/`, `/tasks/in_progress/`, etc.) e do diretório de referência (`/docs/reference/`).
    2.  **Limpeza do Índice**: No arquivo `tasks/index.md`, preserve apenas o cabeçalho da tabela.
    3.  **Commit de Preparação**: Execute um commit com a mensagem "Setup: Limpeza do ambiente de trabalho para novo branch.".
    4.  **Análise do Plano**: Leia o `working-plan.md` para identificar as áreas que exigem pesquisa.
    5.  **Criação das Tarefas de Pesquisa**: Crie `task`s do tipo `research` para cada tópico.
    6.  **Execução da Pesquisa com `gemini-cli`**: Para cada `task` de pesquisa, execute buscas na web e colete documentação oficial. Utilize o comando `gemini query --tool search "seu tópico de pesquisa"` para obter informações. Compile os resultados em arquivos de referência dentro de `/docs/reference/`.

#### Fase 2: Preparação e Decomposição do Plano

* **Objetivo**: Converter o `working-plan.md` em tarefas executáveis e prontas para o `gemini-cli`.
* **Ação**:
    1.  Leia o `working-plan.md` para entender o escopo completo.
    2.  Decomponha o plano em uma série de `task`s atômicas (`development`, `test`, `documentation`).
    3.  Preencha o cabeçalho YAML de cada `task` e salve-as em `/tasks/backlog/`.
    4.  Popule o `tasks/index.md` com as informações de todas as tarefas criadas, com o status inicial "backlog".
    5.  Ao final, anuncie que o setup foi concluído e informe qual será a primeira `task` a ser executada.

#### Fase 3: Execução Inteligente e Dinâmica de Tarefas

* **Objetivo**: Executar as tarefas de forma ordenada, segura e potencializada pelo `gemini-cli`.
* **Ação**: Siga o ciclo de execução para cada tarefa.
* **Ciclo de Execução da Tarefa**:
    1.  **Mover para "Em Progresso"**: Mova o arquivo da tarefa para `/tasks/in_progress/` e atualize seu status no `tasks/index.md`. Realize um commit.
    2.  **Consulta de Conhecimento**: Verifique o diretório `/docs/reference/`. Se a documentação for insuficiente, utilize `gemini query --tool search "dúvida específica"` para buscar conhecimento adicional em tempo real.
    3.  **Executar com `gemini-cli`**: Realize as alterações de código, testes ou documentação. Utilize os comandos do `gemini-cli` para interagir com arquivos, por exemplo: `gemini query "leia o conteúdo de 'arquivo.py' e aplique tal modificação" --tool file_reader --tool file_writer`.
    4.  **Relatar**: Preencha a seção "Relatório de Execução" na `task`, listando os documentos de referência consultados e os comandos `gemini-cli` utilizados.
    5.  **Verificar Sucesso**: Execute testes ou validações para confirmar a conclusão da tarefa.
    6.  **Em caso de Sucesso**:
        1.  Mova a `task` para `/tasks/done/` e atualize o `tasks/index.md`.
        2.  Se a tarefa for de `development`, gere automaticamente uma nova `task` de `test` no `/tasks/backlog/` e atualize o índice.
    7.  **Em caso de Falha**: Mova a `task` para `/tasks/failed/`, atualize o `tasks/index.md` e preencha o relatório com os logs de erro. Anuncie a falha e pare o trabalho.
    8.  **Commit Atômico Final**: Realize o commit referente à conclusão (sucesso ou falha) da `task`.

#### Fase 4: Geração de Relatório e Finalização

* **Objetivo**: Consolidar o trabalho e limpar o ambiente.
* **Ação**:
    1.  Verifique se os diretórios `/tasks/backlog/`, `/tasks/in_progress/` e `/tasks/failed/` estão vazios.
    2.  Compile um relatório final a partir das seções "Relatório de Execução" de todas as tarefas em `/tasks/done/`.
    3.  Salve o relatório em `/final-reports/`.
    4.  Limpe os diretórios de estado e o conteúdo do `tasks/index.md` (preservando o cabeçalho).

#### Fase 5: Atualização da Documentação do Projeto

* **Objetivo**: Manter a documentação do projeto sincronizada com as mudanças.
* **Ação**:
    1.  Com base no relatório final, identifique os impactos na documentação.
    2.  Crie uma `task` do tipo `documentation`.
    3.  Execute a tarefa, utilizando `gemini query "resuma as mudanças e atualize a seção X do README.md"` para auxiliar na geração do conteúdo.

#### Fase 6: Verificação de Inconsistências e Refatoração

* **Objetivo**: Garantir a qualidade e a consistência do código antes do merge.
* **Ação**:
    1.  Execute uma análise completa do código modificado. Você pode usar o `gemini-cli` para isso: `gemini query "analise o código no arquivo 'X' e sugira refatorações"`
    2.  Verifique se há inconsistências, duplicação de código ou oportunidades de refatoração.
    3.  Crie e execute `task`s de `refactor` ou `fix` se necessário.
