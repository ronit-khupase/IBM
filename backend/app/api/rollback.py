"""
Rollback endpoint
"""
from fastapi import APIRouter, HTTPException
from app.models.schemas import RollbackResponse
from app.utils.file_utils import get_project_path
from app.core.snapshot import SnapshotManager

router = APIRouter()


@router.post("/rollback/{project_id}", response_model=RollbackResponse)
async def rollback_migration(project_id: str):
    """
    Rollback to snapshot before migration
    """
    # Find original project
    project_path = get_project_path(project_id, "uploads")
    if not project_path.exists():
        project_path = get_project_path(project_id, "repos")
    
    if not project_path.exists():
        raise HTTPException(status_code=404, detail="Project not found")
    
    try:
        # Perform rollback
        snapshot_manager = SnapshotManager(project_id)
        await snapshot_manager.rollback(project_path)
        
        return RollbackResponse(
            project_id=project_id,
            status="rollback_successful",
            message="Project restored to pre-migration state"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Rollback failed: {str(e)}")

# Made with Bob
