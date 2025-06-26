# Gemini-Flow v2.0 🚀

Bem-vindo ao Gemini-Flow 2.0, um sistema de desenvolvimento orientado a IA que utiliza ferramentas modernas para transformar planos em código.

## Como Usar

1.  **Configure o Agente:** Garanta que seu `gemini-cli` esteja configurado para usar o `gemini-constitution.md` como seu prompt de sistema.
2.  **Siga as Fases:** Use os prompts abaixo para guiar o agente através do ciclo de vida de desenvolvimento.

---

## Guia de Prompts Essenciais

### Fase 1: Planejamento (Humano + Gemini)

**Objetivo:** Colaborar com o Gemini para criar um plano de trabalho detalhado. Este processo é idêntico em espírito ao do `jules-flow`, mas com uma saída mais estruturada.

**Prompt 1.1: Iniciar Planejamento**
*Cole este prompt no `gemini-cli` e anexe o contexto do seu projeto usando MCPs.*

**Exemplo de Comando no Terminal:**

```bash
gemini-cli @git(log:-n 10) @file(package.json,main.go) "PROMPT_PLANEJAMENTO: [descreva aqui o seu objetivo, ex: 'Implementar um sistema de login com autenticação JWT']."
```

**Conteúdo do Prompt (para colar no `gemini-cli` se não usar a linha de comando):**

```
PROMPT_PLANEJAMENTO: [descreva aqui o seu objetivo]

---
INSTRUÇÃO PARA O AGENTE:
Você é um assistente especialista em arquitetura de software, operando sob a constituição `gemini-constitution.md`.

Sua missão é colaborar comigo para criar um plano técnico detalhado.

**Etapa 1: Análise e Discussão Colaborativa**
1.  Analise o contexto que forneci (`@git`, `@file`, etc.).
2.  Inicie uma discussão técnica: sugira as melhores práticas, bibliotecas, arquivos a serem modificados e estratégia de testes. Faça perguntas para refinar a abordagem.

**Etapa 2: Geração do Plano Formal**
1.  Aguarde meu comando explícito: `FINALIZE O PLANO`.
2.  Ao recebê-lo, gere um plano de trabalho em formato **YAML**. O plano deve conter:
    - `geral_objective`: Um resumo claro.
    - `tasks`: Uma lista de tarefas, onde cada tarefa tem `title`, `description` (com critérios de aceitação), e `dependencies` (lista de IDs de outras tarefas).
```

**Exemplo de Saída YAML Esperada:**
```yaml
geral_objective: "Implementar autenticação JWT para a API."
tasks:
  - id: "TASK-001"
    title: "Adicionar bibliotecas de JWT e hash de senha"
    description: "Adicionar as dependências 'golang-jwt/jwt' e 'golang.org/x/crypto/bcrypt' ao go.mod."
    dependencies: []
  - id: "TASK-002"
    title: "Criar endpoint de registro (/register)"
    description: "Criar um endpoint POST que recebe email/senha, faz o hash da senha e salva o novo usuário."
    dependencies: ["TASK-001"]
  - id: "TASK-003"
    title: "Criar endpoint de login (/login)"
    description: "Criar um endpoint POST que valida as credenciais e retorna um token JWT."
    dependencies: ["TASK-002"]
```

### Fase 2: Execução (Gemini Autônomo)

**Objetivo:** Instruir o Gemini a executar o plano YAML gerado, utilizando todo o seu ferramental.

**Prompt 2.1: Executar Plano de Trabalho**
*Este prompt aciona o fluxo de trabalho completo: criação de branch, issues, código, testes e PR.*

```
PROMPT_EXECUCAO: Execute o plano de trabalho.

PLANO_YAML:
"""
[Cole aqui o YAML completo gerado na Fase 1]
"""
---

INSTRUÇÃO PARA O AGENTE:
Siga rigorosamente sua constituição (`GEMINI.md`) e o plano fornecido.

**Sua sequência de ações:**

1.  Crie um branch Git apropriado para este trabalho (ex: `feature/jwt-auth-YYYYMMDD`).
2.  Para cada item na seção `tasks` do YAML, crie uma GitHub Issue correspondente usando `gh issue create`. O corpo da issue deve conter a descrição e os critérios de aceitação.
3.  Execute o ciclo de desenvolvimento para cada issue, uma por uma, respeitando as dependências:
    a. Obtenha contexto com `@file` e `@web` conforme necessário.
    b. Escreva o código e os testes.
    c. Rode os testes para validar.
    d. Faça o commit das alterações com uma mensagem que feche a issue (ex: `feat: Implementa endpoint de login (closes #123)`).
4.  Após todas as issues serem fechadas, crie um Pull Request (`gh pr create`) com um resumo de todo o trabalho realizado.
5.  Aguarde a revisão humana.

```

### Fase 3: Correção e Iteração (Humano + Gemini)

**Objetivo:** Aplicar o feedback de uma revisão de código.

**Prompt 3.1: Aplicar Feedback do Pull Request**

```bash
gemini-cli @git(diff) @web(URL_DO_PR) "PROMPT_CORRECAO: Aplique o feedback do PR. As discussões e solicitações de mudança estão na URL fornecida. Analise o `diff` atual e o feedback para gerar o código corrigido."
```
