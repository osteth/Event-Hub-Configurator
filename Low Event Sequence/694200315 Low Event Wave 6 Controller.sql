DELETE FROM `weenie` WHERE `class_Id` = 694200315;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200315, 'Low Event Wave 6 Controller', 10, '2026-01-12 15:21:57') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200315,   1,         16) /* ItemType - Creature */
     , (694200315,   2,         31) /* CreatureType - Human */
     , (694200315,   6,         -1) /* ItemsCapacity */
     , (694200315,   7,         -1) /* ContainersCapacity */
     , (694200315,  16,          1) /* ItemUseable - No */
     , (694200315,  25,        275) /* Level */
     , (694200315,  81,          4) /* MaxGeneratedObjects - One per position */
     , (694200315,  82,          4) /* InitGeneratedObjects - Spawn all 4 Position Generators immediately when Wave Controller spawns */
     , (694200315,  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , (694200315, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200315, 113,          1) /* Gender - Male */
     , (694200315, 133,          1) /* ShowableOnRadar - ShowNever */
     , (694200315, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , (694200315, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , (694200315, 188,          1) /* HeritageGroup - Aluvian */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200315,   1, True ) /* Stuck */
     , (694200315,  13, True ) /* Ethereal */
     , (694200315,  18, False ) /* Visibility - Invisible */
     , (694200315,  19, False) /* Attackable */
     , (694200315,  52, True ) /* AiImmobile */
     , (694200315,  59, False ) /* GeneratorDisabled - Keep enabled, InitGeneratedObjects=0 prevents initial spawn */
     , (694200315,  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all position generators are destroyed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200315,   1,       5) /* HeartbeatInterval */
     , (694200315,   2,       0) /* HeartbeatTimestamp */
     , (694200315,   3,     0.9) /* HealthRate */
     , (694200315,   4,       4) /* StaminaRate */
     , (694200315,   5,       2) /* ManaRate */
     , (694200315,  41,       5) /* RegenerationInterval */
     , (694200315,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200315,   1, 'Low Event Wave 6 Controller') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200315,   1, 0x02000001) /* Setup */
     , (694200315,   2, 0x09000001) /* MotionTable */
     , (694200315,   3, 0x20000001) /* SoundTable */
     , (694200315,   6, 0x0400007E) /* PaletteBase */
     , (694200315,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES (694200315,   1, 240, 0, 0) /* Strength */
     , (694200315,   2, 200, 0, 0) /* Endurance */
     , (694200315,   3, 250, 0, 0) /* Quickness */
     , (694200315,   4, 200, 0, 0) /* Coordination */
     , (694200315,   5, 290, 0, 0) /* Focus */
     , (694200315,   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES (694200315,   1,   196, 0, 0, 296) /* MaxHealth */
     , (694200315,   3,   196, 0, 0, 396) /* MaxStamina */
     , (694200315,   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES (694200315,  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , (694200315,  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , (694200315, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES (694200315,  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , (694200315,  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , (694200315,  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , (694200315,  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , (694200315,  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , (694200315,  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , (694200315,  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , (694200315,  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , (694200315,  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200315, -1,  694201319, 0, 1, 1, 1, 4, 0, 0, 0, 0x02BF010D,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Position 0 Generator */
     , (694200315, -1,  694201320, 0, 1, 1, 1, 4, 0, 0, 0, 0x02BF0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Position 1 Generator */
     , (694200315, -1,  694201321, 0, 1, 1, 1, 4, 0, 0, 0, 0x02BF0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Position 2 Generator */
     , (694200315, -1,  694201322, 0, 1, 1, 1, 4, 0, 0, 0, 0x02BF0104,  14.955328,  -15.005316,  0.005000,  -0.421018,    0.0,    0.0,   0.907052); /* Generate Position 3 Generator */
