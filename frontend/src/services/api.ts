// frontend/src/services/api.ts

// Define a base URL for the API.
// If using CRA proxy, relative paths like '/start' are fine.
// Otherwise, use the full URL: 'http://localhost:8000'
const API_BASE_URL = ''; // Using relative paths for CRA proxy

// --- TypeScript interfaces for API payloads and responses ---
// These should mirror the Pydantic models in backend/main.py

export interface ApiStartRequest {
  project_name: string;
}

export interface ApiStartResponse {
  status: string;
  project_name: string;
  current_state: string;
  message: string; // This is the initial AI message
}

export interface ApiChatRequest {
  user_message: string;
}

export interface ApiChatResponse {
  user_message: string;
  ai_response: string;
  current_state: string;
  history_length: number;
  is_approval_step: boolean;
}

// No request payload for /approve
export interface ApiApproveResponse {
  status: string;
  new_state: string;
  message: string; // This is the initial AI message for the new phase
}

// No request payload for POST /generate_files
export interface ApiGenerateFilesResponse {
  status: string;
  message: string;
}

// --- API Service Functions ---

/**
 * Helper function to handle fetch responses and errors.
 */
async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let errorData;
    try {
      errorData = await response.json();
    } catch (e) {
      // Not a JSON response, or other error parsing JSON
      throw new Error(response.statusText || `HTTP error! status: ${response.status}`);
    }
    // Use error detail from FastAPI if available
    const message = errorData?.detail || response.statusText || `HTTP error! status: ${response.status}`;
    throw new Error(message);
  }
  return response.json() as Promise<T>;
}

/**
 * Starts a new planning session.
 * Corresponds to backend POST /start
 */
export async function startSession(payload: ApiStartRequest): Promise<ApiStartResponse> {
  const response = await fetch(`${API_BASE_URL}/start`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
  return handleResponse<ApiStartResponse>(response);
}

/**
 * Sends a user message to the chat.
 * Corresponds to backend POST /chat
 */
export async function sendMessage(payload: ApiChatRequest): Promise<ApiChatResponse> {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
  return handleResponse<ApiChatResponse>(response);
}

/**
 * Approves the current phase.
 * Corresponds to backend POST /approve
 */
export async function approvePhase(): Promise<ApiApproveResponse> {
  const response = await fetch(`${API_BASE_URL}/approve`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', // Even if no body, good practice
    },
    // No body for this request as per backend/main.py
  });
  return handleResponse<ApiApproveResponse>(response);
}

/**
 * Triggers the generation of project files.
 * Corresponds to backend POST /generate_files
 */
export async function generateFiles(): Promise<ApiGenerateFilesResponse> {
  const response = await fetch(`${API_BASE_URL}/generate_files`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // No body for this request
  });
  return handleResponse<ApiGenerateFilesResponse>(response);
}
