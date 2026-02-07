DELETE FROM `weenie` WHERE `class_Id` = 694201317;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694201317, 'Low Event Wave 5 Position 2 Generator', 1, '2026-01-12 15:21:57') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694201317,  81,          8) /* MaxGeneratedObjects */
     , (694201317,  82,          8) /* InitGeneratedObjects */
     , (694201317,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694201317, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694201317, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694201317,   1, True ) /* Stuck */
     , (694201317,  11, True ) /* IgnoreCollisions */
     , (694201317,  18, True ) /* Visibility */
     , (694201317,  59, False ) /* GeneratorDisabled - Enable generator on creation */
     , (694201317,  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all mobs are killed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694201317,  41,      15) /* RegenerationInterval */
     , (694201317,  43,       5) /* GeneratorRadius - Tight scatter around position */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694201317,   1, 'Low Event Wave 5 Position 2 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694201317,   1, 0x0200026B) /* Setup */
     , (694201317,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694201317, -1,  290500221, 1,  8,  8, 1, 2, -1, 0, 0, 0, 0.000000, 0.000000, 0.000000,   0.384014,    0.0,    0.0,   0.923327); /* Generate Monster - Scatter around generator location */

