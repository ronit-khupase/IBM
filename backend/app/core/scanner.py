"""
Repository scanner
Scans and analyzes repository structure
"""
from pathlib import Path
from typing import Dict, Any, List
from app.utils.file_utils import scan_directory, read_file_content
from app.core.detector import FrameworkDetector


class RepositoryScanner:
    """Scan and analyze repository"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.detector = FrameworkDetector(project_path)
    
    async def scan(self) -> Dict[str, Any]:
        """
        Perform full repository scan
        """
        # Detect framework
        framework_info = self.detector.detect()
        
        # Scan all files
        all_files = scan_directory(self.project_path)
        
        # Categorize files
        file_categories = self._categorize_files(all_files)
        
        # Generate summary
        summary = self._generate_summary(framework_info, file_categories)
        
        return {
            "framework": framework_info["framework"],
            "version": framework_info.get("version", "unknown"),
            "files_scanned": len(all_files),
            "key_files": framework_info.get("key_files", []),
            "patterns": framework_info.get("patterns", []),
            "file_categories": file_categories,
            "summary": summary
        }
    
    def _categorize_files(self, files: List[Path]) -> Dict[str, int]:
        """
        Categorize files by type
        """
        categories = {
            "python": 0,
            "java": 0,
            "javascript": 0,
            "typescript": 0,
            "html": 0,
            "css": 0,
            "config": 0,
            "other": 0
        }
        
        for file in files:
            ext = file.suffix.lower()
            
            if ext == ".py":
                categories["python"] += 1
            elif ext == ".java":
                categories["java"] += 1
            elif ext == ".js":
                categories["javascript"] += 1
            elif ext in [".ts", ".tsx"]:
                categories["typescript"] += 1
            elif ext in [".html", ".htm"]:
                categories["html"] += 1
            elif ext in [".css", ".scss", ".sass"]:
                categories["css"] += 1
            elif ext in [".json", ".xml", ".yml", ".yaml", ".properties", ".conf"]:
                categories["config"] += 1
            else:
                categories["other"] += 1
        
        return categories
    
    def _generate_summary(
        self,
        framework_info: Dict[str, Any],
        file_categories: Dict[str, int]
    ) -> str:
        """
        Generate human-readable summary
        """
        framework = framework_info.get("framework", "unknown")
        total_files = sum(file_categories.values())
        
        summary = f"Detected {framework.upper()} framework. "
        summary += f"Scanned {total_files} files. "
        
        # Add file type breakdown
        main_types = []
        for ftype, count in file_categories.items():
            if count > 0 and ftype != "other":
                main_types.append(f"{count} {ftype}")
        
        if main_types:
            summary += f"Contains: {', '.join(main_types)}. "
        
        # Add patterns
        patterns = framework_info.get("patterns", [])
        if patterns:
            summary += f"Patterns: {', '.join(patterns)}."
        
        return summary
    
    def get_file_structure(self) -> Dict[str, Any]:
        """
        Get detailed file structure
        """
        structure = {
            "directories": [],
            "files": []
        }
        
        for item in self.project_path.rglob('*'):
            relative_path = str(item.relative_to(self.project_path))
            
            if item.is_dir():
                structure["directories"].append(relative_path)
            else:
                structure["files"].append({
                    "path": relative_path,
                    "size": item.stat().st_size,
                    "extension": item.suffix
                })
        
        return structure

# Made with Bob
