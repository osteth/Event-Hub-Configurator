DELETE FROM `weenie` WHERE `class_Id` = 694200322;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200322, 'Mid Event Wave 2', 1, '2025-10-10 02:04:14') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200322,  81,         10) /* MaxGeneratedObjects */
     , (694200322,  82,          8) /* InitGeneratedObjects */
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
VALUES (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Monster */
         , (694200322, -1,     123456, 1, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0);
