import React from 'react';

interface ApproveButtonAreaProps {
  isApprovalStepEnabled: boolean; // Will come from context or props
  onApprove: () => void; // Callback for approval
  isLoading: boolean;
}

const ApproveButtonArea: React.FC<ApproveButtonAreaProps> = ({ isApprovalStepEnabled, onApprove, isLoading }) => {
  return (
    <div className="approve-button-area" style={{ padding: '10px', textAlign: 'center', marginTop: '10px' }}>
      <button
        onClick={onApprove}
        disabled={!isApprovalStepEnabled || isLoading}
        style={{ padding: '10px 20px', backgroundColor: 'green', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
      >
        {isLoading ? 'Processando...' : 'Aprovar Fase'}
      </button>
      {!isApprovalStepEnabled && <p style={{fontSize: '0.9em', color: '#777'}}>Aguardando conclusão da IA para aprovar.</p>}
    </div>
  );
};

export default ApproveButtonArea;
