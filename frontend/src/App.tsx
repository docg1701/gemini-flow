import React, { useState, useEffect } from 'react';
import './App.css'; // Assuming CRA created this, or will create
import PhaseIndicator from './components/PhaseIndicator';
import ChatWindow from './components/ChatWindow';
import MessageInputBar from './components/MessageInputBar';
import ApproveButtonArea from './components/ApproveButtonArea';
import { Message, AppContextType, defaultAppContext } from './types'; // Using AppContextType for structure guidance

// Placeholder for a real context provider setup
const AppContext = React.createContext<AppContextType>(defaultAppContext);

function App() {
  // These states would ideally come from AppContext as per task-017 strategy
  const [projectName, setProjectName] = useState<string>("Projeto Exemplo"); // Initial placeholder
  const [currentPhase, setCurrentPhase] = useState<string>("Planejamento Inicial"); // Initial placeholder
  const [chatHistory, setChatHistory] = useState<Message[]>([]);
  const [isApprovalStepEnabled, setIsApprovalStepEnabled] = useState<boolean>(false);
  const [isLoadingChat, setIsLoadingChat] = useState<boolean>(false);
  const [chatError, setChatError] = useState<string | null>(null);

  // Placeholder: Simulate receiving initial message or project name step later
  useEffect(() => {
    // This is where a call to /start might happen in task-015
    // For now, add a welcome message
    setChatHistory([
      { id: '1', sender: 'system', text: `Bem-vindo ao Planejador Gemini-Flow! Projeto: ${projectName}`, timestamp: new Date() }
    ]);
    // Simulate enabling approval after some time for testing UI
    // setTimeout(() => setIsApprovalStepEnabled(true), 5000);
  }, [projectName]);

  const handleSendMessage = async (text: string) => {
    setIsLoadingChat(true);
    setChatError(null);
    const userMessage: Message = {
      id: `msg-${Date.now()}`,
      sender: 'user',
      text,
      timestamp: new Date(),
    };
    setChatHistory(prev => [...prev, userMessage]);

    // Simulate AI response (actual API call in task-018)
    setTimeout(() => {
      const aiResponse: Message = {
        id: `msg-${Date.now() + 1}`,
        sender: 'ai',
        text: `Recebi sua mensagem: "${text}". Estou processando... (resposta simulada)`,
        timestamp: new Date(),
      };
      setChatHistory(prev => [...prev, aiResponse]);
      setIsLoadingChat(false);
      // Simulate AI enabling approval
      if (text.toLowerCase().includes("finalizar")) {
        setIsApprovalStepEnabled(true);
      }
    }, 1500);
  };

  const handleApprovePhase = async () => {
    setIsLoadingChat(true); // Use general loading for now
    console.log("Fase aprovada pelo usuário!");
    // Simulate backend call and phase transition
    setTimeout(() => {
      setCurrentPhase(prev => prev + " (Aprovada - Próxima Fase...)");
      setIsApprovalStepEnabled(false); // Reset for next phase
      const systemMessage: Message = {
        id: `msg-${Date.now()}`,
        sender: 'system',
        text: `Fase "${currentPhase}" aprovada. Iniciando próxima fase... (simulado)`,
        timestamp: new Date(),
      };
      setChatHistory(prev => [...prev, systemMessage]);
      setIsLoadingChat(false);
    }, 1000);
  };

  // Placeholder for actual context value
  const appContextValue: AppContextType = {
    ...defaultAppContext, // spread defaults
    projectName,
    setProjectName,
    chatHistory,
    addMessageToHistory: (message) => setChatHistory(prev => [...prev, message]),
    currentPhase,
    setCurrentPhase,
    isApprovalStepEnabled,
    setIsApprovalStepEnabled,
    isLoadingChat,
    setIsLoadingChat,
    chatError,
    setChatError,
    handleSendMessage,
    handleApprovePhase,
    handleStartSession: async (name) => {
      setProjectName(name);
      // Reset other states if needed
      setChatHistory([{ id: 'start', sender: 'system', text: `Nova sessão iniciada para: ${name}`, timestamp: new Date() }]);
      setCurrentPhase("Fase Inicial do Projeto: " + name);
      setIsApprovalStepEnabled(false);
    }
  };


  return (
    // Later, App will be wrapped by a real AppContextProvider
    // For now, components will receive props or use placeholder states.
    // To simulate context usage slightly, we pass down parts of appContextValue
    <div className="App">
      <header className="App-header-main"> {/* Changed class name */}
        <h1>Planejador Gemini-Flow</h1>
      </header>
      <main style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <PhaseIndicator currentPhase={appContextValue.currentPhase} />
        {appContextValue.chatError && <div style={{color: 'red', padding: '10px', border: '1px solid red', margin: '10px 0'}}>Erro: {appContextValue.chatError}</div>}
        <ChatWindow messages={appContextValue.chatHistory} />
        <MessageInputBar onSendMessage={appContextValue.handleSendMessage} isLoading={appContextValue.isLoadingChat} />
        <ApproveButtonArea isApprovalStepEnabled={appContextValue.isApprovalStepEnabled} onApprove={appContextValue.handleApprovePhase} isLoading={appContextValue.isLoadingChat} />

      {/* Example of how ProjectNameInput might be used (task-015) - commented out for now
        {projectName === "Projeto Exemplo" && (
          <div style={{marginTop: '20px', padding: '20px', border: '1px dashed #ccc'}}>
            <h3>Iniciar Novo Projeto</h3>
            <input
              type="text"
              placeholder="Nome do Projeto"
              onKeyDown={(e) => {
                if (e.key === 'Enter' && (e.target as HTMLInputElement).value.trim() !== '') {
                  appContextValue.handleStartSession((e.target as HTMLInputElement).value.trim());
                }
              }}
            />
            <button onClick={() => {
              const name = prompt("Digite o nome do projeto:");
              if (name) appContextValue.handleStartSession(name);
            }}>Iniciar Sessão</button>
          </div>
        )}
      */}
      </main>
    </div>
  );
}

export default App;
