DELETE FROM `weenie` WHERE `class_Id` = 694200319;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200319, 'Low Event Wave 10', 1, '2026-01-11 21:17:45') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200319,  81,         24) /* MaxGeneratedObjects */
     , (694200319,  82,         24) /* InitGeneratedObjects */
     , (694200319,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200319, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200319, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200319,   1, True ) /* Stuck */
     , (694200319,  11, True ) /* IgnoreCollisions */
     , (694200319,  18, True ) /* Visibility */
     , (694200319,  59, False ) /* GeneratorDisabled - Enable generator on creation */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200319,  41,      15) /* RegenerationInterval */
     , (694200319,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200319,   1, 'Low Event Wave 10 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200319,   1, 0x0200026B) /* Setup */
     , (694200319,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200319, -1,   46687111, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster - Specific position (physics engine will find valid nearby position if needed) */
         , (694200319, -1,  290500142, 1,  7,  7, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster - Specific position (physics engine will find valid nearby position if needed) */
         , (694200319, -1,    3512411, 1,  8,  8, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster - Specific position (physics engine will find valid nearby position if needed) */
         , (694200319, -1,   16071234, 1,  6,  6, 1, 4, -1, 0, 0, 0x2bf0104,  14.955328,  -15.005316,  0.005000,  -0.421018,    0.0,    0.0,   0.907052);
