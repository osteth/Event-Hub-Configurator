DELETE FROM `weenie` WHERE `class_Id` = 694201359;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694201359, 'Mid Event Wave 5 Position 0 Generator', 1, '2026-01-12 15:21:57') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694201359,  81,          4) /* MaxGeneratedObjects */
     , (694201359,  82,          4) /* InitGeneratedObjects */
     , (694201359,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694201359, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694201359, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694201359,   1, True ) /* Stuck */
     , (694201359,  11, True ) /* IgnoreCollisions */
     , (694201359,  18, True ) /* Visibility */
     , (694201359,  59, False ) /* GeneratorDisabled - Enable generator on creation */
     , (694201359,  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all mobs are killed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694201359,  41,      15) /* RegenerationInterval */
     , (694201359,  43,       5) /* GeneratorRadius - Tight scatter around position */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694201359,   1, 'Mid Event Wave 5 Position 0 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694201359,   1, 0x0200026B) /* Setup */
     , (694201359,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694201359, -1,  290500179, 1,  4,  4, 1, 2, -1, 0, 0, 0, 0.000000, 0.000000, 0.000000,   0.939595,    0.0,    0.0,  -0.342288); /* Generate Monster - Scatter around generator location */

