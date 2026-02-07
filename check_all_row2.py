#!/usr/bin/env python3
"""Directly check all INSERT statements for row 2 issues"""

import re

filename = "event_hub_random_event_20260110_220122.sql"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all INSERT statements
insert_pattern = r'INSERT\s+INTO\s+`?(\w+)`?\s*\([^)]+\)\s*VALUES\s+([^;]+);'
matches = list(re.finditer(insert_pattern, content, re.IGNORECASE | re.DOTALL))

print(f"Found {len(matches)} INSERT statements\n")

row2_issues = []

for idx, match in enumerate(matches, 1):
    table_name = match.group(1)
    
    # Extract column count
    col_match = re.search(r'\(([^)]+)\)', match.group(0), re.DOTALL)
    if col_match:
        cols = [c.strip().strip('`') for c in col_match.group(1).split(',')]
        col_count = len(cols)
    
    values_text = match.group(2)
    
    # Extract rows
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
    
    # Check row 2 specifically
    if len(rows) >= 2:
        row2 = rows[1]  # Row 2 (0-indexed is 1)
        
        # Count values MySQL-style
        value_count = 0
        current_value = []
        depth = 0
        in_string = False
        string_char = None
        j = 0
        
        while j < len(row2):
            c = row2[j]
            
            if c == '\\' and j + 1 < len(row2):
                current_value.append(c)
                current_value.append(row2[j+1])
                j += 2
                continue
            
            if c in ("'", '"'):
                if not in_string:
                    in_string = True
                    string_char = c
                elif c == string_char:
                    in_string = False
                    string_char = None
                current_value.append(c)
            elif c == '(' and not in_string:
                depth += 1
                current_value.append(c)
            elif c == ')' and not in_string:
                depth -= 1
                current_value.append(c)
            elif c == ',' and not in_string and depth == 0:
                value_count += 1
                current_value = []
            else:
                current_value.append(c)
            
            j += 1
        
        if current_value:
            value_count += 1
        
        if value_count != col_count:
            row2_issues.append({
                'insert_num': idx,
                'table': table_name,
                'row2_values': value_count,
                'expected': col_count,
                'snippet': row2[:100]
            })

if row2_issues:
    print(f"=== Found {len(row2_issues)} INSERT statements with row 2 issues ===\n")
    for issue in row2_issues:
        print(f"INSERT #{issue['insert_num']}: `{issue['table']}`")
        print(f"  Row 2: {issue['row2_values']}/{issue['expected']} values [ERROR]")
        print(f"  Snippet: {issue['snippet']}...")
        print()
else:
    print("No row 2 issues found in any INSERT statement.")
