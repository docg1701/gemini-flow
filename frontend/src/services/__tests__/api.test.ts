// frontend/src/services/__tests__/api.test.ts
import {
  startSession,
  sendMessage,
  approvePhase,
  generateFiles,
  ApiStartRequest,
  ApiStartResponse,
  ApiChatRequest,
  ApiChatResponse,
  ApiApproveResponse,
  ApiGenerateFilesResponse,
} from '../api';

// Mock global fetch
global.fetch = jest.fn();

const mockFetch = global.fetch as jest.Mock;

describe('API Service', () => {
  beforeEach(() => {
    // Clear all instances and calls to constructor and all methods:
    mockFetch.mockClear();
  });

  // --- Test startSession ---
  describe('startSession', () => {
    const mockPayload: ApiStartRequest = { project_name: 'Test Project' };
    const mockSuccessResponse: ApiStartResponse = {
      status: 'session_started',
      project_name: 'Test Project',
      current_state: 'PLANNING',
      message: 'AI message for PLANNING',
    };

    it('should call /start with POST and correct payload, then return data on success', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => mockSuccessResponse,
      } as Response);

      const result = await startSession(mockPayload);

      expect(mockFetch).toHaveBeenCalledTimes(1);
      expect(mockFetch).toHaveBeenCalledWith('/api/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(mockPayload),
      });
      expect(result).toEqual(mockSuccessResponse);
    });

    it('should throw an error if startSession fetch fails (not ok)', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 500,
        statusText: 'Internal Server Error',
        json: async () => ({ detail: 'Server error detail' }),
      } as Response);

      await expect(startSession(mockPayload)).rejects.toThrow('Server error detail');
      expect(mockFetch).toHaveBeenCalledTimes(1);
    });

    it('should throw an error if startSession fetch fails (network error or non-JSON)', async () => {
        mockFetch.mockResolvedValueOnce({
          ok: false,
          status: 404,
          statusText: 'Not Found',
          json: async () => { throw new SyntaxError("Unexpected token < in JSON at position 0"); }, // Simulate non-JSON response
        } as Response);

        await expect(startSession(mockPayload)).rejects.toThrow('Not Found');
        expect(mockFetch).toHaveBeenCalledTimes(1);
      });
  });

  // --- Test sendMessage ---
  describe('sendMessage', () => {
    const mockPayload: ApiChatRequest = { user_message: 'Hello AI' };
    const mockSuccessResponse: ApiChatResponse = {
      user_message: 'Hello AI',
      ai_response: 'Hello User',
      current_state: 'PLANNING',
      history_length: 2,
      is_approval_step: false,
    };

    it('should call /chat with POST and correct payload, then return data on success', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => mockSuccessResponse,
      } as Response);

      const result = await sendMessage(mockPayload);

      expect(mockFetch).toHaveBeenCalledTimes(1);
      expect(mockFetch).toHaveBeenCalledWith('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(mockPayload),
      });
      expect(result).toEqual(mockSuccessResponse);
    });

    it('should throw an error if sendMessage fetch fails', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 400,
        statusText: 'Bad Request',
        json: async () => ({ detail: 'Invalid input' }),
      } as Response);

      await expect(sendMessage(mockPayload)).rejects.toThrow('Invalid input');
    });
  });

  // --- Test approvePhase ---
  describe('approvePhase', () => {
    const mockSuccessResponse: ApiApproveResponse = {
      status: 'state_changed',
      new_state: 'ISSUES',
      message: 'AI message for ISSUES',
    };

    it('should call /approve with POST, then return data on success', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => mockSuccessResponse,
      } as Response);

      const result = await approvePhase();

      expect(mockFetch).toHaveBeenCalledTimes(1);
      expect(mockFetch).toHaveBeenCalledWith('/api/approve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        // No body
      });
      expect(result).toEqual(mockSuccessResponse);
    });

    it('should throw an error if approvePhase fetch fails', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 503,
        statusText: 'Service Unavailable',
        json: async () => ({ detail: 'Approval system down' }),
      } as Response);

      await expect(approvePhase()).rejects.toThrow('Approval system down');
    });
  });

  // --- Test generateFiles ---
  describe('generateFiles', () => {
    const mockSuccessResponse: ApiGenerateFilesResponse = {
      status: 'files_generated',
      message: 'Files generated successfully at /output/Test Project',
    };

    it('should call /generate_files with POST, then return data on success', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => mockSuccessResponse,
      } as Response);

      const result = await generateFiles();

      expect(mockFetch).toHaveBeenCalledTimes(1);
      expect(mockFetch).toHaveBeenCalledWith('/api/generate_files', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        // No body
      });
      expect(result).toEqual(mockSuccessResponse);
    });

    it('should throw an error if generateFiles fetch fails', async () => {
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 403,
        statusText: 'Forbidden',
        json: async () => ({ detail: 'Permission denied' }),
      } as Response);

      await expect(generateFiles()).rejects.toThrow('Permission denied');
    });
  });
});
