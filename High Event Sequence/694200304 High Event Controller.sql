DELETE FROM `weenie` WHERE `class_Id` = 694200304;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200304, 'High Event Controller', 10, '2025-10-10 02:04:14') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200304,   1,         16) /* ItemType - Creature */
     , (694200304,   2,         31) /* CreatureType - Human */
     , (694200304,   6,         -1) /* ItemsCapacity */
     , (694200304,   7,         -1) /* ContainersCapacity */
     , (694200304,  16,          1) /* ItemUseable - No */
     , (694200304,  25,        275) /* Level */
     , (694200304,  81,          1) /* MaxGeneratedObjects */
     , (694200304,  82,          1) /* InitGeneratedObjects */
     , (694200304,  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , (694200304, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200304, 113,          1) /* Gender - Male */
     , (694200304, 133,          1) /* ShowableOnRadar - ShowNever */
     , (694200304, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , (694200304, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , (694200304, 188,          1) /* HeritageGroup - Aluvian */
     , (694200304, 290,          1) /* HearLocalSignals */
     , (694200304, 291,          5) /* HearLocalSignalsRadius */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200304,   1, True ) /* Stuck */
     , (694200304,  13, True ) /* Ethereal */
     , (694200304,  18, True ) /* Visibility */
     , (694200304,  19, False) /* Attackable */
     , (694200304,  52, True ) /* AiImmobile */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200304,   1,       5) /* HeartbeatInterval */
     , (694200304,   2,       0) /* HeartbeatTimestamp */
     , (694200304,   3,     0.9) /* HealthRate */
     , (694200304,   4,       4) /* StaminaRate */
     , (694200304,   5,       2) /* ManaRate */
     , (694200304,  12,     0.5) /* Shade */
     , (694200304,  13,    0.75) /* ArmorModVsSlash */
     , (694200304,  14,    0.57) /* ArmorModVsPierce */
     , (694200304,  15,    0.75) /* ArmorModVsBludgeon */
     , (694200304,  16,     0.5) /* ArmorModVsCold */
     , (694200304,  17,    0.75) /* ArmorModVsFire */
     , (694200304,  18,    0.86) /* ArmorModVsAcid */
     , (694200304,  19,     0.5) /* ArmorModVsElectric */
     , (694200304,  31,      23) /* VisualAwarenessRange */
     , (694200304,  34,       3) /* PowerupTime */
     , (694200304,  36,       1) /* ChargeSpeed */
     , (694200304,  41,       5) /* RegenerationInterval */
     , (694200304,  43,       0) /* GeneratorRadius */
     , (694200304,  64,    0.66) /* ResistSlash */
     , (694200304,  65,    0.85) /* ResistPierce */
     , (694200304,  66,    0.66) /* ResistBludgeon */
     , (694200304,  67,    0.25) /* ResistFire */
     , (694200304,  68,    0.45) /* ResistCold */
     , (694200304,  69,    0.65) /* ResistAcid */
     , (694200304,  70,    0.95) /* ResistElectric */
     , (694200304,  71,       1) /* ResistHealthBoost */
     , (694200304,  72,       1) /* ResistStaminaDrain */
     , (694200304,  73,       1) /* ResistStaminaBoost */
     , (694200304,  74,       1) /* ResistManaDrain */
     , (694200304,  75,       1) /* ResistManaBoost */
     , (694200304, 104,      10) /* ObviousRadarRange */
     , (694200304, 117,     0.5) /* FocusedProbability */
     , (694200304, 121,       1) /* GeneratorInitialDelay */
     , (694200304, 125,       1) /* ResistHealthDrain */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200304,   1, 'High Event Controller') /* Name */
     , (694200304,   5, 'Event Controller') /* Template */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200304,   1, 0x02000001) /* Setup */
     , (694200304,   2, 0x09000001) /* MotionTable */
     , (694200304,   3, 0x20000001) /* SoundTable */
     , (694200304,   6, 0x0400007E) /* PaletteBase */
     , (694200304,   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES (694200304,   1, 240, 0, 0) /* Strength */
     , (694200304,   2, 200, 0, 0) /* Endurance */
     , (694200304,   3, 250, 0, 0) /* Quickness */
     , (694200304,   4, 200, 0, 0) /* Coordination */
     , (694200304,   5, 290, 0, 0) /* Focus */
     , (694200304,   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES (694200304,   1,   196, 0, 0, 296) /* MaxHealth */
     , (694200304,   3,   196, 0, 0, 396) /* MaxStamina */
     , (694200304,   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES (694200304,  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , (694200304,  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , (694200304, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES (694200304,  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , (694200304,  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , (694200304,  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , (694200304,  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , (694200304,  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , (694200304,  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , (694200304,  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , (694200304,  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , (694200304,  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200304, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'DeleteMe', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  77 /* DeleteSelf */, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200304, -1, 694200294, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Bell */
         , (694200304, -1, 694200332, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200333, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200334, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200335, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200336, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200337, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200338, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200339, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200340, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200341, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
         , (694200304, -1, 694200342, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave Generator */
     , (694200304, -1, 694200295, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Exit Controller */;
