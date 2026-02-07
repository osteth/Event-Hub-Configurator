#!/usr/bin/env python3
"""Robustly check all INSERT statements for row 2 issues using same logic as validator"""

import re
import sys
sys.path.insert(0, '.')
from validate_sql import SQLValidator

filename = "event_hub_random_event_20260110_220122.sql"

validator = SQLValidator()

# Manually process to ensure details are captured
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all INSERT statements using same method as validator
i = 0
insert_num = 0
row2_issues = []

while i < len(content):
    insert_pos = content[i:].upper().find('INSERT INTO')
    if insert_pos == -1:
        break
    
    insert_pos += i
    i = insert_pos + 1
    
    # Find statement end
    semicolon_pos = validator._find_statement_end(content, insert_pos)
    if semicolon_pos == -1:
        continue
    
    statement = content[insert_pos:semicolon_pos + 1]
    insert_num += 1
    
    # Validate this INSERT
    line_num = content[:insert_pos].count('\n') + 1
    errors = validator._validate_insert(statement, filename, line_num)
    
    # Check if any errors are for row 2
    for error in errors:
        if 'Row 2' in error or 'row 2' in error:
            # Extract table name
            table_match = re.search(r'INSERT\s+INTO\s+`?(\w+)`?\s*\(', statement, re.IGNORECASE)
            table_name = table_match.group(1) if table_match else "unknown"
            
            row2_issues.append({
                'insert_num': insert_num,
                'table': table_name,
                'line': line_num,
                'error': error
            })

print(f"Processed {insert_num} INSERT statements\n")

if row2_issues:
    print(f"=== Found {len(row2_issues)} INSERT statements with row 2 issues ===\n")
    for issue in row2_issues:
        print(f"INSERT #{issue['insert_num']} (Line ~{issue['line']}): `{issue['table']}`")
        print(f"  {issue['error']}")
        print()
else:
    print("No row 2 issues found by validator.")
    print(f"Total INSERT statements checked: {insert_num}")
    print(f"Total errors found: {len(validator.errors)}")
    
    if validator.errors:
        print("\nAll errors found:")
        for error in validator.errors[:10]:
            print(f"  {error}")
