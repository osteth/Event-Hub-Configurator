"""Configuration file management utilities"""

import csv
import os
from typing import List, Dict, Optional


def load_config(csv_file: str) -> Dict[str, Dict[str, List[tuple]]]:
    """
    Load event configuration from CSV file.
    
    Returns: {tier: {wave_num: [(position_index, wcid, spawn_count), ...]}}
    """
    from collections import defaultdict
    config = defaultdict(lambda: defaultdict(list))
    
    if not os.path.exists(csv_file):
        return config
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tier = row['tier'].lower()
            wave_num = str(row['wave_number'])
            
            if 'position_index' in row and 'spawn_count' in row:
                position_index = int(row['position_index'])
                wcid = int(row['wcid'])
                spawn_count = int(row['spawn_count'])
                
                config[tier][wave_num].append((position_index, wcid, spawn_count))
    
    # Sort position assignments by position_index for each wave
    for tier in config:
        for wave_num in config[tier]:
            config[tier][wave_num].sort(key=lambda x: x[0])
    
    return config


def save_config(config: Dict[str, Dict[str, List[tuple]]], csv_file: str):
    """
    Save event configuration to CSV file.
    
    Args:
        config: Configuration dict {tier: {wave_num: [(position_index, wcid, spawn_count), ...]}}
        csv_file: Output CSV file path
    """
    # Ensure directory exists
    output_dir = os.path.dirname(csv_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    rows = []
    for tier in ['low', 'mid', 'high']:
        if tier not in config:
            continue
        
        for wave_num in sorted(config[tier].keys(), key=lambda x: (x == 'boss', int(x) if x.isdigit() else 0)):
            for position_index, wcid, spawn_count in config[tier][wave_num]:
                rows.append({
                    'tier': tier,
                    'wave_number': wave_num,
                    'position_index': position_index,
                    'wcid': wcid,
                    'spawn_count': spawn_count
                })
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['tier', 'wave_number', 'position_index', 'wcid', 'spawn_count'])
        writer.writeheader()
        writer.writerows(rows)
