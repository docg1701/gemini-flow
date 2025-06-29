import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import ProjectNameInput from './ProjectNameInput';
import { startSession, APIError, ApiStartResponse } from '../services/api';

// Mock only specific functions from the api module
jest.mock('../services/api', () => ({
  ...jest.requireActual('../services/api'), // Keeps actual APIError, etc.
  startSession: jest.fn(),
  // If other api functions were used by this component and needed mocking, add them here.
}));

// Create a typed mock for startSession
const mockStartSession = startSession as jest.MockedFunction<typeof startSession>;

describe('ProjectNameInput', () => {
  const mockOnSessionStart = jest.fn();

  beforeEach(() => {
    // Clear mock history and implementation before each test
    mockStartSession.mockClear();
    mockOnSessionStart.mockClear();
  });

  test('renders the form and allows typing', () => {
    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);

    const inputElement = screen.getByLabelText(/project name/i) as HTMLInputElement;
    expect(inputElement).toBeInTheDocument();
    fireEvent.change(inputElement, { target: { value: 'Test Project' } });
    expect(inputElement.value).toBe('Test Project');

    expect(screen.getByRole('button', { name: /start session/i })).toBeEnabled();
  });

  test('shows error if project name is empty on submit', async () => {
    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);

    const submitButton = screen.getByRole('button', { name: /start session/i });
    fireEvent.submit(submitButton); // Or fireEvent.click(submitButton) then check form submission

    // Wait for error message to appear
    expect(await screen.findByText(/project name cannot be empty/i)).toBeInTheDocument();
    expect(mockStartSession).not.toHaveBeenCalled();
    expect(mockOnSessionStart).not.toHaveBeenCalled();
  });

  test('calls startSession and onSessionStart on successful submission', async () => {
    const mockResponse: ApiStartResponse = {
      status: 'success',
      project_name: 'Test Project',
      current_state: 'planning',
      message: 'Session started',
    };
    mockStartSession.mockResolvedValue(mockResponse);

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);

    const inputElement = screen.getByLabelText(/project name/i);
    fireEvent.change(inputElement, { target: { value: 'Test Project' } });

    const submitButton = screen.getByRole('button', { name: /start session/i });
    fireEvent.click(submitButton);

    expect(submitButton).toBeDisabled();
    expect(screen.getByText(/starting.../i)).toBeInTheDocument();

    await waitFor(() => expect(mockStartSession).toHaveBeenCalledWith({ project_name: 'Test Project' }));
    await waitFor(() => expect(mockOnSessionStart).toHaveBeenCalledWith(mockResponse));

    // Check that loading is reset and no error is shown
    expect(screen.getByRole('button', { name: /start session/i })).toBeEnabled();
    expect(screen.queryByText(/error:/i)).not.toBeInTheDocument();
  });

  test('displays API error message and resets loading state on API failure', async () => {
    const errorMessage = 'Network failed';
    // Simulate an APIError or a generic Error, as the component catches `err.message`
    mockStartSession.mockRejectedValue(new Error(errorMessage));

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);

    const inputElement = screen.getByLabelText(/project name/i);
    fireEvent.change(inputElement, { target: { value: 'Failure Test' } });

    const submitButton = screen.getByRole('button', { name: /start session/i });
    fireEvent.click(submitButton);

    expect(submitButton).toBeDisabled(); // Check loading state
    expect(screen.getByText(/starting.../i)).toBeInTheDocument();

    // Wait for the error message to appear
    expect(await screen.findByText(`Error: ${errorMessage}`)).toBeInTheDocument();

    // Check that loading state is reset
    expect(screen.getByRole('button', { name: /start session/i })).toBeEnabled();
    expect(screen.queryByText(/starting.../i)).not.toBeInTheDocument();

    expect(mockOnSessionStart).not.toHaveBeenCalled();
  });

  test('displays specific APIError message from api.ts and resets loading state', async () => {
    const specificErrorMessage = 'Project already exists.';
    const apiError = new APIError(specificErrorMessage, 409, 'PROJECT_EXISTS'); // Use direct APIError
    mockStartSession.mockRejectedValue(apiError);

    render(<ProjectNameInput onSessionStart={mockOnSessionStart} />);

    const inputElement = screen.getByLabelText(/project name/i);
    fireEvent.change(inputElement, { target: { value: 'Existing Project' } });

    const submitButton = screen.getByRole('button', { name: /start session/i });
    fireEvent.click(submitButton);

    expect(submitButton).toBeDisabled();

    expect(await screen.findByText(`Error: ${specificErrorMessage}`)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /start session/i })).toBeEnabled();
    expect(mockOnSessionStart).not.toHaveBeenCalled();
  });
});
