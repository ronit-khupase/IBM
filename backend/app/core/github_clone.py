"""
GitHub repository cloning functionality
"""
import git
from pathlib import Path
from typing import Tuple
from app.utils.file_utils import generate_project_id, get_project_path


async def clone_github_repo(repo_url: str) -> Tuple[str, Path, str]:
    """
    Clone GitHub repository
    
    Returns:
        Tuple of (project_id, repo_path, message)
    """
    project_id = generate_project_id()
    repo_path = get_project_path(project_id, "repos")
    
    try:
        # Clone repository
        git.Repo.clone_from(repo_url, repo_path)
        
        # Count files
        file_count = len(list(repo_path.rglob('*')))
        
        message = f"Successfully cloned repository from {repo_url}"
        
        return project_id, repo_path, message
        
    except git.GitCommandError as e:
        raise Exception(f"Failed to clone repository: {str(e)}")
    except Exception as e:
        raise Exception(f"Error during cloning: {str(e)}")


def validate_github_url(url: str) -> bool:
    """
    Validate GitHub URL format
    """
    valid_patterns = [
        "github.com",
        "https://github.com/",
        "git@github.com:"
    ]
    
    return any(pattern in url for pattern in valid_patterns)

# Made with Bob
