import React, { useState } from 'react';
import './App.css';
import ProjectNameInput from './components/ProjectNameInput';
import { ApiStartResponse } from './services/api'; // Assuming this is where types are also exported from api.ts

// Placeholder for the main chat interface components (to be developed in task-016)
// These will eventually receive sessionData and other relevant props.
const ChatInterfacePlaceholder: React.FC<{ sessionData: ApiStartResponse }> = ({ sessionData }) => {
  return (
    <div>
      <h2>Chat Interface for: {sessionData.project_name}</h2>
      <p>Current State: {sessionData.current_state}</p>
      <p>Initial AI Message: {sessionData.message}</p>
      <p><em>(Full chat UI will be implemented in task-016)</em></p>
      {/*
        When task-016 is done, this will be replaced by:
        <PhaseIndicator currentPhase={sessionData.current_state} />
        <ChatWindow messages={...} />
        <MessageInputBar onSendMessage={...} isLoading={...} />
        <ApproveButtonArea isApprovalStepEnabled={...} onApprove={...} isLoading={...} />
      */}
    </div>
  );
};

function App() {
  const [sessionData, setSessionData] = useState<ApiStartResponse | null>(null);
  const [appIsLoading, setAppIsLoading] = useState<boolean>(false); // For the /start API call
  const [appError, setAppError] = useState<string | null>(null);

  const handleSessionStarted = (data: ApiStartResponse) => {
    setSessionData(data);
    setAppError(null); // Clear previous errors on new session
    // Further state initializations based on 'data' can happen here if needed
    // e.g., setting initial chat messages from data.message
  };

  // This function will be passed to ProjectNameInput
  // ProjectNameInput will call onSessionStart (which is handleSessionStarted here)
  // and will manage its own internal isLoading/error for the API call itself.
  // App.tsx can also have its own global loading/error for the transition.

  if (appIsLoading) { // This global loading could be for initial app load, not used yet
    return <div className="App"><p>Loading application...</p></div>;
  }

  return (
    <div className="App">
      <header className="App-header-main">
        <h1>Planejador Gemini-Flow</h1>
      </header>
      <main style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        {appError && <p style={{ color: 'red' }}>Application Error: {appError}</p>}

        {!sessionData ? (
          <ProjectNameInput
            onSessionStart={handleSessionStarted}
            // Optionally, ProjectNameInput could call a global error setter:
            // onError={(errorMessage) => setAppError(`Failed to start session: ${errorMessage}`)}
            // But for now, ProjectNameInput handles its own error display for the form.
          />
        ) : (
          <ChatInterfacePlaceholder sessionData={sessionData} />
        )}
      </main>
    </div>
  );
}

export default App;
