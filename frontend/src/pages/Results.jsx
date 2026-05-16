import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { checkStatus } from '../services/api';
import StepIndicator from '../components/StepIndicator';

const Results = () => {
  const { projectId } = useParams();
  const navigate = useNavigate();
  const [status, setStatus] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [downloading, setDownloading] = useState(false);

  useEffect(() => {
    if (!projectId) {
      navigate('/');
      return;
    }
    fetchStatus();
  }, [projectId]);

  const fetchStatus = async () => {
    setLoading(true);
    try {
      const data = await checkStatus(projectId);
      setStatus(data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to fetch status');
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async () => {
    setDownloading(true);
    try {
      const response = await fetch(`http://localhost:8000/api/download/${projectId}`, {
        method: 'GET',
      });
      
      if (!response.ok) {
        throw new Error('Download failed');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `migrated-project-${projectId}.zip`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (err) {
      alert('❌ Download failed: ' + (err.message || 'Unknown error'));
    } finally {
      setDownloading(false);
    }
  };

  if (loading) {
    return (
      <div className="container">
        <div className="card">
          <div className="loading">
            <div className="spinner"></div>
            <p>Loading results...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container">
        <div className="card">
          <div className="warning-box">
            <strong>⚠️ Error:</strong> {error}
            <button className="btn btn-primary" onClick={() => navigate('/')} style={{ marginTop: '1rem' }}>
              ← Go Home
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <StepIndicator currentStep={5} projectId={projectId} />

      <div className="card fade-in">
        <div className="card-header">
          <h1 className="card-title">✅ Migration Complete!</h1>
          <p className="card-subtitle">Your project has been successfully migrated</p>
        </div>

        <div className="success-celebration">
          <div className="celebration-icon">🎉</div>
          <h2>Congratulations!</h2>
          <p>Your legacy code has been modernized</p>
        </div>

        <div className="results-summary">
          <div className="summary-card">
            <div className="summary-icon">📊</div>
            <div className="summary-content">
              <h3>Migration Status</h3>
              <div className={`status-badge status-${status?.status}`}>
                {status?.status?.toUpperCase()}
              </div>
            </div>
          </div>

          {status?.details?.migrated_files && (
            <div className="summary-card">
              <div className="summary-icon">📁</div>
              <div className="summary-content">
                <h3>Files Converted</h3>
                <div className="summary-value">{status.details.migrated_files}</div>
              </div>
            </div>
          )}

          {status?.target_framework && (
            <div className="summary-card">
              <div className="summary-icon">🎯</div>
              <div className="summary-content">
                <h3>Target Framework</h3>
                <div className="summary-value">{status.target_framework.toUpperCase()}</div>
              </div>
            </div>
          )}

          {status?.progress !== undefined && (
            <div className="summary-card">
              <div className="summary-icon">⚡</div>
              <div className="summary-content">
                <h3>Progress</h3>
                <div className="summary-value">{status.progress}%</div>
              </div>
            </div>
          )}
        </div>

        <div className="results-actions">
          <h3>What's Next?</h3>
          <div className="action-grid">
            <div className="action-card" onClick={handleDownload}>
              <div className="action-icon">{downloading ? '⏳' : '📥'}</div>
              <h4>{downloading ? 'Downloading...' : 'Download Project'}</h4>
              <p>Download migrated files as ZIP</p>
            </div>

            <div className="action-card" onClick={() => navigate('/')}>
              <div className="action-icon">🚀</div>
              <h4>New Migration</h4>
              <p>Start migrating another project</p>
            </div>

            <div className="action-card" onClick={() => navigate(`/scan/${projectId}`)}>
              <div className="action-icon">🔍</div>
              <h4>View Scan Results</h4>
              <p>Review original scan data</p>
            </div>

            <div className="action-card" onClick={() => navigate(`/plan/${projectId}`)}>
              <div className="action-icon">📋</div>
              <h4>View Plan</h4>
              <p>Review migration plan</p>
            </div>
          </div>
        </div>

        <div className="feedback-section">
          <h3>💬 How was your experience?</h3>
          <p>Help us improve by sharing your feedback!</p>
          <div className="feedback-buttons">
            <button className="btn btn-secondary">😊 Great</button>
            <button className="btn btn-secondary">😐 Good</button>
            <button className="btn btn-secondary">😕 Needs Work</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Results;

// Made with Bob
