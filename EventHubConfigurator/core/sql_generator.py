"""Wrapper for generate_event_files.py functionality"""

import sys
import os
from typing import Dict, List, Optional
from pathlib import Path

# Add parent directory to path to import the original script
_script_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_script_dir))

# Import the main function and necessary components
import generate_event_files


def generate_sql_files(
    config_path: str,
    output_dir: Optional[str] = None
) -> Dict:
    """
    Generate SQL files from a configuration CSV file.
    
    Args:
        config_path: Path to the configuration CSV file
        output_dir: Output directory (default: same as config file directory)
    
    Returns:
        Dictionary with:
            - 'success': bool
            - 'files': List of generated file paths
            - 'output_dir': Output directory path
            - 'error': Error message if failed
    """
    if not os.path.exists(config_path):
        return {
            'success': False,
            'files': [],
            'output_dir': output_dir or '',
            'error': f'Config file not found: {config_path}'
        }
    
    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(config_path))
    
    # Ensure config_path is absolute before changing directories
    config_path_abs = os.path.abspath(config_path)
    if not os.path.exists(config_path_abs):
        return {
            'success': False,
            'files': [],
            'output_dir': output_dir or '',
            'error': f'Config file not found: {config_path_abs}'
        }
    
    # Change to output directory temporarily to match script behavior
    original_cwd = os.getcwd()
    try:
        os.chdir(output_dir)
        
        # Import necessary functions directly
        from generate_event_files import (
            load_config, PRIMARY_LOCATIONS, get_position_generator_id,
            generate_position_generator, generate_wave_controller,
            generate_controller, generate_exit_controller, WEENIE_IDS
        )
        
        # Load config using absolute path (works regardless of current directory)
        config = load_config(config_path_abs)
        
        generated_files = []
        
        # Process each tier
        for tier in ['low', 'mid', 'high']:
            if tier not in config:
                continue
            
            tier_dir = f"{tier.capitalize()} Event Sequence"
            os.makedirs(tier_dir, exist_ok=True)
            
            tier_data = WEENIE_IDS[tier]
            wave_controller_ids = []
            
            # Calculate central point
            if PRIMARY_LOCATIONS:
                base_cell = PRIMARY_LOCATIONS[0][0]
                avg_x = sum(loc[1] for loc in PRIMARY_LOCATIONS) / len(PRIMARY_LOCATIONS)
                avg_y = sum(loc[2] for loc in PRIMARY_LOCATIONS) / len(PRIMARY_LOCATIONS)
                avg_z = sum(loc[3] for loc in PRIMARY_LOCATIONS) / len(PRIMARY_LOCATIONS)
                central_point = (base_cell, avg_x, avg_y, avg_z)
            else:
                central_point = (0x02BF010D, 29.7, -29.5, 0.005)
            
            # Generate waves 1-10
            for wave_num in range(1, 11):
                wave_key = str(wave_num)
                if wave_key not in config[tier]:
                    continue
                
                position_assignments = config[tier][wave_key]
                if len(position_assignments) == 0:
                    continue
                
                wave_name = f"{tier.capitalize()} Event Wave {wave_num}"
                wave_controller_id = tier_data['waves'][wave_num - 1]
                position_generator_ids = []
                
                # Generate 4 Position Generators
                for position_index in range(4):
                    position_assignment = None
                    for pos_idx, wcid, spawn_count in position_assignments:
                        if pos_idx == position_index:
                            position_assignment = (wcid, spawn_count)
                            break
                    
                    if position_assignment is None:
                        continue
                    
                    wcid, spawn_count = position_assignment
                    position_gen_id = get_position_generator_id(tier, wave_num, position_index)
                    position_name = f"{wave_name} Position {position_index}"
                    location = PRIMARY_LOCATIONS[position_index]
                    
                    sql = generate_position_generator(position_gen_id, position_name, wcid, spawn_count, location)
                    filename = os.path.join(tier_dir, f"{position_gen_id} {position_name} Generator.sql")
                    
                    with open(filename, 'w') as f:
                        f.write(sql)
                    
                    generated_files.append(filename)
                    position_generator_ids.append(position_gen_id)
                
                # Generate Wave Controller
                if len(position_generator_ids) == 4:
                    sql = generate_wave_controller(wave_controller_id, wave_name, position_generator_ids, wave_num)
                    filename = os.path.join(tier_dir, f"{wave_controller_id} {wave_name} Controller.sql")
                    
                    with open(filename, 'w') as f:
                        f.write(sql)
                    
                    generated_files.append(filename)
                    wave_controller_ids.append(wave_controller_id)
            
            # Generate boss wave
            boss_key = 'boss'
            if boss_key in config[tier]:
                position_assignments = config[tier][boss_key]
                if len(position_assignments) > 0:
                    boss_name = f"{tier.capitalize()} Event Boss"
                    boss_controller_id = tier_data['boss']
                    position_generator_ids = []
                    
                    for position_index in range(4):
                        position_assignment = None
                        for pos_idx, wcid, spawn_count in position_assignments:
                            if pos_idx == position_index:
                                position_assignment = (wcid, spawn_count)
                                break
                        
                        if position_assignment is None:
                            continue
                        
                        wcid, spawn_count = position_assignment
                        position_gen_id = get_position_generator_id(tier, 11, position_index)
                        position_name = f"{boss_name} Position {position_index}"
                        location = PRIMARY_LOCATIONS[position_index]
                        
                        sql = generate_position_generator(position_gen_id, position_name, wcid, spawn_count, location)
                        filename = os.path.join(tier_dir, f"{position_gen_id} {position_name} Generator.sql")
                        
                        with open(filename, 'w') as f:
                            f.write(sql)
                        
                        generated_files.append(filename)
                        position_generator_ids.append(position_gen_id)
                    
                    if len(position_generator_ids) == 4:
                        sql = generate_wave_controller(boss_controller_id, boss_name, position_generator_ids, 11)
                        filename = os.path.join(tier_dir, f"{boss_controller_id} {boss_name} Controller.sql")
                        
                        with open(filename, 'w') as f:
                            f.write(sql)
                        
                        generated_files.append(filename)
                        wave_controller_ids.append(boss_controller_id)
            
            # Generate controller
            controller_id = tier_data['controller']
            controller_name = f"{tier.capitalize()} Event Controller"
            
            sql = generate_controller(tier, wave_controller_ids, central_point)
            filename = os.path.join(tier_dir, f"{controller_id} {controller_name}.sql")
            
            with open(filename, 'w') as f:
                f.write(sql)
            
            generated_files.append(filename)
        
        # Generate exit controller
        sql = generate_exit_controller()
        filename = "694200295 Event Exit Controller.sql"
        
        with open(filename, 'w') as f:
            f.write(sql)
        
        generated_files.append(filename)
        
        return {
            'success': True,
            'files': generated_files,
            'output_dir': output_dir,
            'error': None
        }
    except Exception as e:
        import traceback
        return {
            'success': False,
            'files': [],
            'output_dir': output_dir or '',
            'error': f"{str(e)}\n{traceback.format_exc()}"
        }
    finally:
        os.chdir(original_cwd)
