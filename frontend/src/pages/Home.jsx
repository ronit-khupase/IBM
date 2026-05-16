import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { uploadProject, cloneGitHub } from '../services/api';

const Home = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [uploadMethod, setUploadMethod] = useState('zip');
  const [repoUrl, setRepoUrl] = useState('');
  const [error, setError] = useState('');
  const [uploadProgress, setUploadProgress] = useState(0);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    if (!file.name.endsWith('.zip')) {
      setError('Please upload a ZIP file');
      return;
    }

    setLoading(true);
    setError('');
    setUploadProgress(0);

    // Simulate upload progress
    const progressInterval = setInterval(() => {
      setUploadProgress(prev => {
        if (prev >= 90) {
          clearInterval(progressInterval);
          return 90;
        }
        return prev + 10;
      });
    }, 200);

    try {
      const response = await uploadProject(file);
      setUploadProgress(100);
      clearInterval(progressInterval);
      setTimeout(() => {
        navigate(`/scan/${response.project_id}`);
      }, 500);
    } catch (err) {
      clearInterval(progressInterval);
      setError(err.response?.data?.detail || 'Failed to upload project');
    } finally {
      setLoading(false);
    }
  };

  const handleGitHubClone = async (e) => {
    e.preventDefault();
    
    if (!repoUrl) {
      setError('Please enter a GitHub repository URL');
      return;
    }

    setLoading(true);
    setError('');
    setUploadProgress(0);

    const progressInterval = setInterval(() => {
      setUploadProgress(prev => {
        if (prev >= 90) {
          clearInterval(progressInterval);
          return 90;
        }
        return prev + 10;
      });
    }, 300);

    try {
      const response = await cloneGitHub(repoUrl);
      setUploadProgress(100);
      clearInterval(progressInterval);
      setTimeout(() => {
        navigate(`/scan/${response.project_id}`);
      }, 500);
    } catch (err) {
      clearInterval(progressInterval);
      setError(err.response?.data?.detail || 'Failed to clone repository');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="hero-section fade-in">
        <h1 className="hero-title">
          <span className="hero-icon">🔧</span>
          Legacy Code Surgeon AI
        </h1>
        <p className="hero-subtitle">
          Modernize your legacy code with AI-powered migration
        </p>
      </div>

      <div className="card slide-up">
        <div className="card-header">
          <h2 className="card-title">Get Started</h2>
          <p className="card-subtitle">
            Upload your project or clone from GitHub to begin
          </p>
        </div>

        <div className="info-box">
          <strong>🚀 Supported Migration:</strong>
          <div className="migration-badges">
            <span className="migration-badge">Django → FastAPI</span>
          </div>
          <p style={{ marginTop: '1rem', fontSize: '0.9rem' }}>
            Automatically convert your Django projects to modern FastAPI with AI-powered code transformation.
          </p>
        </div>

        {error && (
          <div className="warning-box slide-up">
            <strong>⚠️ Error:</strong> {error}
          </div>
        )}

        <div className="upload-methods">
          <div className="method-tabs">
            <button
              className={`method-tab ${uploadMethod === 'zip' ? 'active' : ''}`}
              onClick={() => setUploadMethod('zip')}
            >
              <span className="tab-icon">📦</span>
              Upload ZIP
            </button>
            <button
              className={`method-tab ${uploadMethod === 'github' ? 'active' : ''}`}
              onClick={() => setUploadMethod('github')}
            >
              <span className="tab-icon">🐙</span>
              Clone from GitHub
            </button>
          </div>

          <div className="method-content">
            {uploadMethod === 'zip' ? (
              <div className="upload-section fade-in">
                <label htmlFor="file-input" className="file-upload-area">
                  <div className="upload-icon">📁</div>
                  <h3>Drop your ZIP file here</h3>
                  <p>or click to browse</p>
                  <input
                    type="file"
                    accept=".zip"
                    onChange={handleFileUpload}
                    disabled={loading}
                    id="file-input"
                    style={{ display: 'none' }}
                  />
                </label>
                {loading && uploadProgress > 0 && (
                  <div className="upload-progress">
                    <div className="progress-bar-wrapper">
                      <div 
                        className="progress-bar progress-primary progress-animated"
                        style={{ width: `${uploadProgress}%` }}
                      >
                        <span className="progress-text">{uploadProgress}%</span>
                      </div>
                    </div>
                    <p className="progress-message">Uploading and extracting files...</p>
                  </div>
                )}
              </div>
            ) : (
              <form onSubmit={handleGitHubClone} className="github-form fade-in">
                <div className="form-group">
                  <label className="form-label">
                    <span className="label-icon">🔗</span>
                    GitHub Repository URL
                  </label>
                  <input
                    type="text"
                    className="form-input"
                    placeholder="https://github.com/username/repository"
                    value={repoUrl}
                    onChange={(e) => setRepoUrl(e.target.value)}
                    disabled={loading}
                  />
                </div>
                {loading && uploadProgress > 0 && (
                  <div className="upload-progress">
                    <div className="progress-bar-wrapper">
                      <div 
                        className="progress-bar progress-primary progress-animated"
                        style={{ width: `${uploadProgress}%` }}
                      >
                        <span className="progress-text">{uploadProgress}%</span>
                      </div>
                    </div>
                    <p className="progress-message">Cloning repository...</p>
                  </div>
                )}
                <button
                  type="submit"
                  className="btn btn-primary btn-large"
                  disabled={loading}
                >
                  {loading ? '🔄 Cloning...' : '🚀 Clone Repository'}
                </button>
              </form>
            )}
          </div>
        </div>
      </div>

      <div className="features-section">
        <h2 className="section-title">How It Works</h2>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">📦</div>
            <h3>1. Upload</h3>
            <p>Upload your legacy project or clone from GitHub</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🔍</div>
            <h3>2. Scan</h3>
            <p>AI analyzes your codebase and detects the framework</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">📋</div>
            <h3>3. Plan</h3>
            <p>Generate a detailed migration plan with AI insights</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>4. Migrate</h3>
            <p>Automatically convert your code to modern frameworks</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;

// Made with Bob
