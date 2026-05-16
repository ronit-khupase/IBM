"""
Project status endpoint
"""
from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.models.schemas import StatusResponse
from app.utils.file_utils import get_project_path

router = APIRouter()


@router.get("/status/{project_id}", response_model=StatusResponse)
async def get_project_status(project_id: str):
    """
    Get project status and details
    """
    # Check different storage locations
    uploads_path = get_project_path(project_id, "uploads")
    repos_path = get_project_path(project_id, "repos")
    migrated_path = get_project_path(project_id, "migrated")
    snapshots_path = get_project_path(project_id, "snapshots")
    
    status = "unknown"
    details = {}
    
    # Determine status
    if migrated_path.exists():
        status = "migrated"
        details["migrated_files"] = len(list(migrated_path.rglob('*')))
        details["output_path"] = str(migrated_path)
    elif snapshots_path.exists() and list(snapshots_path.glob('*')):
        status = "migration_in_progress"
        details["snapshots"] = len(list(snapshots_path.glob('*')))
    elif uploads_path.exists() or repos_path.exists():
        status = "uploaded"
        project_path = uploads_path if uploads_path.exists() else repos_path
        details["files_count"] = len(list(project_path.rglob('*')))
    else:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return StatusResponse(
        project_id=project_id,
        status=status,
        progress=100 if status == "migrated" else 50 if status == "migration_in_progress" else 0,
        details=details
    )

# Made with Bob
