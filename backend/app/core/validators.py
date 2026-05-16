"""
Code validation module
Validates that converted code meets target framework requirements
"""
from typing import Dict, Any, List, Tuple
import re


class ValidationResult:
    """Result of code validation"""
    
    def __init__(self, is_valid: bool, errors: List[str] = None, warnings: List[str] = None):
        self.is_valid = is_valid
        self.errors = errors or []
        self.warnings = warnings or []
    
    def __bool__(self):
        return self.is_valid
    
    def __repr__(self):
        return f"ValidationResult(valid={self.is_valid}, errors={len(self.errors)}, warnings={len(self.warnings)})"


class CodeValidator:
    """Validates converted code against target framework requirements"""
    
    def validate_fastapi_code(self, code: str, file_info: Dict[str, Any]) -> ValidationResult:
        """
        Validate that code is proper FastAPI and not Django
        """
        errors = []
        warnings = []
        
        # Check 1: Must not be empty or error message
        if not code or len(code.strip()) < 20:
            errors.append("Converted code is empty or too short")
            return ValidationResult(False, errors, warnings)
        
        if code.strip().startswith("Error:") or code.strip().startswith("# ERROR:"):
            errors.append("Conversion returned an error message")
            return ValidationResult(False, errors, warnings)
        
        # Check 2: Must have FastAPI imports
        has_fastapi_import = self._check_fastapi_imports(code)
        if not has_fastapi_import:
            errors.append("Missing FastAPI imports (from fastapi import ...)")
        
        # Check 3: Must NOT have Django imports
        django_imports = self._check_django_imports(code)
        if django_imports:
            errors.append(f"Still contains Django imports: {', '.join(django_imports[:3])}")
        
        # Check 4: For view files, must have route decorators
        if file_info.get("category") == "view" or file_info.get("is_django_view"):
            has_routes = self._check_route_decorators(code)
            if not has_routes:
                errors.append("View file missing FastAPI route decorators (@router.get, @app.post, etc.)")
        
        # Check 5: For model files, should use Pydantic
        if file_info.get("category") == "model" or file_info.get("is_django_model"):
            has_pydantic = self._check_pydantic_models(code)
            if not has_pydantic:
                warnings.append("Model file should use Pydantic BaseModel instead of Django models")
        
        # Check 6: Should not have Django-specific patterns
        django_patterns = self._check_django_patterns(code)
        if django_patterns:
            errors.append(f"Contains Django-specific patterns: {', '.join(django_patterns[:3])}")
        
        # Check 7: Should have async functions for FastAPI
        if file_info.get("category") == "view":
            has_async = "async def" in code
            if not has_async:
                warnings.append("Consider using async functions for better FastAPI performance")
        
        is_valid = len(errors) == 0
        return ValidationResult(is_valid, errors, warnings)
    
    def _check_fastapi_imports(self, code: str) -> bool:
        """Check if code has FastAPI imports"""
        fastapi_patterns = [
            r'from fastapi import',
            r'import fastapi',
            r'from fastapi\.',
        ]
        return any(re.search(pattern, code) for pattern in fastapi_patterns)
    
    def _check_django_imports(self, code: str) -> List[str]:
        """Check for Django imports and return list of found imports"""
        django_imports = []
        
        django_patterns = [
            (r'from django\.', 'from django.*'),
            (r'import django', 'import django'),
            (r'from rest_framework', 'from rest_framework'),
            (r'import rest_framework', 'import rest_framework'),
        ]
        
        for pattern, display in django_patterns:
            if re.search(pattern, code):
                django_imports.append(display)
        
        return django_imports
    
    def _check_route_decorators(self, code: str) -> bool:
        """Check if code has FastAPI route decorators"""
        route_patterns = [
            r'@router\.(get|post|put|delete|patch)',
            r'@app\.(get|post|put|delete|patch)',
        ]
        return any(re.search(pattern, code) for pattern in route_patterns)
    
    def _check_pydantic_models(self, code: str) -> bool:
        """Check if code uses Pydantic models"""
        pydantic_patterns = [
            r'from pydantic import.*BaseModel',
            r'class \w+\(BaseModel\)',
        ]
        return any(re.search(pattern, code) for pattern in pydantic_patterns)
    
    def _check_django_patterns(self, code: str) -> List[str]:
        """Check for Django-specific code patterns"""
        patterns_found = []
        
        django_patterns = [
            (r'\.objects\.(get|filter|all|create)', 'Django ORM queries (.objects.)'),
            (r'models\.Model', 'Django Model inheritance'),
            (r'APIView', 'Django REST Framework APIView'),
            (r'@login_required', 'Django @login_required decorator'),
            (r'render\(request', 'Django render() function'),
            (r'HttpResponse', 'Django HttpResponse'),
            (r'Token\.objects', 'Django Token authentication'),
            (r'permission_classes\s*=', 'Django permission_classes'),
        ]
        
        for pattern, description in django_patterns:
            if re.search(pattern, code):
                patterns_found.append(description)
        
        return patterns_found
    
    def validate_conversion_quality(self, original_code: str, converted_code: str) -> Tuple[int, List[str]]:
        """
        Assess quality of conversion
        Returns: (quality_score 0-100, list of issues)
        """
        issues = []
        score = 100
        
        # Check if code was actually transformed
        similarity = self._calculate_similarity(original_code, converted_code)
        if similarity > 0.9:
            issues.append("Code appears unchanged (>90% similar to original)")
            score -= 50
        
        # Check if converted code is longer (good sign of proper conversion)
        original_lines = len(original_code.split('\n'))
        converted_lines = len(converted_code.split('\n'))
        
        if converted_lines < original_lines * 0.5:
            issues.append("Converted code is significantly shorter than original")
            score -= 20
        
        # Check for TODO comments (indicates incomplete conversion)
        todo_count = converted_code.lower().count('todo')
        if todo_count > 3:
            issues.append(f"Too many TODO comments ({todo_count}) - conversion may be incomplete")
            score -= 10
        
        return max(0, score), issues
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate simple similarity ratio between two texts"""
        # Remove whitespace and comments for comparison
        clean1 = re.sub(r'#.*$', '', text1, flags=re.MULTILINE)
        clean1 = re.sub(r'\s+', '', clean1)
        clean2 = re.sub(r'#.*$', '', text2, flags=re.MULTILINE)
        clean2 = re.sub(r'\s+', '', clean2)
        
        if not clean1 or not clean2:
            return 0.0
        
        # Simple character-level similarity
        matches = sum(1 for a, b in zip(clean1, clean2) if a == b)
        max_len = max(len(clean1), len(clean2))
        
        return matches / max_len if max_len > 0 else 0.0


# Singleton instance
_validator: CodeValidator = None


def get_validator() -> CodeValidator:
    """Get or create validator instance"""
    global _validator
    if _validator is None:
        _validator = CodeValidator()
    return _validator


def validate_fastapi_code(code: str, file_info: Dict[str, Any]) -> ValidationResult:
    """Convenience function to validate FastAPI code"""
    validator = get_validator()
    return validator.validate_fastapi_code(code, file_info)


# Made with Bob