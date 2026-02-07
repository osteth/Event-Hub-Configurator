#!/usr/bin/env python3
"""Find all INSERT statements where row 2 has issues"""

import re
from validate_sql import SQLValidator

filename = "event_hub_random_event_20260110_220122.sql"

validator = SQLValidator()
validator.export_mode = True

print(f"Validating {filename}...")
result = validator.validate_file(filename)

print(f"\nTotal INSERT statements: {validator._insert_count}")
print(f"Total rows checked: {len(validator._insert_details)}")

# Find all row 2 entries
row2_issues = [d for d in validator._insert_details if d['row'] == 2 and not d['match']]

if row2_issues:
    print(f"\n=== Found {len(row2_issues)} INSERT statements with row 2 issues ===\n")
    for issue in row2_issues:
        print(f"INSERT #{issue['insert_num']} (Line ~{issue['line']})")
        print(f"  Table: `{issue['table']}`")
        print(f"  Row 2: {issue['values']}/{issue['columns']} values [ERROR]")
        print(f"  Snippet: {issue['snippet'][:80]}...")
        print()
else:
    print("\nNo row 2 issues found in validation details.")
    print("Checking if details were populated...")
    if validator._insert_details:
        print(f"Details were populated ({len(validator._insert_details)} entries)")
        # Show first few row 2 entries
        row2_all = [d for d in validator._insert_details if d['row'] == 2]
        print(f"\nTotal row 2 entries found: {len(row2_all)}")
        if row2_all:
            print("\nFirst 5 row 2 entries:")
            for d in row2_all[:5]:
                status = "OK" if d['match'] else "ERROR"
                print(f"  INSERT #{d['insert_num']}: Row 2 = {d['values']}/{d['columns']} [{status}]")
    else:
        print("ERROR: Details were NOT populated!")
