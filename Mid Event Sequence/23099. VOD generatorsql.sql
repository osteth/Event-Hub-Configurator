DELETE FROM `weenie` WHERE `class_Id` = 23099;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (23099, 'deathvalleygenerator', 1, '2021-11-17 16:56:08') /* Generic */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (23099,  81,          1) /* MaxGeneratedObjects */
     , (23099,  82,          1) /* InitGeneratedObjects */
     , (23099,  93,       1044) /* PhysicsState - Ethereal, IgnoreCollisions, Gravity */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (23099,   1, True ) /* Stuck */
     , (23099,  11, True ) /* IgnoreCollisions */
     , (23099,  18, True ) /* Visibility */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (23099,  41,     600) /* RegenerationInterval */
     , (23099,  43,       3) /* GeneratorRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (23099,   1, 'Death Valley Generator') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (23099,   1, 0x0200026B) /* Setup */
     , (23099,   8, 0x06001066) /* Icon */;

INSERT INTO `weenie_properties_generator` (`object_Id`, `probability`, `weenie_Class_Id`, `delay`, `init_Create`, `max_Create`, `when_Create`, `where_Create`, `stack_Size`, `palette_Id`, `shade`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (23099, 0.005, 300101023, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate SwarthyGen (300101023) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.01, 300101025, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate oblitGen (300101025) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.015, 300101024, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate TremendousGen (300101024) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.04, 23103, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Olthoi Generator (23103) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.07, 90000115, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Mythical Valley Weapons Chest (90000115) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.1, 90000116, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Mythical Valley Armor Chest (90000116) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.13, 23105, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Tumerok Generator (23105) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.15, 46284, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Bloodroot Vine (46284) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.175, 23100, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Drudge Generator (23100) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.205, 23104, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Shadow Generator (23104) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.235, 23102, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Lugian Generator (23102) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.265, 23098, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Banderling Generator (23098) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.295, 23106, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Undead Generator (23106) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.325, 23101, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Grievver Generator (23101) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.355, 10614684, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Bile Grievver (10614684) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.385, 10614682, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Void Knight (10614682) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.41, 10614681, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Wretched (10614681) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.46, 23087, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Raider Justicar (23087) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.49, 23088, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Raider Prefect (23088) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.525, 10614679, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Transcendent Tumerok (10614679) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.555, 10614680, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Revered Tumerok Shaman (10614680) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.585, 10614695, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Dark Guardian (10614695) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.605, 10614694, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Lich Oppressor (10614694) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.645, 23098, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Banderling Generator (23098) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.675, 23100, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Drudge Generator (23100) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.705, 23568, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Dreadful Ursuin (23568) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.735, 7133, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Titanium Armoredillo Camp Generator (7133) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.745, 23550, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Platinum Golem Mountain King (23550) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.775, 34572, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Shadowy Statue of the Hopeslayer (34572) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.8, 23587, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Knath Generator (23587) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.83, 23588, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Virindi Paradox Generator (23588) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.86, 23589, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Virindi Quidiox Generator (23589) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.89, 71041, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Shadow-Touched Virindi Paradox Generator (71041) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.91, 71042, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Shadow-Touched Virindi Quidiox Generator (71042) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.945, 23586, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Death Valley Gromnie Generator (23586) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.965, 10614676, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Sentient Crystal Shard (10614676) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.97, 30886, 1800, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Fallen Tumerok (30886) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.975, 10614678, 1800, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Fallen Shadow (10614678) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.98, 30888, 1800, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Fallen Grievver (30888) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.985, 30889, 1800, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Fallen Crystal Shard (30889) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.99, 30890, 1800, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Fallen Lugian (30890) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.995, 30891, 1800, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Fallen Drudge (30891) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 0.996, 290500559, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Valley Shark (290500559) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */
     , (23099, 1, 31688, 900, 1, 1, 1, 2, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0) /* Generate Red Monster Seed (31688) (x1 up to max of 1) - Regenerate upon Destruction - Location to (re)Generate: Scatter */;

