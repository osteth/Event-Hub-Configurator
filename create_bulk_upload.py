#!/usr/bin/env python3
"""
Bulk Upload Generator for Event Hub SQL Files

This script combines all generated SQL files into a single bulk upload file
that can be executed on the ACE server.

Usage:
    python create_bulk_upload.py [output_file]
    
    If output_file is not specified, defaults to 'event_hub_bulk_upload.sql'
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def get_sql_files(base_dir):
    """Collect all SQL files in the expected order."""
    sql_files = []
    
    # Define the order we want files in
    file_order = [
        # Root directory files (bell, etc.)
        "694200294 Event Bell.sql",
        "694200295 Event Exit Controller.sql",
    ]
    
    # Define tier configurations
    tiers = [
        {
            'name': 'Low',
            'dir': 'Low Event Sequence',
            'controller_id': 694200293,
            'wave_ids': [694200310, 694200311, 694200312, 694200313, 694200314,
                         694200315, 694200316, 694200317, 694200318, 694200319],
            'boss_id': 694200320,
            'position_base': 694201299
        },
        {
            'name': 'Mid',
            'dir': 'Mid Event Sequence',
            'controller_id': 694200300,
            'wave_ids': [694200321, 694200322, 694200323, 694200324, 694200325,
                         694200326, 694200327, 694200328, 694200329, 694200330],
            'boss_id': 694200331,
            'position_base': 694201343
        },
        {
            'name': 'High',
            'dir': 'High Event Sequence',
            'controller_id': 694200304,
            'wave_ids': [694200332, 694200333, 694200334, 694200335, 694200336,
                         694200337, 694200338, 694200339, 694200340, 694200341],
            'boss_id': 694200342,
            'position_base': 694201387
        }
    ]
    
    # Build file order for each tier
    for tier in tiers:
        tier_dir = tier['dir']
        tier_name = tier['name']
        
        # For each wave (1-10)
        for wave_num in range(1, 11):
            wave_controller_id = tier['wave_ids'][wave_num - 1]
            position_base = tier['position_base'] + ((wave_num - 1) * 4)
            
            # Add Position Generators for this wave (positions 0-3)
            for pos in range(4):
                pos_gen_id = position_base + pos
                file_order.append(f"{tier_dir}/{pos_gen_id} {tier_name} Event Wave {wave_num} Position {pos} Generator.sql")
            
            # Add Wave Controller
            file_order.append(f"{tier_dir}/{wave_controller_id} {tier_name} Event Wave {wave_num} Controller.sql")
        
        # Boss wave (wave 11)
        boss_controller_id = tier['boss_id']
        boss_position_base = tier['position_base'] + (10 * 4)  # After 10 waves
        
        # Add Position Generators for boss (positions 0-3)
        for pos in range(4):
            pos_gen_id = boss_position_base + pos
            file_order.append(f"{tier_dir}/{pos_gen_id} {tier_name} Event Boss Position {pos} Generator.sql")
        
        # Add Boss Wave Controller
        file_order.append(f"{tier_dir}/{boss_controller_id} {tier_name} Event Boss Controller.sql")
        
        # Add Event Controller (after all waves)
        file_order.append(f"{tier_dir}/{tier['controller_id']} {tier_name} Event Controller.sql")
    
    # Find all SQL files that exist
    found_files = []
    for file_path in file_order:
        full_path = os.path.join(base_dir, file_path)
        if os.path.exists(full_path):
            found_files.append((file_path, full_path))
        else:
            print(f"Warning: {file_path} not found, skipping...", file=sys.stderr)
    
    return found_files

def read_sql_file(file_path):
    """Read a SQL file and return its contents."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return None

def create_bulk_upload(output_file, base_dir=None):
    """Create a bulk upload SQL file from all individual SQL files."""
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    sql_files = get_sql_files(base_dir)
    
    if not sql_files:
        print("No SQL files found!", file=sys.stderr)
        return False
    
    print(f"Found {len(sql_files)} SQL files to combine...")
    
    # Create the bulk upload file
    with open(output_file, 'w', encoding='utf-8') as out:
        # Write header
        out.write("-- ============================================\n")
        out.write("-- Event Hub Bulk Upload SQL File\n")
        out.write(f"-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out.write(f"-- Total Files: {len(sql_files)}\n")
        out.write("-- ============================================\n\n")
        out.write("-- This file contains all Event Hub weenies in the correct order.\n")
        out.write("-- Execute this file on your ACE server database.\n\n")
        
        # Process each file
        current_section = None
        for i, (relative_path, full_path) in enumerate(sql_files, 1):
            # Determine section for comments
            if "Event Hub Portal" in relative_path or "event portal" in relative_path:
                section = "Portals"
            elif "Event Bell" in relative_path:
                section = "Event Bell"
            elif "Exit Controller" in relative_path or "Reward Room" in relative_path:
                section = "Controllers"
            elif "Low Event" in relative_path:
                section = "Low Event Sequence"
            elif "Mid Event" in relative_path:
                section = "Mid Event Sequence"
            elif "High Event" in relative_path:
                section = "High Event Sequence"
            else:
                section = "Other"
            
            # Add section header if changed
            if section != current_section:
                out.write(f"\n-- ============================================\n")
                out.write(f"-- {section}\n")
                out.write(f"-- ============================================\n\n")
                current_section = section
            
            # Add file header
            out.write(f"-- File {i}/{len(sql_files)}: {relative_path}\n")
            out.write(f"-- {'=' * 60}\n")
            
            # Read and write file contents
            content = read_sql_file(full_path)
            if content:
                out.write(content)
                # Ensure file ends with newline
                if not content.endswith('\n'):
                    out.write('\n')
                out.write('\n')
            else:
                out.write(f"-- ERROR: Could not read file\n\n")
        
        # Write footer
        out.write("\n-- ============================================\n")
        out.write("-- End of Bulk Upload\n")
        out.write("-- ============================================\n")
    
    print(f"Bulk upload file created: {output_file}")
    print(f"Total files combined: {len(sql_files)}")
    return True

def main():
    """Main entry point."""
    # Get output file from command line or use default
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    else:
        # Generate descriptive filename with date
        date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"event_hub_random_event_{date_str}.sql"
    
    # Get the script's directory as base directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create bulk upload
    success = create_bulk_upload(output_file, script_dir)
    
    if success:
        print(f"\n[SUCCESS] Bulk upload file ready: {output_file}")
        print(f"\nTo use this file:")
        print(f"  1. Copy {output_file} to your server")
        print(f"  2. Execute it on your ACE database:")
        print(f"     mysql -u [username] -p [database] < {output_file}")
        print(f"     OR import via phpMyAdmin/HeidiSQL/etc.")
    else:
        print("\n[ERROR] Failed to create bulk upload file.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
