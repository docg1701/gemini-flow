import React, { useState } from 'react';
import { startSession, ApiStartResponse } from '../services/api';

interface ProjectNameInputProps {
  onSessionStart: (sessionData: ApiStartResponse) => void;
  // Optional: onError callback for more specific error handling in parent
  // onError: (errorMessage: string) => void;
}

const ProjectNameInput: React.FC<ProjectNameInputProps> = ({ onSessionStart }) => {
  const [projectName, setProjectName] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!projectName.trim()) {
      setError('Project name cannot be empty.');
      return;
    }
    setIsLoading(true);
    setError(null);
    try {
      const response = await startSession({ project_name: projectName });
      onSessionStart(response);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred while starting the session.');
      }
      // Optionally call onError prop if provided
      // if (onError) onError(error instanceof Error ? error.message : 'Unknown error');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="project-name-input-form">
      <h2>Start a New Project</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="projectName">Project Name:</label>
          <input
            type="text"
            id="projectName"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            disabled={isLoading}
            required
          />
        </div>
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Starting...' : 'Start Session'}
        </button>
      </form>
      {error && <p className="error-message-form">Error: {error}</p>}
    </div>
  );
};

export default ProjectNameInput;
