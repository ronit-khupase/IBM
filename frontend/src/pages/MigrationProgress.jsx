import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, useSearchParams } from 'react-router-dom';
import { migrateProject } from '../services/api';
import StepIndicator from '../components/StepIndicator';
import ProgressBar from '../components/ProgressBar';

const MigrationProgress = () => {
  const { projectId } = useParams();
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const targetFramework = searchParams.get('target') || 'fastapi';
  
  const [progress, setProgress] = useState(0);
  const [currentStep, setCurrentStep] = useState('Initializing...');
  const [migrateData, setMigrateData] = useState(null);
  const [error, setError] = useState('');

  const migrationSteps = [
    { progress: 10, message: 'Creating backup snapshot...' },
    { progress: 20, message: 'Analyzing source code structure...' },
    { progress: 35, message: 'Converting models and entities...' },
    { progress: 50, message: 'Migrating routes and controllers...' },
    { progress: 65, message: 'Updating configuration files...' },
    { progress: 80, message: 'Applying modern patterns...' },
    { progress: 90, message: 'Validating migrated code...' },
    { progress: 100, message: 'Migration complete!' }
  ];

  useEffect(() => {
    if (!projectId) {
      navigate('/');
      return;
    }
    startMigration();
  }, [projectId]);

  const startMigration = async () => {
    let stepIndex = 0;

    // Simulate step-by-step progress
    const progressInterval = setInterval(() => {
      if (stepIndex < migrationSteps.length) {
        setProgress(migrationSteps[stepIndex].progress);
        setCurrentStep(migrationSteps[stepIndex].message);
        stepIndex++;
      } else {
        clearInterval(progressInterval);
      }
    }, 1500);

    try {
      const data = await migrateProject(projectId, targetFramework);
      setMigrateData(data);
      clearInterval(progressInterval);
      setProgress(100);
      setCurrentStep('Migration completed successfully!');
      
      // Auto-redirect to results after 2 seconds
      setTimeout(() => {
        navigate(`/results/${projectId}`);
      }, 2000);
    } catch (err) {
      clearInterval(progressInterval);
      setError(err.response?.data?.detail || 'Migration failed');
      setCurrentStep('Migration failed');
    }
  };

  return (
    <div className="container">
      <StepIndicator currentStep={4} projectId={projectId} />

      <div className="card fade-in">
        <div className="card-header">
          <h1 className="card-title">⚡ Migration in Progress</h1>
          <p className="card-subtitle">
            Converting to {targetFramework.toUpperCase()}
          </p>
        </div>

        {!error && (
          <div className="migration-progress-container">
            <div className="progress-circle-wrapper">
              <svg className="progress-circle" viewBox="0 0 200 200">
                <circle
                  className="progress-circle-bg"
                  cx="100"
                  cy="100"
                  r="90"
                />
                <circle
                  className="progress-circle-fill"
                  cx="100"
                  cy="100"
                  r="90"
                  style={{
                    strokeDasharray: `${2 * Math.PI * 90}`,
                    strokeDashoffset: `${2 * Math.PI * 90 * (1 - progress / 100)}`
                  }}
                />
                <text
                  x="100"
                  y="100"
                  className="progress-circle-text"
                  textAnchor="middle"
                  dominantBaseline="middle"
                >
                  {progress}%
                </text>
              </svg>
            </div>

            <div className="migration-status">
              <div className="status-message">
                <div className="status-icon pulse">⚡</div>
                <h3>{currentStep}</h3>
              </div>

              <ProgressBar 
                progress={progress} 
                animated={true}
                color="success"
              />

              <div className="migration-steps-list">
                {migrationSteps.map((step, idx) => (
                  <div 
                    key={idx} 
                    className={`migration-step ${progress >= step.progress ? 'completed' : progress >= step.progress - 10 ? 'active' : ''}`}
                  >
                    <div className="step-indicator-dot">
                      {progress >= step.progress ? '✓' : '○'}
                    </div>
                    <div className="step-message">{step.message}</div>
                  </div>
                ))}
              </div>
            </div>

            <div className="info-box" style={{ marginTop: '2rem' }}>
              <strong>⏱️ Please wait...</strong>
              <p style={{ marginTop: '0.5rem' }}>
                This process may take a few minutes depending on your project size.
                Do not close this window.
              </p>
            </div>
          </div>
        )}

        {error && (
          <div className="warning-box">
            <strong>❌ Migration Failed</strong>
            <p style={{ marginTop: '0.5rem' }}>{error}</p>
            <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
              <button 
                className="btn btn-primary" 
                onClick={() => navigate(`/plan/${projectId}`)}
              >
                ← Back to Plan
              </button>
              <button 
                className="btn btn-secondary" 
                onClick={() => navigate('/')}
              >
                Start New Project
              </button>
            </div>
          </div>
        )}

        {migrateData && progress === 100 && (
          <div className="success-box slide-up">
            <strong>✅ Migration Successful!</strong>
            <p style={{ marginTop: '0.5rem' }}>
              Redirecting to results page...
            </p>
          </div>
        )}
      </div>
    </div>
  );
};

export default MigrationProgress;

// Made with Bob
