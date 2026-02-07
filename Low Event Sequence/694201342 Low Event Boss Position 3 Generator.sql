DELETE FROM `weenie` WHERE `class_Id` = 694201342;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694201342, 'Low Event Boss Position 3 Generator', 1, '2026-01-12 15:21:57') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694201342,  81,         10) /* MaxGeneratedObjects */
     , (694201342,  82,         10) /* InitGeneratedObjects */
     , (694201342,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694201342, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694201342, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694201342,   1, True ) /* Stuck */
     , (694201342,  11, True ) /* IgnoreCollisions */
     , (694201342,  18, True ) /* Visibility */
     , (694201342,  59, False ) /* GeneratorDisabled - Enable generator on creation */
     , (694201342,  74, True ) /* GeneratorAutomaticDestruction - Auto-destroy when all mobs are killed */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694201342,  41,      15) /* RegenerationInterval */
     , (694201342,  43,       5) /* GeneratorRadius - Tight scatter around position */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694201342,   1, 'Low Event Boss Position 3 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694201342,   1, 0x0200026B) /* Setup */
     , (694201342,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694201342, -1,  300101053, 1, 10, 10, 1, 2, -1, 0, 0, 0, 0.000000, 0.000000, 0.000000,  -0.421018,    0.0,    0.0,   0.907052); /* Generate Monster - Scatter around generator location */

