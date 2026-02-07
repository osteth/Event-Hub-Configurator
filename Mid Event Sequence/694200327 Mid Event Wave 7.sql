DELETE FROM `weenie` WHERE `class_Id` = 694200327;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200327, 'Mid Event Wave 7', 1, '2026-01-11 21:17:45') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200327,  81,         17) /* MaxGeneratedObjects */
     , (694200327,  82,         17) /* InitGeneratedObjects */
     , (694200327,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200327, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200327, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200327,   1, True ) /* Stuck */
     , (694200327,  11, True ) /* IgnoreCollisions */
     , (694200327,  18, True ) /* Visibility */
     , (694200327,  59, False ) /* GeneratorDisabled - Enable generator on creation */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200327,  41,      15) /* RegenerationInterval */
     , (694200327,  43,      30) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200327,   1, 'Mid Event Wave 7 Gen') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200327,   1, 0x0200026B) /* Setup */
     , (694200327,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200327, -1,  290500041, 1,  9,  9, 1, 4, -1, 0, 0, 0x2bf010d,  15.039770,  -45.088928,  0.005000,   0.939595,    0.0,    0.0,  -0.342288) /* Generate Monster - Specific position (physics engine will find valid nearby position if needed) */
         , (694200327, -1,  290444502, 1,  1,  1, 1, 4, -1, 0, 0, 0x2bf0116,  44.864212,  -43.889206,  0.005000,   0.899738,    0.0,    0.0,   0.436431) /* Generate Monster - Specific position (physics engine will find valid nearby position if needed) */
         , (694200327, -1,  290500015, 1,  4,  4, 1, 4, -1, 0, 0, 0x2bf0113,  44.843174,  -14.990232,  0.005000,   0.384014,    0.0,    0.0,   0.923327) /* Generate Monster - Specific position (physics engine will find valid nearby position if needed) */
         , (694200327, -1,  290500015, 1,  3,  3, 1, 4, -1, 0, 0, 0x2bf0104,  14.955328,  -15.005316,  0.005000,  -0.421018,    0.0,    0.0,   0.907052);
