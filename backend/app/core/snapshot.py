"""
Snapshot and rollback functionality
Creates backups before migration and supports rollback
"""
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional
from app.utils.file_utils import get_project_path, copy_directory, delete_directory


class SnapshotManager:
    """Manage snapshots and rollbacks"""
    
    def __init__(self, project_id: str):
        self.project_id = project_id
        self.snapshot_path = get_project_path(project_id, "snapshots")
    
    async def create_snapshot(self, source_path: Path) -> str:
        """
        Create snapshot of project before migration
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_dir = self.snapshot_path / timestamp
        
        # Copy entire project
        copy_directory(source_path, snapshot_dir)
        
        return f"Snapshot created at {timestamp}"
    
    async def rollback(self, target_path: Path) -> bool:
        """
        Rollback to latest snapshot
        """
        # Find latest snapshot
        snapshots = sorted(self.snapshot_path.glob("*"), reverse=True)
        
        if not snapshots:
            raise Exception("No snapshots found for rollback")
        
        latest_snapshot = snapshots[0]
        
        # Delete current migrated version
        migrated_path = get_project_path(self.project_id, "migrated")
        if migrated_path.exists():
            delete_directory(migrated_path)
        
        # Restore from snapshot
        copy_directory(latest_snapshot, target_path)
        
        return True
    
    def list_snapshots(self) -> list:
        """
        List all available snapshots
        """
        if not self.snapshot_path.exists():
            return []
        
        snapshots = []
        for snapshot_dir in sorted(self.snapshot_path.glob("*"), reverse=True):
            snapshots.append({
                "timestamp": snapshot_dir.name,
                "path": str(snapshot_dir),
                "size": self._get_dir_size(snapshot_dir)
            })
        
        return snapshots
    
    def _get_dir_size(self, path: Path) -> int:
        """
        Calculate directory size in bytes
        """
        total = 0
        for item in path.rglob('*'):
            if item.is_file():
                total += item.stat().st_size
        return total
    
    async def cleanup_old_snapshots(self, keep_count: int = 3) -> None:
        """
        Keep only the latest N snapshots
        """
        snapshots = sorted(self.snapshot_path.glob("*"), reverse=True)
        
        # Delete old snapshots
        for snapshot in snapshots[keep_count:]:
            delete_directory(snapshot)

# Made with Bob
