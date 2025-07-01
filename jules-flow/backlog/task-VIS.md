---
id: task-VIS
title: "Gerar/Atualizar VISION.md com base no working-plan.md e análise do código existente"
type: documentation # Ou vision_generation
status: backlog
priority: high
dependencies: []
parent_plan_objective_id: "Fase2.2" # Referência ao passo do plano mestre
discovered_research_needed: []
assigned_to: Jules
created_by: Jules
created_at: 2024-07-31T12:05:00Z # Placeholder
updated_at: 2024-07-31T12:05:00Z # Placeholder
tags: ["documentation", "vision", "planning", "architecture"]
description: |
  Analisar o `jules-flow/working-plan.md` atual e, se aplicável, o código existente no repositório (especialmente se for uma atualização e não um projeto do zero). Com base nisso, gerar ou atualizar o arquivo `VISION.md` na raiz do projeto. Este arquivo deve detalhar:
  *   O objetivo geral do projeto (conforme `jules-flow/working-plan.md`).
  *   A arquitetura principal pretendida ou existente.
  *   Uma descrição das principais funcionalidades ou módulos que serão desenvolvidos/afetados, conforme inferido do `jules-flow/working-plan.md`.
  *   Quaisquer princípios de design ou tecnologias chave mencionadas ou implícitas no `jules-flow/working-plan.md`.
  *   Os principais fluxos de interação ou dados esperados.
  O `VISION.md` servirá como um documento de referência de alto nível para guiar o desenvolvimento subsequente.

# Não modificar esta seção manualmente. Jules irá preenchê-la.
# ---------------------------------------------------------------
# RELATÓRIO DE EXECUÇÃO (Preenchido por Jules ao concluir/falhar)
# ---------------------------------------------------------------
# outcome: success | failure
# outcome_reason: ""
# start_time: YYYY-MM-DDTHH:MM:SSZ
# end_time: YYYY-MM-DDTHH:MM:SSZ
# duration_minutes: 0
# files_modified:
#   - VISION.md
# reference_documents_consulted:
#   - jules-flow/working-plan.md
#   - (Potencialmente outros arquivos de código fonte se fosse uma atualização)
# execution_details: |
#   Conteúdo do VISION.md gerado/atualizado com base na análise.
# ---------------------------------------------------------------
---

## Arquivos Relevantes (Escopo da Tarefa)
* `jules-flow/working-plan.md` (para leitura)
* `VISION.md` (para criação/atualização na raiz do projeto)
* Potenciais diretórios de código fonte para análise contextual (ex: `src/`, `app/`, `backend/`, `frontend/` - neste caso, o working-plan indica remoção de backend/ e frontend/, então o foco é no novo `app/`)

## Critérios de Aceitação
1.  Um arquivo `VISION.md` é criado/atualizado na raiz do projeto.
2.  O `VISION.md` contém seções detalhando:
    *   Objetivo Geral do Projeto.
    *   Arquitetura Principal (Nova: NiceGUI monolítico com LangChain).
    *   Principais Funcionalidades/Módulos (conforme `working-plan.md`: UI wizard, orquestrador LangChain, geração de arquivos de projeto).
    *   Princípios de Design/Tecnologias Chave (NiceGUI, LangChain, Python monolítico).
    *   Principais Fluxos de Interação/Dados (Usuário -> Wizard UI -> Coleta de Dados -> Orquestrador LangChain -> Geração de Arquivos -> Feedback ao Usuário).

## Observações Adicionais
O `working-plan.md` detalha uma migração significativa de uma arquitetura FastAPI + React para uma aplicação monolítica NiceGUI + LangChain. O `VISION.md` deve refletir claramente esta nova direção.
---
