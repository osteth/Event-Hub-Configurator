"""File operation utilities"""

import os
from pathlib import Path


def get_data_path(filename: str) -> str:
    """Get path to a file in the data directory.
    
    Priority:
    1. EventHubConfigurator/data/ (for packaged app)
    2. Parent directory (for development/testing)
    
    Returns the path to the file, creating data directory if needed.
    """
    # Get the application directory (EventHubConfigurator/)
    script_dir = Path(__file__).parent.parent.parent
    data_dir = script_dir / 'data'
    
    # Ensure data directory exists
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
    
    # Primary location: EventHubConfigurator/data/
    data_file = data_dir / filename
    if data_file.exists():
        return str(data_file)
    
    # Fallback to parent directory (for development when running from source)
    parent_dir = script_dir.parent
    fallback_path = parent_dir / filename
    if fallback_path.exists():
        # Copy to data directory for future use
        try:
            import shutil
            shutil.copy2(fallback_path, data_file)
            return str(data_file)
        except Exception:
            # If copy fails, just use the fallback
            return str(fallback_path)
    
    # Return expected path (will be created when needed)
    return str(data_file)


def get_default_config_path() -> str:
    """Get default path for saving config files."""
    script_dir = Path(__file__).parent.parent.parent.parent
    return str(script_dir.parent)


def open_file_location(file_path: str):
    """Open the folder containing the file in Windows Explorer."""
    import subprocess
    folder = os.path.dirname(os.path.abspath(file_path))
    subprocess.Popen(f'explorer "{folder}"')


def open_file_in_editor(file_path: str):
    """Open a file in the system's default text editor."""
    import subprocess
    os.startfile(file_path)
