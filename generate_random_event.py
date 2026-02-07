#!/usr/bin/env python3
"""
Random Event Configuration Generator
Generates random event configurations from Spawnable Mobs List
"""

import csv
import random
import argparse
import sys
import os
from collections import defaultdict
from typing import Dict, List, Tuple


def load_mob_spawn_data(csv_path: str = 'Spawnable Mobs List.csv') -> Dict[int, int]:
    """Load mob spawn data from CSV file. Returns dict mapping WCID to max spawns per location."""
    spawn_map = {}
    mapping_file = os.path.join(os.path.dirname(__file__), csv_path)
    
    if os.path.exists(mapping_file):
        with open(mapping_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                wcid_str = row.get('ID', '').strip()
                if wcid_str and wcid_str.isdigit():
                    wcid = int(wcid_str)
                    spawns_per_location_str = row.get('Spawns Per Location', '') or ''
                    spawns_per_location_str = spawns_per_location_str.strip() if spawns_per_location_str else ''
                    if spawns_per_location_str and spawns_per_location_str.isdigit():
                        spawn_map[wcid] = int(spawns_per_location_str)
                    else:
                        # Default to 1 if not specified
                        spawn_map[wcid] = 1
    else:
        print(f"Warning: Spawnable Mobs List file not found: {mapping_file}")
        print("  Using default: all mobs can spawn 1 per location")
    
    return spawn_map


def load_spawnable_mobs(csv_file: str = 'Spawnable Mobs List.csv') -> Dict[str, Dict[str, List[Tuple[int, str]]]]:
    """
    Load and categorize spawnable mobs by difficulty and boss status.
    Returns: {difficulty: {'boss': [(id, name), ...], 'regular': [(id, name), ...]}}
    """
    mobs = {
        'Low': {'boss': [], 'regular': []},
        'Mid': {'boss': [], 'regular': []},
        'High': {'boss': [], 'regular': []}
    }
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Skip rows with empty IDs
                mob_id = row.get('ID', '').strip()
                if not mob_id:
                    continue
                
                try:
                    mob_id = int(mob_id)
                except ValueError:
                    continue
                
                name = row.get('Name', 'Unknown').strip()
                difficulty = row.get('Difficulty', '').strip()
                is_boss = row.get('Difficulty (eg: boss)', '').strip().upper() == 'TRUE'
                
                # Categorize by difficulty
                if difficulty in mobs:
                    if is_boss:
                        mobs[difficulty]['boss'].append((mob_id, name))
                    else:
                        mobs[difficulty]['regular'].append((mob_id, name))
    
    except FileNotFoundError:
        print(f"Error: Could not find '{csv_file}'")
        sys.exit(1)
    
    return mobs


def generate_wave(mobs: List[Tuple[int, str]], mixed: bool = False) -> List[int]:
    """
    Generate a wave of 10 monster slots.
    
    Args:
        mobs: List of (id, name) tuples to choose from
        mixed: If True, randomly mix different mobs; if False, use same mob for all slots
    
    Returns:
        List of 10 mob IDs
    """
    if not mobs:
        raise ValueError("No mobs available to generate wave")
    
    if mixed:
        # Randomly select different mobs for each slot
        return [random.choice(mobs)[0] for _ in range(10)]
    else:
        # Select one mob and use for all 10 slots
        selected_mob = random.choice(mobs)
        return [selected_mob[0]] * 10


def generate_boss_wave(boss_mobs: List[Tuple[int, str]], 
                      regular_mobs: List[Tuple[int, str]], 
                      boss_count: int = 1,
                      mixed: bool = False) -> List[int]:
    """
    Generate a boss wave with specified number of bosses and regular mobs.
    
    Args:
        boss_mobs: List of boss (id, name) tuples
        regular_mobs: List of regular (id, name) tuples
        boss_count: Number of boss mobs in the wave
        mixed: If True, use different regular mobs; if False, use same regular mob
    
    Returns:
        List of 10 mob IDs (boss_count bosses + remaining regular mobs)
    """
    if not boss_mobs:
        raise ValueError("No boss mobs available for boss wave")
    if not regular_mobs:
        raise ValueError("No regular mobs available for boss wave")
    if boss_count < 1 or boss_count > 10:
        raise ValueError("Boss count must be between 1 and 10")
    
    wave = []
    
    # Add boss mobs
    if boss_count == 1:
        # Single boss
        wave.append(random.choice(boss_mobs)[0])
    else:
        # Multiple bosses - can be same or different
        for _ in range(boss_count):
            wave.append(random.choice(boss_mobs)[0])
    
    # Fill remaining slots with regular mobs
    remaining_slots = 10 - boss_count
    if mixed:
        # Different regular mobs
        for _ in range(remaining_slots):
            wave.append(random.choice(regular_mobs)[0])
    else:
        # Same regular mob for all remaining slots
        selected_regular = random.choice(regular_mobs)[0]
        wave.extend([selected_regular] * remaining_slots)
    
    return wave


def generate_event_config(mobs: Dict[str, Dict[str, List[Tuple[int, str]]]], 
                         spawn_data: Dict[int, int],
                         tiers: List[str],
                         mixed_waves: bool = False,
                         boss_count: int = 1) -> List[Dict[str, any]]:
    """
    Generate complete event configuration with position assignments and spawn counts.
    
    Args:
        mobs: Categorized mobs dictionary
        spawn_data: Dict mapping WCID to max spawns per location
        tiers: List of tiers to generate ('low', 'mid', 'high')
        mixed_waves: Whether to mix different mobs in each wave
        boss_count: Number of bosses in boss wave
    
    Returns:
        List of configuration rows with position_index and spawn_count
    """
    config = []
    NUM_PRIMARY_POSITIONS = 4
    
    for tier in tiers:
        tier_cap = tier.capitalize()
        
        # Check if we have mobs for this tier
        if not mobs[tier_cap]['regular']:
            print(f"Warning: No regular mobs found for {tier} tier, skipping...")
            continue
        if not mobs[tier_cap]['boss']:
            print(f"Warning: No boss mobs found for {tier} tier, skipping...")
            continue
        
        print(f"\nGenerating {tier.upper()} tier:")
        print(f"  Available regular mobs: {len(mobs[tier_cap]['regular'])}")
        print(f"  Available boss mobs: {len(mobs[tier_cap]['boss'])}")
        
        # Generate 10 regular waves
        for wave_num in range(1, 11):
            # Get unique mob types for this wave
            if mixed_waves:
                # For mixed waves, get 4 different mobs (one per position)
                unique_mobs = [random.choice(mobs[tier_cap]['regular'])[0] for _ in range(NUM_PRIMARY_POSITIONS)]
            else:
                # For same-mob waves, pick 4 different mobs (one per position)
                # The "same mob per wave" mode means the same set of mobs across waves, not same mob in all positions
                unique_mobs = [random.choice(mobs[tier_cap]['regular'])[0] for _ in range(NUM_PRIMARY_POSITIONS)]
            
            # Assign one mob type to each of the 4 primary positions
            for position_index in range(NUM_PRIMARY_POSITIONS):
                # Each position gets a different mob type
                mob_type = unique_mobs[position_index]
                
                # Get max spawns per location for this mob type
                max_spawns_for_mob = spawn_data.get(mob_type, 1)
                if max_spawns_for_mob <= 0:
                    max_spawns_for_mob = 1
                
                # Random spawn count for this position (1 to max_spawns_for_mob)
                spawn_count = random.randint(1, max_spawns_for_mob)
                
                config.append({
                    'tier': tier,
                    'wave_number': wave_num,
                    'position_index': position_index,
                    'wcid': mob_type,
                    'spawn_count': spawn_count
                })
            
            print(f"  [OK] Wave {wave_num} generated")
        
        # Generate boss wave
        # Assign bosses and regular mobs to positions
        boss_mobs = [m[0] for m in mobs[tier_cap]['boss']]
        regular_mobs = [m[0] for m in mobs[tier_cap]['regular']]
        
        # Assign bosses to first N positions
        for position_index in range(min(boss_count, NUM_PRIMARY_POSITIONS)):
            boss_type = random.choice(boss_mobs)
            max_spawns_for_boss = spawn_data.get(boss_type, 1)
            if max_spawns_for_boss <= 0:
                max_spawns_for_boss = 1
            spawn_count = random.randint(1, max_spawns_for_boss)
            
            config.append({
                'tier': tier,
                'wave_number': 'boss',
                'position_index': position_index,
                'wcid': boss_type,
                'spawn_count': spawn_count
            })
        
        # Fill remaining positions with regular mobs
        for position_index in range(boss_count, NUM_PRIMARY_POSITIONS):
            regular_type = random.choice(regular_mobs)
            max_spawns_for_regular = spawn_data.get(regular_type, 1)
            if max_spawns_for_regular <= 0:
                max_spawns_for_regular = 1
            spawn_count = random.randint(1, max_spawns_for_regular)
            
            config.append({
                'tier': tier,
                'wave_number': 'boss',
                'position_index': position_index,
                'wcid': regular_type,
                'spawn_count': spawn_count
            })
        
        print(f"  [OK] Boss wave generated ({boss_count} boss(es) + {NUM_PRIMARY_POSITIONS-boss_count} regular)")
    
    return config


def write_config_csv(config: List[Dict[str, any]], output_file: str):
    """Write configuration to CSV file with position assignments."""
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['tier', 'wave_number', 'position_index', 'wcid', 'spawn_count'])
        writer.writeheader()
        writer.writerows(config)
    
    print(f"\n[SUCCESS] Configuration written to: {output_file}")
    print(f"   Total rows: {len(config)}")


def print_summary(config: List[Dict[str, any]]):
    """Print summary of generated configuration."""
    tiers = set(row['tier'] for row in config)
    print(f"\n[SUMMARY] Summary:")
    print(f"   Tiers generated: {', '.join(sorted(tiers))}")
    print(f"   Total waves per tier: 11 (10 regular + 1 boss)")
    print(f"   Total monsters per wave: 10")
    print(f"   Total configuration entries: {len(config)}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate random event configuration from Spawnable Mobs List',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all tiers with same-mob waves (default)
  python generate_random_event.py
  
  # Generate only low and mid tiers
  python generate_random_event.py --tiers low mid
  
  # Generate with mixed mobs per wave
  python generate_random_event.py --mixed-waves
  
  # Generate high tier only with custom output
  python generate_random_event.py -t high -o high_event.csv
  
  # Boss wave with 3 bosses instead of 1
  python generate_random_event.py --boss-count 3
  
  # Full randomization for all tiers
  python generate_random_event.py -t all -m -o random_mixed_event.csv
        """
    )
    
    parser.add_argument(
        '--tiers', '-t',
        nargs='+',
        choices=['low', 'mid', 'high', 'all'],
        default=['all'],
        help='Which tier(s) to generate (default: all)'
    )
    
    parser.add_argument(
        '--mixed-waves', '-m',
        action='store_true',
        help='Mix different mobs in each wave (default: same mob per wave)'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='random_event.csv',
        help='Output CSV filename (default: random_event.csv)'
    )
    
    parser.add_argument(
        '--boss-count',
        type=int,
        default=1,
        choices=range(1, 11),
        metavar='COUNT',
        help='Number of bosses in boss wave (default: 1, max: 10)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducible results'
    )
    
    parser.add_argument(
        '--mobs-file',
        default='Spawnable Mobs List.csv',
        help='Path to spawnable mobs CSV (default: Spawnable Mobs List.csv)'
    )
    
    args = parser.parse_args()
    
    # Set random seed if provided
    if args.seed:
        random.seed(args.seed)
        print(f"🎲 Using random seed: {args.seed}")
    
    # Handle 'all' tiers
    if 'all' in args.tiers:
        tiers = ['low', 'mid', 'high']
    else:
        tiers = args.tiers
    
    print("=" * 60)
    print("Random Event Configuration Generator")
    print("=" * 60)
    print(f"\n[CONFIG] Configuration:")
    print(f"   Tiers: {', '.join(tiers)}")
    print(f"   Wave mode: {'Mixed mobs' if args.mixed_waves else 'Same mob per wave'}")
    print(f"   Boss wave: {args.boss_count} boss(es) + {10-args.boss_count} regular mob(s)")
    print(f"   Output file: {args.output}")
    
    # Load spawnable mobs
    print(f"\n[LOAD] Loading mobs from: {args.mobs_file}")
    mobs = load_spawnable_mobs(args.mobs_file)
    
    # Load spawn data for position assignments
    spawn_data = load_mob_spawn_data(args.mobs_file)
    
    # Generate configuration
    config = generate_event_config(mobs, spawn_data, tiers, args.mixed_waves, args.boss_count)
    
    if not config:
        print("\n[ERROR] No configuration generated. Check your spawnable mobs file.")
        sys.exit(1)
    
    # Write to CSV
    write_config_csv(config, args.output)
    
    # Print summary
    print_summary(config)
    
    print(f"\n[NEXT] Next step: Run 'python generate_event_files.py {args.output}' to create SQL files")
    print("=" * 60)


if __name__ == '__main__':
    main()
