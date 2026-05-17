# 🚀 Deployment Guide - Legacy Code Surgeon AI

Complete guide for deploying the Legacy Code Surgeon AI platform to production.

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Start with Docker](#quick-start-with-docker)
- [Manual Deployment](#manual-deployment)
- [Environment Configuration](#environment-configuration)
- [Production Checklist](#production-checklist)
- [Cloud Deployment](#cloud-deployment)
- [Monitoring & Maintenance](#monitoring--maintenance)
- [Troubleshooting](#troubleshooting)

---

## 🔧 Prerequisites

### Required
- **Docker** 20.10+ and **Docker Compose** 2.0+
- **IBM Bob AI API Key** (Get from IBM Cloud)
- **Domain name** (for production)
- **SSL Certificate** (recommended for production)

### Optional
- **GitHub Personal Access Token** (for private repos)
- **Monitoring tools** (Prometheus, Grafana)
- **Reverse proxy** (Nginx, Traefik)

---

## 🐳 Quick Start with Docker

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/legacy-code-surgeon-ai.git
cd legacy-code-surgeon-ai
```

### 2. Configure Environment
```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your credentials
nano .env
```

**Required variables:**
```env
BOB_AI_API_KEY=your_bob_api_key_here
SECRET_KEY=generate_strong_random_string_here
ENVIRONMENT=production
```

### 3. Build and Run
```bash
# Build and start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### 4. Access Application
- **Frontend**: http://localhost
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### 5. Stop Services
```bash
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

---

## 🔨 Manual Deployment

### Backend Deployment

#### 1. Setup Python Environment
```bash
cd backend

# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

#### 3. Run Backend
```bash
# Development
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production with Gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend Deployment

#### 1. Setup Node Environment
```bash
cd frontend

# Install dependencies
npm install
```

#### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your API URL
```

#### 3. Build and Serve
```bash
# Build for production
npm run build

# Preview build
npm run preview

# Serve with a static server
npx serve -s dist -l 3000
```

---

## ⚙️ Environment Configuration

### Backend (.env)
```env
# IBM Bob AI
BOB_AI_API_KEY=your_api_key_here
BOB_AI_API_URL=https://api.dataplatform.cloud.ibm.com/semantic_agents/public/v1/mcp_server/mcp/

# Application
ENVIRONMENT=production
API_HOST=0.0.0.0
API_PORT=8000
LOG_LEVEL=INFO

# Security
SECRET_KEY=your-strong-random-secret-key
JWT_EXPIRATION_MINUTES=60

# CORS
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Storage
STORAGE_BASE_DIR=app/storage
MAX_UPLOAD_SIZE_MB=100
TEMP_FILE_RETENTION_HOURS=24

# Optional: GitHub
GITHUB_TOKEN=your_github_token_here
```

### Frontend (.env)
```env
# API Configuration
VITE_API_URL=https://api.yourdomain.com

# For local development
# VITE_API_URL=http://localhost:8000
```

### Generate Secret Key
```bash
# Python method
python -c "import secrets; print(secrets.token_urlsafe(32))"

# OpenSSL method
openssl rand -base64 32
```

---

## ✅ Production Checklist

### Security
- [ ] Change default `SECRET_KEY` to strong random string
- [ ] Update `BOB_AI_API_KEY` with production key
- [ ] Configure proper CORS origins (remove `*`)
- [ ] Enable HTTPS/SSL certificates
- [ ] Set up firewall rules
- [ ] Implement rate limiting
- [ ] Add input validation
- [ ] Enable security headers

### Performance
- [ ] Enable gzip compression
- [ ] Configure caching headers
- [ ] Optimize Docker images
- [ ] Set up CDN for static assets
- [ ] Configure database connection pooling (if using DB)
- [ ] Enable logging and monitoring

### Reliability
- [ ] Set up health checks
- [ ] Configure automatic restarts
- [ ] Implement backup strategy
- [ ] Set up error tracking (Sentry)
- [ ] Configure log rotation
- [ ] Test rollback procedures

### Monitoring
- [ ] Set up application monitoring
- [ ] Configure log aggregation
- [ ] Set up alerts for errors
- [ ] Monitor API response times
- [ ] Track resource usage
- [ ] Set up uptime monitoring

---

## ☁️ Cloud Deployment

### AWS Deployment

#### Using ECS (Elastic Container Service)
```bash
# Build and push images
docker build -f Dockerfile.backend -t your-registry/backend:latest .
docker build -f Dockerfile.frontend -t your-registry/frontend:latest .

docker push your-registry/backend:latest
docker push your-registry/frontend:latest

# Deploy to ECS using task definitions
```

#### Using EC2
```bash
# SSH into EC2 instance
ssh -i your-key.pem ec2-user@your-instance

# Install Docker
sudo yum update -y
sudo yum install docker -y
sudo service docker start

# Clone and deploy
git clone your-repo
cd legacy-code-surgeon-ai
docker-compose up -d
```

### Google Cloud Platform

#### Using Cloud Run
```bash
# Build and deploy backend
gcloud builds submit --tag gcr.io/PROJECT_ID/backend
gcloud run deploy backend --image gcr.io/PROJECT_ID/backend --platform managed

# Build and deploy frontend
gcloud builds submit --tag gcr.io/PROJECT_ID/frontend
gcloud run deploy frontend --image gcr.io/PROJECT_ID/frontend --platform managed
```

### Azure Deployment

#### Using Azure Container Instances
```bash
# Create resource group
az group create --name legacy-surgeon --location eastus

# Deploy containers
az container create --resource-group legacy-surgeon \
  --name backend --image your-registry/backend:latest \
  --dns-name-label legacy-surgeon-backend --ports 8000

az container create --resource-group legacy-surgeon \
  --name frontend --image your-registry/frontend:latest \
  --dns-name-label legacy-surgeon-frontend --ports 80
```

### DigitalOcean

#### Using App Platform
```bash
# Use doctl CLI or web interface
doctl apps create --spec app-spec.yaml
```

---

## 📊 Monitoring & Maintenance

### Health Checks
```bash
# Backend health
curl http://localhost:8000/health

# Frontend health
curl http://localhost/

# Docker health
docker-compose ps
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend

# Last 100 lines
docker-compose logs --tail=100
```

### Update Application
```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Backup Data
```bash
# Backup storage directory
tar -czf backup-$(date +%Y%m%d).tar.gz backend/app/storage/

# Restore backup
tar -xzf backup-20260517.tar.gz -C backend/app/
```

### Database Maintenance (if applicable)
```bash
# Backup database
docker-compose exec backend python manage.py dumpdata > backup.json

# Restore database
docker-compose exec backend python manage.py loaddata backup.json
```

---

## 🔍 Troubleshooting

### Common Issues

#### Backend won't start
```bash
# Check logs
docker-compose logs backend

# Common fixes:
# 1. Verify BOB_AI_API_KEY is set
# 2. Check port 8000 is not in use
# 3. Ensure storage directories exist
# 4. Verify Python dependencies installed
```

#### Frontend can't connect to backend
```bash
# Check CORS settings in backend/.env
CORS_ORIGINS=http://localhost,http://localhost:80

# Verify API URL in frontend
echo $VITE_API_URL

# Check network connectivity
docker-compose exec frontend ping backend
```

#### Storage permission errors
```bash
# Fix permissions
sudo chown -R 1000:1000 backend/app/storage/
chmod -R 755 backend/app/storage/
```

#### Out of memory
```bash
# Increase Docker memory limit
# Edit docker-compose.yml
services:
  backend:
    mem_limit: 2g
  frontend:
    mem_limit: 1g
```

#### SSL/HTTPS issues
```bash
# Use Let's Encrypt with Certbot
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Or use Traefik as reverse proxy with automatic SSL
```

### Performance Issues

#### Slow API responses
- Check Bob AI API rate limits
- Enable caching for repeated requests
- Optimize file processing
- Increase worker processes

#### High memory usage
- Limit concurrent migrations
- Clean up temporary files regularly
- Optimize Docker images
- Use memory profiling tools

---

## 📞 Support

### Getting Help
- **Documentation**: Check README.md and inline code comments
- **Logs**: Always check logs first: `docker-compose logs -f`
- **Health Check**: Verify services are healthy: `docker-compose ps`
- **GitHub Issues**: Report bugs and request features

### Useful Commands
```bash
# Restart specific service
docker-compose restart backend

# Rebuild specific service
docker-compose up -d --build backend

# Remove all containers and volumes
docker-compose down -v

# Clean up Docker system
docker system prune -a

# Check resource usage
docker stats
```

---

## 🔐 Security Best Practices

1. **Never commit `.env` files** to version control
2. **Use strong, unique passwords** for all services
3. **Keep dependencies updated** regularly
4. **Enable HTTPS** in production
5. **Implement rate limiting** to prevent abuse
6. **Sanitize user inputs** to prevent injection attacks
7. **Use secrets management** for sensitive data
8. **Regular security audits** and penetration testing
9. **Monitor logs** for suspicious activity
10. **Keep backups** in secure, separate location

---

## 📝 License

MIT License - See LICENSE file for details

---

**Made with ❤️ for IBM Hackathon 2026**

For more information, see [README.md](README.md)