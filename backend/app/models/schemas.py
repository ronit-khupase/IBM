"""
Pydantic models for Legacy Code Surgeon AI
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class GitHubCloneRequest(BaseModel):
    """Request model for cloning GitHub repository"""
    repo_url: str = Field(..., description="GitHub repository URL")


class ScanResponse(BaseModel):
    """Response model for repository scan"""
    project_id: str
    framework: str
    files_scanned: int
    summary: str
    detected_patterns: Optional[List[str]] = []


class MigrationPlanRequest(BaseModel):
    """Request model for generating migration plan"""
    target_framework: Optional[str] = "fastapi"


class MigrationPlanResponse(BaseModel):
    """Response model for migration plan"""
    project_id: str
    steps: List[str]
    bugs: List[str]
    suggestions: List[str]
    flowchart: str
    estimated_complexity: str


class MigrateRequest(BaseModel):
    """Request model for migration"""
    target_framework: str = Field(..., description="Target framework (fastapi, springboot, express)")


class MigrateResponse(BaseModel):
    """Response model for migration"""
    project_id: str
    converted_files: int
    output_path: str
    target_framework: str
    status: str


class RollbackResponse(BaseModel):
    """Response model for rollback"""
    project_id: str
    status: str
    message: str


class StatusResponse(BaseModel):
    """Response model for project status"""
    project_id: str
    status: str
    framework: Optional[str] = None
    target_framework: Optional[str] = None
    progress: Optional[int] = 0
    details: Optional[Dict[str, Any]] = {}


class UploadResponse(BaseModel):
    """Response model for file upload"""
    project_id: str
    message: str
    files_extracted: int


class ErrorResponse(BaseModel):
    """Error response model"""
    error: str
    detail: Optional[str] = None

# Made with Bob
