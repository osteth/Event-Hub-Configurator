"""Wrapper for generate_random_event.py functionality"""

import sys
import os
import random
from typing import List, Dict, Optional
from pathlib import Path

# Add parent directory to path to import the original script
_script_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_script_dir))

from generate_random_event import (
    load_spawnable_mobs,
    load_mob_spawn_data,
    generate_event_config,
    write_config_csv
)


def generate_random_event(
    tiers: List[str] = None,
    mixed_waves: bool = False,
    boss_count: int = 1,
    seed: Optional[int] = None,
    output_file: Optional[str] = None,
    mob_list_path: Optional[str] = None
) -> str:
    """
    Generate a random event configuration and save it to a CSV file.
    
    Args:
        tiers: List of tiers to generate ('low', 'mid', 'high', or ['all'])
        mixed_waves: If True, mix different mobs in each wave
        boss_count: Number of bosses in boss wave (1-10)
        seed: Random seed for reproducible results
        output_file: Output CSV file path (default: timestamped name)
        mob_list_path: Path to Spawnable Mobs List.csv (default: data/Spawnable Mobs List.csv)
    
    Returns:
        Path to the generated CSV file
    """
    if tiers is None:
        tiers = ['all']
    
    if 'all' in tiers:
        tiers = ['low', 'mid', 'high']
    
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Determine mob list path
    if mob_list_path is None:
        # Use the bundled data file from app directory
        from gui.utils.file_utils import get_data_path
        mob_list_path = get_data_path('Spawnable Mobs List.csv')
    
    # Load mob data
    mobs = load_spawnable_mobs(mob_list_path)
    spawn_data = load_mob_spawn_data(mob_list_path)
    
    # Generate configuration (function expects all tiers at once)
    config = generate_event_config(
        mobs=mobs,
        spawn_data=spawn_data,
        tiers=tiers,
        mixed_waves=mixed_waves,
        boss_count=boss_count
    )
    
    # Determine output file
    if output_file is None:
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(_script_dir, f'random_event_{timestamp}.csv')
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    # Write CSV file
    write_config_csv(config, output_file)
    
    return output_file
