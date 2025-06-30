// frontend/src/services/api.ts

// Define a base URL for the API.
// API calls will be proxied by Nginx to the backend.
// All API calls should be prefixed with /api
const API_BASE_URL = '/api';

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


// --- Custom Error Class ---
export class APIError extends Error {
  status: number;
  errorCode?: string;
  errorData?: any; // To store the full error response body if needed

  constructor(message: string, status: number, errorCode?: string, errorData?: any) {
    super(message);
    this.name = 'APIError';
    this.status = status;
    this.errorCode = errorCode;
    this.errorData = errorData;
    // Set the prototype explicitly for correct instanceof checks.
    Object.setPrototypeOf(this, APIError.prototype);
  }
}

/**
 * Helper function to handle fetch responses and parse API errors.
 */
async function handleApiResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let errorJson: any = null;
    let errorMessage = `HTTP error! Status: ${response.status} ${response.statusText || ''}`.trim();
    let errorCode: string | undefined = undefined;

    try {
      errorJson = await response.json();
      if (errorJson && errorJson.detail) {
        errorMessage = errorJson.detail;
      }
      if (errorJson && errorJson.error_code) {
        errorCode = errorJson.error_code;
      }
    } catch (e) {
      // Response was not JSON or error parsing JSON.
      // errorMessage is already set to a default from response.statusText.
      // If response.statusText is also empty, it falls back to the generic HTTP error message.
    }
    throw new APIError(errorMessage, response.status, errorCode, errorJson);
  }
  return response.json() as Promise<T>;
}

/**
 * Wraps fetch calls to also catch network errors and convert them to APIError.
 */
async function fetchWithErrorHandling<T>(url: string, options?: RequestInit): Promise<T> {
  try {
    const response = await fetch(url, options);
    return await handleApiResponse<T>(response);
  } catch (error) {
    if (error instanceof APIError) {
      throw error; // Re-throw if it's already our custom APIError (from handleApiResponse)
    }
    // This catches network errors (e.g., server down, DNS issues) or other unexpected errors during fetch
    const message = error instanceof Error ? error.message : 'A network error occurred. Please check your connection.';
    throw new APIError(message, 0, 'NETWORK_ERROR'); // status 0 for network errors
  }
}

/**
 * Starts a new planning session.
 * Corresponds to backend POST /start
 */
export async function startSession(payload: ApiStartRequest): Promise<ApiStartResponse> {
  return fetchWithErrorHandling<ApiStartResponse>(`${API_BASE_URL}/start`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
}

/**
 * Sends a user message to the chat.
 * Corresponds to backend POST /chat
 */
export async function sendMessage(payload: ApiChatRequest): Promise<ApiChatResponse> {
  return fetchWithErrorHandling<ApiChatResponse>(`${API_BASE_URL}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });
}

/**
 * Approves the current phase.
 * Corresponds to backend POST /approve
 */
export async function approvePhase(): Promise<ApiApproveResponse> {
  return fetchWithErrorHandling<ApiApproveResponse>(`${API_BASE_URL}/approve`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json', // Even if no body, good practice
    },
    // No body for this request as per backend/main.py
  });
}

/**
 * Triggers the generation of project files.
 * Corresponds to backend POST /generate_files
 */
export async function generateFiles(): Promise<ApiGenerateFilesResponse> {
  return fetchWithErrorHandling<ApiGenerateFilesResponse>(`${API_BASE_URL}/generate_files`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // No body for this request
  });
}
