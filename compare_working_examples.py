#!/usr/bin/env python3
"""
Compare working example files against generated files to identify differences.
This helps fix the generator script to produce correct output.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional

def extract_insert_statements(content: str) -> List[Dict]:
    """Extract all INSERT statements from SQL content."""
    inserts = []
    
    # Find all INSERT INTO statements
    pattern = r'INSERT\s+INTO\s+`?(\w+)`?\s*\(([^)]+)\)\s*VALUES\s+([^;]+);'
    
    for match in re.finditer(pattern, content, re.IGNORECASE | re.DOTALL):
        table_name = match.group(1)
        columns_text = match.group(2)
        values_text = match.group(3)
        
        # Extract column names
        columns = [col.strip().strip('`') for col in columns_text.split(',')]
        
        # Extract value rows
        rows = extract_value_rows(values_text)
        
        inserts.append({
            'table': table_name,
            'columns': columns,
            'column_count': len(columns),
            'rows': rows,
            'full_match': match.group(0),
            'start_pos': match.start()
        })
    
    return inserts

def extract_value_rows(values_text: str) -> List[Dict]:
    """Extract individual rows from VALUES clause."""
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
                value_count = count_values(row_content)
                rows.append({
                    'content': row_content,
                    'value_count': value_count,
                    'full_row': values_text[row_start:i+1]
                })
                row_start = -1
        
        i += 1
    
    return rows

def count_values(row_text: str) -> int:
    """Count values in a row MySQL-style."""
    value_count = 0
    depth = 0
    in_string = False
    string_char = None
    i = 0
    
    while i < len(row_text):
        char = row_text[i]
        
        if char == '\\' and i + 1 < len(row_text):
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
            value_count += 1
        
        i += 1
    
    # Last value (no trailing comma)
    if row_text.strip():
        value_count += 1
    
    return value_count

def compare_files(working_file: str, generated_file: str):
    """Compare a working example file against a generated file."""
    print(f"\n{'='*80}")
    print(f"Comparing:")
    print(f"  Working: {working_file}")
    print(f"  Generated: {generated_file}")
    print(f"{'='*80}\n")
    
    # Read files
    with open(working_file, 'r', encoding='utf-8') as f:
        working_content = f.read()
    
    with open(generated_file, 'r', encoding='utf-8') as f:
        generated_content = f.read()
    
    # Extract INSERT statements
    working_inserts = extract_insert_statements(working_content)
    generated_inserts = extract_insert_statements(generated_content)
    
    print(f"Working file: {len(working_inserts)} INSERT statements")
    print(f"Generated file: {len(generated_inserts)} INSERT statements\n")
    
    # Compare INSERT statements
    differences = []
    
    # Match INSERTs by table name and approximate position
    for i, working_insert in enumerate(working_inserts):
        # Try to find matching INSERT in generated file
        matching_generated = None
        for gen_insert in generated_inserts:
            if gen_insert['table'] == working_insert['table']:
                # Check if column lists match
                if gen_insert['columns'] == working_insert['columns']:
                    matching_generated = gen_insert
                    break
        
        if not matching_generated:
            differences.append({
                'type': 'missing_insert',
                'table': working_insert['table'],
                'working': working_insert
            })
            continue
        
        # Compare column lists
        if working_insert['columns'] != matching_generated['columns']:
            differences.append({
                'type': 'column_mismatch',
                'table': working_insert['table'],
                'working_columns': working_insert['columns'],
                'generated_columns': matching_generated['columns']
            })
        
        # Compare rows
        working_rows = working_insert['rows']
        generated_rows = matching_generated['rows']
        
        if len(working_rows) != len(generated_rows):
            differences.append({
                'type': 'row_count_mismatch',
                'table': working_insert['table'],
                'working_count': len(working_rows),
                'generated_count': len(generated_rows)
            })
        
        # Compare each row
        for row_idx, (w_row, g_row) in enumerate(zip(working_rows, generated_rows)):
            if w_row['value_count'] != g_row['value_count']:
                differences.append({
                    'type': 'value_count_mismatch',
                    'table': working_insert['table'],
                    'row': row_idx + 1,
                    'working_count': w_row['value_count'],
                    'generated_count': g_row['value_count'],
                    'working_row': w_row['content'][:100],
                    'generated_row': g_row['content'][:100],
                    'expected_columns': working_insert['column_count']
                })
    
    # Report differences
    if differences:
        print(f"Found {len(differences)} differences:\n")
        for diff in differences:
            if diff['type'] == 'value_count_mismatch':
                print(f"❌ VALUE COUNT MISMATCH")
                print(f"   Table: `{diff['table']}`")
                print(f"   Row: {diff['row']}")
                print(f"   Expected: {diff['expected_columns']} columns")
                print(f"   Working example: {diff['working_count']} values")
                print(f"   Generated: {diff['generated_count']} values")
                print(f"   Working snippet: {diff['working_row']}...")
                print(f"   Generated snippet: {diff['generated_row']}...")
                print()
            elif diff['type'] == 'column_mismatch':
                print(f"❌ COLUMN MISMATCH")
                print(f"   Table: `{diff['table']}`")
                print(f"   Working columns: {len(diff['working_columns'])}")
                print(f"   Generated columns: {len(diff['generated_columns'])}")
                if diff['working_columns'] != diff['generated_columns']:
                    print(f"   Working: {', '.join(diff['working_columns'][:5])}...")
                    print(f"   Generated: {', '.join(diff['generated_columns'][:5])}...")
                print()
            elif diff['type'] == 'row_count_mismatch':
                print(f"❌ ROW COUNT MISMATCH")
                print(f"   Table: `{diff['table']}`")
                print(f"   Working: {diff['working_count']} rows")
                print(f"   Generated: {diff['generated_count']} rows")
                print()
    else:
        print("✅ No differences found! Files match exactly.\n")
    
    return differences

def main():
    if len(sys.argv) < 3:
        print("Usage: python compare_working_examples.py <working_controller> <working_wave> [generated_controller] [generated_wave]")
        print("\nExample:")
        print("  python compare_working_examples.py \\")
        print("    '../694200300 Mid Controller.sql' \\")
        print("    '../694200321 Mid Event Wave 1.sql' \\")
        print("    'Mid Event Sequence/694200300 Mid Event Controller.sql' \\")
        print("    'Mid Event Sequence/694200321 Mid Event Wave 1.sql'")
        sys.exit(1)
    
    working_controller = sys.argv[1]
    working_wave = sys.argv[2]
    generated_controller = sys.argv[3] if len(sys.argv) > 3 else None
    generated_wave = sys.argv[4] if len(sys.argv) > 4 else None
    
    # Default generated file paths if not provided
    if not generated_controller:
        generated_controller = "Mid Event Sequence/694200300 Mid Event Controller.sql"
    if not generated_wave:
        generated_wave = "Mid Event Sequence/694200321 Mid Event Wave 1.sql"
    
    all_differences = []
    
    if Path(working_controller).exists() and Path(generated_controller).exists():
        diffs = compare_files(working_controller, generated_controller)
        all_differences.extend(diffs)
    else:
        print(f"Warning: Could not find controller files")
    
    if Path(working_wave).exists() and Path(generated_wave).exists():
        diffs = compare_files(working_wave, generated_wave)
        all_differences.extend(diffs)
    else:
        print(f"Warning: Could not find wave files")
    
    # Summary
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total differences found: {len(all_differences)}")
    
    value_count_errors = [d for d in all_differences if d['type'] == 'value_count_mismatch']
    if value_count_errors:
        print(f"\n⚠️  VALUE COUNT ERRORS (these cause MySQL import failures):")
        for err in value_count_errors:
            print(f"   - {err['table']} row {err['row']}: {err['generated_count']}/{err['expected_columns']} values (should be {err['working_count']})")

if __name__ == '__main__':
    main()
