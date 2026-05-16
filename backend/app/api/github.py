"""
GitHub repository cloning endpoint
"""
from fastapi import APIRouter, HTTPException
from app.models.schemas import GitHubCloneRequest, UploadResponse
from app.core.github_clone import clone_github_repo, validate_github_url

router = APIRouter()


@router.post("/github", response_model=UploadResponse)
async def clone_repository(request: GitHubCloneRequest):
    """
    Clone GitHub repository
    """
    # Validate URL
    if not validate_github_url(request.repo_url):
        raise HTTPException(
            status_code=400,
            detail="Invalid GitHub URL. Must be a valid GitHub repository URL"
        )
    
    try:
        project_id, repo_path, message = await clone_github_repo(request.repo_url)
        
        # Count files
        files_count = len(list(repo_path.rglob('*')))
        
        return UploadResponse(
            project_id=project_id,
            message=message,
            files_extracted=files_count
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Made with Bob
