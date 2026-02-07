#!/usr/bin/env python3
"""Count values in a specific row string"""

# Test the Event Bell Sound action (first row)
row = "@parent_id,  0,   9, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

# Count commas (simple - won't work if there are strings with commas, but this row doesn't have that)
values = [v.strip() for v in row.split(',')]
print(f"Row 1 (Sound): {len(values)} values")
print(f"Values: {values}")

# Test Event Bell StartEvent action (second row)
row2 = "@parent_id,  1,  88, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

# For row2, we need to handle the string 'StartEvent' properly
# Count commas outside of strings
comma_count = 0
in_string = False
string_char = None
i = 0

while i < len(row2):
    char = row2[i]
    if char == '\\' and i + 1 < len(row2):
        i += 2
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
    i += 1

print(f"\nRow 2 (StartEvent): {comma_count + 1} values")

# Test Event Bell DeleteSelf action (third row)
row3 = "@parent_id,  2,  77, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

values3 = [v.strip() for v in row3.split(',')]
print(f"\nRow 3 (DeleteSelf): {len(values3)} values")
print(f"First 5: {values3[:5]}")
print(f"Last 5: {values3[-5:]}")
