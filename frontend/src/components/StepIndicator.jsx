import React from 'react';
import { useNavigate } from 'react-router-dom';

const StepIndicator = ({ currentStep, projectId }) => {
  const navigate = useNavigate();
  
  const steps = [
    { id: 1, name: 'Upload', path: '/', icon: '📦' },
    { id: 2, name: 'Scan', path: `/scan/${projectId}`, icon: '🔍' },
    { id: 3, name: 'Plan', path: `/plan/${projectId}`, icon: '📋' },
    { id: 4, name: 'Migrate', path: `/migrate/${projectId}`, icon: '⚡' },
    { id: 5, name: 'Results', path: `/results/${projectId}`, icon: '✅' }
  ];

  const getStepStatus = (stepId) => {
    if (stepId < currentStep) return 'completed';
    if (stepId === currentStep) return 'active';
    return 'pending';
  };

  return (
    <div className="step-indicator">
      {steps.map((step, index) => (
        <React.Fragment key={step.id}>
          <div 
            className={`step-item ${getStepStatus(step.id)}`}
            onClick={() => {
              if (step.id <= currentStep && projectId) {
                navigate(step.path);
              }
            }}
            style={{ cursor: step.id <= currentStep && projectId ? 'pointer' : 'default' }}
          >
            <div className="step-icon">{step.icon}</div>
            <div className="step-name">{step.name}</div>
            {step.id < currentStep && <div className="step-check">✓</div>}
          </div>
          {index < steps.length - 1 && (
            <div className={`step-connector ${step.id < currentStep ? 'completed' : ''}`}></div>
          )}
        </React.Fragment>
      ))}
    </div>
  );
};

export default StepIndicator;

// Made with Bob
