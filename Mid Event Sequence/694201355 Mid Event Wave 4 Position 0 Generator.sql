DELETE FROM `weenie` WHERE `class_Id` = 694201355;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694201355, 'Mid Event Wave 4 Position 0 Generator', 1, '2026-01-12 15:21:57') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694201355,  81,          5) /* MaxGeneratedObjects */
     , (694201355,  82,          5) /* InitGeneratedObjects */
     , (694201355,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694201355, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694201355, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694201355,   1, True ) /* Stuck */
     , (694201355,  11, True ) /* IgnoreCollisions */
     , (694201355,  18, True ) /* Visibility */
     , (694201355,  59, False ) /* GeneratorDisabled - Enable generator on creation */
     , (694201355,  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all mobs are killed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694201355,  41,      15) /* RegenerationInterval */
     , (694201355,  43,       5) /* GeneratorRadius - Tight scatter around position */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694201355,   1, 'Mid Event Wave 4 Position 0 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694201355,   1, 0x0200026B) /* Setup */
     , (694201355,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694201355, -1,  290444492, 1,  5,  5, 1, 2, -1, 0, 0, 0, 0.000000, 0.000000, 0.000000,   0.939595,    0.0,    0.0,  -0.342288); /* Generate Monster - Scatter around generator location */

