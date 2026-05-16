import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { generatePlan } from '../services/api';
import StepIndicator from '../components/StepIndicator';
import ProgressBar from '../components/ProgressBar';

const MigrationPlan = () => {
  const { projectId } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [planData, setPlanData] = useState(null);
  const [error, setError] = useState('');
  const targetFramework = 'fastapi'; // Fixed to FastAPI only
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (!projectId) {
      navigate('/');
    }
  }, [projectId]);

  const handleGeneratePlan = async () => {
    setLoading(true);
    setError('');
    setPlanData(null);
    
    // Simulate progress
    const progressInterval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 90) {
          clearInterval(progressInterval);
          return 90;
        }
        return prev + 15;
      });
    }, 300);

    try {
      const data = await generatePlan(projectId, targetFramework);
      setPlanData(data);
      setProgress(100);
      clearInterval(progressInterval);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to generate plan');
      clearInterval(progressInterval);
    } finally {
      setTimeout(() => setLoading(false), 500);
    }
  };

  const handleStartMigration = () => {
    navigate(`/migrate/${projectId}?target=${targetFramework}`);
  };

  return (
    <div className="container">
      <StepIndicator currentStep={3} projectId={projectId} />

      <div className="card fade-in">
        <div className="card-header">
          <h1 className="card-title">📋 Migration Plan</h1>
          <p className="card-subtitle">Generate AI-powered migration strategy</p>
        </div>

        {!planData && !loading && (
          <div className="plan-setup slide-up">
            <div className="info-box">
              <strong>🎯 Target Framework: FastAPI</strong>
              <p style={{ marginTop: '0.5rem' }}>
                Your Django project will be converted to FastAPI, a modern, fast Python web framework.
              </p>
            </div>

            <div className="info-box">
              <strong>💡 What happens next?</strong>
              <ul style={{ marginTop: '0.5rem', marginLeft: '1.5rem' }}>
                <li>AI analyzes your codebase structure</li>
                <li>Generates step-by-step migration plan</li>
                <li>Identifies potential issues and bugs</li>
                <li>Provides optimization suggestions</li>
              </ul>
            </div>

            <button
              className="btn btn-primary btn-large"
              onClick={handleGeneratePlan}
              disabled={loading}
            >
              🚀 Generate Migration Plan
            </button>
          </div>
        )}

        {loading && (
          <div className="plan-progress">
            <ProgressBar 
              progress={progress} 
              label="AI is analyzing your project and generating migration plan..." 
              animated={true}
              color="info"
            />
            <div className="loading-details">
              <div className="loading-spinner-large"></div>
              <div className="loading-steps">
                <div className={`loading-step ${progress > 20 ? 'active' : ''}`}>
                  <span className="step-dot"></span>
                  <span>Analyzing project structure...</span>
                </div>
                <div className={`loading-step ${progress > 50 ? 'active' : ''}`}>
                  <span className="step-dot"></span>
                  <span>Identifying migration patterns...</span>
                </div>
                <div className={`loading-step ${progress > 80 ? 'active' : ''}`}>
                  <span className="step-dot"></span>
                  <span>Generating recommendations...</span>
                </div>
              </div>
            </div>
          </div>
        )}

        {error && (
          <div className="warning-box">
            <strong>⚠️ Error:</strong> {error}
            <button className="btn btn-secondary" onClick={handleGeneratePlan} style={{ marginTop: '1rem' }}>
              🔄 Retry
            </button>
          </div>
        )}

        {!loading && planData && (
          <div className="plan-content slide-up">
            <div className="success-box">
              <strong>✅ Migration Plan Generated!</strong> Review the plan below.
            </div>

            <div className="complexity-badge">
              <span className="badge-label">Estimated Complexity:</span>
              <span className={`badge-value complexity-${planData.estimated_complexity.toLowerCase()}`}>
                {planData.estimated_complexity}
              </span>
            </div>

            <div className="plan-section">
              <h3 className="section-title">
                <span className="section-icon">📝</span>
                Migration Steps
              </h3>
              <ol className="steps-list">
                {planData.steps.map((step, idx) => (
                  <li key={idx} className="step-item-detailed">
                    <span className="step-number">{idx + 1}</span>
                    <span className="step-text">{step}</span>
                  </li>
                ))}
              </ol>
            </div>

            {planData.bugs && planData.bugs.length > 0 && (
              <div className="plan-section">
                <h3 className="section-title">
                  <span className="section-icon">⚠️</span>
                  Potential Issues
                </h3>
                <ul className="issues-list">
                  {planData.bugs.map((bug, idx) => (
                    <li key={idx} className="issue-item warning">
                      <span className="issue-icon">⚠️</span>
                      <span>{bug}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            {planData.suggestions && planData.suggestions.length > 0 && (
              <div className="plan-section">
                <h3 className="section-title">
                  <span className="section-icon">💡</span>
                  Optimization Suggestions
                </h3>
                <ul className="suggestions-list">
                  {planData.suggestions.map((suggestion, idx) => (
                    <li key={idx} className="suggestion-item">
                      <span className="suggestion-icon">💡</span>
                      <span>{suggestion}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className="action-buttons">
              <button className="btn btn-success btn-large pulse" onClick={handleStartMigration}>
                ⚡ Start Migration
              </button>
              <button className="btn btn-secondary" onClick={() => navigate(`/scan/${projectId}`)}>
                ← Back to Scan Results
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default MigrationPlan;

// Made with Bob
