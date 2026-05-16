"""
Repository scanning endpoint
"""
from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.models.schemas import ScanResponse
from app.utils.file_utils import get_project_path
from app.core.scanner import RepositoryScanner

router = APIRouter()


@router.get("/scan/{project_id}", response_model=ScanResponse)
async def scan_repository(project_id: str):
    """
    Scan uploaded/cloned repository
    """
    # Try to find project in uploads or repos
    project_path = get_project_path(project_id, "uploads")
    if not project_path.exists():
        project_path = get_project_path(project_id, "repos")
    
    if not project_path.exists():
        raise HTTPException(status_code=404, detail="Project not found")
    
    try:
        # Scan repository
        scanner = RepositoryScanner(project_path)
        scan_results = await scanner.scan()
        
        return ScanResponse(
            project_id=project_id,
            framework=scan_results["framework"],
            files_scanned=scan_results["files_scanned"],
            summary=scan_results["summary"],
            detected_patterns=scan_results.get("patterns", [])
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scan failed: {str(e)}")

# Made with Bob
