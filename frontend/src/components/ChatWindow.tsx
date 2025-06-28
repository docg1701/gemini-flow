import React from 'react';
import { Message } from '../types'; // Assuming types are in ../types

interface ChatWindowProps {
  messages: Message[]; // Will come from context or props
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages }) => {
  return (
    <div className="chat-window" style={{ height: '400px', overflowY: 'auto', border: '1px solid #ccc', padding: '10px', margin: '10px 0' }}>
      {messages.length === 0 && <p>Nenhuma mensagem ainda...</p>}
      {messages.map((msg) => (
        <div key={msg.id} className={`message ${msg.sender}`} style={{ marginBottom: '10px', textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
          <div style={{
            display: 'inline-block',
            padding: '8px 12px',
            borderRadius: '10px',
            backgroundColor: msg.sender === 'user' ? '#dcf8c6' : (msg.sender === 'ai' ? '#f1f0f0' : '#e0e0e0'),
            maxWidth: '70%',
          }}>
            <strong>{msg.sender === 'ai' ? 'Jules' : (msg.sender === 'system' ? 'Sistema' : 'Você')}: </strong>
            {msg.text}
            <div style={{ fontSize: '0.75em', color: '#888', marginTop: '4px' }}>
              {new Date(msg.timestamp).toLocaleTimeString()}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ChatWindow;
