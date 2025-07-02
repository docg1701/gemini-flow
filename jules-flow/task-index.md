# Índice de Tarefas Jules-Flow

| ID da Tarefa | Título | Tipo | Status | Prioridade | Dependências | Atribuído |
|--------------|--------|------|--------|------------|--------------|-----------|
| task-R01     | Pesquisa sobre Estrutura e Boas Práticas em NiceGUI | research | done        | high       | []           | Jules     |
| task-R02     | Pesquisa sobre Uso de LangChain para Geração de Código e Conteúdo Estruturado | research | done        | high       | []           | Jules     |
| task-R03     | Pesquisa sobre Integração NiceGUI e LangChain | research | done        | medium     | ["task-R01", "task-R02"] | Jules     |
| task-R04     | Pesquisa sobre Estrutura de Projeto Python Monolítico com NiceGUI | research | done        | medium     | ["task-R01"] | Jules     |
| task-VIS     | Gerar/Atualizar VISION.md com base no working-plan.md e análise do código existente | documentation | done        | high       | []           | Jules     |
| task-P1-DEV-01 | WP1: Criar estrutura app/ e remover /frontend, /backend | development | done        | high       | []           | Jules     |
| task-P1-DEV-02 | WP1: Atualizar requirements.txt para NiceGUI e LangChain | development | done        | high       | ["task-P1-DEV-01"] | Jules     |
| task-P1-DEV-03 | WP1: Criar app/main.py básico para NiceGUI | development | done        | high       | ["task-P1-DEV-01"] | Jules     |
| task-P1-TEST-01 | WP1: Teste da estrutura básica e execução mínima de app/main.py | test | done        | medium     | ["task-P1-DEV-01", "task-P1-DEV-02", "task-P1-DEV-03"] | Jules     |
| task-P2-DEV-01 | WP2: Criar app/services/orchestrator.py com função básica LangChain/Gemini | development | done        | high       | ["task-P1-DEV-03"] | Jules     |
| task-P2-DEV-02 | WP2: Adicionar botão em app/main.py para chamar orquestrador e exibir resultado | development | done        | high       | ["task-P1-DEV-03", "task-P2-DEV-01"] | Jules     |
| task-P2-TEST-01 | WP2: Teste da integração NiceGUI-LangChain (PoC) | test | in_progress | medium     | ["task-P2-DEV-01", "task-P2-DEV-02"] | Jules     |
| task-P3-DEV-01 | WP3: Implementar estrutura do wizard com ui.stepper em NiceGUI | development | backlog    | high       | ["task-P1-DEV-03"] | Jules     |
| task-P3-DEV-02 | WP3: Criar módulos de UI para cada passo do wizard e coletar dados | development | backlog    | high       | ["task-P3-DEV-01"] | Jules     |
| task-P3-TEST-01 | WP3: Testes para a UI do wizard (navegação, coleta de dados) | test | backlog    | medium     | ["task-P3-DEV-01", "task-P3-DEV-02"] | Jules     |
| task-P4-DEV-01 | WP4: Implementar chain LangChain em orchestrator.py para gerar Dockerfile | development | backlog    | high       | ["task-P2-DEV-01"] | Jules     |
| task-P4-DEV-02 | WP4: Implementar chain LangChain para gerar .gitignore | development | backlog    | medium     | ["task-P2-DEV-01"] | Jules     |
| task-P4-DEV-03 | WP4: Implementar chain LangChain para gerar novo requirements.txt | development | backlog    | medium     | ["task-P1-DEV-02", "task-P2-DEV-01"] | Jules     |
| task-P4-DEV-04 | WP4: Implementar chain LangChain para gerar GEMINI.md | development | backlog    | high       | ["task-P2-DEV-01"] | Jules     |
| task-P4-TEST-01 | WP4: Testes unitários para as chains de geração de arquivos no orquestrador | test | backlog    | medium     | ["task-P4-DEV-01", "task-P4-DEV-02", "task-P4-DEV-03", "task-P4-DEV-04"] | Jules     |
| task-P5-DEV-01 | WP5: Implementar criação de diretório de saída e salvamento de arquivos | development | backlog    | high       | ["task-P4-DEV-01", "task-P4-DEV-02", "task-P4-DEV-03", "task-P4-DEV-04"] | Jules     |
| task-P5-DEV-02 | WP5: Adicionar tela final no wizard NiceGUI com mensagem de sucesso e caminho | development | backlog    | medium     | ["task-P3-DEV-01", "task-P5-DEV-01"] | Jules     |
| task-P5-TEST-01 | WP5: Teste de integração do fluxo completo de geração e saída | test | backlog    | medium     | ["task-P3-TEST-01", "task-P4-TEST-01", "task-P5-DEV-01", "task-P5-DEV-02"] | Jules     |
| task-P6-DOC-01 | WP6: Atualizar README.md principal com nova arquitetura e instruções | documentation | backlog    | medium     | ["task-P5-DEV-02"] | Jules     |
| task-P6-DOC-02 | WP6: Remover documentação antiga (FastAPI/React) | documentation | backlog    | low        | ["task-P6-DOC-01"] | Jules     |
