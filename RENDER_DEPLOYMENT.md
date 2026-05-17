# 🚀 Render.com Deployment Guide

Complete step-by-step guide to deploy Legacy Code Surgeon AI on Render.com

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Method 1: Blueprint Deployment (Recommended)](#method-1-blueprint-deployment-recommended)
- [Method 2: Manual Deployment](#method-2-manual-deployment)
- [Configuration](#configuration)
- [Post-Deployment](#post-deployment)
- [Troubleshooting](#troubleshooting)
- [Cost Estimation](#cost-estimation)

---

## 🔧 Prerequisites

1. **Render Account**
   - Sign up at [render.com](https://render.com)
   - Free tier available

2. **GitHub Repository**
   - Push your code to GitHub
   - Make repository public or connect Render to private repo

3. **IBM Bob AI API Key**
   - Get from IBM Cloud
   - Keep it ready for configuration

---

## 🎯 Method 1: Blueprint Deployment (Recommended)

This method uses the `render.yaml` file to deploy both services automatically.

### Step 1: Push Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Ready for Render deployment"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/legacy-code-surgeon-ai.git

# Push to GitHub
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com)
   - Click "New +" → "Blueprint"

2. **Connect Repository**
   - Select "Connect a repository"
   - Choose your GitHub repository
   - Click "Connect"

3. **Configure Blueprint**
   - Render will detect `render.yaml`
   - Review the services:
     - `legacy-surgeon-backend` (Python/FastAPI)
     - `legacy-surgeon-frontend` (Static Site)

4. **Set Environment Variables**
   - Click on "Environment Variables"
   - Add `BOB_AI_API_KEY`:
     ```
     Key: BOB_AI_API_KEY
     Value: your_bob_api_key_here
     ```
   - Other variables are auto-configured

5. **Deploy**
   - Click "Apply"
   - Wait 5-10 minutes for deployment
   - Both services will deploy automatically

### Step 3: Update Frontend API URL

After backend deploys, you'll get a URL like:
`https://legacy-surgeon-backend.onrender.com`

1. Go to frontend service settings
2. Update `VITE_API_URL` environment variable:
   ```
   VITE_API_URL=https://legacy-surgeon-backend.onrender.com
   ```
3. Trigger manual deploy for frontend

---

## 🔨 Method 2: Manual Deployment

Deploy backend and frontend separately.

### Backend Deployment

1. **Create Web Service**
   - Dashboard → "New +" → "Web Service"
   - Connect your repository
   - Select branch: `main`

2. **Configure Service**
   ```
   Name: legacy-surgeon-backend
   Region: Oregon (or closest to you)
   Branch: main
   Root Directory: (leave empty)
   Runtime: Python 3
   Build Command: pip install -r backend/requirements.txt
   Start Command: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

3. **Set Environment Variables**
   ```
   PYTHON_VERSION=3.11.0
   BOB_AI_API_KEY=your_api_key_here
   BOB_AI_API_URL=https://api.dataplatform.cloud.ibm.com/semantic_agents/public/v1/mcp_server/mcp/
   ENVIRONMENT=production
   SECRET_KEY=generate_strong_random_key
   LOG_LEVEL=INFO
   CORS_ORIGINS=https://your-frontend-url.onrender.com
   API_HOST=0.0.0.0
   ```

4. **Add Disk Storage (Optional)**
   - Go to "Disks" tab
   - Add disk:
     ```
     Name: storage
     Mount Path: /app/backend/app/storage
     Size: 1 GB
     ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Note the URL: `https://legacy-surgeon-backend.onrender.com`

### Frontend Deployment

1. **Create Static Site**
   - Dashboard → "New +" → "Static Site"
   - Connect your repository
   - Select branch: `main`

2. **Configure Service**
   ```
   Name: legacy-surgeon-frontend
   Branch: main
   Root Directory: (leave empty)
   Build Command: cd frontend && npm install && npm run build
   Publish Directory: frontend/dist
   ```

3. **Set Environment Variables**
   ```
   NODE_VERSION=18.17.0
   VITE_API_URL=https://legacy-surgeon-backend.onrender.com
   ```

4. **Configure Redirects**
   - Create `frontend/public/_redirects` file:
   ```
   /*    /index.html   200
   ```

5. **Deploy**
   - Click "Create Static Site"
   - Wait for deployment (3-5 minutes)
   - Access at: `https://legacy-surgeon-frontend.onrender.com`

---

## ⚙️ Configuration

### Environment Variables Reference

#### Backend Required Variables
```env
BOB_AI_API_KEY=your_bob_api_key_here          # REQUIRED
BOB_AI_API_URL=https://api.dataplatform...    # Auto-set
ENVIRONMENT=production                          # Auto-set
SECRET_KEY=auto_generated_by_render            # Auto-generated
CORS_ORIGINS=https://your-frontend.onrender.com # Update after frontend deploy
```

#### Frontend Required Variables
```env
VITE_API_URL=https://your-backend.onrender.com  # Update after backend deploy
```

### Generate Secret Key

If not using auto-generation:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🔄 Post-Deployment

### 1. Verify Backend

```bash
# Health check
curl https://legacy-surgeon-backend.onrender.com/health

# Expected response:
{
  "status": "healthy",
  "bob_ai_configured": true
}
```

### 2. Verify Frontend

- Visit: `https://legacy-surgeon-frontend.onrender.com`
- Should see the home page
- Try uploading a test file

### 3. Update CORS

1. Go to backend service settings
2. Update `CORS_ORIGINS`:
   ```
   CORS_ORIGINS=https://legacy-surgeon-frontend.onrender.com
   ```
3. Save and redeploy

### 4. Test Full Workflow

1. Upload a Django project (ZIP or GitHub)
2. Scan the repository
3. Generate migration plan
4. Execute migration
5. Download results

---

## 🔍 Troubleshooting

### Backend Issues

#### Service Won't Start
```bash
# Check logs in Render dashboard
# Common issues:
# 1. Missing BOB_AI_API_KEY
# 2. Wrong Python version
# 3. Dependencies not installed
```

**Solution:**
- Verify all environment variables are set
- Check build logs for errors
- Ensure `requirements.txt` is in `backend/` directory

#### 502 Bad Gateway
```bash
# Backend is starting but not responding
# Check start command
```

**Solution:**
- Verify start command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Check if port binding is correct
- Review application logs

#### CORS Errors
```bash
# Frontend can't connect to backend
```

**Solution:**
- Update `CORS_ORIGINS` in backend with frontend URL
- Redeploy backend service
- Clear browser cache

### Frontend Issues

#### Build Fails
```bash
# npm install or build errors
```

**Solution:**
- Check Node version (should be 18+)
- Verify `package.json` is in `frontend/` directory
- Check build command: `cd frontend && npm install && npm run build`

#### API Connection Failed
```bash
# Frontend can't reach backend
```

**Solution:**
- Verify `VITE_API_URL` is set correctly
- Check backend is running
- Test backend URL directly

#### 404 on Routes
```bash
# React Router routes return 404
```

**Solution:**
- Create `frontend/public/_redirects`:
  ```
  /*    /index.html   200
  ```
- Redeploy frontend

### Storage Issues

#### Files Not Persisting
```bash
# Uploaded files disappear after restart
```

**Solution:**
- Add persistent disk in Render dashboard
- Mount to `/app/backend/app/storage`
- Minimum 1GB recommended

---

## 💰 Cost Estimation

### Free Tier
- **Backend**: Free tier available (750 hours/month)
- **Frontend**: Free for static sites
- **Storage**: 1GB free

**Limitations:**
- Services spin down after 15 minutes of inactivity
- Cold start time: 30-60 seconds
- Shared resources

### Paid Plans

#### Starter Plan ($7/month per service)
- Always on (no spin down)
- Faster performance
- More resources

#### Professional Plan ($25/month per service)
- Dedicated resources
- Auto-scaling
- Priority support

### Recommended Setup

**For Development/Testing:**
- Free tier for both services
- Total: $0/month

**For Production:**
- Starter plan for backend: $7/month
- Free tier for frontend: $0/month
- 1GB storage: Free
- **Total: $7/month**

---

## 🔐 Security Checklist

Before going live:

- [ ] Set strong `SECRET_KEY`
- [ ] Configure proper `CORS_ORIGINS`
- [ ] Enable HTTPS (automatic on Render)
- [ ] Set up custom domain (optional)
- [ ] Configure environment variables securely
- [ ] Review `SECURITY.md`
- [ ] Set up monitoring/alerts
- [ ] Test all endpoints

---

## 📊 Monitoring

### View Logs

1. **Backend Logs**
   - Dashboard → Backend Service → Logs
   - Real-time log streaming
   - Filter by severity

2. **Frontend Logs**
   - Dashboard → Frontend Service → Logs
   - Build and deploy logs

### Metrics

- Dashboard shows:
  - CPU usage
  - Memory usage
  - Request count
  - Response times

### Alerts

Set up in Render dashboard:
- Service down alerts
- High error rate alerts
- Resource usage alerts

---

## 🔄 Updates & Redeployment

### Automatic Deployment

Render auto-deploys on git push:

```bash
# Make changes
git add .
git commit -m "Update feature"
git push origin main

# Render automatically deploys
```

### Manual Deployment

1. Go to service in dashboard
2. Click "Manual Deploy"
3. Select branch
4. Click "Deploy"

### Rollback

1. Go to service → "Deploys"
2. Find previous successful deploy
3. Click "Rollback to this version"

---

## 🌐 Custom Domain (Optional)

### Add Custom Domain

1. **Backend Domain**
   - Service Settings → Custom Domains
   - Add: `api.yourdomain.com`
   - Update DNS records as shown

2. **Frontend Domain**
   - Service Settings → Custom Domains
   - Add: `yourdomain.com` or `www.yourdomain.com`
   - Update DNS records

3. **Update Environment Variables**
   - Backend `CORS_ORIGINS`: Add custom domain
   - Frontend `VITE_API_URL`: Use custom backend domain

### SSL Certificates

- Automatic SSL via Let's Encrypt
- Free and auto-renewing
- HTTPS enforced by default

---

## 📞 Support

### Render Support
- Documentation: [render.com/docs](https://render.com/docs)
- Community: [community.render.com](https://community.render.com)
- Status: [status.render.com](https://status.render.com)

### Project Support
- GitHub Issues: Report bugs
- Documentation: See `README.md` and `DEPLOYMENT.md`

---

## 🎉 Success!

Your application should now be live at:
- **Frontend**: `https://legacy-surgeon-frontend.onrender.com`
- **Backend**: `https://legacy-surgeon-backend.onrender.com`
- **API Docs**: `https://legacy-surgeon-backend.onrender.com/docs`

---

## 📝 Quick Reference

### Useful Commands

```bash
# View backend logs
render logs legacy-surgeon-backend

# View frontend logs
render logs legacy-surgeon-frontend

# Restart service
render restart legacy-surgeon-backend

# Deploy specific branch
render deploy --branch develop
```

### Important URLs

- Dashboard: https://dashboard.render.com
- Backend: https://legacy-surgeon-backend.onrender.com
- Frontend: https://legacy-surgeon-frontend.onrender.com
- API Docs: https://legacy-surgeon-backend.onrender.com/docs

---

**Made with ❤️ for easy deployment on Render.com**

For more deployment options, see [DEPLOYMENT.md](DEPLOYMENT.md)