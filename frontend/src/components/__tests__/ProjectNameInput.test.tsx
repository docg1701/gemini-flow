import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import ProjectNameInput from '../ProjectNameInput'; // Adjust path as necessary
import { startSession, ApiStartResponse } from '../../services/api'; // Adjust path

// Mock the api service
jest.mock('../../services/api', () => ({
  startSession: jest.fn(),
}));

// Typed mock
const mockedStartSession = startSession as jest.MockedFunction<typeof startSession>;

describe('ProjectNameInput Component', () => {
  const mockOnSessionStart = jest.fn();

  beforeEach(() => {
    mockedStartSession.mockClear();
    mockOnSessionStart.mockClear();
  });

  test('renders initially with input, label, and button', () => {
    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    expect(screen.getByRole('heading', { name: /Start a New Project/i, level: 2 })).toBeInTheDocument();
    expect(screen.getByLabelText(/Project Name:/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Start Session/i })).toBeInTheDocument();
  });

  test('allows typing in the project name input', async () => {
    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    const input = screen.getByLabelText(/Project Name:/i) as HTMLInputElement;
    await userEvent.type(input, 'My Test Project');
    expect(input.value).toBe('My Test Project');
  });

  test('shows error if project name is empty on submit', async () => {
    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    const button = screen.getByRole('button', { name: /Start Session/i });
    await userEvent.click(button);

    expect(await screen.findByText('Error: Project name cannot be empty.')).toBeInTheDocument();
    expect(mockedStartSession).not.toHaveBeenCalled();
    expect(mockOnSessionStart).not.toHaveBeenCalled();
  });

  test('calls startSession and onSessionStart on successful submission', async () => {
    const mockResponse: ApiStartResponse = {
      status: 'session_started',
      project_name: 'My Test Project',
      current_state: 'PLANNING',
      message: 'Session started successfully',
    };
    mockedStartSession.mockResolvedValueOnce(mockResponse);

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    const input = screen.getByLabelText(/Project Name:/i);
    const button = screen.getByRole('button', { name: /Start Session/i });

    await userEvent.type(input, 'My Test Project');
    await userEvent.click(button);

    await waitFor(() => expect(mockedStartSession).toHaveBeenCalledTimes(1));
    expect(mockedStartSession).toHaveBeenCalledWith({ project_name: 'My Test Project' });

    await waitFor(() => expect(mockOnSessionStart).toHaveBeenCalledTimes(1));
    expect(mockOnSessionStart).toHaveBeenCalledWith(mockResponse);

    // Check that no error message is displayed
    expect(screen.queryByText(/Error:/i)).not.toBeInTheDocument();
  });

  test('displays loading state on button and disables input/button during API call', async () => {
    // Mock startSession to resolve after a delay to check loading state
    mockedStartSession.mockImplementationOnce(() =>
      new Promise(resolve => setTimeout(() => resolve({
        status: 'session_started',
        project_name: 'Loading Test',
        current_state: 'PLANNING',
        message: 'Done loading',
      } as ApiStartResponse), 50))
    );

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    const input = screen.getByLabelText(/Project Name:/i) as HTMLInputElement;
    const button = screen.getByRole('button', { name: /Start Session/i }) as HTMLButtonElement;

    await userEvent.type(input, 'Loading Test');
    // Don't await the click fully, check intermediate state
    userEvent.click(button);

    // Check for loading state immediately after click (or as soon as possible)
    await waitFor(() => {
      expect(screen.getByRole('button', { name: /Starting.../i })).toBeInTheDocument();
      expect(input).toBeDisabled();
      expect(button).toBeDisabled();
    });

    // Wait for the call to complete to avoid issues with other tests or unhandled promises
    await waitFor(() => expect(mockOnSessionStart).toHaveBeenCalledTimes(1));
  });

  test('displays error message if startSession call fails', async () => {
    const errorMessage = 'Network Error';
    mockedStartSession.mockRejectedValueOnce(new Error(errorMessage));

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    const input = screen.getByLabelText(/Project Name:/i);
    const button = screen.getByRole('button', { name: /Start Session/i });

    await userEvent.type(input, 'Error Test');
    await userEvent.click(button);

    expect(await screen.findByText(`Error: ${errorMessage}`)).toBeInTheDocument();
    expect(mockOnSessionStart).not.toHaveBeenCalled();
  });

  test('displays generic error message if startSession fails with non-Error object', async () => {
    mockedStartSession.mockRejectedValueOnce("Some string error"); // Not an Error instance

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);
    const input = screen.getByLabelText(/Project Name:/i);
    const button = screen.getByRole('button', { name: /Start Session/i });

    await userEvent.type(input, "Non-Error Test");
    await userEvent.click(button);

    expect(await screen.findByText('Error: An unknown error occurred while starting the session.')).toBeInTheDocument();
    expect(mockOnSessionStart).not.toHaveBeenCalled();
  });
});
