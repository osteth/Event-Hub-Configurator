"""Wrapper for validate_sql.py functionality"""

import sys
import os
import importlib
from typing import Dict, List
from pathlib import Path

# Add parent directory to path to import the original script
_script_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_script_dir))

# Force fresh import by removing from cache if it exists
# This ensures we always get the latest version, not a cached one
if 'validate_sql' in sys.modules:
    del sys.modules['validate_sql']

# Import fresh
from validate_sql import SQLValidator


def validate_bulk_upload(file_path: str, validate_individual_files: bool = True) -> Dict:
    """
    Validate a bulk upload SQL file.
    
    Args:
        file_path: Path to the SQL file to validate
        validate_individual_files: If True, validate individual files first, then bulk upload
    
    Returns:
        Dictionary with:
            - 'success': bool
            - 'errors': List of error messages
            - 'warnings': List of warning messages
            - 'file_count': Number of files validated
            - 'error_count': Number of errors found
            - 'warning_count': Number of warnings found
    """
    if not os.path.exists(file_path):
        return {
            'success': False,
            'errors': [f'File not found: {file_path}'],
            'warnings': [],
            'file_count': 0,
            'error_count': 1,
            'warning_count': 0
        }
    
    validator = SQLValidator()
    validator.verbose = False
    
    # Verify we're using the updated validator by checking if it has the fix
    # The fix sets depth=1 and col_start=0 in _validate_insert
    import inspect
    source = inspect.getsource(validator._validate_insert)
    has_fix = 'depth = 1' in source and 'col_start = 0' in source
    
    if not has_fix:
        # This shouldn't happen, but log a warning
        import warnings
        warnings.warn("Validator may not have the column extraction fix applied!")
    
    is_valid = validator.validate_bulk_upload(file_path, validate_individual_files=validate_individual_files)
    
    return {
        'success': is_valid and validator.error_count == 0,
        'errors': validator.errors,
        'warnings': validator.warnings,
        'file_count': validator.file_count,
        'error_count': validator.error_count,
        'warning_count': len(validator.warnings)
    }
