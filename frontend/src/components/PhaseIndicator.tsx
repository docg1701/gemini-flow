import React from 'react';

interface PhaseIndicatorProps {
  currentPhase: string; // Will come from context or props
}

const PhaseIndicator: React.FC<PhaseIndicatorProps> = ({ currentPhase }) => {
  return (
    <div className="phase-indicator" style={{ padding: '10px', backgroundColor: '#f0f0f0', textAlign: 'center' }}>
      <h2>Fase Atual: {currentPhase}</h2>
    </div>
  );
};

export default PhaseIndicator;
