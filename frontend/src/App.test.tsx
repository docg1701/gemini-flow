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

      render(<App />);
      const projectNameInput = screen.getByLabelText(/Project Name:/i);
      const startSessionButton = screen.getByRole('button', { name: /Start Session/i });

      // Wrap the sequence of user interaction and the resulting async updates in act
      await act(async () => {
        await userEvent.type(projectNameInput, testProjectName);
        await userEvent.click(startSessionButton);
        // Wait for the mocked startSession promise to resolve,
        // ensuring subsequent state updates within its chain are processed before act finishes.
        if (mockApi.startSession.mock.results[0]) { // Ensure the function was called
          await mockApi.startSession.mock.results[0].value;
        }
      });

      // Now, after act has completed, the state should be updated.
      // Assertions can be made. Using findBy* for elements that appear asynchronously,
      // and queryBy* for elements that should be gone.

      expect(mockApi.startSession).toHaveBeenCalledWith({ project_name: testProjectName });
      expect(mockApi.startSession).toHaveBeenCalledTimes(1);

      // Check that ProjectNameInput is hidden
      expect(screen.queryByRole('heading', { name: /Start a New Project/i, level: 2 })).not.toBeInTheDocument();
      expect(screen.queryByLabelText(/Project Name:/i)).not.toBeInTheDocument();
      expect(screen.queryByRole('button', { name: /Start Session/i })).not.toBeInTheDocument();

      // Check that ChatInterfacePlaceholder is visible with correct data
      const heading = await screen.findByRole('heading', { name: `Chat Interface for: ${testProjectName}`, level: 2 });
      expect(heading).toBeInTheDocument();

      expect(await screen.findByText(`Current State: PLANNING`)).toBeInTheDocument();
      expect(await screen.findByText(/Initial AI Message: Mensagem recebida: 'Olá! Vamos começar o planejamento do projeto.'/i)).toBeInTheDocument();
      expect(await screen.findByText(/\(Full chat UI will be implemented in task-016\)/i)).toBeInTheDocument();
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
