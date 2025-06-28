import React from 'react';
import { render, screen }
from '@testing-library/react';
import App from './App';

describe('App Component Rendering', () => {
  beforeEach(() => {
    render(<App />);
  });

  test('renders the main application title "Planejador Gemini-Flow"', () => {
    // Check for the main title in the header
    const titleElement = screen.getByRole('heading', { name: /Planejador Gemini-Flow/i, level: 1 });
    expect(titleElement).toBeInTheDocument();
  });

  test('renders PhaseIndicator component with default phase text', () => {
    // Checks for "Fase Atual:" which is part of PhaseIndicator's structure
    // and the default initial phase text from App.tsx's state
    const phaseText = screen.getByText(/Fase Atual: Planejamento Inicial/i);
    expect(phaseText).toBeInTheDocument();
  });

  test('renders ChatWindow component (checking for placeholder text when no messages)', () => {
    // App.tsx initializes with a system message, so "Nenhuma mensagem ainda..." won't be there initially.
    // Instead, check for the initial system message.
    const initialMessage = screen.getByText(/Bem-vindo ao Planejador Gemini-Flow! Projeto: Projeto Exemplo/i);
    expect(initialMessage).toBeInTheDocument();
  });

  test('renders MessageInputBar component (checking for input placeholder and send button)', () => {
    const inputElement = screen.getByPlaceholderText(/Digite sua mensagem.../i);
    expect(inputElement).toBeInTheDocument();
    const sendButton = screen.getByRole('button', { name: /Enviar/i });
    expect(sendButton).toBeInTheDocument();
  });

  test('renders ApproveButtonArea component (checking for the approve button)', () => {
    const approveButton = screen.getByRole('button', { name: /Aprovar Fase/i });
    expect(approveButton).toBeInTheDocument();
    // Also check for the helper text when button is likely disabled initially
    const helperText = screen.getByText(/Aguardando conclusão da IA para aprovar./i);
    expect(helperText).toBeInTheDocument();
  });
});
