#!/usr/bin/env python3
"""Test validation and write detailed output to file"""

import sys
from validate_sql import SQLValidator

filename = "event_hub_random_event_20260110_210255.sql"
output_file = "validation_report.txt"

validator = SQLValidator()
validator.verbose = True

print(f"Validating {filename}...")
print(f"Output will be written to {output_file}")

# Redirect stdout to file
original_stdout = sys.stdout
with open(output_file, 'w', encoding='utf-8') as f:
    sys.stdout = f
    
    validator.validate_bulk_upload(filename)
    validator.print_report()
    
    # Also print detailed info
    print("\n" + "="*80)
    print("DETAILED VALIDATION INFO")
    print("="*80)
    print(f"Total INSERT statements found: {validator._insert_count}")
    print(f"Total errors: {validator.error_count}")
    
sys.stdout = original_stdout

print(f"\nValidation complete. Check {output_file} for details.")
