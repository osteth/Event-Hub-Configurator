#!/usr/bin/env python3
"""Debug validation by testing actual SQL rows"""

# Read the actual file and check the first emote_action INSERT
with open('event_hub_random_event_20260110_205311.sql', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first emote_action INSERT
import re
pattern = r'INSERT INTO `weenie_properties_emote_action`[^;]+VALUES\s+([^;]+);'
match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

if match:
    values_clause = match.group(1)
    print("VALUES clause found:")
    print(values_clause[:200])
    print("\n" + "="*80 + "\n")
    
    # Extract each row
    rows = []
    depth = 0
    in_string = False
    string_char = None
    row_start = -1
    i = 0
    
    while i < len(values_clause):
        char = values_clause[i]
        
        # Handle escaped characters
        if char == '\\' and i + 1 < len(values_clause):
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
                row_content = values_clause[row_start+1:i]
                rows.append(row_content)
                row_start = -1
        
        i += 1
    
    print(f"Found {len(rows)} rows\n")
    
    for idx, row in enumerate(rows, 1):
        # Count commas at top level
        comma_count = 0
        depth = 0
        in_string = False
        string_char = None
        i = 0
        
        while i < len(row):
            char = row[i]
            
            if char == '\\' and i + 1 < len(row):
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
                depth += 1
            elif char == ')' and not in_string:
                depth -= 1
            elif char == ',' and not in_string and depth == 0:
                comma_count += 1
            
            i += 1
        
        value_count = comma_count + 1
        print(f"Row {idx}: {value_count} values")
        print(f"  First 50 chars: {row[:50]}...")
        print(f"  Last 50 chars: ...{row[-50:]}")
        print()
