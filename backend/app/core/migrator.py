"""
Code migration engine
Converts legacy code to modern frameworks using IBM Bob AI
"""
from pathlib import Path
from typing import Dict, Any, List
from app.core.bob_client import get_bob_client
from app.core.snapshot import SnapshotManager
from app.utils.file_utils import (
    get_project_path,
    scan_directory,
    read_file_content,
    write_file_content,
    get_relative_path
)


class CodeMigrator:
    """Migrate code from one framework to another"""
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.bob_client = get_bob_client()
        self.snapshot_manager = SnapshotManager(project_id)
    
    async def migrate(
        self,
        source_framework: str,
        target_framework: str,
        source_path: Path
    ) -> Dict[str, Any]:
        """
        Perform migration from source to target framework
        """
        print(f"\n{'='*80}")
        print(f"🚀 STARTING MIGRATION")
        print(f"{'='*80}")
        print(f"Project ID: {self.project_id}")
        print(f"Source Framework: {source_framework}")
        print(f"Target Framework: {target_framework}")
        print(f"Source Path: {source_path}")
        print(f"{'='*80}\n")
        
        # Create snapshot before migration
        print("📸 Creating snapshot...")
        await self.snapshot_manager.create_snapshot(source_path)
        print("✅ Snapshot created\n")
        
        # Get files to migrate
        print("🔍 Finding files to migrate...")
        files_to_migrate = self._get_migration_files(source_framework, source_path)
        print(f"✅ Found {len(files_to_migrate)} files to migrate\n")
        
        for i, f in enumerate(files_to_migrate[:5], 1):
            print(f"  {i}. {f.name}")
        if len(files_to_migrate) > 5:
            print(f"  ... and {len(files_to_migrate) - 5} more files\n")
        
        # Prepare output directory
        output_path = get_project_path(self.project_id, "migrated")
        output_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Output directory: {output_path}\n")
        
        # Migrate files
        converted_files = []
        print(f"🔄 Starting file conversion...\n")
        
        for idx, file_path in enumerate(files_to_migrate, 1):
            try:
                print(f"[{idx}/{len(files_to_migrate)}] Converting: {file_path.name}")
                converted = await self._migrate_file(
                    file_path=file_path,
                    source_framework=source_framework,
                    target_framework=target_framework,
                    source_path=source_path,
                    output_path=output_path
                )
                if converted:
                    converted_files.append(converted)
                    print(f"  ✅ Converted successfully\n")
                else:
                    print(f"  ⚠️  Conversion returned None\n")
            except Exception as e:
                print(f"  ❌ Error: {str(e)}\n")
        
        # Generate project structure files
        print("📝 Generating project structure files...")
        await self._generate_project_files(target_framework, output_path)
        print("✅ Project files generated\n")
        
        print(f"{'='*80}")
        print(f"✅ MIGRATION COMPLETE")
        print(f"{'='*80}")
        print(f"Converted Files: {len(converted_files)}")
        print(f"Output Path: {output_path}")
        print(f"{'='*80}\n")
        
        return {
            "converted_files": len(converted_files),
            "output_path": str(output_path),
            "target_framework": target_framework,
            "files": converted_files
        }
    
    def _get_migration_files(
        self,
        framework: str,
        source_path: Path
    ) -> List[Path]:
        """
        Get list of files to migrate based on framework
        """
        if framework.lower() == "django":
            return self._get_django_files(source_path)
        elif framework.lower() == "spring":
            return self._get_spring_files(source_path)
        elif framework.lower() == "flask":
            return self._get_flask_files(source_path)
        else:
            # Default: get all Python or Java files
            return scan_directory(source_path, extensions=['.py', '.java'])
    
    def _get_django_files(self, source_path: Path) -> List[Path]:
        """Get Django files to migrate"""
        target_files = []
        all_files = scan_directory(source_path)
        
        for file in all_files:
            if file.suffix == '.py':
                filename = file.name
                # Focus on key Django files
                if any(pattern in filename for pattern in [
                    'views', 'models', 'urls', 'serializers', 'forms'
                ]):
                    target_files.append(file)
        
        return target_files[:20]  # Limit for MVP
    
    def _get_spring_files(self, source_path: Path) -> List[Path]:
        """Get Spring files to migrate"""
        target_files = []
        all_files = scan_directory(source_path)
        
        for file in all_files:
            if file.suffix == '.java':
                content = read_file_content(file)
                # Look for Spring annotations
                if any(annotation in content for annotation in [
                    '@RestController', '@Controller', '@Entity', '@Service'
                ]):
                    target_files.append(file)
        
        return target_files[:20]  # Limit for MVP
    
    def _get_flask_files(self, source_path: Path) -> List[Path]:
        """Get Flask files to migrate"""
        target_files = []
        all_files = scan_directory(source_path)
        
        for file in all_files:
            if file.suffix == '.py':
                content = read_file_content(file)
                if 'flask' in content.lower():
                    target_files.append(file)
        
        return target_files[:15]
    
    async def _migrate_file(
        self,
        file_path: Path,
        source_framework: str,
        target_framework: str,
        source_path: Path,
        output_path: Path
    ) -> Dict[str, str]:
        """
        Migrate a single file
        """
        # Read source code
        source_code = read_file_content(file_path)
        
        # Determine file type
        file_type = self._determine_file_type(file_path, source_code)
        
        # Convert using Bob AI
        converted_code = await self.bob_client.migrate_code(
            source_code=source_code,
            source_framework=source_framework,
            target_framework=target_framework,
            file_type=file_type
        )
        
        # Determine output path
        relative_path = get_relative_path(file_path, source_path)
        output_file = output_path / relative_path
        
        # Adjust extension if needed
        if target_framework.lower() == "fastapi" and output_file.suffix == '.java':
            output_file = output_file.with_suffix('.py')
        
        # Write converted code
        write_file_content(output_file, converted_code)
        
        return {
            "source": relative_path,
            "target": str(output_file.relative_to(output_path)),
            "type": file_type
        }
    
    def _determine_file_type(self, file_path: Path, content: str) -> str:
        """
        Determine file type for migration
        """
        filename = file_path.name.lower()
        
        if 'model' in filename:
            return "model"
        elif 'view' in filename or 'controller' in filename:
            return "controller"
        elif 'url' in filename or 'route' in filename:
            return "routes"
        elif 'serializer' in filename:
            return "serializer"
        elif 'service' in filename:
            return "service"
        else:
            return "general"
    
    async def _generate_project_files(
        self,
        target_framework: str,
        output_path: Path
    ) -> None:
        """
        Generate necessary project files for target framework
        """
        if target_framework.lower() == "fastapi":
            await self._generate_fastapi_files(output_path)
        elif target_framework.lower() == "springboot":
            await self._generate_springboot_files(output_path)
    
    async def _generate_fastapi_files(self, output_path: Path) -> None:
        """Generate FastAPI project files"""
        
        # main.py
        main_content = '''"""
FastAPI Application - Migrated from legacy framework
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Migrated API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Migrated API is running"}

# Import your migrated routes here
'''
        write_file_content(output_path / "main.py", main_content)
        
        # requirements.txt
        requirements = '''fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic==2.5.3
'''
        write_file_content(output_path / "requirements.txt", requirements)
        
        # README.md
        readme = '''# Migrated FastAPI Application

This application was automatically migrated from a legacy framework.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Notes

- Review all migrated code
- Update database connections
- Configure environment variables
- Test all endpoints
'''
        write_file_content(output_path / "README.md", readme)
    
    async def _generate_springboot_files(self, output_path: Path) -> None:
        """Generate Spring Boot project files"""
        
        # application.properties
        properties = '''server.port=8080
spring.application.name=migrated-app
'''
        config_dir = output_path / "src" / "main" / "resources"
        write_file_content(config_dir / "application.properties", properties)

# Made with Bob
