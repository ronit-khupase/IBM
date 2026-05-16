import React from 'react';

const ProgressBar = ({ progress, label, animated = true, color = 'primary' }) => {
  const colorClasses = {
    primary: 'progress-primary',
    success: 'progress-success',
    warning: 'progress-warning',
    info: 'progress-info'
  };

  return (
    <div className="progress-container">
      {label && <div className="progress-label">{label}</div>}
      <div className="progress-bar-wrapper">
        <div 
          className={`progress-bar ${colorClasses[color]} ${animated ? 'progress-animated' : ''}`}
          style={{ width: `${progress}%` }}
        >
          <span className="progress-text">{progress}%</span>
        </div>
      </div>
    </div>
  );
};

export default ProgressBar;

// Made with Bob
