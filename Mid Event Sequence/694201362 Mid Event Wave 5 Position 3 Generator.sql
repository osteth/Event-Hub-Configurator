DELETE FROM `weenie` WHERE `class_Id` = 694201362;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694201362, 'Mid Event Wave 5 Position 3 Generator', 1, '2026-01-12 15:21:57') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694201362,  81,          7) /* MaxGeneratedObjects */
     , (694201362,  82,          7) /* InitGeneratedObjects */
     , (694201362,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694201362, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694201362, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694201362,   1, True ) /* Stuck */
     , (694201362,  11, True ) /* IgnoreCollisions */
     , (694201362,  18, True ) /* Visibility */
     , (694201362,  59, False ) /* GeneratorDisabled - Enable generator on creation */
     , (694201362,  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all mobs are killed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694201362,  41,      15) /* RegenerationInterval */
     , (694201362,  43,       5) /* GeneratorRadius - Tight scatter around position */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694201362,   1, 'Mid Event Wave 5 Position 3 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694201362,   1, 0x0200026B) /* Setup */
     , (694201362,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694201362, -1,  290500041, 1,  7,  7, 1, 2, -1, 0, 0, 0, 0.000000, 0.000000, 0.000000,  -0.421018,    0.0,    0.0,   0.907052); /* Generate Monster - Scatter around generator location */

