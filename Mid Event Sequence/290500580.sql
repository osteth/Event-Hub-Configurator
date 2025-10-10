DELETE FROM `weenie` WHERE `class_Id` = 290500580;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (290500580, 'Open Chest Big Boss', 20, '2005-02-09 10:00:00') /* Chest */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (290500580,   1,        512) /* ItemType - Container */
     , (290500580,   5,       6000) /* EncumbranceVal */
     , (290500580,   6,         -1) /* ItemsCapacity */
     , (290500580,   7,         -1) /* ContainersCapacity */
     , (290500580,   8,       3000) /* Mass */
     , (290500580,  16,         48) /* ItemUseable - ViewedRemote */
     , (290500580,  19,        200) /* Value */
     , (290500580,  81,         10) /* MaxGeneratedObjects */
     , (290500580,  82,          2) /* InitGeneratedObjects */
     , (290500580,  83,          2) /* ActivationResponse - Use */
     , (290500580,  93,       1048) /* PhysicsState - ReportCollisions, IgnoreCollisions, Gravity */
     , (290500580,  96,      50000) /* EncumbranceCapacity */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (290500580,   1, True ) /* Stuck */
     , (290500580,   2, False) /* Open */
     , (290500580,  12, True ) /* ReportCollisions */
     , (290500580,  13, False) /* Ethereal */
     , (290500580,  33, False) /* ResetMessagePending */
     , (290500580,  34, False) /* DefaultOpen */
     , (290500580,  86, True ) /* ChestRegenOnClose */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (290500580,  41,      60) /* RegenerationInterval */
     , (290500580,  54,       1) /* UseRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (290500580,   1, 'Big Bosses Enlightenment Chest') /* Name */
     , (290500580,  14, 'Use this item to open it and see its contents.') /* Use */
     , (290500580,  33, 'Big_Boss_Enlightenment_Chest') /* Quest */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (290500580,   1, 0x0200007C) /* Setup */
     , (290500580,   2, 0x09000004) /* MotionTable */
     , (290500580,   3, 0x20000021) /* SoundTable */
     , (290500580,   8, 0x06001022) /* Icon */
     , (290500580,  22, 0x3400002B) /* PhysicsEffectTable */;

INSERT INTO `weenie_properties_create_list` (`object_Id`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`)
VALUES (290500580, 9, 300000,  0, 0, 1, False) /* Create Enlightenment Token (300000) for ContainTreasure */
     , (290500580, 9, 3110335,  0, 0, 1, False) /* Create Part of a Medallion (3110335) for ContainTreasure */;

