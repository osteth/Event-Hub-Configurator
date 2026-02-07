#!/usr/bin/env python3
"""Test if details are being populated"""

from validate_sql import SQLValidator

v = SQLValidator()
v.export_mode = True

print("Before validation:")
print(f"  _insert_details length: {len(v._insert_details)}")
print(f"  export_mode: {v.export_mode}")

result = v.validate_file('event_hub_random_event_20260110_213856.sql')

print("\nAfter validation:")
print(f"  _insert_details length: {len(v._insert_details)}")
print(f"  _insert_count: {v._insert_count}")
print(f"  error_count: {v.error_count}")

if v._insert_details:
    print(f"\nFirst detail: {v._insert_details[0]}")
else:
    print("\nNo details found - checking why...")
    # Check if _validate_insert is being called
    print(f"  INSERT count suggests {v._insert_count} INSERTs were processed")
