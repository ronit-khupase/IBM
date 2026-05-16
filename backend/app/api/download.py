"""
Download endpoint for migrated projects
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
from pathlib import Path

router = APIRouter()

MIGRATED_DIR = Path("app/storage/migrated")


@router.get("/download/{project_id}")
async def download_migrated_project(project_id: str):
    """
    Download migrated project as ZIP file
    """
    project_path = MIGRATED_DIR / project_id
    
    if not project_path.exists():
        raise HTTPException(status_code=404, detail="Migrated project not found")
    
    # Create ZIP file
    zip_path = f"app/storage/migrated_{project_id}"
    
    try:
        # Create zip archive
        shutil.make_archive(zip_path, 'zip', project_path)
        zip_file = f"{zip_path}.zip"
        
        if not os.path.exists(zip_file):
            raise HTTPException(status_code=500, detail="Failed to create ZIP file")
        
        return FileResponse(
            path=zip_file,
            media_type='application/zip',
            filename=f"migrated-project-{project_id}.zip"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download failed: {str(e)}")

# Made with Bob
