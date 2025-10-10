DELETE FROM `weenie` WHERE `class_Id` = 694200302;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200302, 'Mid event Boss generator', 1, '2022-03-31 06:02:40') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200302,  81,         10) /* MaxGeneratedObjects */
     , (694200302,  82,          8) /* InitGeneratedObjects */
     , (694200302,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */
     , (694200302, 103,          2) /* GeneratorDestructionType - Destroy */
     , (694200302, 145,          2) /* GeneratorEndDestructionType - Destroy */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200302,   1, True ) /* Stuck */
     , (694200302,  11, True ) /* IgnoreCollisions */
     , (694200302,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200302,  41,      15) /* RegenerationInterval */
     , (694200302,  43,      50) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200302,   1, 'Mid event Boss') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200302,   1, 0x0200026B) /* Setup */
     , (694200302,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (694200302, -1, 290500147, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient Crystal (290500279) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
	 , (694200302, -1, 290500148, 1600, 1, 1, 1, 20, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Halaetan Ancient chunk (290500148) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */;

