import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { scanRepository } from '../services/api';
import StepIndicator from '../components/StepIndicator';
import ProgressBar from '../components/ProgressBar';

const ScanResults = () => {
  const { projectId } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [scanData, setScanData] = useState(null);
  const [error, setError] = useState('');
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (!projectId) {
      navigate('/');
      return;
    }
    handleScan();
  }, [projectId]);

  const handleScan = async () => {
    setLoading(true);
    setError('');
    
    // Simulate progress
    const progressInterval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 90) {
          clearInterval(progressInterval);
          return 90;
        }
        return prev + 10;
      });
    }, 200);

    try {
      const data = await scanRepository(projectId);
      setScanData(data);
      setProgress(100);
      clearInterval(progressInterval);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to scan repository');
      clearInterval(progressInterval);
    } finally {
      setTimeout(() => setLoading(false), 500);
    }
  };

  const handleContinue = () => {
    navigate(`/plan/${projectId}`);
  };

  return (
    <div className="container">
      <StepIndicator currentStep={2} projectId={projectId} />

      <div className="card fade-in">
        <div className="card-header">
          <h1 className="card-title">🔍 Scanning Repository</h1>
          <p className="card-subtitle">Analyzing your codebase and detecting frameworks</p>
        </div>

        {loading && (
          <div className="scan-progress">
            <ProgressBar 
              progress={progress} 
              label="Scanning files and detecting patterns..." 
              animated={true}
              color="primary"
            />
            <div className="loading-details">
              <div className="loading-spinner-large"></div>
              <p>Please wait while we analyze your project...</p>
            </div>
          </div>
        )}

        {error && (
          <div className="warning-box">
            <strong>⚠️ Error:</strong> {error}
            <button className="btn btn-secondary" onClick={handleScan} style={{ marginTop: '1rem' }}>
              🔄 Retry Scan
            </button>
          </div>
        )}

        {!loading && scanData && (
          <div className="scan-results-content slide-up">
            <div className="success-box">
              <strong>✅ Scan Complete!</strong> Successfully analyzed your project.
            </div>

            <div className="stats-grid">
              <div className="stat-card">
                <div className="stat-icon">🎯</div>
                <div className="stat-value">{scanData.framework.toUpperCase()}</div>
                <div className="stat-label">Framework Detected</div>
              </div>
              <div className="stat-card">
                <div className="stat-icon">📁</div>
                <div className="stat-value">{scanData.files_scanned}</div>
                <div className="stat-label">Files Scanned</div>
              </div>
              <div className="stat-card">
                <div className="stat-icon">🔍</div>
                <div className="stat-value">{scanData.detected_patterns?.length || 0}</div>
                <div className="stat-label">Patterns Found</div>
              </div>
            </div>

            <div className="info-section">
              <h3>📊 Analysis Summary</h3>
              <p className="summary-text">{scanData.summary}</p>
            </div>

            {scanData.detected_patterns && scanData.detected_patterns.length > 0 && (
              <div className="patterns-section">
                <h3>🎨 Detected Patterns</h3>
                <div className="pattern-grid">
                  {scanData.detected_patterns.map((pattern, idx) => (
                    <div key={idx} className="pattern-badge">
                      <span className="pattern-icon">✓</span>
                      <span>{pattern}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            <div className="action-buttons">
              <button className="btn btn-primary btn-large" onClick={handleContinue}>
                Continue to Migration Plan →
              </button>
              <button className="btn btn-secondary" onClick={() => navigate('/')}>
                ← Start New Project
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ScanResults;

// Made with Bob
