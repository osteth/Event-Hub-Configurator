#!/usr/bin/env python3
"""
Verbose validation script - shows exactly what it's finding
"""

import sys
import os
from validate_sql import SQLValidator

# Add verbose flag
class VerboseSQLValidator(SQLValidator):
    def _validate_insert(self, statement: str, file_path: str, line_num: int):
        """Override to add verbose output"""
        errors = super()._validate_insert(statement, file_path, line_num)
        
        # Extract table name
        import re
        table_match = re.search(r'INSERT\s+INTO\s+`?(\w+)`?\s*\(', statement, re.IGNORECASE)
        if table_match:
            table_name = table_match.group(1)
            
            # Only show verbose for emote_action or if there are errors
            if table_name == 'weenie_properties_emote_action' or errors:
                print(f"\n[DEBUG] Validating INSERT into `{table_name}` at line ~{line_num}")
                
                # Extract column count
                remaining = statement[table_match.end():]
                depth = 0
                col_start = -1
                col_end = -1
                in_string = False
                string_char = None
                
                for i, char in enumerate(remaining):
                    if char in ("'", '"') and (i == 0 or remaining[i-1] != '\\'):
                        if not in_string:
                            in_string = True
                            string_char = char
                        elif char == string_char:
                            in_string = False
                            string_char = None
                    elif char == '(' and not in_string:
                        if depth == 0:
                            col_start = i + 1
                        depth += 1
                    elif char == ')' and not in_string:
                        depth -= 1
                        if depth == 0 and col_start != -1:
                            col_end = i
                            break
                
                if col_start != -1 and col_end != -1:
                    columns_str = remaining[col_start:col_end]
                    columns = [col.strip().strip('`') for col in columns_str.split(',')]
                    column_count = len(columns)
                    print(f"  Columns defined: {column_count}")
                    
                    # Extract and count rows
                    values_matches = list(re.finditer(r'VALUES\s+', statement, re.IGNORECASE))
                    for values_match in values_matches:
                        values_start = values_match.end()
                        values_text = statement[values_start:]
                        rows = self._extract_value_rows(values_text)
                        print(f"  Rows found: {len(rows)}")
                        
                        for row_num, row_content in enumerate(rows, start=1):
                            value_count = self._count_top_level_commas(row_content) + 1
                            status = "OK" if value_count == column_count else "ERROR"
                            print(f"    Row {row_num}: {value_count} values [{status}]")
                            if value_count != column_count:
                                print(f"      Snippet: {row_content[:80]}...")
        
        return errors

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python validate_sql_verbose.py <file>")
        sys.exit(1)
    
    validator = VerboseSQLValidator()
    validator.validate_bulk_upload(sys.argv[1])
    validator.print_report()
