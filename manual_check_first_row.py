#!/usr/bin/env python3
"""Manually check the first emote_action row in the bulk upload"""

import re

filename = "event_hub_random_event_20260110_205630.sql"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find first emote_action INSERT
pattern = r'INSERT INTO `weenie_properties_emote_action`[^;]+VALUES\s+([^;]+);'
match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

if match:
    values_clause = match.group(1)
    print("First emote_action VALUES clause:")
    print("="*80)
    
    # Extract first row (before first comma at depth 0 after VALUES)
    # Find first complete parenthesized group
    depth = 0
    in_string = False
    string_char = None
    row_start = -1
    i = 0
    
    while i < len(values_clause):
        char = values_clause[i]
        
        if char == '\\' and i + 1 < len(values_clause):
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
                first_row = values_clause[row_start+1:i]
                print(f"First row content:\n{first_row}\n")
                print("="*80)
                
                # Count commas at top level
                comma_count = 0
                depth2 = 0
                in_string2 = False
                string_char2 = None
                j = 0
                
                while j < len(first_row):
                    c = first_row[j]
                    
                    if c == '\\' and j + 1 < len(first_row):
                        j += 2
                        continue
                    
                    if c in ("'", '"'):
                        if not in_string2:
                            in_string2 = True
                            string_char2 = c
                        elif c == string_char2:
                            in_string2 = False
                            string_char2 = None
                    elif c == '(' and not in_string2:
                        depth2 += 1
                    elif c == ')' and not in_string2:
                        depth2 -= 1
                    elif c == ',' and not in_string2 and depth2 == 0:
                        comma_count += 1
                    
                    j += 1
                
                value_count = comma_count + 1
                print(f"Comma count: {comma_count}")
                print(f"Value count: {value_count}")
                print(f"Expected: 40")
                print(f"Match: {'YES' if value_count == 40 else 'NO'}")
                
                # Also try simple split to see what we get
                simple_split = [v.strip() for v in first_row.split(',')]
                print(f"\nSimple split count: {len(simple_split)}")
                print(f"First 10 values: {simple_split[:10]}")
                print(f"Last 10 values: {simple_split[-10:]}")
                break
        
        i += 1
