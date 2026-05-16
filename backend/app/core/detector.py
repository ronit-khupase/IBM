"""
Framework detection logic
Detects Django, Spring Framework, and other frameworks
"""
from pathlib import Path
from typing import Dict, List, Optional
from app.utils.file_utils import scan_directory, read_file_content


class FrameworkDetector:
    """Detect framework type from repository structure"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.files = scan_directory(project_path)
    
    def detect(self) -> Dict[str, any]:
        """
        Detect framework and return details
        """
        # Check for Django
        if self._is_django():
            return {
                "framework": "django",
                "version": self._detect_django_version(),
                "key_files": self._get_django_files(),
                "patterns": ["MVT", "ORM", "Admin Panel"]
            }
        
        # Check for Spring
        if self._is_spring():
            return {
                "framework": "spring",
                "version": self._detect_spring_version(),
                "key_files": self._get_spring_files(),
                "patterns": ["MVC", "Dependency Injection", "Annotations"]
            }
        
        # Check for Flask
        if self._is_flask():
            return {
                "framework": "flask",
                "version": "unknown",
                "key_files": self._get_flask_files(),
                "patterns": ["Microframework", "Decorators"]
            }
        
        # Check for Express
        if self._is_express():
            return {
                "framework": "express",
                "version": "unknown",
                "key_files": self._get_express_files(),
                "patterns": ["Middleware", "Routes"]
            }
        
        # Unknown framework
        return {
            "framework": "unknown",
            "version": "unknown",
            "key_files": [],
            "patterns": []
        }
    
    def _is_django(self) -> bool:
        """Check if project is Django"""
        indicators = [
            "manage.py",
            "settings.py",
            "wsgi.py"
        ]
        return self._has_files(indicators, min_count=2)
    
    def _is_spring(self) -> bool:
        """Check if project is Spring Framework"""
        indicators = [
            "pom.xml",
            "build.gradle",
            "application.properties",
            "application.yml"
        ]
        
        if not self._has_files(indicators, min_count=1):
            return False
        
        # Check for Spring annotations in Java files
        java_files = [f for f in self.files if f.suffix == '.java']
        for java_file in java_files[:10]:  # Check first 10 files
            content = read_file_content(java_file)
            if any(annotation in content for annotation in [
                "@RestController",
                "@Controller",
                "@SpringBootApplication",
                "@Entity",
                "@Service"
            ]):
                return True
        
        return False
    
    def _is_flask(self) -> bool:
        """Check if project is Flask"""
        for file in self.files:
            if file.suffix == '.py':
                content = read_file_content(file)
                if "from flask import" in content or "import flask" in content:
                    return True
        return False
    
    def _is_express(self) -> bool:
        """Check if project is Express.js"""
        if self._has_files(["package.json"]):
            package_json = self.project_path / "package.json"
            if package_json.exists():
                content = read_file_content(package_json)
                return "express" in content.lower()
        return False
    
    def _has_files(self, filenames: List[str], min_count: int = 1) -> bool:
        """Check if project has specified files"""
        found = 0
        for filename in filenames:
            for file in self.files:
                if file.name == filename:
                    found += 1
                    break
        return found >= min_count
    
    def _detect_django_version(self) -> str:
        """Detect Django version from requirements or imports"""
        # Check requirements.txt
        req_file = self.project_path / "requirements.txt"
        if req_file.exists():
            content = read_file_content(req_file)
            for line in content.split('\n'):
                if 'django' in line.lower():
                    return line.strip()
        return "unknown"
    
    def _detect_spring_version(self) -> str:
        """Detect Spring version from pom.xml or build.gradle"""
        pom_file = self.project_path / "pom.xml"
        if pom_file.exists():
            content = read_file_content(pom_file)
            if "spring-boot" in content:
                return "Spring Boot"
            return "Spring Framework"
        return "unknown"
    
    def _get_django_files(self) -> List[str]:
        """Get key Django files"""
        key_patterns = ["manage.py", "settings.py", "urls.py", "models.py", "views.py", "admin.py"]
        return self._find_files_by_name(key_patterns)
    
    def _get_spring_files(self) -> List[str]:
        """Get key Spring files"""
        key_files = []
        for file in self.files:
            if file.suffix == '.java':
                content = read_file_content(file)
                if any(annotation in content for annotation in [
                    "@RestController", "@Controller", "@Entity", "@Service", "@Repository"
                ]):
                    key_files.append(str(file.relative_to(self.project_path)))
        return key_files[:20]  # Limit to 20 files
    
    def _get_flask_files(self) -> List[str]:
        """Get key Flask files"""
        flask_files = []
        for file in self.files:
            if file.suffix == '.py':
                content = read_file_content(file)
                if "flask" in content.lower():
                    flask_files.append(str(file.relative_to(self.project_path)))
        return flask_files[:10]
    
    def _get_express_files(self) -> List[str]:
        """Get key Express files"""
        return self._find_files_by_name(["package.json", "app.js", "server.js", "index.js"])
    
    def _find_files_by_name(self, names: List[str]) -> List[str]:
        """Find files by name patterns"""
        found = []
        for name in names:
            for file in self.files:
                if name in file.name:
                    found.append(str(file.relative_to(self.project_path)))
        return found

# Made with Bob
