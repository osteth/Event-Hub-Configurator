#!/usr/bin/env python3
"""Check INSERT statements with 3 rows (focus on row 2)"""

from validate_sql import SQLValidator
import re

filename = "event_hub_random_event_20260112_011109.sql"

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all INSERT INTO statements with VALUES
insert_pattern = r'INSERT\s+INTO\s+`?(\w+)`?\s*\((.*?)\)\s*VALUES\s+(.*?);'
matches = list(re.finditer(insert_pattern, content, re.DOTALL | re.IGNORECASE))

print(f"Found {len(matches)} INSERT statements\n")

# Check each INSERT for 3 rows
for i, match in enumerate(matches):
    table_name = match.group(1)
    columns_str = match.group(2)
    values_str = match.group(3)
    
    # Count columns
    columns = [c.strip().strip('`') for c in columns_str.split(',')]
    column_count = len(columns)
    
    # Extract rows using the validator's method
    validator = SQLValidator()
    rows = validator._extract_value_rows('VALUES ' + values_str)
    
    if len(rows) == 3:  # 3-row INSERT (like wave controllers)
        print(f"INSERT #{i+1}: `{table_name}` ({column_count} columns, 3 rows)")
        
        # Check each row using validator's counting method
        for row_num, row_content in enumerate(rows, 1):
            value_count = validator._count_values_mysql_style(row_content)
            match_status = "OK" if value_count == column_count else "ERROR"
            print(f"  Row {row_num}: {value_count} values (expected {column_count}) [{match_status}]")
            
            if row_num == 2 and value_count != column_count:
                print(f"    *** ROW 2 MISMATCH FOUND! ***")
                print(f"    Row content (first 300 chars): {row_content[:300]}")
                print(f"    Full row: {row_content}")
            elif row_num == 2:
                # Show row 2 even if it's OK, to help debug
                if table_name == 'weenie_properties_emote_action':
                    print(f"    Row 2 snippet: {row_content[:200]}...")
        print()
