#!/usr/bin/env python3
"""
Asheron's Call ACE Event Generator
Generates SQL weenie files for multi-tier events from CSV configuration
"""

import csv
import os
import sys
import random
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Optional


# Load mob spawn data from Spawnable Mobs List.csv
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
                        # Default to 1 if not specified (safer - prevents infinite loops)
                        spawn_map[wcid] = 1
    else:
        print(f"Warning: Spawnable Mobs List file not found: {mapping_file}")
        print("  Using default: all mobs can spawn 1 per location")
    
    return spawn_map

# Load spawn data at module level
MOB_SPAWN_DATA = load_mob_spawn_data()

# High-ceiling spawn locations - one primary location from each of the 4 main areas
# Format: (cell_id, x, y, z, angles_w, angles_x, angles_y, angles_z)
PRIMARY_LOCATIONS = [
    # Location 1 - 0x02BF010D
    (0x02BF010D, 15.039770, -45.088928, 0.005000, 0.939595, 0.0, 0.0, -0.342288),
    # Location 2 - 0x02BF0116
    (0x02BF0116, 44.864212, -43.889206, 0.005000, 0.899738, 0.0, 0.0, 0.436431),
    # Location 3 - 0x02BF0113
    (0x02BF0113, 44.843174, -14.990232, 0.005000, 0.384014, 0.0, 0.0, 0.923327),
    # Location 4 - 0x02BF0104 (updated from 0x02BF0103 to match actual spawn location)
    (0x02BF0104, 14.955328, -15.005316, 0.005000, -0.421018, 0.0, 0.0, 0.907052),
]

# Weenie ID mappings from Event Hub Weenie ID's.md
WEENIE_IDS = {
    'event_bell': 694200294,
    'exit_controller': 694200295,
    'low': {
        'controller': 694200293,
        'waves': [694200310, 694200311, 694200312, 694200313, 694200314, 
                  694200315, 694200316, 694200317, 694200318, 694200319],
        'boss': 694200320
    },
    'mid': {
        'controller': 694200300,
        'waves': [694200321, 694200322, 694200323, 694200324, 694200325,
                  694200326, 694200327, 694200328, 694200329, 694200330],
        'boss': 694200331
    },
    'high': {
        'controller': 694200304,
        'waves': [694200332, 694200333, 694200334, 694200335, 694200336,
                  694200337, 694200338, 694200339, 694200340, 694200341],
        'boss': 694200342
    }
}


def load_config(csv_file: str) -> Dict[str, Dict[str, List[Tuple[int, int, int]]]]:
    """
    Load event configuration from CSV file with position assignments.
    Returns: {tier: {wave_num: [(position_index, wcid, spawn_count), ...]}}
    """
    config = defaultdict(lambda: defaultdict(list))
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tier = row['tier'].lower()
            wave_num = str(row['wave_number'])  # Keep as string to handle 'boss'
            
            # Check if this is the new format (with position_index and spawn_count)
            if 'position_index' in row and 'spawn_count' in row:
                position_index = int(row['position_index'])
                wcid = int(row['wcid'])
                spawn_count = int(row['spawn_count'])
                
                config[tier][wave_num].append((position_index, wcid, spawn_count))
            else:
                # Legacy format support: slot-based
                # Convert to new format by assigning to positions
                slot = int(row['slot'])
                wcid = int(row['wcid'])
                
                # Map slot to position (4 positions, distribute slots evenly)
                position_index = (slot - 1) % 4
                # Default spawn count of 1 for legacy format
                spawn_count = 1
                
                config[tier][wave_num].append((position_index, wcid, spawn_count))
    
    # Sort position assignments by position_index for each wave
    for tier in config:
        for wave_num in config[tier]:
            config[tier][wave_num].sort(key=lambda x: x[0])
    
    return config


def get_position_generator_id(tier: str, wave_num: int, position_index: int) -> int:
    """Calculate position generator weenie ID based on tier, wave number, and position.
    
    Args:
        tier: Tier name ('low', 'mid', 'high')
        wave_num: Wave number (1-10 for regular waves, 11 for boss)
        position_index: Position index (0-3)
    
    Returns:
        Position generator weenie ID
    """
    base_id = 694201299
    tier_offsets = {'low': 0, 'mid': 44, 'high': 88}
    tier_offset = tier_offsets.get(tier.lower(), 0)
    
    # Calculate: base + tier_offset + (wave-1)*4 + position
    return base_id + tier_offset + ((wave_num - 1) * 4) + position_index


def generate_position_generator(weenie_id: int, position_name: str, wcid: int, spawn_count: int, location: Tuple) -> str:
    """Generate SQL for a single position generator.
    
    Args:
        weenie_id: The weenie ID for this position generator
        position_name: Name of the position (e.g., "Low Event Wave 1 Position 0")
        wcid: Mob weenie class ID to spawn
        spawn_count: Number of mobs to spawn at this position
        location: Tuple of (cell_id, x, y, z, angles_w, angles_x, angles_y, angles_z)
    
    Returns:
        SQL string for the position generator
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cell_id, x, y, z, w, x_ang, y_ang, z_ang = location
    
    # Validate spawn count against max_spawns_per_location
    max_spawns_for_mob = MOB_SPAWN_DATA.get(wcid, 1)
    if max_spawns_for_mob <= 0:
        max_spawns_for_mob = 1
    
    # Cap spawn count to the actual limit
    if spawn_count > max_spawns_for_mob:
        print(f"Warning: {position_name} (WCID {wcid}) has spawn_count {spawn_count} but max is {max_spawns_for_mob}. Capping to {max_spawns_for_mob}.")
        spawn_count = max_spawns_for_mob
    
    sql = f"""DELETE FROM `weenie` WHERE `class_Id` = {weenie_id};

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES ({weenie_id}, '{position_name} Generator', 1, '{timestamp}') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},  81, {spawn_count:>10}) /* MaxGeneratedObjects */
     , ({weenie_id},  82, {spawn_count:>10}) /* InitGeneratedObjects */
     , ({weenie_id},  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , ({weenie_id}, 103,          2) /* GeneratorDestructionType - Destroy */
     , ({weenie_id}, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, True ) /* Stuck */
     , ({weenie_id},  11, True ) /* IgnoreCollisions */
     , ({weenie_id},  18, True ) /* Visibility */
     , ({weenie_id},  59, False ) /* GeneratorDisabled - Enable generator on creation */
     , ({weenie_id},  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all mobs are killed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},  41,      15) /* RegenerationInterval */
     , ({weenie_id},  43,       5) /* GeneratorRadius - Tight scatter around position */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, '{position_name} Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, 0x0200026B) /* Setup */
     , ({weenie_id},   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES ({weenie_id}, -1, {wcid:>10}, 1, {spawn_count:>2}, {spawn_count:>2}, 1, 2, -1, 0, 0, 0, 0.000000, 0.000000, 0.000000, {w:>10.6f}, {x_ang:>6.1f}, {y_ang:>6.1f}, {z_ang:>10.6f}); /* Generate Monster - Scatter around generator location */

"""
    
    return sql


def generate_wave_controller(weenie_id: int, wave_name: str, position_generator_ids: List[int], wave_num: int = 1) -> str:
    """Generate SQL for a wave controller that spawns 4 Position Generators.
    
    Args:
        weenie_id: The weenie ID for this wave controller
        wave_name: Name of the wave
        position_generator_ids: List of 4 position generator weenie IDs (one per position)
        wave_num: Wave number for progression
    
    Returns:
        SQL string for the wave controller
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    wave_signal = f"Wave{wave_num}"
    
    if len(position_generator_ids) != 4:
        raise ValueError(f"Wave {wave_name} must have exactly 4 position generator IDs")
    
    sql = f"""DELETE FROM `weenie` WHERE `class_Id` = {weenie_id};

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES ({weenie_id}, '{wave_name} Controller', 10, '{timestamp}') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1,         16) /* ItemType - Creature */
     , ({weenie_id},   2,         31) /* CreatureType - Human */
     , ({weenie_id},   6,         -1) /* ItemsCapacity */
     , ({weenie_id},   7,         -1) /* ContainersCapacity */
     , ({weenie_id},  16,          1) /* ItemUseable - No */
     , ({weenie_id},  25,        275) /* Level */
     , ({weenie_id},  81,          4) /* MaxGeneratedObjects - One per position */
     , ({weenie_id},  82,          4) /* InitGeneratedObjects - Spawn all 4 Position Generators immediately when Wave Controller spawns */
     , ({weenie_id},  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , ({weenie_id}, 103,          2) /* GeneratorDestructionType - Destroy */
     , ({weenie_id}, 113,          1) /* Gender - Male */
     , ({weenie_id}, 133,          1) /* ShowableOnRadar - ShowNever */
     , ({weenie_id}, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , ({weenie_id}, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , ({weenie_id}, 188,          1) /* HeritageGroup - Aluvian */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, True ) /* Stuck */
     , ({weenie_id},  13, True ) /* Ethereal */
     , ({weenie_id},  18, False ) /* Visibility - Invisible */
     , ({weenie_id},  19, False) /* Attackable */
     , ({weenie_id},  52, True ) /* AiImmobile */
     , ({weenie_id},  59, False ) /* GeneratorDisabled - Keep enabled, InitGeneratedObjects=0 prevents initial spawn */
     , ({weenie_id},  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all position generators are destroyed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1,       5) /* HeartbeatInterval */
     , ({weenie_id},   2,       0) /* HeartbeatTimestamp */
     , ({weenie_id},   3,     0.9) /* HealthRate */
     , ({weenie_id},   4,       4) /* StaminaRate */
     , ({weenie_id},   5,       2) /* ManaRate */
     , ({weenie_id},  41,       5) /* RegenerationInterval */
     , ({weenie_id},  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, '{wave_name} Controller') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, 0x02000001) /* Setup */
     , ({weenie_id},   2, 0x09000001) /* MotionTable */
     , ({weenie_id},   3, 0x20000001) /* SoundTable */
     , ({weenie_id},   6, 0x0400007E) /* PaletteBase */
     , ({weenie_id},   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES ({weenie_id},   1, 240, 0, 0) /* Strength */
     , ({weenie_id},   2, 200, 0, 0) /* Endurance */
     , ({weenie_id},   3, 250, 0, 0) /* Quickness */
     , ({weenie_id},   4, 200, 0, 0) /* Coordination */
     , ({weenie_id},   5, 290, 0, 0) /* Focus */
     , ({weenie_id},   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES ({weenie_id},   1,   196, 0, 0, 296) /* MaxHealth */
     , ({weenie_id},   3,   196, 0, 0, 396) /* MaxStamina */
     , ({weenie_id},   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES ({weenie_id},  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , ({weenie_id},  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , ({weenie_id}, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES ({weenie_id},  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , ({weenie_id},  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , ({weenie_id},  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , ({weenie_id},  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , ({weenie_id},  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , ({weenie_id},  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , ({weenie_id},  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , ({weenie_id},  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , ({weenie_id},  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES """
    
    # Generate entries for each position generator
    generator_lines = []
    for i, pos_gen_id in enumerate(position_generator_ids):
        location = PRIMARY_LOCATIONS[i]
        cell_id, x, y, z, w, x_ang, y_ang, z_ang = location
        line = f"({weenie_id}, -1, {pos_gen_id:>10}, 0, 1, 1, 1, 4, 0, 0, 0, 0x{cell_id:08X}, {x:>10.6f}, {y:>11.6f}, {z:>9.6f}, {w:>10.6f}, {x_ang:>6.1f}, {y_ang:>6.1f}, {z_ang:>10.6f})"
        if i < len(position_generator_ids) - 1:
            generator_lines.append(line + f" /* Generate Position {i} Generator */")
        else:
            generator_lines.append(line + f"; /* Generate Position {i} Generator */")
    
    sql += "\n     , ".join(generator_lines)
    sql += "\n"
    
    return sql


def generate_controller(tier: str, wave_ids: List[int], central_point: Tuple[int, float, float, float] = None) -> str:
    """Generate SQL for event controller weenie.
    
    Args:
        tier: Tier name ('low', 'mid', 'high')
        wave_ids: List of wave generator weenie IDs
        central_point: Tuple of (cell_id, x, y, z) for spawning wave generators at central location
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tier_name = tier.capitalize()
    controller_id = WEENIE_IDS[tier]['controller']
    
    # Default central point if not provided (fallback to Event Controller location)
    if central_point is None:
        central_point = (0x02BF0110, 30.055235, -29.301636, 0.005)  # Event Controller location
    
    sql = f"""DELETE FROM `weenie` WHERE `class_Id` = {controller_id};

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES ({controller_id}, '{tier_name} Event Controller', 10, '{timestamp}') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES ({controller_id},   1,         16) /* ItemType - Creature */
     , ({controller_id},   2,         31) /* CreatureType - Human */
     , ({controller_id},   6,         -1) /* ItemsCapacity */
     , ({controller_id},   7,         -1) /* ContainersCapacity */
     , ({controller_id},  16,          1) /* ItemUseable - No */
     , ({controller_id},  25,        275) /* Level */
     , ({controller_id},  81,          2) /* MaxGeneratedObjects - Event Bell + Wave 1 Controller */
     , ({controller_id},  82,          1) /* InitGeneratedObjects - Only spawn Bell initially, Wave 1 spawns when Bell is destroyed */
     , ({controller_id},  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , ({controller_id}, 103,          2) /* GeneratorDestructionType - Destroy */
     , ({controller_id}, 113,          1) /* Gender - Male */
     , ({controller_id}, 133,          1) /* ShowableOnRadar - ShowNever */
     , ({controller_id}, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , ({controller_id}, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , ({controller_id}, 188,          1) /* HeritageGroup - Aluvian */
     , ({controller_id}, 290,          1) /* HearLocalSignals */
     , ({controller_id}, 291,          5) /* HearLocalSignalsRadius */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES ({controller_id},   1, True ) /* Stuck */
     , ({controller_id},  13, True ) /* Ethereal */
     , ({controller_id},  18, False ) /* Visibility */
     , ({controller_id},  19, False) /* Attackable */
     , ({controller_id},  52, True ) /* AiImmobile */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES ({controller_id},   1,       5) /* HeartbeatInterval */
     , ({controller_id},   2,       0) /* HeartbeatTimestamp */
     , ({controller_id},   3,     0.9) /* HealthRate */
     , ({controller_id},   4,       4) /* StaminaRate */
     , ({controller_id},   5,       2) /* ManaRate */
     , ({controller_id},  12,     0.5) /* Shade */
     , ({controller_id},  13,    0.75) /* ArmorModVsSlash */
     , ({controller_id},  14,    0.57) /* ArmorModVsPierce */
     , ({controller_id},  15,    0.75) /* ArmorModVsBludgeon */
     , ({controller_id},  16,     0.5) /* ArmorModVsCold */
     , ({controller_id},  17,    0.75) /* ArmorModVsFire */
     , ({controller_id},  18,    0.86) /* ArmorModVsAcid */
     , ({controller_id},  19,     0.5) /* ArmorModVsElectric */
     , ({controller_id},  31,      23) /* VisualAwarenessRange */
     , ({controller_id},  34,       3) /* PowerupTime */
     , ({controller_id},  36,       1) /* ChargeSpeed */
     , ({controller_id},  41,       5) /* RegenerationInterval */
     , ({controller_id},  43,       0) /* GeneratorRadius */
     , ({controller_id},  64,    0.66) /* ResistSlash */
     , ({controller_id},  65,    0.85) /* ResistPierce */
     , ({controller_id},  66,    0.66) /* ResistBludgeon */
     , ({controller_id},  67,    0.25) /* ResistFire */
     , ({controller_id},  68,    0.45) /* ResistCold */
     , ({controller_id},  69,    0.65) /* ResistAcid */
     , ({controller_id},  70,    0.95) /* ResistElectric */
     , ({controller_id},  71,       1) /* ResistHealthBoost */
     , ({controller_id},  72,       1) /* ResistStaminaDrain */
     , ({controller_id},  73,       1) /* ResistStaminaBoost */
     , ({controller_id},  74,       1) /* ResistManaDrain */
     , ({controller_id},  75,       1) /* ResistManaBoost */
     , ({controller_id}, 104,      10) /* ObviousRadarRange */
     , ({controller_id}, 117,     0.5) /* FocusedProbability */
     , ({controller_id}, 121,       1) /* GeneratorInitialDelay */
     , ({controller_id}, 125,       1) /* ResistHealthDrain */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES ({controller_id},   1, '{tier_name} Event Controller') /* Name */
     , ({controller_id},   5, 'Event Controller') /* Template */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES ({controller_id},   1, 0x02000001) /* Setup */
     , ({controller_id},   2, 0x09000001) /* MotionTable */
     , ({controller_id},   3, 0x20000001) /* SoundTable */
     , ({controller_id},   6, 0x0400007E) /* PaletteBase */
     , ({controller_id},   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES ({controller_id},   1, 240, 0, 0) /* Strength */
     , ({controller_id},   2, 200, 0, 0) /* Endurance */
     , ({controller_id},   3, 250, 0, 0) /* Quickness */
     , ({controller_id},   4, 200, 0, 0) /* Coordination */
     , ({controller_id},   5, 290, 0, 0) /* Focus */
     , ({controller_id},   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES ({controller_id},   1,   196, 0, 0, 296) /* MaxHealth */
     , ({controller_id},   3,   196, 0, 0, 396) /* MaxStamina */
     , ({controller_id},   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES ({controller_id},  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , ({controller_id},  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , ({controller_id}, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES ({controller_id},  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , ({controller_id},  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , ({controller_id},  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , ({controller_id},  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , ({controller_id},  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , ({controller_id},  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , ({controller_id},  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , ({controller_id},  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , ({controller_id},  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

"""
    
    # Generator entries - simple flow: Bell spawns, when Bell is destroyed, Wave 1 spawns
    sql += f"""
INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES ({controller_id}, -1, {WEENIE_IDS['event_bell']}, 0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Bell at Event Controller location (spawn on creation) */"""
    
    # Wave 1 spawns when Bell is destroyed (after bell is rung and deletes itself)
    if len(wave_ids) > 0:
        sql += f"\n     , ({controller_id}, -1, {wave_ids[0]}, 0, 0, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0); /* Generate Wave 1 Controller (spawn when Event Bell is destroyed) */\n"""
    
    return sql


def generate_exit_controller() -> str:
    """Generate SQL for event exit controller weenie."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    exit_controller_id = WEENIE_IDS['exit_controller']
    
    sql = f"""DELETE FROM `weenie` WHERE `class_Id` = {exit_controller_id};

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES ({exit_controller_id}, 'Event Exit Controller', 1, '{timestamp}') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES ({exit_controller_id},  81,          1) /* MaxGeneratedObjects */
     , ({exit_controller_id},  82,          0) /* InitGeneratedObjects - Start inactive, spawn portal after boss wave + delay */
     , ({exit_controller_id},  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , ({exit_controller_id}, 103,          2) /* GeneratorDestructionType - Destroy */
     , ({exit_controller_id}, 133,          1) /* ShowableOnRadar - ShowNever */
     , ({exit_controller_id}, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , ({exit_controller_id}, 290,          1) /* HearLocalSignals */
     , ({exit_controller_id}, 291,          5) /* HearLocalSignalsRadius */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES ({exit_controller_id},   1, True ) /* Stuck */
     , ({exit_controller_id},  11, True ) /* IgnoreCollisions */
     , ({exit_controller_id},  18, True ) /* Visibility */
     , ({exit_controller_id},  59, False ) /* GeneratorDisabled - Enable generator on creation */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES ({exit_controller_id},  41,       5) /* RegenerationInterval */
     , ({exit_controller_id},  43,      10) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES ({exit_controller_id},   1, 'Event Exit Controller') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES ({exit_controller_id},   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES ({exit_controller_id},  9,      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL); /* Generation - Exit Controller spawned when Wave 11 is destroyed */

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88, 240, 1, NULL, 'SpawnExit', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL); /* LocalSignal - Send activation signal after 240 seconds (4 minutes) delay */

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES ({exit_controller_id}, 37,      1, NULL, NULL, NULL, 'SpawnExit', NULL, NULL, NULL); /* ReceiveLocalSignal - Activate generator to spawn portal */

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  72, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* Generate - Activate generator to spawn portal */
     , (@parent_id,  1,  23, 0, 1, NULL, 'EventRewards', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL); /* StartEvent - Start EventRewards event when portal opens */

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES ({exit_controller_id},  9,      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL); /* Generation - Portal spawned */

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88, 180, 1, NULL, 'DeleteMe', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* LocalSignal - Send DeleteMe signal to portal after 180 seconds (3 minutes) to close it */
     , (@parent_id,  1,  24, 180, 1, NULL, 'EventRewards', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* StopEvent - Stop EventRewards event when portal closes (180 seconds after portal opens) */
     , (@parent_id,  2,  88, 0, 1, NULL, 'DeleteEventController', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* LocalSignal - Tell Event Controller to delete itself when event is complete */
     , (@parent_id,  3,  77, 2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL); /* DeleteSelf */

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES ({exit_controller_id}, 1, 694200296, 0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0); /* Generate Reward Room Portal (694200296) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Specific */

"""
    
    return sql


def generate_event_bell(tier: str, wave_1_controller_id: int) -> str:
    """Generate SQL for event bell that spawns Wave 1 Controller when rung."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bell_id = WEENIE_IDS['event_bell']
    
    sql = f"""DELETE FROM `weenie` WHERE `class_Id` = {bell_id};

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES ({bell_id}, 'Event Bell', 10, '{timestamp}') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES ({bell_id},   1,         16) /* ItemType - Creature */
     , ({bell_id},   6,         -1) /* ItemsCapacity */
     , ({bell_id},   7,         -1) /* ContainersCapacity */
     , ({bell_id},  16,         32) /* ItemUseable - Remote */
     , ({bell_id},  93,    6292508) /* PhysicsState - Ethereal, ReportCollisions, IgnoreCollisions, Gravity, ReportCollisionsAsEnvironment, EdgeSlide */
     , ({bell_id},  95,          8) /* RadarBlipColor - Yellow */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES ({bell_id},   1, True ) /* Stuck */
     , ({bell_id},  19, False) /* Attackable */
     , ({bell_id},  52, True ) /* AiImmobile */
     , ({bell_id},  82, True ) /* DontTurnOrMoveWhenGiving */
     , ({bell_id},  83, True ) /* NpcLooksLikeObject */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES ({bell_id},  54,       3) /* UseRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES ({bell_id},   1, 'Event Bell') /* Name */
     , ({bell_id},  14, 'Use this bell to begin this Event.') /* Use */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES ({bell_id},   1, 0x02001696) /* Setup */
     , ({bell_id},   2, 0x090001C2) /* MotionTable */
     , ({bell_id},   3, 0x200000A4) /* SoundTable */
     , ({bell_id},   8, 0x06002150) /* Icon */
     , ({bell_id},  22, 0x3400002B) /* PhysicsEffectTable */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES ({bell_id},  7 /* Use */,      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,   9 /* Sound */, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1 /* Speak1 */, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
     , (@parent_id,  1,  88 /* LocalSignal */, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* Send StartEvent signal to Event Controller */
     , (@parent_id,  2,  77 /* DeleteSelf */, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

"""
    
    return sql


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_event_files.py <config.csv>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    
    if not os.path.exists(config_file):
        print(f"Error: Config file '{config_file}' not found")
        sys.exit(1)
    
    print(f"Loading configuration from {config_file}...")
    config = load_config(config_file)
    
    # Process each tier
    for tier in ['low', 'mid', 'high']:
        if tier not in config:
            print(f"Warning: No configuration found for {tier} tier, skipping...")
            continue
        
        print(f"\nGenerating {tier.upper()} tier files...")
        
        # Create output directory
        tier_dir = f"{tier.capitalize()} Event Sequence"
        os.makedirs(tier_dir, exist_ok=True)
        
        tier_data = WEENIE_IDS[tier]
        wave_controller_ids = []
        
        # Calculate central point from PRIMARY_LOCATIONS
        if PRIMARY_LOCATIONS:
            base_cell = PRIMARY_LOCATIONS[0][0]
            avg_x = sum(loc[1] for loc in PRIMARY_LOCATIONS) / len(PRIMARY_LOCATIONS)
            avg_y = sum(loc[2] for loc in PRIMARY_LOCATIONS) / len(PRIMARY_LOCATIONS)
            avg_z = sum(loc[3] for loc in PRIMARY_LOCATIONS) / len(PRIMARY_LOCATIONS)
            central_point = (base_cell, avg_x, avg_y, avg_z)
        else:
            central_point = (0x02BF0110, 30.055235, -29.301636, 0.005)  # Event Controller location
        
        # Generate wave files (1-10)
        for wave_num in range(1, 11):
            wave_key = str(wave_num)
            if wave_key not in config[tier]:
                print(f"  Warning: Wave {wave_num} not configured for {tier} tier")
                continue
            
            position_assignments = config[tier][wave_key]
            if len(position_assignments) == 0:
                print(f"  Error: Wave {wave_num} has no position assignments configured")
                continue
            
            wave_name = f"{tier.capitalize()} Event Wave {wave_num}"
            wave_controller_id = tier_data['waves'][wave_num - 1]
            position_generator_ids = []
            
            # Generate 4 Position Generators (one per position)
            for position_index in range(4):
                # Find assignment for this position
                position_assignment = None
                for pos_idx, wcid, spawn_count in position_assignments:
                    if pos_idx == position_index:
                        position_assignment = (wcid, spawn_count)
                        break
                
                if position_assignment is None:
                    print(f"  Warning: Wave {wave_num} position {position_index} has no assignment, skipping...")
                    continue
                
                wcid, spawn_count = position_assignment
                position_gen_id = get_position_generator_id(tier, wave_num, position_index)
                position_name = f"{wave_name} Position {position_index}"
                location = PRIMARY_LOCATIONS[position_index]
                
                # Generate Position Generator SQL
                sql = generate_position_generator(position_gen_id, position_name, wcid, spawn_count, location)
                filename = f"{tier_dir}/{position_gen_id} {position_name} Generator.sql"
                
                with open(filename, 'w') as f:
                    f.write(sql)
                
                position_generator_ids.append(position_gen_id)
                print(f"  [OK] Generated: {filename}")
            
            # Generate Wave Controller that spawns the 4 Position Generators
            if len(position_generator_ids) == 4:
                sql = generate_wave_controller(wave_controller_id, wave_name, position_generator_ids, wave_num)
                filename = f"{tier_dir}/{wave_controller_id} {wave_name} Controller.sql"
                
                with open(filename, 'w') as f:
                    f.write(sql)
                
                wave_controller_ids.append(wave_controller_id)
                print(f"  [OK] Generated: {filename}")
            else:
                print(f"  Error: Wave {wave_num} must have exactly 4 position generators, found {len(position_generator_ids)}")
        
        # Generate boss file
        boss_key = 'boss'
        if boss_key in config[tier]:
            position_assignments = config[tier][boss_key]
            if len(position_assignments) > 0:
                boss_name = f"{tier.capitalize()} Event Boss"
                boss_controller_id = tier_data['boss']
                position_generator_ids = []
                
                # Generate 4 Position Generators for boss
                for position_index in range(4):
                    # Find assignment for this position
                    position_assignment = None
                    for pos_idx, wcid, spawn_count in position_assignments:
                        if pos_idx == position_index:
                            position_assignment = (wcid, spawn_count)
                            break
                    
                    if position_assignment is None:
                        print(f"  Warning: Boss position {position_index} has no assignment, skipping...")
                        continue
                    
                    wcid, spawn_count = position_assignment
                    position_gen_id = get_position_generator_id(tier, 11, position_index)  # Boss is wave 11
                    position_name = f"{boss_name} Position {position_index}"
                    location = PRIMARY_LOCATIONS[position_index]
                    
                    # Generate Position Generator SQL
                    sql = generate_position_generator(position_gen_id, position_name, wcid, spawn_count, location)
                    filename = f"{tier_dir}/{position_gen_id} {position_name} Generator.sql"
                    
                    with open(filename, 'w') as f:
                        f.write(sql)
                    
                    position_generator_ids.append(position_gen_id)
                    print(f"  [OK] Generated: {filename}")
                
                # Generate Boss Wave Controller
                if len(position_generator_ids) == 4:
                    sql = generate_wave_controller(boss_controller_id, boss_name, position_generator_ids, 11)
                    filename = f"{tier_dir}/{boss_controller_id} {boss_name} Controller.sql"
                    
                    with open(filename, 'w') as f:
                        f.write(sql)
                    
                    wave_controller_ids.append(boss_controller_id)
                    print(f"  [OK] Generated: {filename}")
                else:
                    print(f"  Error: Boss must have exactly 4 position generators, found {len(position_generator_ids)}")
            else:
                print(f"  Warning: Boss wave not properly configured for {tier} tier")
        
        # Generate controller file
        controller_id = tier_data['controller']
        controller_name = f"{tier.capitalize()} Event Controller"
        
        sql = generate_controller(tier, wave_controller_ids, central_point)
        filename = f"{tier_dir}/{controller_id} {controller_name}.sql"
        
        with open(filename, 'w') as f:
            f.write(sql)
        
        print(f"  [OK] Generated: {filename}")
    
    # Generate exit controller file
    print(f"\nGenerating Exit Controller...")
    exit_controller_id = WEENIE_IDS['exit_controller']
    sql = generate_exit_controller()
    filename = f"{exit_controller_id} Event Exit Controller.sql"
    
    with open(filename, 'w') as f:
        f.write(sql)
    
    print(f"  [OK] Generated: {filename}")
    
    print("\n[SUCCESS] Event generation complete!")


if __name__ == '__main__':
    main()
