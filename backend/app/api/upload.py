"""
File upload endpoint
Handles ZIP file uploads
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import aiofiles
from app.models.schemas import UploadResponse
from app.utils.file_utils import generate_project_id, get_project_path, extract_zip

router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_project(file: UploadFile = File(...)):
    """
    Upload ZIP file containing project
    """
    # Validate file type
    if not file.filename.endswith('.zip'):
        raise HTTPException(status_code=400, detail="Only ZIP files are allowed")
    
    # Generate project ID
    project_id = generate_project_id()
    project_path = get_project_path(project_id, "uploads")
    project_path.mkdir(parents=True, exist_ok=True)
    
    # Save uploaded file
    zip_path = project_path / "upload.zip"
    
    try:
        async with aiofiles.open(zip_path, 'wb') as f:
            content = await file.read()
            await f.write(content)
        
        # Extract ZIP
        files_extracted = await extract_zip(zip_path, project_path)
        
        # Remove ZIP file after extraction
        zip_path.unlink()
        
        return UploadResponse(
            project_id=project_id,
            message="Project uploaded and extracted successfully",
            files_extracted=files_extracted
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# Made with Bob
