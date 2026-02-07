#!/usr/bin/env python3
"""Manual test to count values in specific rows"""

# Test row 1 from Event Bell
row1 = "@parent_id,  0,   9, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"
# Test row 2 from Event Bell  
row2 = "@parent_id,  1,  88, 0, 1, NULL, 'StartEvent', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"
# Test row 3 from Event Bell
row3 = "@parent_id,  2,  77, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL"

def count_values_manual(text):
    """Manually count values by parsing carefully"""
    values = []
    current = []
    depth = 0
    in_string = False
    string_char = None
    i = 0
    
    while i < len(text):
        char = text[i]
        
        # Handle escaped characters
        if char == '\\' and i + 1 < len(text):
            current.append(char)
            current.append(text[i+1])
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
            current.append(char)
        
        # Handle parentheses
        elif char == '(' and not in_string:
            depth += 1
            current.append(char)
        elif char == ')' and not in_string:
            depth -= 1
            current.append(char)
        
        # Handle commas
        elif char == ',' and not in_string and depth == 0:
            value = ''.join(current).strip()
            if value:
                values.append(value)
            current = []
        else:
            current.append(char)
        
        i += 1
    
    # Add last value
    if current:
        value = ''.join(current).strip()
        if value:
            values.append(value)
    
    return values

print("Row 1 (Sound):", len(count_values_manual(row1)), "values")
print("Row 2 (LocalSignal):", len(count_values_manual(row2)), "values")
print("Row 3 (DeleteSelf):", len(count_values_manual(row3)), "values")

print("\nRow 1 values:", count_values_manual(row1))
print("\nRow 2 values:", count_values_manual(row2))
print("\nRow 3 values:", count_values_manual(row3))
