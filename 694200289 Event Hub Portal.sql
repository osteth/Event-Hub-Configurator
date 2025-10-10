DELETE FROM `weenie` WHERE `class_Id` = 694200289;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200289, 'Event Hub Portal', 7, '2021-11-08 06:01:47') /* Portal */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200289,   1,      65536) /* ItemType - Portal */
     , (694200289,  16,         32) /* ItemUseable - Remote */
     , (694200289,  86,        100) /* MinLevel */
     , (694200289,  93,       3084) /* PhysicsState - Ethereal, ReportCollisions, Gravity, LightingOn */
     , (694200289, 111,         49) /* PortalBitmask - Unrestricted, NoSummon, NoRecall */
     , (694200289, 133,          4) /* ShowableOnRadar - ShowAlways */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200289,   1, True ) /* Stuck */
     , (694200289,  11, False) /* IgnoreCollisions */
     , (694200289,  12, True ) /* ReportCollisions */
     , (694200289,  13, True ) /* Ethereal */
     , (694200289,  15, True ) /* LightsStatus */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200289,  54,    -0.1) /* UseRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200289,   1, 'Event Portal') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200289,   1, 0x020005D5) /* Setup */
     , (694200289,   2, 0x09000003) /* MotionTable */
     , (694200289,   8, 0x0600106B) /* Icon */;

INSERT INTO `weenie_properties_position` (`object_Id`, `position_Type`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`, `variation_Id`)
VALUES (694200289, 2, 0x02940101, -0.891188, -70.121735, 0.005000, -0.700158, 0, 0, 0.713988, 2) /* Destination */
/* @teleloc     0x02940101 [-0.891188 -70.121735 0.005000] -0.700158 0.000000 0.000000 0.713988  */;

