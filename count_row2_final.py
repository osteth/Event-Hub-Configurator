#!/usr/bin/env python3
"""Final count of row 2"""

# Row 2 from the bulk upload file
row = "@parent_id,  1,  88, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

# Count commas outside strings
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
print(f"Match: {'YES' if value_count == 40 else 'NO'}")
print(f"Difference: {value_count - 40}")

# Count NULLs after 'StartEvent'
parts = row.split("'StartEvent'")
if len(parts) == 2:
    after = parts[1]
    nulls_after = after.count('NULL')
    print(f"\nNULLs after 'StartEvent': {nulls_after}")
    print(f"Values before 'StartEvent': 7")
    print(f"Total: 7 + {nulls_after} = {7 + nulls_after}")
