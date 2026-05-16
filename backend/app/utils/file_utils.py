"""
File utility functions for Legacy Code Surgeon AI
"""
import os
import shutil
import zipfile
import uuid
from pathlib import Path
from typing import List, Optional


# Storage paths
BASE_DIR = Path(__file__).parent.parent
STORAGE_DIR = BASE_DIR / "storage"
UPLOADS_DIR = STORAGE_DIR / "uploads"
REPOS_DIR = STORAGE_DIR / "repos"
MIGRATED_DIR = STORAGE_DIR / "migrated"
SNAPSHOTS_DIR = STORAGE_DIR / "snapshots"

# Ensure directories exist
for directory in [UPLOADS_DIR, REPOS_DIR, MIGRATED_DIR, SNAPSHOTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def generate_project_id() -> str:
    """Generate unique project ID"""
    return str(uuid.uuid4())


def get_project_path(project_id: str, storage_type: str = "uploads") -> Path:
    """Get path for a project"""
    storage_map = {
        "uploads": UPLOADS_DIR,
        "repos": REPOS_DIR,
        "migrated": MIGRATED_DIR,
        "snapshots": SNAPSHOTS_DIR
    }
    return storage_map.get(storage_type, UPLOADS_DIR) / project_id


async def extract_zip(zip_path: Path, extract_to: Path) -> int:
    """
    Extract ZIP file to destination
    Returns number of files extracted
    """
    extract_to.mkdir(parents=True, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        file_count = len(zip_ref.namelist())
    
    return file_count


def should_ignore(path: Path) -> bool:
    """
    Check if path should be ignored during scanning
    """
    ignore_patterns = [
        'node_modules',
        '.git',
        'venv',
        '__pycache__',
        'target',
        'build',
        'dist',
        '.idea',
        '.vscode',
        '*.pyc',
        '*.class',
        '.DS_Store'
    ]
    
    path_str = str(path)
    for pattern in ignore_patterns:
        if pattern in path_str:
            return True
    return False


def scan_directory(directory: Path, extensions: Optional[List[str]] = None) -> List[Path]:
    """
    Recursively scan directory for files
    Optionally filter by extensions
    """
    files = []
    
    for item in directory.rglob('*'):
        if item.is_file() and not should_ignore(item):
            if extensions:
                if item.suffix in extensions:
                    files.append(item)
            else:
                files.append(item)
    
    return files


def copy_directory(src: Path, dst: Path) -> None:
    """
    Copy entire directory tree
    """
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def delete_directory(path: Path) -> None:
    """
    Delete directory and all contents
    """
    if path.exists():
        shutil.rmtree(path)


def read_file_content(file_path: Path) -> str:
    """
    Read file content safely
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"# Error reading file: {str(e)}"


def write_file_content(file_path: Path, content: str) -> None:
    """
    Write content to file
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def get_relative_path(file_path: Path, base_path: Path) -> str:
    """
    Get relative path from base
    """
    try:
        return str(file_path.relative_to(base_path))
    except ValueError:
        return str(file_path)

# Made with Bob
