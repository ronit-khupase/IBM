"""
Code migration endpoint
"""
from fastapi import APIRouter, HTTPException
from app.models.schemas import MigrateRequest, MigrateResponse
from app.utils.file_utils import get_project_path
from app.core.scanner import RepositoryScanner
from app.core.migrator import CodeMigrator

router = APIRouter()


@router.post("/migrate/{project_id}", response_model=MigrateResponse)
async def migrate_project(
    project_id: str,
    request: MigrateRequest
):
    """
    Migrate project to target framework
    """
    # Find project
    project_path = get_project_path(project_id, "uploads")
    if not project_path.exists():
        project_path = get_project_path(project_id, "repos")
    
    if not project_path.exists():
        raise HTTPException(status_code=404, detail="Project not found")
    
    try:
        # Scan to detect source framework
        scanner = RepositoryScanner(project_path)
        scan_results = await scanner.scan()
        source_framework = scan_results["framework"]
        
        if source_framework == "unknown":
            raise HTTPException(
                status_code=400,
                detail="Unable to detect source framework"
            )
        
        # Perform migration
        migrator = CodeMigrator(project_id)
        migration_result = await migrator.migrate(
            source_framework=source_framework,
            target_framework=request.target_framework,
            source_path=project_path
        )
        
        return MigrateResponse(
            project_id=project_id,
            converted_files=migration_result["converted_files"],
            output_path=migration_result["output_path"],
            target_framework=request.target_framework,
            status="completed"
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Migration failed: {str(e)}")

# Made with Bob
