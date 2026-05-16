"""
Migration planner
Generates migration plans using IBM Bob AI
"""
from typing import Dict, Any
from app.core.bob_client import get_bob_client


class MigrationPlanner:
    """Generate migration plans"""
    
    def __init__(self):
        self.bob_client = get_bob_client()
    
    async def generate_plan(
        self,
        source_framework: str,
        target_framework: str,
        scan_results: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate comprehensive migration plan
        """
        # Prepare repository summary
        repository_summary = self._prepare_summary(scan_results)
        
        # Get migration plan from Bob AI
        plan = await self.bob_client.generate_migration_plan(
            source_framework=source_framework,
            target_framework=target_framework,
            repository_summary=repository_summary
        )
        
        # Generate flowchart
        flowchart = await self.bob_client.generate_flowchart(
            migration_steps=plan.get("steps", [])
        )
        
        return {
            "steps": plan.get("steps", []),
            "bugs": plan.get("bugs", []),
            "suggestions": plan.get("suggestions", []),
            "flowchart": flowchart,
            "estimated_complexity": plan.get("complexity", "Medium")
        }
    
    def _prepare_summary(self, scan_results: Dict[str, Any]) -> str:
        """
        Prepare repository summary for AI
        """
        summary = f"""
Framework: {scan_results.get('framework', 'unknown')}
Version: {scan_results.get('version', 'unknown')}
Files Scanned: {scan_results.get('files_scanned', 0)}

Key Files:
{chr(10).join(f'- {f}' for f in scan_results.get('key_files', [])[:10])}

Detected Patterns:
{chr(10).join(f'- {p}' for p in scan_results.get('patterns', []))}

File Categories:
{chr(10).join(f'- {k}: {v}' for k, v in scan_results.get('file_categories', {}).items() if v > 0)}
"""
        return summary.strip()
    
    def validate_migration_path(
        self,
        source_framework: str,
        target_framework: str
    ) -> bool:
        """
        Validate if migration path is supported
        """
        supported_migrations = {
            "django": ["fastapi", "express"],
            "spring": ["springboot", "fastapi"],
            "flask": ["fastapi"],
            "express": ["fastapi"]
        }
        
        source = source_framework.lower()
        target = target_framework.lower()
        
        if source in supported_migrations:
            return target in supported_migrations[source]
        
        return False

# Made with Bob
