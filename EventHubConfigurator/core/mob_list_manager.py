"""Mob list management - CSV read/write functionality"""

import csv
import os
from typing import List, Dict, Optional


def load_mob_list(csv_path: str) -> List[Dict]:
    """
    Load mob list from CSV file.
    
    Args:
        csv_path: Path to Spawnable Mobs List.csv
    
    Returns:
        List of dictionaries with keys: 'ID', 'Name', 'Difficulty', 'Boss', 'Spawns Per Location'
    """
    mobs = []
    
    if not os.path.exists(csv_path):
        return mobs
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Skip rows with empty ID
                id_str = row.get('ID', '').strip()
                if not id_str:
                    continue
                
                try:
                    mob_id = int(id_str)
                except ValueError:
                    # Skip rows with invalid ID
                    continue
                
                # Handle Spawns Per Location - default to 1 if empty or invalid
                spawns_str = row.get('Spawns Per Location', '1').strip()
                if not spawns_str:
                    spawns_str = '1'
                try:
                    spawns = int(spawns_str)
                    if spawns < 1:
                        spawns = 1
                except ValueError:
                    spawns = 1
                
                mob = {
                    'ID': mob_id,
                    'Name': row.get('Name', '').strip(),
                    'Difficulty': row.get('Difficulty', '').strip(),
                    'Boss': row.get('Difficulty (eg: boss)', '').strip().upper() == 'TRUE',
                    'Spawns Per Location': spawns
                }
                mobs.append(mob)
    except Exception as e:
        raise Exception(f"Error loading mob list: {e}")
    
    return mobs


def save_mob_list(mobs: List[Dict], csv_path: str):
    """
    Save mob list to CSV file.
    
    Args:
        mobs: List of mob dictionaries
        csv_path: Path to save the CSV file
    """
    # Ensure directory exists
    output_dir = os.path.dirname(csv_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    try:
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['ID', 'Name', 'Difficulty', 'Difficulty (eg: boss)', 'Spawns Per Location']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for mob in mobs:
                row = {
                    'ID': mob.get('ID', 0),
                    'Name': mob.get('Name', ''),
                    'Difficulty': mob.get('Difficulty', ''),
                    'Difficulty (eg: boss)': 'TRUE' if mob.get('Boss', False) else 'FALSE',
                    'Spawns Per Location': mob.get('Spawns Per Location', 1)
                }
                writer.writerow(row)
    except Exception as e:
        raise Exception(f"Error saving mob list: {e}")


def add_mob(mob_dict: Dict, csv_path: str):
    """
    Add a new mob to the CSV file.
    
    Args:
        mob_dict: Dictionary with mob data (ID, Name, Difficulty, Boss, Spawns Per Location)
        csv_path: Path to the CSV file
    """
    mobs = load_mob_list(csv_path)
    
    # Check for duplicate ID
    if any(m['ID'] == mob_dict['ID'] for m in mobs):
        raise ValueError(f"Mob with ID {mob_dict['ID']} already exists")
    
    mobs.append(mob_dict)
    save_mob_list(mobs, csv_path)


def update_mob(wcid: int, mob_dict: Dict, csv_path: str):
    """
    Update an existing mob in the CSV file.
    
    Args:
        wcid: WCID of the mob to update
        mob_dict: Updated mob data
        csv_path: Path to the CSV file
    """
    mobs = load_mob_list(csv_path)
    
    found = False
    for i, mob in enumerate(mobs):
        if mob['ID'] == wcid:
            mobs[i] = mob_dict
            found = True
            break
    
    if not found:
        raise ValueError(f"Mob with ID {wcid} not found")
    
    save_mob_list(mobs, csv_path)


def delete_mob(wcid: int, csv_path: str):
    """
    Delete a mob from the CSV file.
    
    Args:
        wcid: WCID of the mob to delete
        csv_path: Path to the CSV file
    """
    mobs = load_mob_list(csv_path)
    
    original_count = len(mobs)
    mobs = [m for m in mobs if m['ID'] != wcid]
    
    if len(mobs) == original_count:
        raise ValueError(f"Mob with ID {wcid} not found")
    
    save_mob_list(mobs, csv_path)
