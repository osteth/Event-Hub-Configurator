#!/usr/bin/env python3
"""Quick test to count values in Event Bell"""
import re

line1 = "VALUES (@parent_id,  0,   9, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* Sound, Speak1 */"
line2 = "     , (@parent_id,  1,  88, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* LocalSignal */"
line3 = "     , (@parent_id,  2,  77, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL) /* DeleteSelf */;"

def count_values(line):
    # Remove comments
    line = re.sub(r'/\*.*?\*/', '', line).strip()
    
    # Extract content between parentheses
    match = re.search(r'\(([^)]+)\)', line)
    if not match:
        return 0
    
    content = match.group(1)
    
    # Count commas at top level
    count = 0
    depth = 0
    in_string = False
    string_char = None
    
    for i, char in enumerate(content):
        if char in ("'", '"') and (i == 0 or content[i-1] != '\\'):
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
            count += 1
    
    return count + 1  # +1 because n commas = n+1 values

print("Line 1 (Sound):", count_values(line1), "values")
print("Line 2 (LocalSignal):", count_values(line2), "values")
print("Line 3 (DeleteSelf):", count_values(line3), "values")
