#!/usr/bin/env python3
"""Test script to verify validator fix is working"""

import sys
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Clear any cached modules
if 'validate_sql' in sys.modules:
    del sys.modules['validate_sql']
if 'core.validator' in sys.modules:
    del sys.modules['core.validator']

from validate_sql import SQLValidator

# Test with a known bad INSERT (row 2 has wrong value count)
test_sql = """INSERT INTO `weenie_properties_emote_action` (`emote_Id`, `order`, `type`, `delay`, `extent`, `motion`, `message`, `test_String`, `min`, `max`, `min_64`, `max_64`, `min_Dbl`, `max_Dbl`, `stat`, `display`, `amount`, `amount_64`, `hero_X_P_64`, `percent`, `spell_Id`, `wealth_Rating`, `treasure_Class`, `treasure_Type`, `p_Script`, `sound`, `destination_Type`, `weenie_Class_Id`, `stack_Size`, `palette`, `shade`, `try_To_Bond`, `obj_Cell_Id`, `origin_X`, `origin_Y`, `origin_Z`, `angles_W`, `angles_X`, `angles_Y`, `angles_Z`)
VALUES (@parent_id, 0, 19, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
     , (@parent_id, 1, 5, 0, 1, 318767239, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);"""

print("=" * 80)
print("Testing Validator Fix")
print("=" * 80)
print()

validator = SQLValidator()
errors = validator._validate_insert(test_sql, "test.sql", 1)

print(f"Errors found: {len(errors)}")
print()

if errors:
    print("[SUCCESS] VALIDATOR IS WORKING - It detected the error!")
    print()
    print("First error:")
    print(errors[0])
else:
    print("[FAILED] VALIDATOR IS NOT WORKING - It should have detected an error!")
    print()
    print("This means the fix is not being applied.")
    print("Please restart the application completely to clear Python's module cache.")

print()
print("=" * 80)
