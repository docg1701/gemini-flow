import React, { useState }
from 'react';

interface MessageInputBarProps {
  onSendMessage: (message: string) => void; // Callback to send message
  isLoading: boolean;
}

const MessageInputBar: React.FC<MessageInputBarProps> = ({ onSendMessage, isLoading }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (message.trim() && !isLoading) {
      onSendMessage(message.trim());
      setMessage('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="message-input-bar" style={{ display: 'flex', padding: '10px' }}>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Digite sua mensagem..."
        disabled={isLoading}
        style={{ flexGrow: 1, marginRight: '10px', padding: '8px' }}
      />
      <button type="submit" disabled={isLoading || !message.trim()} style={{ padding: '8px 15px' }}>
        {isLoading ? 'Enviando...' : 'Enviar'}
      </button>
    </form>
  );
};

export default MessageInputBar;
