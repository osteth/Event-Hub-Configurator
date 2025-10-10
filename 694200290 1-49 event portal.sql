DELETE FROM `weenie` WHERE `class_Id` = 694200290;

INSERT INTO `weenie` (`class_Id`, `class_Name`, `type`, `last_Modified`)
VALUES (694200290, '1-49 ENL Event Portal', 7, '2021-11-08 06:01:47') /* Portal */;

INSERT INTO `weenie_properties_int` (`object_Id`, `type`, `value`)
VALUES (694200290,   1,      65536) /* ItemType - Portal */
     , (694200290,  16,         32) /* ItemUseable - Remote */
     , (694200290,  86,        100) /* MinLevel */
     , (694200290,  93,       3084) /* PhysicsState - Ethereal, ReportCollisions, Gravity, LightingOn */
     , (694200290, 111,         49) /* PortalBitmask - Unrestricted, NoSummon, NoRecall */
     , (694200290, 133,          4) /* ShowableOnRadar - ShowAlways */
	 , (694200290, 9019,          4) /* PortalReqType */
     , (694200290, 9020,         1) /* PortalReqValue */
     , (694200290, 9021,        49) /* PortalReqMaxValue */;

INSERT INTO `weenie_properties_bool` (`object_Id`, `type`, `value`)
VALUES (694200290,   1, True ) /* Stuck */
     , (694200290,  11, False) /* IgnoreCollisions */
     , (694200290,  12, True ) /* ReportCollisions */
     , (694200290,  13, True ) /* Ethereal */
     , (694200290,  15, True ) /* LightsStatus */;

INSERT INTO `weenie_properties_float` (`object_Id`, `type`, `value`)
VALUES (694200290,  54,    -0.1) /* UseRadius */;

INSERT INTO `weenie_properties_string` (`object_Id`, `type`, `value`)
VALUES (694200290,   1, '1-49 ENL Event Portal') /* Name */;

INSERT INTO `weenie_properties_d_i_d` (`object_Id`, `type`, `value`)
VALUES (694200290,   1, 0x020005D5) /* Setup */
     , (694200290,   2, 0x09000003) /* MotionTable */
     , (694200290,   8, 0x0600106B) /* Icon */;

INSERT INTO `weenie_properties_position` (`object_Id`, `position_Type`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`, `variation_Id`)
VALUES (694200290, 2, 0x02BF015A, 29.765373, -37.349480, 18.004999, -0.015889, 0, 0, 0.999874, 2) /* Destination */
/* @teleloc    0x02BF015A [29.765373 -37.349480 18.004999] -0.015889 0.000000 0.000000 0.999874  */;

