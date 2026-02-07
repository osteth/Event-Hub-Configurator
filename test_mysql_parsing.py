#!/usr/bin/env python3
"""Test MySQL-style parsing to find the actual issue"""

import re

filename = "event_hub_random_event_20260110_210255.sql"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find ALL emote_action INSERTs
pattern = r'INSERT INTO `weenie_properties_emote_action`[^;]+?;'
matches = list(re.finditer(pattern, content, re.DOTALL | re.IGNORECASE))

print(f"Found {len(matches)} emote_action INSERT statements\n")

for match_idx, match in enumerate(matches, 1):
    statement = match.group(0)
    
    # Extract column count
    col_match = re.search(r'\(([^)]+)\)', statement, re.DOTALL)
    if col_match:
        cols = [c.strip().strip('`') for c in col_match.group(1).split(',')]
        col_count = len(cols)
        print(f"INSERT #{match_idx}: {col_count} columns defined")
    
    # Extract VALUES
    values_match = re.search(r'VALUES\s+(.+?);', statement, re.DOTALL | re.IGNORECASE)
    if values_match:
        values_text = values_match.group(1)
        
        # Parse rows more carefully
        rows = []
        depth = 0
        in_string = False
        string_char = None
        row_start = -1
        
        i = 0
        while i < len(values_text):
            char = values_text[i]
            
            # Handle escaped characters
            if char == '\\' and i + 1 < len(values_text):
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
            
            # Handle parentheses
            elif char == '(' and not in_string:
                if depth == 0:
                    row_start = i
                depth += 1
            elif char == ')' and not in_string:
                depth -= 1
                if depth == 0 and row_start != -1:
                    row_content = values_text[row_start+1:i]
                    rows.append(row_content)
                    row_start = -1
            
            i += 1
        
        print(f"  Found {len(rows)} rows")
        
        # Check each row
        for row_idx, row in enumerate(rows, 1):
            # Count values by counting commas at top level
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
                print(f"    Snippet: {row[:100]}...")
            else:
                print(f"  [OK] Row {row_idx}: {value_count} values")
        
        print()
