"""
Legacy Code Surgeon AI - FastAPI Backend
Main application entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import routers
from app.api import upload, github, scan, plan, migrate, status, download

# Create FastAPI app
app = FastAPI(
    title="Legacy Code Surgeon AI",
    description="AI-powered Django to FastAPI migration platform",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(github.router, prefix="/api", tags=["GitHub"])
app.include_router(scan.router, prefix="/api", tags=["Scan"])
app.include_router(plan.router, prefix="/api", tags=["Plan"])
app.include_router(migrate.router, prefix="/api", tags=["Migrate"])
app.include_router(status.router, prefix="/api", tags=["Status"])
app.include_router(download.router, prefix="/api", tags=["Download"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Legacy Code Surgeon AI API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    bob_api_key = os.getenv("BOB_AI_API_KEY")
    
    return {
        "status": "healthy",
        "bob_ai_configured": bool(bob_api_key)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Made with Bob
