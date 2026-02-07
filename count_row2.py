#!/usr/bin/env python3
"""Count values in row 2 of Event Bell"""

row = "@parent_id,  1,  88, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

# Count commas properly handling the string 'StartEvent'
comma_count = 0
in_string = False
string_char = None
i = 0

while i < len(row):
    char = row[i]
    
    # Handle escaped characters
    if char == '\\' and i + 1 < len(row):
        i += 2
        continue
    
    # Handle string literals
    if char in ("'", '"'):
        if not in_string:
            in_string = True
            string_char = char
        elif char == string_char:
            in_string = False
            string_char = None
    
    # Count commas outside strings
    elif char == ',' and not in_string:
        comma_count += 1
    
    i += 1

value_count = comma_count + 1
print(f"Row 2 value count: {value_count}")
print(f"Expected: 40")
print(f"Match: {'YES' if value_count == 40 else 'NO'}")

# Also show what a simple split would give (incorrect)
simple_split = [v.strip() for v in row.split(',')]
print(f"\nSimple split (incorrect, splits on string): {len(simple_split)} values")

# Count NULLs after 'StartEvent'
parts = row.split("'StartEvent'")
if len(parts) == 2:
    after_startevent = parts[1]
    nulls_after = after_startevent.count('NULL')
    print(f"\nNULLs after 'StartEvent': {nulls_after}")
    print(f"Values before 'StartEvent': 7 (including 'StartEvent' itself)")
    print(f"Total: 7 + {nulls_after} = {7 + nulls_after}")
