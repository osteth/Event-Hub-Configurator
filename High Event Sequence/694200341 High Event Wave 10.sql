DELETE FROM `weenie` WHERE `class_Id` = 694200341;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200341, 'High Event Wave 10', 1, '2025-10-10 02:04:14') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200341,  81,         10) /* MaxGeneratedObjects */
     , (694200341,  82,          8) /* InitGeneratedObjects */
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
VALUES (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200341, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0);
