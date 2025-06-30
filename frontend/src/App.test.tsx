import React from 'react';
import { render, screen, waitFor, act } from '@testing-library/react'; // Import act
import userEvent from '@testing-library/user-event';
import App from './App';
import { ApiStartResponse } from './services/api'; // Import the type

// Mock the api service
// The actual orchestrator.process_user_message for "Olá! Vamos começar o planejamento do projeto."
// will result in a specific simulated message.
// Let's use that expected structure for the mock.
const mockProjectName = "Meu Projeto de Teste"; // Consistent with test usage
const mockInitialMessageFromOrchestrator = `Mensagem recebida: 'Olá! Vamos começar o planejamento do projeto.'. Estado atual: PLANNING. Prompt ativo: gemini-gem-arquiteto-de-projetos.md. Histórico contém 1 mensagens. (Resposta simulada)`;

jest.mock('./services/api', () => ({
  // __esModule: true, // Not strictly needed for jest.mock if default export isn't used by component
  startSession: jest.fn(async (payload: { project_name: string }): Promise<ApiStartResponse> => {
    // Simulate the structure of ApiStartResponse from backend/main.py
    // The 'message' field in ApiStartResponse from the /start endpoint
    // is derived from orchestrator.process_user_message("Olá! Vamos começar o planejamento do projeto.")
    return Promise.resolve({
      status: "session_started",
      project_name: payload.project_name,
      current_state: "PLANNING", // Default initial state
      message: mockInitialMessageFromOrchestrator
    });
  })
}));


describe('App Component Rendering', () => {
  test('renders the main application title "Planejador Gemini-Flow"', () => {
    render(<App />);
    const titleElement = screen.getByRole('heading', { name: /Planejador Gemini-Flow/i, level: 1 });
    expect(titleElement).toBeInTheDocument();
  });

  describe('Before session starts', () => {
    beforeEach(() => {
      render(<App />);
    });

    test('renders ProjectNameInput component initially', () => {
      expect(screen.getByRole('heading', { name: /Start a New Project/i, level: 2 })).toBeInTheDocument();
      expect(screen.getByLabelText(/Project Name:/i)).toBeInTheDocument();
      expect(screen.getByRole('button', { name: /Start Session/i })).toBeInTheDocument();
    });

    test('does not render chat interface placeholder initially', () => {
      expect(screen.queryByText(/Chat Interface for:/i)).not.toBeInTheDocument();
    });
  });

  describe('After session starts', () => {
    const testProjectName = "Meu Projeto de Teste";

    // Removed beforeEach for this block to consolidate into a single test case for clarity.

    test('renders ChatInterfacePlaceholder and hides ProjectNameInput after starting a session', async () => {
      const mockApi = require('./services/api');
      // Garanta que o mock está limpo e configurado para este teste
      mockApi.startSession.mockResolvedValueOnce({
        status: "session_started",
        project_name: testProjectName,
        current_state: "PLANNING",
        message: mockInitialMessageFromOrchestrator
      });

      render(<App />);
      const projectNameInput = screen.getByLabelText(/Project Name:/i);
      const startSessionButton = screen.getByRole('button', { name: /Start Session/i });

      await userEvent.type(projectNameInput, testProjectName);

      // Envolver o clique e a espera pelas atualizações de estado em act()
      // Desta vez, vamos garantir que a promise do mock seja explicitamente aguardada DENTRO do act
      // e que o RTL possa processar as atualizações.
      await act(async () => {
        await userEvent.click(startSessionButton);
        // Essencial: esperar que a promise do mock startSession resolva.
        // Isso garante que onSessionStart (e, portanto, setSessionData) seja chamado.
        // Verifique se mock.results existe e tem o valor esperado
        if (mockApi.startSession.mock.results && mockApi.startSession.mock.results.length > 0 && mockApi.startSession.mock.results[0].type === 'return') {
            await mockApi.startSession.mock.results[0].value;
        } else {
            // Se a promise não estiver lá como esperado, podemos lançar um erro ou lidar com isso
            // console.error("Mock promise not found or not resolved as expected");
            // Para o teste, podemos apenas deixar que as asserções subsequentes falhem se a UI não atualizar.
        }
      });

      // Após o act, as atualizações de estado síncronas (setSessionData) devem ter ocorrido.
      // Agora, verificamos o resultado.

      // Esperar que o ProjectNameInput desapareça
      await waitFor(() => {
        expect(screen.queryByRole('heading', { name: /Start a New Project/i, level: 2 })).not.toBeInTheDocument();
      });
      expect(screen.queryByLabelText(/Project Name:/i)).not.toBeInTheDocument();
      expect(screen.queryByRole('button', { name: /Start Session/i })).not.toBeInTheDocument();

      // Verificar se o ChatInterfacePlaceholder apareceu
      // findBy* já usa waitFor, então está bom para elementos que aparecem.
      const heading = await screen.findByRole('heading', { name: `Chat Interface for: ${testProjectName}`, level: 2 });
      expect(heading).toBeInTheDocument();
      expect(screen.getByText(`Current State: PLANNING`)).toBeInTheDocument();
      expect(screen.getByText(/Initial AI Message: Mensagem recebida: 'Olá! Vamos começar o planejamento do projeto.'/i)).toBeInTheDocument();
      expect(screen.getByText(/\(Full chat UI will be implemented in task-016\)/i)).toBeInTheDocument();

      expect(mockApi.startSession).toHaveBeenCalledTimes(1); // A chamada já ocorreu dentro do userEvent.click
    });

    // The old tests for specific components are no longer applicable
    // as ChatInterfacePlaceholder is shown instead.
    // These can be reinstated/adapted when task-016 is done.

    // test('renders PhaseIndicator component with default phase text', () => {
    //   const phaseText = screen.getByText(/Fase Atual: PLANNING/i); // Assuming PLANNING is default
    //   expect(phaseText).toBeInTheDocument();
    // });

    // test('renders ChatWindow component with initial message', () => {
    //   expect(screen.getByText(/Bem-vindo ao Planejador Gemini-Flow! Projeto: Meu Projeto de Teste/i)).toBeInTheDocument();
    // });

    // test('renders MessageInputBar component', () => {
    //   expect(screen.getByPlaceholderText(/Digite sua mensagem.../i)).toBeInTheDocument();
    //   expect(screen.getByRole('button', { name: /Enviar/i })).toBeInTheDocument();
    // });

    // test('renders ApproveButtonArea component', () => {
    //   expect(screen.getByRole('button', { name: /Aprovar Fase/i })).toBeInTheDocument();
    //   expect(screen.getByText(/Aguardando conclusão da IA para aprovar./i)).toBeInTheDocument();
    // });
  });
});
