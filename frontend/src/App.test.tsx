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
      mockApi.startSession.mockClear(); // Clear for this specific test, as it's self-contained.

      // It's better to mockClear before each test or in a beforeEach if the mock is shared.
      // For this isolated test, clearing it here is fine.
      mockApi.startSession.mockClear();

      mockApi.startSession.mockClear();

      render(<App />);
      const projectNameInput = screen.getByLabelText(/Project Name:/i);
      const startSessionButton = screen.getByRole('button', { name: /Start Session/i });

      // Envolver a interação e a espera pela atualização de estado em act()
      await act(async () => {
        await userEvent.type(projectNameInput, testProjectName);
        await userEvent.click(startSessionButton);
        // Dê uma chance para a promise do mock resolver e as atualizações de estado iniciais ocorrerem
        // Esta é uma pequena pausa para ajudar o scheduler do Jest/RTL
        await new Promise(resolve => setTimeout(resolve, 0));
      });

      // Verificar se o mock foi chamado
      expect(mockApi.startSession).toHaveBeenCalledWith({ project_name: testProjectName });
      expect(mockApi.startSession).toHaveBeenCalledTimes(1);

      // Esperar que o ProjectNameInput desapareça
      await waitFor(() => {
        expect(screen.queryByRole('heading', { name: /Start a New Project/i, level: 2 })).not.toBeInTheDocument();
      });
      // Confirmar outros elementos do ProjectNameInput também sumiram
      expect(screen.queryByLabelText(/Project Name:/i)).not.toBeInTheDocument();
      expect(screen.queryByRole('button', { name: /Start Session/i })).not.toBeInTheDocument();

      // Agora, verificar se o ChatInterfacePlaceholder apareceu
      const heading = await screen.findByRole('heading', { name: `Chat Interface for: ${testProjectName}`, level: 2 });
      expect(heading).toBeInTheDocument();

      expect(screen.getByText(`Current State: PLANNING`)).toBeInTheDocument();
      expect(screen.getByText(/Initial AI Message: Mensagem recebida: 'Olá! Vamos começar o planejamento do projeto.'/i)).toBeInTheDocument();
      expect(screen.getByText(/\(Full chat UI will be implemented in task-016\)/i)).toBeInTheDocument();
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
