DELETE FROM `weenie` WHERE `class_Id` = 694200295;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200295, 'noobeventexitcontroller', 10, '2022-03-31 06:02:40') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200295,   1,         16) /* ItemType - Creature */
     , (694200295,   2,         31) /* CreatureType - Human */
     , (694200295,   6,         -1) /* ItemsCapacity */
     , (694200295,   7,         -1) /* ContainersCapacity */
     , (694200295,  16,          1) /* ItemUseable - No */
     , (694200295,  25,        275) /* Level */
     , (694200295,  81,          1) /* MaxGeneratedObjects */
     , (694200295,  82,          1) /* InitGeneratedObjects */
     , (694200295,  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , (694200295, 113,          1) /* Gender - Male */
     , (694200295, 133,          1) /* ShowableOnRadar - ShowNever */
     , (694200295, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , (694200295, 188,          1) /* HeritageGroup - Aluvian */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200295,   1, True ) /* Stuck */
     , (694200295,  13, True ) /* Ethereal */
     , (694200295,  18, True ) /* Visibility */
     , (694200295,  19, False) /* Attackable */
     , (694200295,  52, True ) /* AiImmobile */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200295,   1,       5) /* HeartbeatInterval */
     , (694200295,   2,       0) /* HeartbeatTimestamp */
     , (694200295,   3,     0.9) /* HealthRate */
     , (694200295,   4,       4) /* StaminaRate */
     , (694200295,   5,       2) /* ManaRate */
     , (694200295,  12,     0.5) /* Shade */
     , (694200295,  13,    0.75) /* ArmorModVsSlash */
     , (694200295,  14,    0.57) /* ArmorModVsPierce */
     , (694200295,  15,    0.75) /* ArmorModVsBludgeon */
     , (694200295,  16,     0.5) /* ArmorModVsCold */
     , (694200295,  17,    0.75) /* ArmorModVsFire */
     , (694200295,  18,    0.86) /* ArmorModVsAcid */
     , (694200295,  19,     0.5) /* ArmorModVsElectric */
     , (694200295,  31,      23) /* VisualAwarenessRange */
     , (694200295,  34,       3) /* PowerupTime */
     , (694200295,  36,       1) /* ChargeSpeed */
     , (694200295,  41,       5) /* RegenerationInterval */
     , (694200295,  43,      10) /* GeneratorRadius */
     , (694200295,  64,    0.66) /* ResistSlash */
     , (694200295,  65,    0.85) /* ResistPierce */
     , (694200295,  66,    0.66) /* ResistBludgeon */
     , (694200295,  67,    0.25) /* ResistFire */
     , (694200295,  68,    0.45) /* ResistCold */
     , (694200295,  69,    0.65) /* ResistAcid */
     , (694200295,  70,    0.95) /* ResistElectric */
     , (694200295,  71,       1) /* ResistHealthBoost */
     , (694200295,  72,       1) /* ResistStaminaDrain */
     , (694200295,  73,       1) /* ResistStaminaBoost */
     , (694200295,  74,       1) /* ResistManaDrain */
     , (694200295,  75,       1) /* ResistManaBoost */
     , (694200295, 104,      10) /* ObviousRadarRange */
     , (694200295, 117,     0.5) /* FocusedProbability */
     , (694200295, 125,       1) /* ResistHealthDrain */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200295,   1, 'Event Exit Controller') /* Name */
     , (694200295,   5, 'Event Exit Controller') /* Template */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200295,   1, 0x02000001) /* Setup */
     , (694200295,   2, 0x09000001) /* MotionTable */
     , (694200295,   3, 0x20000001) /* SoundTable */
     , (694200295,   6, 0x0400007E) /* PaletteBase */
     , (694200295,   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES (694200295,   1, 240, 0, 0) /* Strength */
     , (694200295,   2, 200, 0, 0) /* Endurance */
     , (694200295,   3, 250, 0, 0) /* Quickness */
     , (694200295,   4, 200, 0, 0) /* Coordination */
     , (694200295,   5, 290, 0, 0) /* Focus */
     , (694200295,   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES (694200295,   1,   196, 0, 0, 296) /* MaxHealth */
     , (694200295,   3,   196, 0, 0, 396) /* MaxStamina */
     , (694200295,   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES (694200295,  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , (694200295,  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , (694200295, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES (694200295,  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , (694200295,  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , (694200295,  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , (694200295,  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , (694200295,  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , (694200295,  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , (694200295,  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , (694200295,  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , (694200295,  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200295,  9 /* Generation */,      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88 /* LocalSignal */, 0, 1, NULL, 'DeleteMe', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
     , (@parent_id,  1,  77 /* DeleteSelf */, 2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200295, 1, 694200296, 0, 1, 1, 1, 4, 0, 0, 0, 0, 0, , 0, 1, 0, 0, 0) /* Generate Reward Room Portal (694200296) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Specific */;

