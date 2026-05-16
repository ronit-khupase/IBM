import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Upload ZIP file
export const uploadProject = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await api.post('/api/upload', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

// Clone GitHub repository
export const cloneGitHub = async (repoUrl) => {
  const response = await api.post('/api/github', { repo_url: repoUrl });
  return response.data;
};

// Scan repository
export const scanRepository = async (projectId) => {
  const response = await api.get(`/api/scan/${projectId}`);
  return response.data;
};

// Generate migration plan
export const generatePlan = async (projectId, targetFramework) => {
  const response = await api.post(`/api/plan/${projectId}`, {
    target_framework: targetFramework,
  });
  return response.data;
};

// Migrate project
export const migrateProject = async (projectId, targetFramework) => {
  const response = await api.post(`/api/migrate/${projectId}`, {
    target_framework: targetFramework,
  });
  return response.data;
};

// Rollback migration
export const rollbackMigration = async (projectId) => {
  const response = await api.post(`/api/rollback/${projectId}`);
  return response.data;
};

// Check project status
export const checkStatus = async (projectId) => {
  const response = await api.get(`/api/status/${projectId}`);
  return response.data;
};

// Health check
export const healthCheck = async () => {
  const response = await api.get('/health');
  return response.data;
};

export default api;

// Made with Bob
