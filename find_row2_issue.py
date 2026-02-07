#!/usr/bin/env python3
"""Find the actual row 2 issue in the SQL file"""

from validate_sql import SQLValidator
import re

filename = "event_hub_random_event_20260112_011109.sql"

validator = SQLValidator()
validator.export_mode = True

print(f"Validating {filename}...")
result = validator.validate_file(filename)

print(f"\nTotal INSERT statements: {validator._insert_count}")
print(f"Total details: {len(validator._insert_details)}")

# Read the file and find all multi-row INSERTs
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all INSERT INTO statements
insert_pattern = r'INSERT\s+INTO\s+`?(\w+)`?\s*\((.*?)\)\s*VALUES\s+(.*?);'
matches = list(re.finditer(insert_pattern, content, re.DOTALL | re.IGNORECASE))

print(f"\nFound {len(matches)} INSERT statements via regex")

# Check each INSERT for multi-row VALUES
for i, match in enumerate(matches[:20]):  # Check first 20
    table_name = match.group(1)
    columns_str = match.group(2)
    values_str = match.group(3)
    
    # Count columns
    columns = [c.strip().strip('`') for c in columns_str.split(',')]
    column_count = len(columns)
    
    # Count rows in VALUES (rows are separated by ), or ), /*)
    # Simple approach: count occurrences of ), that aren't inside strings
    rows = []
    depth = 0
    in_string = False
    string_char = None
    row_start = -1
    
    for j, char in enumerate(values_str):
        if char in ("'", '"') and (j == 0 or values_str[j-1] != '\\'):
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None
        elif char == '(' and not in_string:
            if depth == 0:
                row_start = j
            depth += 1
        elif char == ')' and not in_string:
            depth -= 1
            if depth == 0 and row_start != -1:
                rows.append(values_str[row_start+1:j])
                row_start = -1
    
    if len(rows) >= 2:  # Multi-row INSERT
        print(f"\nINSERT #{i+1}: `{table_name}` ({column_count} columns, {len(rows)} rows)")
        
        # Check each row
        for row_num, row_content in enumerate(rows, 1):
            # Count commas at top level
            comma_count = 0
            depth = 0
            in_string = False
            string_char = None
            
            for char in row_content:
                if char in ("'", '"') and (len(row_content) == 0 or row_content[max(0, row_content.index(char)-1)] != '\\'):
                    in_string = not in_string
                    if not in_string:
                        string_char = None
                    else:
                        string_char = char
                elif char == '(' and not in_string:
                    depth += 1
                elif char == ')' and not in_string:
                    depth -= 1
                elif char == ',' and not in_string and depth == 0:
                    comma_count += 1
            
            value_count = comma_count + 1
            match_status = "OK" if value_count == column_count else "ERROR"
            print(f"  Row {row_num}: {value_count} values (expected {column_count}) [{match_status}]")
            
            if row_num == 2 and value_count != column_count:
                print(f"    *** ROW 2 MISMATCH FOUND! ***")
                print(f"    Row content: {row_content[:200]}...")
