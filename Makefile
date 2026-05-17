# Makefile for Legacy Code Surgeon AI
# Simplifies common development and deployment tasks

.PHONY: help install dev build up down logs clean test lint format security

# Default target
help:
	@echo "Legacy Code Surgeon AI - Available Commands"
	@echo "============================================"
	@echo "Development:"
	@echo "  make install    - Install all dependencies"
	@echo "  make dev        - Start development servers"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make format     - Format code"
	@echo ""
	@echo "Docker:"
	@echo "  make build      - Build Docker images"
	@echo "  make up         - Start Docker containers"
	@echo "  make down       - Stop Docker containers"
	@echo "  make logs       - View Docker logs"
	@echo "  make restart    - Restart Docker containers"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make security   - Run security checks"
	@echo "  make backup     - Backup storage data"
	@echo ""

# Install dependencies
install:
	@echo "Installing backend dependencies..."
	cd backend && pip install -r requirements.txt
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "✓ Dependencies installed"

# Development servers
dev:
	@echo "Starting development servers..."
	@echo "Backend: http://localhost:8000"
	@echo "Frontend: http://localhost:3000"
	@echo "Press Ctrl+C to stop"
	@make -j2 dev-backend dev-frontend

dev-backend:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend:
	cd frontend && npm run dev

# Docker commands
build:
	@echo "Building Docker images..."
	docker-compose build --no-cache
	@echo "✓ Images built successfully"

up:
	@echo "Starting Docker containers..."
	docker-compose up -d
	@echo "✓ Containers started"
	@echo "Frontend: http://localhost"
	@echo "Backend: http://localhost:8000"
	@make status

down:
	@echo "Stopping Docker containers..."
	docker-compose down
	@echo "✓ Containers stopped"

restart:
	@make down
	@make up

logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

status:
	@echo "Container Status:"
	@docker-compose ps

# Testing
test:
	@echo "Running backend tests..."
	cd backend && pytest
	@echo "Running frontend tests..."
	cd frontend && npm test

test-backend:
	cd backend && pytest -v

test-frontend:
	cd frontend && npm test

# Code quality
lint:
	@echo "Linting backend..."
	cd backend && flake8 app/
	cd backend && mypy app/
	@echo "Linting frontend..."
	cd frontend && npm run lint

format:
	@echo "Formatting backend code..."
	cd backend && black app/
	cd backend && isort app/
	@echo "Formatting frontend code..."
	cd frontend && npm run format

# Security
security:
	@echo "Running security checks..."
	@echo "Checking Python dependencies..."
	cd backend && pip install safety && safety check
	@echo "Checking Node dependencies..."
	cd frontend && npm audit
	@echo "✓ Security checks complete"

# Maintenance
clean:
	@echo "Cleaning build artifacts..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf backend/dist backend/build 2>/dev/null || true
	rm -rf frontend/dist frontend/build 2>/dev/null || true
	rm -rf frontend/node_modules/.cache 2>/dev/null || true
	@echo "✓ Cleaned build artifacts"

clean-all: clean
	@echo "Removing all generated files..."
	rm -rf backend/venv backend/.venv 2>/dev/null || true
	rm -rf frontend/node_modules 2>/dev/null || true
	docker-compose down -v
	@echo "✓ All generated files removed"

backup:
	@echo "Creating backup..."
	tar -czf backup-$$(date +%Y%m%d-%H%M%S).tar.gz backend/app/storage/
	@echo "✓ Backup created"

# Production deployment
deploy-prod:
	@echo "Deploying to production..."
	@echo "⚠️  Make sure you have:"
	@echo "  1. Updated .env with production values"
	@echo "  2. Generated strong SECRET_KEY"
	@echo "  3. Configured CORS_ORIGINS"
	@echo "  4. Set up SSL certificates"
	@read -p "Continue? [y/N] " -n 1 -r; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		make build && make up; \
	fi

# Health checks
health:
	@echo "Checking service health..."
	@curl -s http://localhost:8000/health | python -m json.tool || echo "Backend not responding"
	@curl -s http://localhost/ > /dev/null && echo "Frontend: OK" || echo "Frontend: Not responding"

# Database operations (if applicable)
db-migrate:
	cd backend && alembic upgrade head

db-rollback:
	cd backend && alembic downgrade -1

# Environment setup
setup-env:
	@echo "Setting up environment files..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "✓ Created .env from .env.example"; \
		echo "⚠️  Please update .env with your values"; \
	else \
		echo "✓ .env already exists"; \
	fi
	@if [ ! -f frontend/.env ]; then \
		cp frontend/.env.example frontend/.env; \
		echo "✓ Created frontend/.env"; \
	fi

# Quick start
quickstart: setup-env install
	@echo ""
	@echo "✓ Setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Update .env with your BOB_AI_API_KEY"
	@echo "  2. Run 'make dev' to start development servers"
	@echo "  3. Or run 'make up' to start with Docker"
	@echo ""

# Made with Bob
