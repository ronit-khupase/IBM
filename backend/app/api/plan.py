"""
Migration plan generation endpoint
"""
from fastapi import APIRouter, HTTPException
from app.models.schemas import MigrationPlanRequest, MigrationPlanResponse
from app.utils.file_utils import get_project_path
from app.core.scanner import RepositoryScanner
from app.core.planner import MigrationPlanner

router = APIRouter()


@router.post("/plan/{project_id}", response_model=MigrationPlanResponse)
async def generate_migration_plan(
    project_id: str,
    request: MigrationPlanRequest
):
    """
    Generate migration plan for project
    """
    # Find project
    project_path = get_project_path(project_id, "uploads")
    if not project_path.exists():
        project_path = get_project_path(project_id, "repos")
    
    if not project_path.exists():
        raise HTTPException(status_code=404, detail="Project not found")
    
    try:
        # Scan repository first
        scanner = RepositoryScanner(project_path)
        scan_results = await scanner.scan()
        
        source_framework = scan_results["framework"]
        target_framework = "fastapi"  # Fixed to FastAPI only
        
        # Validate source is Django
        if source_framework.lower() != "django":
            raise HTTPException(
                status_code=400,
                detail=f"Only Django to FastAPI migration is supported. Detected: {source_framework}"
            )
        
        # Generate plan
        planner = MigrationPlanner()
        plan = await planner.generate_plan(
            source_framework=source_framework,
            target_framework=target_framework,
            scan_results=scan_results
        )
        
        return MigrationPlanResponse(
            project_id=project_id,
            steps=plan["steps"],
            bugs=plan["bugs"],
            suggestions=plan["suggestions"],
            flowchart=plan["flowchart"],
            estimated_complexity=plan["estimated_complexity"]
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Plan generation failed: {str(e)}")

# Made with Bob
