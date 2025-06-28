# Pesquisa sobre React com TypeScript para Frontend

## Documentação Oficial
- React: [https://react.dev/](https://react.dev/)
- TypeScript: [https://www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)
- Create React App (com TypeScript): [https://create-react-app.dev/docs/adding-typescript/](https://create-react-app.dev/docs/adding-typescript/)

## Conceitos Chave para o Projeto "Planejador Gemini-Flow"

### 1. Criação de Componentes Funcionais com TypeScript
- Usar a sintaxe de componentes funcionais.
- Tipar props e estado.
- Exemplo:
  ```tsx
  import React from 'react';

  interface GreetingProps {
    name: string;
  }

  const Greeting: React.FC<GreetingProps> = ({ name }) => {
    return <h1>Hello, {name}!</h1>;
  };

  export default Greeting;
  ```

### 2. Gerenciamento de Estado com Hooks
- **`useState`**: Para gerenciar o estado local do componente (histórico do chat, fase atual, input do usuário).
  ```tsx
  const [message, setMessage] = React.useState<string>("");
  const [chatHistory, setChatHistory] = React.useState<Array<{ sender: string; text: string }>>([]);
  ```
- **`useEffect`**: Para lidar com efeitos colaterais (ex: chamar API quando um estado muda, focar em input).
  ```tsx
  React.useEffect(() => {
    // Chamar API para buscar dados iniciais, por exemplo
  }, []); // Array de dependências vazio executa apenas uma vez
  ```

### 3. Comunicação com APIs (Fetch ou Axios)
- Usar `fetch` (nativo do browser) ou `axios` (biblioteca popular) para fazer chamadas HTTP para o backend FastAPI.
- Tipar os dados esperados da API.
- Exemplo com `fetch`:
  ```tsx
  interface ApiResponse {
    reply: string;
    is_approval_step: boolean;
  }

  async function sendMessage(userMessage: string): Promise<ApiResponse> {
    const response = await fetch('/api/chat', { // '/api' pode ser configurado com proxy no package.json
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userMessage }),
    });
    if (!response.ok) {
      // Lidar com erros da API
      const errorData = await response.json();
      throw new Error(errorData.detail || 'API request failed');
    }
    return response.json() as Promise<ApiResponse>;
  }
  ```

### 4. Tratamento de Erros em Chamadas de API
- Usar `try...catch` para capturar erros de rede ou respostas de erro do backend.
- Exibir mensagens amigáveis para o usuário.
- Exemplo:
  ```tsx
  const [error, setError] = React.useState<string | null>(null);

  const handleSendMessage = async (text: string) => {
    try {
      setError(null);
      const response = await sendMessage(text);
      // Atualizar chatHistory com response.reply
      // Atualizar estado do botão Aprovar com response.is_approval_step
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("An unknown error occurred.");
      }
    }
  };
  ```

### 5. Estilização Básica (CSS Global)
- Criar um arquivo CSS global (ex: `src/index.css` ou `src/App.css`) e importá-lo no componente principal (`App.tsx` ou `index.tsx`).
- Usar classes CSS para estilizar os componentes.
- Foco em layout limpo e legibilidade para a interface de chat.

### 6. Estrutura do Projeto Frontend
- Organizar componentes em um diretório `src/components/`.
- `App.tsx` será o componente principal que orquestra a UI.
- Serviços de API podem ser agrupados em `src/services/api.ts`.
- Tipos e interfaces podem ir para `src/types/` ou definidos junto aos componentes/serviços que os utilizam.

### 7. Componentes Planejados
- **`ProjectNameInput`**: Componente inicial para pedir o nome do projeto.
- **`ChatInterface`**: Componente principal contendo:
    - Indicador de Fase (ex: "Fase 1: Planejamento").
    - Janela de Chat (exibe histórico de mensagens).
    - Input de Mensagem.
    - Botão "Enviar".
    - Botão "Aprovar" (habilitado/desabilitado com base no flag `is_approval_step` do backend).

### 8. Estado Global (Opcional, se necessário)
- Para aplicações mais complexas, considerar `Context API` ou bibliotecas como Redux Toolkit, Zustand.
- Para este projeto, `useState` e passagem de props podem ser suficientes inicialmente, mas se o estado do botão "Aprovar" ou a fase atual precisarem ser acessados por muitos componentes aninhados, `Context API` pode ser uma boa opção.
  ```tsx
  // Exemplo de Context
  interface AppState {
    currentPhase: string;
    isApprovalStep: boolean;
    // ... outros estados
  }
  const AppContext = React.createContext<AppState | undefined>(undefined);
  // ... provedor e consumidor
  ```

## Considerações Adicionais
- **`create-react-app frontend --template typescript`**: Comando para inicializar o projeto.
- **Proxy para API**: Para desenvolvimento, configurar o `proxy` no `package.json` para evitar problemas de CORS ao chamar o backend FastAPI (ex: `"proxy": "http://localhost:8000"` se o backend rodar na porta 8000).
- **Build**: `npm run build` para criar a versão de produção.

Este resumo cobre os pontos principais para iniciar o desenvolvimento do frontend com React e TypeScript, conforme o `working-plan.md`.
