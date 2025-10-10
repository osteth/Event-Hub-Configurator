#!/usr/bin/env python3
"""
Asheron's Call ACE Event Generator
Generates SQL weenie files for multi-tier events from CSV configuration
"""

import csv
import os
import sys
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple


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


def load_config(csv_file: str) -> Dict[str, Dict[int, List[int]]]:
    """
    Load event configuration from CSV file.
    Returns: {tier: {wave_num: [wcid1, wcid2, ..., wcid10]}}
    """
    config = defaultdict(lambda: defaultdict(list))
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tier = row['tier'].lower()
            wave_num = row['wave_number']
            slot = int(row['slot'])
            wcid = int(row['wcid'])
            
            # Ensure we have a list with 10 slots
            while len(config[tier][wave_num]) < 10:
                config[tier][wave_num].append(None)
            
            config[tier][wave_num][slot - 1] = wcid
    
    return config


def generate_wave_generator(weenie_id: int, wave_name: str, monsters: List[int]) -> str:
    """Generate SQL for a wave generator weenie."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Ensure we have exactly 10 monsters
    if len(monsters) != 10:
        raise ValueError(f"Wave {wave_name} must have exactly 10 monsters, got {len(monsters)}")
    
    sql = f"""DELETE FROM `weenie` WHERE `class_Id` = {weenie_id};

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES ({weenie_id}, '{wave_name}', 1, '{timestamp}') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},  81,         10) /* MaxGeneratedObjects */
     , ({weenie_id},  82,          8) /* InitGeneratedObjects */
     , ({weenie_id},  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , ({weenie_id}, 103,          2) /* GeneratorDestructionType - Destroy */
     , ({weenie_id}, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, True ) /* Stuck */
     , ({weenie_id},  11, True ) /* IgnoreCollisions */
     , ({weenie_id},  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},  41,      15) /* RegenerationInterval */
     , ({weenie_id},  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, '{wave_name} Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES ({weenie_id},   1, 0x0200026B) /* Setup */
     , ({weenie_id},   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES """
    
    # Generate 10 monster entries
    generator_lines = []
    for i, wcid in enumerate(monsters):
        line = f"({weenie_id}, -1, {wcid:>10}, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0)"
        if i < 9:
            generator_lines.append(line + " /* Generate Monster */")
        else:
            generator_lines.append(line + ";")
    
    sql += "\n         , ".join(generator_lines)
    sql += "\n"
    
    return sql


def generate_controller(tier: str, wave_ids: List[int]) -> str:
    """Generate SQL for event controller weenie."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tier_name = tier.capitalize()
    controller_id = WEENIE_IDS[tier]['controller']
    
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
     , ({controller_id},  81,          1) /* MaxGeneratedObjects */
     , ({controller_id},  82,          1) /* InitGeneratedObjects */
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
     , ({controller_id},  18, True ) /* Visibility */
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

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES ({controller_id}, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'DeleteMe', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  77 /* DeleteSelf */, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES ({controller_id}, -1, {WEENIE_IDS['event_bell']}, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Bell */"""
    
    # Add all wave generators
    for wave_id in wave_ids:
        sql += f"\n         , ({controller_id}, -1, {wave_id}, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */"
    
    # Add exit controller
    sql += f"\n     , ({controller_id}, -1, {WEENIE_IDS['exit_controller']}, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Exit Controller */;\n"
    
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
        wave_ids = []
        
        # Generate wave files (1-10)
        for wave_num in range(1, 11):
            wave_key = str(wave_num)
            if wave_key not in config[tier]:
                print(f"  Warning: Wave {wave_num} not configured for {tier} tier")
                continue
            
            monsters = config[tier][wave_key]
            if None in monsters:
                print(f"  Error: Wave {wave_num} has missing monster slots")
                continue
            
            weenie_id = tier_data['waves'][wave_num - 1]
            wave_name = f"{tier.capitalize()} Event Wave {wave_num}"
            
            sql = generate_wave_generator(weenie_id, wave_name, monsters)
            filename = f"{tier_dir}/{weenie_id} {wave_name}.sql"
            
            with open(filename, 'w') as f:
                f.write(sql)
            
            wave_ids.append(weenie_id)
            print(f"  ✓ Generated: {filename}")
        
        # Generate boss file
        boss_key = 'boss'
        if boss_key in config[tier]:
            monsters = config[tier][boss_key]
            if None not in monsters and len(monsters) == 10:
                weenie_id = tier_data['boss']
                boss_name = f"{tier.capitalize()} Event Boss"
                
                sql = generate_wave_generator(weenie_id, boss_name, monsters)
                filename = f"{tier_dir}/{weenie_id} {boss_name}.sql"
                
                with open(filename, 'w') as f:
                    f.write(sql)
                
                wave_ids.append(weenie_id)
                print(f"  ✓ Generated: {filename}")
            else:
                print(f"  Warning: Boss wave not properly configured for {tier} tier")
        
        # Generate controller file
        controller_id = tier_data['controller']
        controller_name = f"{tier.capitalize()} Event Controller"
        
        sql = generate_controller(tier, wave_ids)
        filename = f"{tier_dir}/{controller_id} {controller_name}.sql"
        
        with open(filename, 'w') as f:
            f.write(sql)
        
        print(f"  ✓ Generated: {filename}")
    
    print("\n✅ Event generation complete!")


if __name__ == '__main__':
    main()
