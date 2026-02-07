#!/usr/bin/env python3
"""Find the exact issue by checking each INSERT statement"""

import re

filename = "event_hub_random_event_20260110_210255.sql"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find first few INSERT statements
insert_pattern = r'INSERT\s+INTO\s+`?(\w+)`?\s*\([^)]+\)\s*VALUES\s+([^;]+);'
matches = list(re.finditer(insert_pattern, content, re.IGNORECASE | re.DOTALL))

print(f"Found {len(matches)} INSERT statements\n")
print("Checking first 10 INSERT statements:\n")

for idx, match in enumerate(matches[:10], 1):
    table_name = match.group(1)
    columns_str = match.group(0).split('(')[1].split(')')[0]
    columns = [c.strip().strip('`') for c in columns_str.split(',')]
    col_count = len(columns)
    
    values_text = match.group(2)
    
    # Count rows by finding parenthesized groups
    rows = []
    depth = 0
    in_string = False
    string_char = None
    row_start = -1
    
    i = 0
    while i < len(values_text):
        char = values_text[i]
        
        if char == '\\' and i + 1 < len(values_text):
            i += 2
            continue
        
        if char in ("'", '"'):
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None
        elif char == '(' and not in_string:
            if depth == 0:
                row_start = i
            depth += 1
        elif char == ')' and not in_string:
            depth -= 1
            if depth == 0 and row_start != -1:
                rows.append(values_text[row_start+1:i])
                row_start = -1
        
        i += 1
    
    print(f"INSERT #{idx}: `{table_name}`")
    print(f"  Columns: {col_count}")
    print(f"  Rows: {len(rows)}")
    
    # Check each row
    has_error = False
    for row_idx, row in enumerate(rows, 1):
        # Count commas at top level
        comma_count = 0
        depth = 0
        in_string = False
        string_char = None
        
        j = 0
        while j < len(row):
            c = row[j]
            
            if c == '\\' and j + 1 < len(row):
                j += 2
                continue
            
            if c in ("'", '"'):
                if not in_string:
                    in_string = True
                    string_char = c
                elif c == string_char:
                    in_string = False
                    string_char = None
            elif c == '(' and not in_string:
                depth += 1
            elif c == ')' and not in_string:
                depth -= 1
            elif c == ',' and not in_string and depth == 0:
                comma_count += 1
            
            j += 1
        
        value_count = comma_count + 1
        
        if value_count != col_count:
            print(f"  [ERROR] Row {row_idx}: Expected {col_count}, found {value_count}")
            print(f"    Snippet: {row[:100]}")
            has_error = True
    
    if not has_error:
        print(f"  [OK] All rows valid")
    print()
