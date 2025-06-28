// Based on the conceptual example in task-017's execution report

export interface Message {
  id: string;
  sender: 'user' | 'ai' | 'system'; // Added 'system' for general messages
  text: string;
  timestamp: Date;
}

export interface AppContextType {
  projectName: string;
  setProjectName: (name: string) => void;
  chatHistory: Message[];
  addMessageToHistory: (message: Message) => void; // Simplified for now
  currentPhase: string;
  setCurrentPhase: (phase: string) => void;
  isApprovalStepEnabled: boolean;
  setIsApprovalStepEnabled: (isEnabled: boolean) => void;
  isLoadingChat: boolean;
  setIsLoadingChat: (isLoading: boolean) => void;
  chatError: string | null;
  setChatError: (error: string | null) => void;

  // Placeholder for functions that will interact with API
  handleSendMessage: (text: string)   => Promise<void>;
  handleApprovePhase: () => Promise<void>;
  handleStartSession: (projectName: string) => Promise<void>;
}

// Default context value, parts will be implemented by the Provider
export const defaultAppContext: AppContextType = {
  projectName: '',
  setProjectName: () => {},
  chatHistory: [],
  addMessageToHistory: () => {},
  currentPhase: 'Initializing...',
  setCurrentPhase: () => {},
  isApprovalStepEnabled: false,
  setIsApprovalStepEnabled: () => {},
  isLoadingChat: false,
  setIsLoadingChat: () => {},
  chatError: null,
  setChatError: () => {},
  handleSendMessage: async () => {},
  handleApprovePhase: async () => {},
  handleStartSession: async () => {},
};
