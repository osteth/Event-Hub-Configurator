"""Wrapper for create_bulk_upload.py functionality"""

import sys
import os
from typing import Optional
from pathlib import Path

# Add parent directory to path to import the original script
_script_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_script_dir))

from create_bulk_upload import create_bulk_upload, get_sql_files


def create_bulk_upload_file(
    sql_dir: Optional[str] = None,
    output_file: Optional[str] = None
) -> str:
    """
    Create a bulk upload SQL file from all SQL files in the directory.
    
    Args:
        sql_dir: Directory containing SQL files (default: current directory)
        output_file: Output file path (default: timestamped name)
    
    Returns:
        Path to the created bulk upload file
    """
    if sql_dir is None:
        sql_dir = _script_dir
    
    if output_file is None:
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(sql_dir, f'event_hub_random_event_{timestamp}.sql')
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # Ensure sql_dir is absolute
    sql_dir_abs = os.path.abspath(sql_dir)
    if not os.path.exists(sql_dir_abs):
        raise Exception(f"SQL directory does not exist: {sql_dir_abs}")
    
    # Ensure output_file is absolute
    if not os.path.isabs(output_file):
        output_file = os.path.join(sql_dir_abs, output_file)
    
    # Change to SQL directory to match script behavior
    original_cwd = os.getcwd()
    try:
        os.chdir(sql_dir_abs)
        success = create_bulk_upload(output_file, sql_dir_abs)
        
        if not success:
            raise Exception("Failed to create bulk upload file")
        
        return output_file
    except Exception as e:
        import traceback
        raise Exception(f"Error creating bulk upload: {str(e)}\n{traceback.format_exc()}")
    finally:
        os.chdir(original_cwd)
