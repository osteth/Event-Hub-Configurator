#!/usr/bin/env python3
"""Count values in row 2 exactly"""

row = "@parent_id,  1,  88, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

# Count commas outside of strings
comma_count = 0
in_string = False
string_char = None

for i, char in enumerate(row):
    if char == '\\' and i > 0:
        continue
    
    if char in ("'", '"'):
        if not in_string:
            in_string = True
            string_char = char
        elif char == string_char:
            in_string = False
            string_char = None
    elif char == ',' and not in_string:
        comma_count += 1

value_count = comma_count + 1
print(f"Row 2 value count: {value_count}")
print(f"Expected: 40")
print(f"Difference: {value_count - 40}")

# Also show what a simple split gives
simple = [v.strip() for v in row.split(',')]
print(f"\nSimple split count: {len(simple)}")
print(f"First 10: {simple[:10]}")
print(f"Last 10: {simple[-10:]}")
