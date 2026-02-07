-- ============================================
-- Event Hub Bulk Upload SQL File
-- Generated: 2026-01-11 01:58:35
-- Total Files: 38
-- ============================================

-- This file contains all Event Hub weenies in the correct order.
-- Execute this file on your ACE server database.


-- ============================================
-- Event Bell
-- ============================================

-- File 1/38: 694200294 Event Bell.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200294;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200294, 'Event Bell', 10, '2022-03-31 06:02:40') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200294,   1,         16) /* ItemType - Creature */
     , (694200294,   6,         -1) /* ItemsCapacity */
     , (694200294,   7,         -1) /* ContainersCapacity */
     , (694200294,  16,         32) /* ItemUseable - Remote */
     , (694200294,  93,    6292508) /* PhysicsState - Ethereal, ReportCollisions, IgnoreCollisions, Gravity, ReportCollisionsAsEnvironment, EdgeSlide */
     , (694200294,  95,          8) /* RadarBlipColor - Yellow */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200294,   1, True ) /* Stuck */
     , (694200294,  19, False) /* Attackable */
     , (694200294,  52, True ) /* AiImmobile */
     , (694200294,  82, True ) /* DontTurnOrMoveWhenGiving */
     , (694200294,  83, True ) /* NpcLooksLikeObject */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200294,  54,       3) /* UseRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200294,   1, 'Event Bell') /* Name */
     , (694200294,  14, 'Use this bell to begin this Event.') /* Use */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200294,   1, 0x02001696) /* Setup */
     , (694200294,   2, 0x090001C2) /* MotionTable */
     , (694200294,   3, 0x200000A4) /* SoundTable */
     , (694200294,   8, 0x06002150) /* Icon */
     , (694200294,  22, 0x3400002B) /* PhysicsEffectTable */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200294,  7 /* Use */,      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,   9 /* Sound */, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1 /* Speak1 */, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
     , (@parent_id,  1,  77 /* DeleteSelf */, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);



-- ============================================
-- Controllers
-- ============================================

-- File 2/38: 694200295 Event Exit Controller.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200295;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200295, 'Event Exit Controller', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200295,  81,          1) /* MaxGeneratedObjects */
     , (694200295,  82,          1) /* InitGeneratedObjects */
     , (694200295,  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , (694200295, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200295, 133,          1) /* ShowableOnRadar - ShowNever */
     , (694200295, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200295,   1, True ) /* Stuck */
     , (694200295,  11, True ) /* IgnoreCollisions */
     , (694200295,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200295,  41,       5) /* RegenerationInterval */
     , (694200295,  43,      10) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200295,   1, 'Event Exit Controller') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200295,   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200295,  9,      1, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* Generation */;

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88 /* LocalSignal */, 0, 1, NULL, 'DeleteMe', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
     , (@parent_id,  1,  77 /* DeleteSelf */, 2, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200295, 1, 694200296, 0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Reward Room Portal (694200296) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Specific */;



-- ============================================
-- Low Event Sequence
-- ============================================

-- File 3/38: Low Event Sequence/694200293 Low Event Controller.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200293;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200293, 'Low Event Controller', 10, '2026-01-11 01:58:27') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200293,   1,         16) /* ItemType - Creature */
     , (694200293,   2,         31) /* CreatureType - Human */
     , (694200293,   6,         -1) /* ItemsCapacity */
     , (694200293,   7,         -1) /* ContainersCapacity */
     , (694200293,  16,          1) /* ItemUseable - No */
     , (694200293,  25,        275) /* Level */
     , (694200293,  81,          1) /* MaxGeneratedObjects */
     , (694200293,  82,          1) /* InitGeneratedObjects */
     , (694200293,  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , (694200293, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200293, 113,          1) /* Gender - Male */
     , (694200293, 133,          1) /* ShowableOnRadar - ShowNever */
     , (694200293, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , (694200293, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , (694200293, 188,          1) /* HeritageGroup - Aluvian */
     , (694200293, 290,          1) /* HearLocalSignals */
     , (694200293, 291,          5) /* HearLocalSignalsRadius */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200293,   1, True ) /* Stuck */
     , (694200293,  13, True ) /* Ethereal */
     , (694200293,  18, True ) /* Visibility */
     , (694200293,  19, False) /* Attackable */
     , (694200293,  52, True ) /* AiImmobile */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200293,   1,       5) /* HeartbeatInterval */
     , (694200293,   2,       0) /* HeartbeatTimestamp */
     , (694200293,   3,     0.9) /* HealthRate */
     , (694200293,   4,       4) /* StaminaRate */
     , (694200293,   5,       2) /* ManaRate */
     , (694200293,  12,     0.5) /* Shade */
     , (694200293,  13,    0.75) /* ArmorModVsSlash */
     , (694200293,  14,    0.57) /* ArmorModVsPierce */
     , (694200293,  15,    0.75) /* ArmorModVsBludgeon */
     , (694200293,  16,     0.5) /* ArmorModVsCold */
     , (694200293,  17,    0.75) /* ArmorModVsFire */
     , (694200293,  18,    0.86) /* ArmorModVsAcid */
     , (694200293,  19,     0.5) /* ArmorModVsElectric */
     , (694200293,  31,      23) /* VisualAwarenessRange */
     , (694200293,  34,       3) /* PowerupTime */
     , (694200293,  36,       1) /* ChargeSpeed */
     , (694200293,  41,       5) /* RegenerationInterval */
     , (694200293,  43,       0) /* GeneratorRadius */
     , (694200293,  64,    0.66) /* ResistSlash */
     , (694200293,  65,    0.85) /* ResistPierce */
     , (694200293,  66,    0.66) /* ResistBludgeon */
     , (694200293,  67,    0.25) /* ResistFire */
     , (694200293,  68,    0.45) /* ResistCold */
     , (694200293,  69,    0.65) /* ResistAcid */
     , (694200293,  70,    0.95) /* ResistElectric */
     , (694200293,  71,       1) /* ResistHealthBoost */
     , (694200293,  72,       1) /* ResistStaminaDrain */
     , (694200293,  73,       1) /* ResistStaminaBoost */
     , (694200293,  74,       1) /* ResistManaDrain */
     , (694200293,  75,       1) /* ResistManaBoost */
     , (694200293, 104,      10) /* ObviousRadarRange */
     , (694200293, 117,     0.5) /* FocusedProbability */
     , (694200293, 121,       1) /* GeneratorInitialDelay */
     , (694200293, 125,       1) /* ResistHealthDrain */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200293,   1, 'Low Event Controller') /* Name */
     , (694200293,   5, 'Event Controller') /* Template */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200293,   1, 0x02000001) /* Setup */
     , (694200293,   2, 0x09000001) /* MotionTable */
     , (694200293,   3, 0x20000001) /* SoundTable */
     , (694200293,   6, 0x0400007E) /* PaletteBase */
     , (694200293,   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES (694200293,   1, 240, 0, 0) /* Strength */
     , (694200293,   2, 200, 0, 0) /* Endurance */
     , (694200293,   3, 250, 0, 0) /* Quickness */
     , (694200293,   4, 200, 0, 0) /* Coordination */
     , (694200293,   5, 290, 0, 0) /* Focus */
     , (694200293,   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES (694200293,   1,   196, 0, 0, 296) /* MaxHealth */
     , (694200293,   3,   196, 0, 0, 396) /* MaxStamina */
     , (694200293,   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES (694200293,  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , (694200293,  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , (694200293, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES (694200293,  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , (694200293,  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , (694200293,  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , (694200293,  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , (694200293,  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , (694200293,  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , (694200293,  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , (694200293,  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , (694200293,  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200293, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'DeleteMe', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  77 /* DeleteSelf */, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200293, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'StartEvent', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88 /* LocalSignal - Send signal to activate Wave 1 Generator */, 0, 1, NULL, 'Wave1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200293, -1, 694200294, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Bell (where_Create = 4 = Specific) */
     , (694200293, -1, 694200310, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 1 Generator */
     , (694200293, -1, 694200311, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 2 Generator */
     , (694200293, -1, 694200312, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 3 Generator */
     , (694200293, -1, 694200313, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 4 Generator */
     , (694200293, -1, 694200314, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 5 Generator */
     , (694200293, -1, 694200315, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 6 Generator */
     , (694200293, -1, 694200316, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 7 Generator */
     , (694200293, -1, 694200317, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 8 Generator */
     , (694200293, -1, 694200318, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 9 Generator */
     , (694200293, -1, 694200319, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 10 Generator */
     , (694200293, -1, 694200320, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 11 Generator */
     , (694200293, -1, 694200295, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Exit Controller (where_Create = 4 = Specific) */;

-- File 4/38: Low Event Sequence/694200310 Low Event Wave 1.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200310;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200310, 'Low Event Wave 1', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200310,  81,         19) /* MaxGeneratedObjects */
     , (694200310,  82,         19) /* InitGeneratedObjects */
     , (694200310,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200310, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200310, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200310,   1, True ) /* Stuck */
     , (694200310,  11, True ) /* IgnoreCollisions */
     , (694200310,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200310,  41,      15) /* RegenerationInterval */
     , (694200310,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200310,   1, 'Low Event Wave 1 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200310,   1, 0x0200026B) /* Setup */
     , (694200310,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200310, -1,  290500204, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200310, -1,  290500204, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200310, -1,  290500204, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200310, -1,  290500204, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 5/38: Low Event Sequence/694200311 Low Event Wave 2.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200311;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200311, 'Low Event Wave 2', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200311,  81,          4) /* MaxGeneratedObjects */
     , (694200311,  82,          4) /* InitGeneratedObjects */
     , (694200311,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200311, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200311, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200311,   1, True ) /* Stuck */
     , (694200311,  11, True ) /* IgnoreCollisions */
     , (694200311,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200311,  41,      15) /* RegenerationInterval */
     , (694200311,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200311,   1, 'Low Event Wave 2 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200311,   1, 0x0200026B) /* Setup */
     , (694200311,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200311, -1,  290500000, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200311, -1,  290500000, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200311, -1,  290500000, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200311, -1,  290500000, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 6/38: Low Event Sequence/694200312 Low Event Wave 3.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200312;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200312, 'Low Event Wave 3', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200312,  81,         25) /* MaxGeneratedObjects */
     , (694200312,  82,         25) /* InitGeneratedObjects */
     , (694200312,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200312, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200312, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200312,   1, True ) /* Stuck */
     , (694200312,  11, True ) /* IgnoreCollisions */
     , (694200312,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200312,  41,      15) /* RegenerationInterval */
     , (694200312,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200312,   1, 'Low Event Wave 3 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200312,   1, 0x0200026B) /* Setup */
     , (694200312,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200312, -1,  300101015, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200312, -1,  300101015, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200312, -1,  300101015, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200312, -1,  300101015, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 7/38: Low Event Sequence/694200313 Low Event Wave 4.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200313;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200313, 'Low Event Wave 4', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200313,  81,         18) /* MaxGeneratedObjects */
     , (694200313,  82,         18) /* InitGeneratedObjects */
     , (694200313,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200313, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200313, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200313,   1, True ) /* Stuck */
     , (694200313,  11, True ) /* IgnoreCollisions */
     , (694200313,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200313,  41,      15) /* RegenerationInterval */
     , (694200313,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200313,   1, 'Low Event Wave 4 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200313,   1, 0x0200026B) /* Setup */
     , (694200313,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200313, -1,  300101050, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200313, -1,  300101050, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200313, -1,  300101050, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200313, -1,  300101050, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 8/38: Low Event Sequence/694200314 Low Event Wave 5.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200314;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200314, 'Low Event Wave 5', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200314,  81,          4) /* MaxGeneratedObjects */
     , (694200314,  82,          4) /* InitGeneratedObjects */
     , (694200314,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200314, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200314, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200314,   1, True ) /* Stuck */
     , (694200314,  11, True ) /* IgnoreCollisions */
     , (694200314,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200314,  41,      15) /* RegenerationInterval */
     , (694200314,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200314,   1, 'Low Event Wave 5 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200314,   1, 0x0200026B) /* Setup */
     , (694200314,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200314, -1,  290444463, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200314, -1,  290444463, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200314, -1,  290444463, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200314, -1,  290444463, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 9/38: Low Event Sequence/694200315 Low Event Wave 6.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200315;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200315, 'Low Event Wave 6', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200315,  81,         25) /* MaxGeneratedObjects */
     , (694200315,  82,         25) /* InitGeneratedObjects */
     , (694200315,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200315, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200315, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200315,   1, True ) /* Stuck */
     , (694200315,  11, True ) /* IgnoreCollisions */
     , (694200315,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200315,  41,      15) /* RegenerationInterval */
     , (694200315,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200315,   1, 'Low Event Wave 6 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200315,   1, 0x0200026B) /* Setup */
     , (694200315,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200315, -1,  300101012, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200315, -1,  300101012, 1, 10, 10, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200315, -1,  300101012, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200315, -1,  300101012, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 10/38: Low Event Sequence/694200316 Low Event Wave 7.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200316;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200316, 'Low Event Wave 7', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200316,  81,         34) /* MaxGeneratedObjects */
     , (694200316,  82,         34) /* InitGeneratedObjects */
     , (694200316,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200316, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200316, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200316,   1, True ) /* Stuck */
     , (694200316,  11, True ) /* IgnoreCollisions */
     , (694200316,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200316,  41,      15) /* RegenerationInterval */
     , (694200316,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200316,   1, 'Low Event Wave 7 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200316,   1, 0x0200026B) /* Setup */
     , (694200316,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200316, -1,  290500219, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200316, -1,  290500219, 1, 10, 10, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200316, -1,  290500219, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200316, -1,  290500219, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 11/38: Low Event Sequence/694200317 Low Event Wave 8.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200317;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200317, 'Low Event Wave 8', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200317,  81,         20) /* MaxGeneratedObjects */
     , (694200317,  82,         20) /* InitGeneratedObjects */
     , (694200317,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200317, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200317, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200317,   1, True ) /* Stuck */
     , (694200317,  11, True ) /* IgnoreCollisions */
     , (694200317,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200317,  41,      15) /* RegenerationInterval */
     , (694200317,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200317,   1, 'Low Event Wave 8 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200317,   1, 0x0200026B) /* Setup */
     , (694200317,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200317, -1,  300101045, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200317, -1,  300101045, 1,  5,  5, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200317, -1,  300101045, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200317, -1,  300101045, 1,  5,  5, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 12/38: Low Event Sequence/694200318 Low Event Wave 9.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200318;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200318, 'Low Event Wave 9', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200318,  81,         10) /* MaxGeneratedObjects */
     , (694200318,  82,         10) /* InitGeneratedObjects */
     , (694200318,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200318, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200318, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200318,   1, True ) /* Stuck */
     , (694200318,  11, True ) /* IgnoreCollisions */
     , (694200318,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200318,  41,      15) /* RegenerationInterval */
     , (694200318,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200318,   1, 'Low Event Wave 9 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200318,   1, 0x0200026B) /* Setup */
     , (694200318,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200318, -1,  290500142, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200318, -1,  290500142, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200318, -1,  290500142, 1,  5,  5, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200318, -1,  290500142, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 13/38: Low Event Sequence/694200319 Low Event Wave 10.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200319;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200319, 'Low Event Wave 10', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200319,  81,         23) /* MaxGeneratedObjects */
     , (694200319,  82,         23) /* InitGeneratedObjects */
     , (694200319,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200319, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200319, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200319,   1, True ) /* Stuck */
     , (694200319,  11, True ) /* IgnoreCollisions */
     , (694200319,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200319,  41,      15) /* RegenerationInterval */
     , (694200319,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200319,   1, 'Low Event Wave 10 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200319,   1, 0x0200026B) /* Setup */
     , (694200319,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200319, -1,  290500142, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200319, -1,  290500142, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200319, -1,  290500142, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200319, -1,  290500142, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 14/38: Low Event Sequence/694200320 Low Event Boss.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200320;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200320, 'Low Event Boss', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200320,  81,         17) /* MaxGeneratedObjects */
     , (694200320,  82,         17) /* InitGeneratedObjects */
     , (694200320,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200320, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200320, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200320,   1, True ) /* Stuck */
     , (694200320,  11, True ) /* IgnoreCollisions */
     , (694200320,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200320,  41,      15) /* RegenerationInterval */
     , (694200320,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200320,   1, 'Low Event Boss Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200320,   1, 0x0200026B) /* Setup */
     , (694200320,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200320, -1,   81000030, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200320, -1,   46687111, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200320, -1,  440531111, 1, 10, 10, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200320, -1,  290444491, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);


-- ============================================
-- Mid Event Sequence
-- ============================================

-- File 15/38: Mid Event Sequence/694200300 Mid Event Controller.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200300;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200300, 'Mid Event Controller', 10, '2026-01-11 01:58:27') /* Creature */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200300,   1,         16) /* ItemType - Creature */
     , (694200300,   2,         31) /* CreatureType - Human */
     , (694200300,   6,         -1) /* ItemsCapacity */
     , (694200300,   7,         -1) /* ContainersCapacity */
     , (694200300,  16,          1) /* ItemUseable - No */
     , (694200300,  25,        275) /* Level */
     , (694200300,  81,          1) /* MaxGeneratedObjects */
     , (694200300,  82,          1) /* InitGeneratedObjects */
     , (694200300,  93,       1040) /* PhysicsState - IgnoreCollisions, Gravity */
     , (694200300, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200300, 113,          1) /* Gender - Male */
     , (694200300, 133,          1) /* ShowableOnRadar - ShowNever */
     , (694200300, 134,         16) /* PlayerKillerStatus - RubberGlue */
     , (694200300, 145,          2) /* GeneratorEndDestructionType - Destroy */
     , (694200300, 188,          1) /* HeritageGroup - Aluvian */
     , (694200300, 290,          1) /* HearLocalSignals */
     , (694200300, 291,          5) /* HearLocalSignalsRadius */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200300,   1, True ) /* Stuck */
     , (694200300,  13, True ) /* Ethereal */
     , (694200300,  18, True ) /* Visibility */
     , (694200300,  19, False) /* Attackable */
     , (694200300,  52, True ) /* AiImmobile */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200300,   1,       5) /* HeartbeatInterval */
     , (694200300,   2,       0) /* HeartbeatTimestamp */
     , (694200300,   3,     0.9) /* HealthRate */
     , (694200300,   4,       4) /* StaminaRate */
     , (694200300,   5,       2) /* ManaRate */
     , (694200300,  12,     0.5) /* Shade */
     , (694200300,  13,    0.75) /* ArmorModVsSlash */
     , (694200300,  14,    0.57) /* ArmorModVsPierce */
     , (694200300,  15,    0.75) /* ArmorModVsBludgeon */
     , (694200300,  16,     0.5) /* ArmorModVsCold */
     , (694200300,  17,    0.75) /* ArmorModVsFire */
     , (694200300,  18,    0.86) /* ArmorModVsAcid */
     , (694200300,  19,     0.5) /* ArmorModVsElectric */
     , (694200300,  31,      23) /* VisualAwarenessRange */
     , (694200300,  34,       3) /* PowerupTime */
     , (694200300,  36,       1) /* ChargeSpeed */
     , (694200300,  41,       5) /* RegenerationInterval */
     , (694200300,  43,       0) /* GeneratorRadius */
     , (694200300,  64,    0.66) /* ResistSlash */
     , (694200300,  65,    0.85) /* ResistPierce */
     , (694200300,  66,    0.66) /* ResistBludgeon */
     , (694200300,  67,    0.25) /* ResistFire */
     , (694200300,  68,    0.45) /* ResistCold */
     , (694200300,  69,    0.65) /* ResistAcid */
     , (694200300,  70,    0.95) /* ResistElectric */
     , (694200300,  71,       1) /* ResistHealthBoost */
     , (694200300,  72,       1) /* ResistStaminaDrain */
     , (694200300,  73,       1) /* ResistStaminaBoost */
     , (694200300,  74,       1) /* ResistManaDrain */
     , (694200300,  75,       1) /* ResistManaBoost */
     , (694200300, 104,      10) /* ObviousRadarRange */
     , (694200300, 117,     0.5) /* FocusedProbability */
     , (694200300, 121,       1) /* GeneratorInitialDelay */
     , (694200300, 125,       1) /* ResistHealthDrain */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200300,   1, 'Mid Event Controller') /* Name */
     , (694200300,   5, 'Event Controller') /* Template */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200300,   1, 0x02000001) /* Setup */
     , (694200300,   2, 0x09000001) /* MotionTable */
     , (694200300,   3, 0x20000001) /* SoundTable */
     , (694200300,   6, 0x0400007E) /* PaletteBase */
     , (694200300,   8, 0x06000FF1) /* Icon */;

INSERT INTO `weenie_properties_attribute` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`)
VALUES (694200300,   1, 240, 0, 0) /* Strength */
     , (694200300,   2, 200, 0, 0) /* Endurance */
     , (694200300,   3, 250, 0, 0) /* Quickness */
     , (694200300,   4, 200, 0, 0) /* Coordination */
     , (694200300,   5, 290, 0, 0) /* Focus */
     , (694200300,   6, 290, 0, 0) /* Self */;

INSERT INTO `weenie_properties_attribute_2nd` (`object_Id`, `type`, `init_Level`, `level_From_C_P`, `c_P_Spent`, `current_Level`)
VALUES (694200300,   1,   196, 0, 0, 296) /* MaxHealth */
     , (694200300,   3,   196, 0, 0, 396) /* MaxStamina */
     , (694200300,   5,   196, 0, 0, 486) /* MaxMana */;

INSERT INTO `weenie_properties_skill` (`object_Id`, `type`, `level_From_P_P`, `s_a_c`, `p_p`, `init_Level`, `resistance_At_Last_Check`, `last_Used_Time`)
VALUES (694200300,  6, 0, 2, 0,   1, 0, 0) /* MeleeDefense        Trained */
     , (694200300,  7, 0, 2, 0,   1, 0, 0) /* MissileDefense      Trained */
     , (694200300, 13, 0, 2, 0,   1, 0, 0) /* UnarmedCombat       Trained */;

INSERT INTO `weenie_properties_body_part` (`object_Id`, `key`, `d_Type`, `d_Val`, `d_Var`, `base_Armor`, `armor_Vs_Slash`, `armor_Vs_Pierce`, `armor_Vs_Bludgeon`, `armor_Vs_Cold`, `armor_Vs_Fire`, `armor_Vs_Acid`, `armor_Vs_Electric`, `armor_Vs_Nether`, `b_h`, `h_l_f`, `m_l_f`, `l_l_f`, `h_r_f`, `m_r_f`, `l_r_f`, `h_l_b`, `m_l_b`, `l_l_b`, `h_r_b`, `m_r_b`, `l_r_b`)
VALUES (694200300,  0,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0, 0.33,    0,    0) /* Head */
     , (694200300,  1,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0, 0.44, 0.17,    0) /* Chest */
     , (694200300,  2,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0,    0, 0.17,    0) /* Abdomen */
     , (694200300,  3,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 1, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0, 0.23, 0.03,    0) /* UpperArm */
     , (694200300,  4,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0,    0,  0.3,    0) /* LowerArm */
     , (694200300,  5,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 2,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0,    0,  0.2,    0) /* Hand */
     , (694200300,  6,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18,    0, 0.13, 0.18) /* UpperLeg */
     , (694200300,  7,  4,  0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6,    0,    0,  0.6) /* LowerLeg */
     , (694200300,  8,  4,  2, 0.75,    0,    0,    0,    0,    0,    0,    0,    0,    0, 3,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22,    0,    0, 0.22) /* Foot */;

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200300, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'DeleteMe', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  77 /* DeleteSelf */, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200300, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'StartEvent', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88 /* LocalSignal - Send signal to activate Wave 1 Generator */, 0, 1, NULL, 'Wave1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200300, -1, 694200294, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Bell (where_Create = 4 = Specific) */
     , (694200300, -1, 694200321, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 1 Generator */
     , (694200300, -1, 694200322, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 2 Generator */
     , (694200300, -1, 694200323, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 3 Generator */
     , (694200300, -1, 694200324, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 4 Generator */
     , (694200300, -1, 694200325, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 5 Generator */
     , (694200300, -1, 694200326, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 6 Generator */
     , (694200300, -1, 694200327, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 7 Generator */
     , (694200300, -1, 694200328, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 8 Generator */
     , (694200300, -1, 694200329, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 9 Generator */
     , (694200300, -1, 694200330, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 10 Generator */
     , (694200300, -1, 694200331, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 11 Generator */
     , (694200300, -1, 694200295, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Exit Controller (where_Create = 4 = Specific) */;

-- File 16/38: Mid Event Sequence/694200321 Mid Event Wave 1.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200321;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200321, 'Mid Event Wave 1', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200321,  81,         15) /* MaxGeneratedObjects */
     , (694200321,  82,         15) /* InitGeneratedObjects */
     , (694200321,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200321, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200321, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200321,   1, True ) /* Stuck */
     , (694200321,  11, True ) /* IgnoreCollisions */
     , (694200321,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200321,  41,      15) /* RegenerationInterval */
     , (694200321,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200321,   1, 'Mid Event Wave 1 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200321,   1, 0x0200026B) /* Setup */
     , (694200321,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200321, -1,  290500015, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200321, -1,  290500015, 1,  5,  5, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200321, -1,  290500015, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200321, -1,  290500015, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 17/38: Mid Event Sequence/694200322 Mid Event Wave 2.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200322;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200322, 'Mid Event Wave 2', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200322,  81,          4) /* MaxGeneratedObjects */
     , (694200322,  82,          4) /* InitGeneratedObjects */
     , (694200322,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200322, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200322, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200322,   1, True ) /* Stuck */
     , (694200322,  11, True ) /* IgnoreCollisions */
     , (694200322,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200322,  41,      15) /* RegenerationInterval */
     , (694200322,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200322,   1, 'Mid Event Wave 2 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200322,   1, 0x0200026B) /* Setup */
     , (694200322,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200322, -1,  290500274, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200322, -1,  290500274, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200322, -1,  290500274, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200322, -1,  290500274, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 18/38: Mid Event Sequence/694200323 Mid Event Wave 3.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200323;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200323, 'Mid Event Wave 3', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200323,  81,         17) /* MaxGeneratedObjects */
     , (694200323,  82,         17) /* InitGeneratedObjects */
     , (694200323,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200323, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200323, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200323,   1, True ) /* Stuck */
     , (694200323,  11, True ) /* IgnoreCollisions */
     , (694200323,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200323,  41,      15) /* RegenerationInterval */
     , (694200323,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200323,   1, 'Mid Event Wave 3 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200323,   1, 0x0200026B) /* Setup */
     , (694200323,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200323, -1,  290500179, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200323, -1,  290500179, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200323, -1,  290500179, 1,  5,  5, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200323, -1,  290500179, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 19/38: Mid Event Sequence/694200324 Mid Event Wave 4.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200324;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200324, 'Mid Event Wave 4', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200324,  81,         26) /* MaxGeneratedObjects */
     , (694200324,  82,         26) /* InitGeneratedObjects */
     , (694200324,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200324, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200324, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200324,   1, True ) /* Stuck */
     , (694200324,  11, True ) /* IgnoreCollisions */
     , (694200324,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200324,  41,      15) /* RegenerationInterval */
     , (694200324,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200324,   1, 'Mid Event Wave 4 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200324,   1, 0x0200026B) /* Setup */
     , (694200324,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200324, -1,    3001008, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200324, -1,    3001008, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200324, -1,    3001008, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200324, -1,    3001008, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 20/38: Mid Event Sequence/694200325 Mid Event Wave 5.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200325;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200325, 'Mid Event Wave 5', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200325,  81,         13) /* MaxGeneratedObjects */
     , (694200325,  82,         13) /* InitGeneratedObjects */
     , (694200325,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200325, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200325, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200325,   1, True ) /* Stuck */
     , (694200325,  11, True ) /* IgnoreCollisions */
     , (694200325,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200325,  41,      15) /* RegenerationInterval */
     , (694200325,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200325,   1, 'Mid Event Wave 5 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200325,   1, 0x0200026B) /* Setup */
     , (694200325,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200325, -1,    8814694, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200325, -1,    8814694, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200325, -1,    8814694, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200325, -1,    8814694, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 21/38: Mid Event Sequence/694200326 Mid Event Wave 6.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200326;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200326, 'Mid Event Wave 6', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200326,  81,         15) /* MaxGeneratedObjects */
     , (694200326,  82,         15) /* InitGeneratedObjects */
     , (694200326,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200326, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200326, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200326,   1, True ) /* Stuck */
     , (694200326,  11, True ) /* IgnoreCollisions */
     , (694200326,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200326,  41,      15) /* RegenerationInterval */
     , (694200326,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200326,   1, 'Mid Event Wave 6 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200326,   1, 0x0200026B) /* Setup */
     , (694200326,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200326, -1,  290500089, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200326, -1,  290500089, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200326, -1,  290500089, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200326, -1,  290500089, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 22/38: Mid Event Sequence/694200327 Mid Event Wave 7.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200327;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200327, 'Mid Event Wave 7', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200327,  81,          4) /* MaxGeneratedObjects */
     , (694200327,  82,          4) /* InitGeneratedObjects */
     , (694200327,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200327, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200327, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200327,   1, True ) /* Stuck */
     , (694200327,  11, True ) /* IgnoreCollisions */
     , (694200327,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200327,  41,      15) /* RegenerationInterval */
     , (694200327,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200327,   1, 'Mid Event Wave 7 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200327,   1, 0x0200026B) /* Setup */
     , (694200327,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200327, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200327, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200327, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200327, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 23/38: Mid Event Sequence/694200328 Mid Event Wave 8.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200328;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200328, 'Mid Event Wave 8', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200328,  81,          4) /* MaxGeneratedObjects */
     , (694200328,  82,          4) /* InitGeneratedObjects */
     , (694200328,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200328, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200328, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200328,   1, True ) /* Stuck */
     , (694200328,  11, True ) /* IgnoreCollisions */
     , (694200328,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200328,  41,      15) /* RegenerationInterval */
     , (694200328,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200328,   1, 'Mid Event Wave 8 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200328,   1, 0x0200026B) /* Setup */
     , (694200328,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200328, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200328, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200328, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200328, -1,  290500025, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 24/38: Mid Event Sequence/694200329 Mid Event Wave 9.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200329;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200329, 'Mid Event Wave 9', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200329,  81,         12) /* MaxGeneratedObjects */
     , (694200329,  82,         12) /* InitGeneratedObjects */
     , (694200329,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200329, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200329, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200329,   1, True ) /* Stuck */
     , (694200329,  11, True ) /* IgnoreCollisions */
     , (694200329,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200329,  41,      15) /* RegenerationInterval */
     , (694200329,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200329,   1, 'Mid Event Wave 9 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200329,   1, 0x0200026B) /* Setup */
     , (694200329,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200329, -1,  290500015, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200329, -1,  290500015, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200329, -1,  290500015, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200329, -1,  290500015, 1,  5,  5, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 25/38: Mid Event Sequence/694200330 Mid Event Wave 10.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200330;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200330, 'Mid Event Wave 10', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200330,  81,         26) /* MaxGeneratedObjects */
     , (694200330,  82,         26) /* InitGeneratedObjects */
     , (694200330,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200330, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200330, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200330,   1, True ) /* Stuck */
     , (694200330,  11, True ) /* IgnoreCollisions */
     , (694200330,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200330,  41,      15) /* RegenerationInterval */
     , (694200330,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200330,   1, 'Mid Event Wave 10 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200330,   1, 0x0200026B) /* Setup */
     , (694200330,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200330, -1,     601669, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200330, -1,     601669, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200330, -1,     601669, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200330, -1,     601669, 1, 10, 10, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 26/38: Mid Event Sequence/694200331 Mid Event Boss.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200331;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200331, 'Mid Event Boss', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200331,  81,         12) /* MaxGeneratedObjects */
     , (694200331,  82,         12) /* InitGeneratedObjects */
     , (694200331,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200331, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200331, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200331,   1, True ) /* Stuck */
     , (694200331,  11, True ) /* IgnoreCollisions */
     , (694200331,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200331,  41,      15) /* RegenerationInterval */
     , (694200331,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200331,   1, 'Mid Event Boss Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200331,   1, 0x0200026B) /* Setup */
     , (694200331,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200331, -1,  290500064, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200331, -1,  290500119, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200331, -1,   36826001, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200331, -1,  290500041, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);


-- ============================================
-- High Event Sequence
-- ============================================

-- File 27/38: High Event Sequence/694200304 High Event Controller.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200304;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200304, 'High Event Controller', 10, '2026-01-11 01:58:27') /* Creature */;

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

INSERT INTO `weenie_properties_emote` (`object_Id`, `category`, `probability`, `weenie_Class_Id`, `style`, `substyle`, `quest`, `vendor_Type`, `min_Health`, `max_Health`)
VALUES (694200304, 37 /* ReceiveLocalSignal */,      1, NULL, NULL, NULL, 'StartEvent', NULL, NULL, NULL);

SET @parent_id = LAST_INSERT_ID();

INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id,  0,  88 /* LocalSignal - Send signal to activate Wave 1 Generator */, 0, 1, NULL, 'Wave1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200304, -1, 694200294, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Bell (where_Create = 4 = Specific) */
     , (694200304, -1, 694200332, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 1 Generator */
     , (694200304, -1, 694200333, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 2 Generator */
     , (694200304, -1, 694200334, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 3 Generator */
     , (694200304, -1, 694200335, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 4 Generator */
     , (694200304, -1, 694200336, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 5 Generator */
     , (694200304, -1, 694200337, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 6 Generator */
     , (694200304, -1, 694200338, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 7 Generator */
     , (694200304, -1, 694200339, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 8 Generator */
     , (694200304, -1, 694200340, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 9 Generator */
     , (694200304, -1, 694200341, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 10 Generator */
     , (694200304, -1, 694200342, 1600, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wave 11 Generator */
     , (694200304, -1, 694200295, 1600, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Event Exit Controller (where_Create = 4 = Specific) */;

-- File 28/38: High Event Sequence/694200332 High Event Wave 1.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200332;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200332, 'High Event Wave 1', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200332,  81,          4) /* MaxGeneratedObjects */
     , (694200332,  82,          4) /* InitGeneratedObjects */
     , (694200332,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200332, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200332, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200332,   1, True ) /* Stuck */
     , (694200332,  11, True ) /* IgnoreCollisions */
     , (694200332,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200332,  41,      15) /* RegenerationInterval */
     , (694200332,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200332,   1, 'High Event Wave 1 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200332,   1, 0x0200026B) /* Setup */
     , (694200332,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200332, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200332, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200332, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200332, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 29/38: High Event Sequence/694200333 High Event Wave 2.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200333;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200333, 'High Event Wave 2', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200333,  81,          4) /* MaxGeneratedObjects */
     , (694200333,  82,          4) /* InitGeneratedObjects */
     , (694200333,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200333, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200333, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200333,   1, True ) /* Stuck */
     , (694200333,  11, True ) /* IgnoreCollisions */
     , (694200333,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200333,  41,      15) /* RegenerationInterval */
     , (694200333,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200333,   1, 'High Event Wave 2 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200333,   1, 0x0200026B) /* Setup */
     , (694200333,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200333, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200333, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200333, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200333, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 30/38: High Event Sequence/694200334 High Event Wave 3.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200334;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200334, 'High Event Wave 3', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200334,  81,         26) /* MaxGeneratedObjects */
     , (694200334,  82,         26) /* InitGeneratedObjects */
     , (694200334,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200334, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200334, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200334,   1, True ) /* Stuck */
     , (694200334,  11, True ) /* IgnoreCollisions */
     , (694200334,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200334,  41,      15) /* RegenerationInterval */
     , (694200334,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200334,   1, 'High Event Wave 3 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200334,   1, 0x0200026B) /* Setup */
     , (694200334,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200334, -1,  290500551, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200334, -1,  290500551, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200334, -1,  290500551, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200334, -1,  290500551, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 31/38: High Event Sequence/694200335 High Event Wave 4.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200335;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200335, 'High Event Wave 4', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200335,  81,          4) /* MaxGeneratedObjects */
     , (694200335,  82,          4) /* InitGeneratedObjects */
     , (694200335,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200335, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200335, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200335,   1, True ) /* Stuck */
     , (694200335,  11, True ) /* IgnoreCollisions */
     , (694200335,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200335,  41,      15) /* RegenerationInterval */
     , (694200335,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200335,   1, 'High Event Wave 4 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200335,   1, 0x0200026B) /* Setup */
     , (694200335,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200335, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200335, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200335, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200335, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 32/38: High Event Sequence/694200336 High Event Wave 5.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200336;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200336, 'High Event Wave 5', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200336,  81,         19) /* MaxGeneratedObjects */
     , (694200336,  82,         19) /* InitGeneratedObjects */
     , (694200336,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200336, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200336, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200336,   1, True ) /* Stuck */
     , (694200336,  11, True ) /* IgnoreCollisions */
     , (694200336,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200336,  41,      15) /* RegenerationInterval */
     , (694200336,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200336,   1, 'High Event Wave 5 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200336,   1, 0x0200026B) /* Setup */
     , (694200336,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200336, -1,  290500118, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200336, -1,  290500118, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200336, -1,  290500118, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200336, -1,  290500118, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 33/38: High Event Sequence/694200337 High Event Wave 6.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200337;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200337, 'High Event Wave 6', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200337,  81,         30) /* MaxGeneratedObjects */
     , (694200337,  82,         30) /* InitGeneratedObjects */
     , (694200337,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200337, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200337, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200337,   1, True ) /* Stuck */
     , (694200337,  11, True ) /* IgnoreCollisions */
     , (694200337,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200337,  41,      15) /* RegenerationInterval */
     , (694200337,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200337,   1, 'High Event Wave 6 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200337,   1, 0x0200026B) /* Setup */
     , (694200337,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200337, -1,  290500551, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200337, -1,  290500551, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200337, -1,  290500551, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200337, -1,  290500551, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 34/38: High Event Sequence/694200338 High Event Wave 7.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200338;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200338, 'High Event Wave 7', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200338,  81,          4) /* MaxGeneratedObjects */
     , (694200338,  82,          4) /* InitGeneratedObjects */
     , (694200338,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200338, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200338, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200338,   1, True ) /* Stuck */
     , (694200338,  11, True ) /* IgnoreCollisions */
     , (694200338,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200338,  41,      15) /* RegenerationInterval */
     , (694200338,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200338,   1, 'High Event Wave 7 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200338,   1, 0x0200026B) /* Setup */
     , (694200338,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200338, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200338, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200338, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200338, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 35/38: High Event Sequence/694200339 High Event Wave 8.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200339;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200339, 'High Event Wave 8', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200339,  81,          4) /* MaxGeneratedObjects */
     , (694200339,  82,          4) /* InitGeneratedObjects */
     , (694200339,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200339, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200339, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200339,   1, True ) /* Stuck */
     , (694200339,  11, True ) /* IgnoreCollisions */
     , (694200339,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200339,  41,      15) /* RegenerationInterval */
     , (694200339,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200339,   1, 'High Event Wave 8 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200339,   1, 0x0200026B) /* Setup */
     , (694200339,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200339, -1,  146410001, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200339, -1,  146410001, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200339, -1,  146410001, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200339, -1,  146410001, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 36/38: High Event Sequence/694200340 High Event Wave 9.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200340;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200340, 'High Event Wave 9', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200340,  81,          4) /* MaxGeneratedObjects */
     , (694200340,  82,          4) /* InitGeneratedObjects */
     , (694200340,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200340, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200340, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200340,   1, True ) /* Stuck */
     , (694200340,  11, True ) /* IgnoreCollisions */
     , (694200340,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200340,  41,      15) /* RegenerationInterval */
     , (694200340,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200340,   1, 'High Event Wave 9 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200340,   1, 0x0200026B) /* Setup */
     , (694200340,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200340, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200340, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200340, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200340, -1,  290500012, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 37/38: High Event Sequence/694200341 High Event Wave 10.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200341;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200341, 'High Event Wave 10', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200341,  81,          4) /* MaxGeneratedObjects */
     , (694200341,  82,          4) /* InitGeneratedObjects */
     , (694200341,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200341, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200341, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200341,   1, True ) /* Stuck */
     , (694200341,  11, True ) /* IgnoreCollisions */
     , (694200341,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200341,  41,      15) /* RegenerationInterval */
     , (694200341,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200341,   1, 'High Event Wave 10 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200341,   1, 0x0200026B) /* Setup */
     , (694200341,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200341, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200341, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200341, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200341, -1,  290500094, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);

-- File 38/38: High Event Sequence/694200342 High Event Boss.sql
-- ============================================================
DELETE FROM `weenie` WHERE `class_Id` = 694200342;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200342, 'High Event Boss', 1, '2026-01-11 01:58:27') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200342,  81,          7) /* MaxGeneratedObjects */
     , (694200342,  82,          7) /* InitGeneratedObjects */
     , (694200342,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200342, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200342, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200342,   1, True ) /* Stuck */
     , (694200342,  11, True ) /* IgnoreCollisions */
     , (694200342,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200342,  41,      15) /* RegenerationInterval */
     , (694200342,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200342,   1, 'High Event Boss Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200342,   1, 0x0200026B) /* Setup */
     , (694200342,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200342, -1,  290500002, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster */
         , (694200342, -1,  290500550, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster */
         , (694200342, -1, 2904444721, 1,  2,  2, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster */
         , (694200342, -1,  300101054, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0103,  14.977105,  -14.885592,  0.005000,  -0.388751,    0.0,    0.0,   0.921343);


-- ============================================
-- End of Bulk Upload
-- ============================================
