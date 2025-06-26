# gemini-flow 🚀

Bem-vindo ao `gemini-flow`, um processo estruturado para o desenvolvimento de software de alta qualidade utilizando o `gemini-cli`.

## Visão Geral

Este repositório fornece um fluxo de trabalho baseado em prompts para guiar o `gemini-cli` através das fases do ciclo de vida de desenvolvimento de software (SDLC). O objetivo é substituir interações vagas por comandos precisos, resultando em código e planejamento mais seguros, estruturados e fáceis de manter.

## Como Usar

1.  **Configure o Agente:** Configure seu `gemini-cli` para usar o conteúdo do arquivo `GEMINI.md` como seu prompt de sistema ou base. Isso garante que o agente siga as regras de comportamento e raciocínio definidas.
2.  **Siga as Fases:** Navegue pelas fases de desenvolvimento abaixo.
3.  **Copie e Cole:** Copie o template de prompt da fase desejada, preencha os placeholders (ex: `[sua ideia]`) e envie para o `gemini-cli`.
4.  **Fiscalize e Itere:** Revise a saída do Gemini. O bloco `<thinking>` oferece total transparência sobre o processo do agente. Use essa informação para refinar seus prompts ou corrigir o curso.
---

## Prompts para o Ciclo de Desenvolvimento

### Fase 1: Planejamento

O objetivo é transformar uma ideia vaga em um plano de projeto estruturado em YAML, conforme a teoria do Meta-Prompt.

**Prompt 1.1: Geração do Plano Global**

```
PROMPT: Geração de Plano de Software.
DESCRIÇÃO_PROJETO: "[Descreva a ideia central do seu projeto de forma clara e concisa. Ex: Uma plataforma de agendamento de mentorias para desenvolvedores juniores.]"
STACK_TECNOLOGICO_ALVO: "[Liste as linguagens, frameworks e bancos de dados que você pretende usar. Ex: Frontend em Vue.js com TypeScript, Backend em Go com Gin, Banco de Dados PostgreSQL.]"

```
---

### Fase 2: Escolha de Ferramentas

Com o plano em mãos, detalhamos as ferramentas e bibliotecas específicas.

**Prompt 2.1: Detalhamento do Ecossistema de Ferramentas**

```
PROMPT: Detalhamento do Ecossistema de Ferramentas.
PLANO_YAML:
"""
[Cole aqui o YAML gerado na Fase 1]
"""
FOCO_ANALISE: "[Especifique uma área para análise. Ex: 'Com base no plano, recomende as melhores bibliotecas de UI para Vue.js e justifique a escolha para os componentes definidos.' ou 'Compare ORMs para Go adequados para o esquema de banco de dados proposto.']"
```
---

### Fase 3: Roteiro de Desenvolvimento (Tasks)

Quebramos o plano de implementação em um roteiro detalhado, pronto para um sistema de gerenciamento de projetos.

**Prompt 3.1: Geração de Épicos e User Stories**

```
PROMPT: Geração de Roteiro de Desenvolvimento (Épicos e User Stories).
PLANO_YAML:
"""
[Cole aqui o YAML gerado na Fase 1]
"""
METODOLOGIA: "[Especifique a metodologia. Ex: Scrum]"
OUTPUT_FORMAT: "Gere uma lista de Épicos. Para cada Épico, detalhe as User Stories correspondentes no formato 'Como um [usuário], eu quero [objetivo], para que [benefício]'."
```
---

### Fase 4: Pesquisa de Referências

Antes de codificar, buscamos a documentação mais atualizada para garantir as melhores práticas.

**Prompt 4.1: Pesquisa em Documentação**

```
PROMPT: Pesquisa de Referências em Documentação Atualizada.
MCP_SERVER: "context7"
TAREFA_ESPECIFICA: "[Descreva a tarefa que você precisa implementar. Ex: 'Implementar autenticação JWT no backend Go com o framework Gin, seguindo as melhores práticas de segurança de 2025.']"
FOCO_PESQUISA: "Busque tutoriais, exemplos de código e a documentação oficial. Priorize fontes publicadas nos últimos 18 meses. Forneça um resumo e os links."
```
---

### Fase 5: Controle de Tarefas e Codificação

Geramos o código para uma tarefa específica, seguindo o plano.

**Prompt 5.1: Implementação de Tarefa**

```
PROMPT: Implementação de Tarefa Específica.
PLANO_YAML:
"""
[Cole aqui o YAML completo]
"""
ID_TAREFA: "[Cole o ID da tarefa do plano. Ex: TASK-003]"
REFERENCIAS:
"""
[Opcional: cole aqui os resultados da pesquisa da Fase 4]
"""
OUTPUT_FORMAT: "Gere o código completo para esta tarefa, incluindo arquivos, estrutura de pastas e testes unitários. Explique as decisões de implementação."
```
---

### Fase 6: Controle de Versionamento

Mantemos o repositório organizado e seguimos uma estratégia de branching clara.

**Prompt 6.1: Criação de Estratégia de Branch**

```
PROMPT: Controle de Versionamento.
TAREFA_ATUAL: "Implementação da feature: [Nome da feature ou ID da tarefa, ex: Autenticação de Usuário]."
ESTRATEGIA_BRANCHING: "[GitFlow ou GitHub Flow]"
AÇÃO: "Gere os comandos git exatos, desde a criação da branch até a abertura do Pull Request (PR), incluindo um template de descrição para o PR."
```
---

### Fase 7: Atualização de Documentação

O código só está completo quando a documentação está atualizada.

**Prompt 7.1: Geração de Documentação de API**

```
PROMPT: Atualização de Documentação Oficial.
TIPO_DOCUMENTACAO: "[Swagger/OpenAPI, ou Documentação de Componente em Markdown]"
CODIGO_FONTE:
"""
[Cole o código da função, classe ou endpoint da API que você acabou de criar]
"""
AÇÃO: "Gere a documentação correspondente para o código fornecido, seguindo as melhores práticas para o tipo de documentação especificado."

```
---

### Fase 8: Resolução de Bugs e Issues

Abordamos problemas de forma sistemática e organizada.

**Prompt 8.1: Análise e Correção de Bug**

```
PROMPT: Resolução de Bug.
DESCRIÇÃO_BUG: "[Descreva o comportamento inesperado. Inclua logs de erro, se houver. Ex: 'Ao tentar fazer login com uma senha incorreta, a API retorna um erro 500 Internal Server Error ao invés de um 401 Unauthorized.']"
CODIGO_RELEVANTE:
"""
[Cole o trecho de código onde você suspeita que o erro ocorre]
"""
AÇÃO: "Analise o código, identifique a causa raiz do bug, proponha a correção e gere o código corrigido com uma explicação da mudança."
```
