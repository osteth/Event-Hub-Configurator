#!/usr/bin/env python3
"""
SQL Validation Script for Event Hub Weenie Files
Validates SQL syntax, column counts, and data integrity before upload

Version: 2.0 (Fixed column extraction bug - 2026-01-12)
"""

import re
import sys
import os
from pathlib import Path
from typing import List, Tuple, Dict

class SQLValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.file_count = 0
        self.error_count = 0
        self._insert_count = 0
        self.verbose = False
        self.export_mode = False
        self._insert_details = []  # Store details for export
        
    def validate_file(self, file_path: str) -> bool:
        """Validate a single SQL file"""
        self.file_count += 1
        file_errors = []
        file_warnings = []
        
        # Reset per-file tracking (but keep global counts like _insert_count)
        # Only reset _insert_details if this is the first file (for bulk uploads)
        if self.file_count == 1:
            self._insert_details = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            self.errors.append(f"{file_path}: Failed to read file - {e}")
            return False
        
        # Validate all INSERT statements directly from content
        # This is more reliable than splitting statements and ensures we check EVERY INSERT
        file_errors.extend(self._validate_all_inserts(content, file_path))
        
        if file_errors:
            self.errors.extend([f"{file_path}: {e}" for e in file_errors])
            self.error_count += len(file_errors)
            return False
        
        if file_warnings:
            self.warnings.extend([f"{file_path}: {w}" for w in file_warnings])
        
        return True
    
    def _split_statements(self, content: str) -> List[str]:
        """Split SQL content into individual statements"""
        # Remove comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        content = re.sub(r'--.*$', '', content, flags=re.MULTILINE)
        
        # Split by semicolon
        statements = []
        current = []
        in_string = False
        string_char = None
        
        for char in content:
            if char in ("'", '"') and (not current or current[-1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
            
            current.append(char)
            
            if char == ';' and not in_string:
                stmt = ''.join(current).strip()
                if stmt and stmt != ';':
                    statements.append(stmt)
                current = []
        
        return statements
    
    def _validate_statement(self, statement: str, file_path: str, line_num: int) -> List[str]:
        """Validate a single SQL statement"""
        errors = []
        
        # Check for INSERT statements
        if 'INSERT INTO' in statement.upper():
            errors.extend(self._validate_insert(statement, file_path, line_num))
        
        return errors
    
    def _validate_all_inserts(self, content: str, file_path: str) -> List[str]:
        """Validate ALL INSERT statements in the content"""
        errors = []
        
        # Try to identify source file from comments (for bulk upload files)
        # Look for file markers like "-- File X/Y: path/to/file.sql"
        source_file = None
        lines_before_insert = content[:content.upper().find('INSERT INTO')] if 'INSERT INTO' in content.upper() else ''
        for line in lines_before_insert.split('\n')[-10:]:  # Check last 10 lines before first INSERT
            if '-- File' in line and '.sql' in line:
                # Extract file path from comment
                import re
                match = re.search(r'-- File \d+/\d+:\s*(.+\.sql)', line)
                if match:
                    source_file = match.group(1).strip()
                    break
        
        # Find all INSERT INTO statements by finding the start and matching to semicolon
        # This is more reliable than regex for multi-line statements
        i = 0
        while i < len(content):
            # Find "INSERT INTO" (case insensitive)
            insert_pos = content[i:].upper().find('INSERT INTO')
            if insert_pos == -1:
                break
            
            insert_pos += i
            i = insert_pos + 1
            
            # Update source file if we find a new file marker before this INSERT
            # Check backwards from insert_pos for file markers
            check_start = max(0, insert_pos - 500)  # Check up to 500 chars back
            section_before = content[check_start:insert_pos]
            for line in section_before.split('\n'):
                if '-- File' in line and '.sql' in line:
                    import re
                    match = re.search(r'-- File \d+/\d+:\s*(.+\.sql)', line)
                    if match:
                        source_file = match.group(1).strip()
                        break
            
            # Find the matching semicolon (end of statement)
            # Need to handle semicolons inside strings and comments
            semicolon_pos = self._find_statement_end(content, insert_pos)
            if semicolon_pos == -1:
                # Statement not properly terminated, skip it
                continue
            
            statement = content[insert_pos:semicolon_pos + 1]
            line_num = content[:insert_pos].count('\n') + 1
            
            # Add source file context to file_path for better error messages
            effective_file_path = file_path
            if source_file and 'bulk' in file_path.lower() or 'event_hub' in file_path.lower():
                effective_file_path = f"{file_path} (from {source_file})"
            
            insert_errors = self._validate_insert(statement, effective_file_path, line_num)
            errors.extend(insert_errors)
        
        return errors
    
    def _find_statement_end(self, content: str, start_pos: int) -> int:
        """Find the end of an SQL statement (semicolon) handling strings and comments"""
        in_string = False
        string_char = None
        in_comment = False
        comment_type = None  # '--' or '/*'
        i = start_pos
        
        while i < len(content):
            char = content[i]
            
            # Handle comments
            if not in_string and not in_comment:
                if i + 1 < len(content):
                    two_chars = content[i:i+2]
                    if two_chars == '--':
                        in_comment = True
                        comment_type = '--'
                        i += 2
                        continue
                    elif two_chars == '/*':
                        in_comment = True
                        comment_type = '/*'
                        i += 2
                        continue
            
            if in_comment:
                if comment_type == '--' and char == '\n':
                    in_comment = False
                    comment_type = None
                elif comment_type == '/*' and i + 1 < len(content) and content[i:i+2] == '*/':
                    in_comment = False
                    comment_type = None
                    i += 2
                    continue
            
            # Handle string literals
            if not in_comment:
                if char == '\\' and i + 1 < len(content):
                    i += 2
                    continue
                
                if char in ("'", '"'):
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char:
                        in_string = False
                        string_char = None
            
            # Found semicolon outside string and comment
            if char == ';' and not in_string and not in_comment:
                return i
            
            i += 1
        
        return -1
    
    def _validate_insert(self, statement: str, file_path: str, line_num: int) -> List[str]:
        """Validate INSERT statement column/value counts"""
        errors = []
        
        # Track INSERT count
        if not hasattr(self, '_insert_count'):
            self._insert_count = 0
        self._insert_count += 1
        insert_number = self._insert_count
        
        # Extract table name and columns
        table_match = re.search(r'INSERT\s+INTO\s+`?(\w+)`?\s*\(', statement, re.IGNORECASE)
        if not table_match:
            return errors
        
        table_name = table_match.group(1)
        
        # Extract column list - find first complete parenthesized group after table name
        # This handles multi-line column lists
        # Note: table_match.end() points to right after the opening '('
        remaining = statement[table_match.end():]
        depth = 1  # We're already inside the opening parenthesis
        col_start = 0  # Start from the beginning of remaining (which is inside the parentheses)
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
                depth += 1
            elif char == ')' and not in_string:
                depth -= 1
                if depth == 0:
                    col_end = i
                    break
        
        if col_end == -1:
            return errors
        
        columns_str = remaining[col_start:col_end]
        columns = [col.strip().strip('`') for col in columns_str.split(',')]
        column_count = len(columns)
        
        # Extract VALUES clause(s) - find all occurrences
        values_start_positions = []
        search_pos = 0
        while True:
            values_match = re.search(r'VALUES\s+', statement[search_pos:], re.IGNORECASE)
            if not values_match:
                break
            values_start_positions.append(search_pos + values_match.end())
            search_pos += values_match.end()
        
        if not values_start_positions:
            # No VALUES clause found - this is unusual but not necessarily an error
            return errors
        
        for values_start in values_start_positions:
            # Find all rows in VALUES clause (rows are separated by commas at depth 0)
            # Each row is a complete parenthesized group
            values_text = statement[values_start:]
            rows = self._extract_value_rows(values_text)
            
            if not rows:
                # Couldn't extract rows - might be a parsing issue
                errors.append(f"Line ~{line_num}: Could not parse VALUES clause for `{table_name}`")
                continue
            
            for row_num, row_content in enumerate(rows, start=1):
                # Count values MySQL-style (this matches how MySQL actually parses)
                # MySQL is very strict about value boundaries
                value_count = self._count_values_mysql_style(row_content)
                
                # Also do comma-based count as a sanity check
                comma_count = self._count_top_level_commas(row_content) + 1
                
                # If they differ significantly, there might be a parsing issue
                # Use the more conservative count (lower of the two) to catch potential issues
                if abs(value_count - comma_count) > 0:
                    # Log as warning but use MySQL-style count (more accurate)
                    if self.verbose:
                        print(f"[WARN] Row {row_num}: Count mismatch - MySQL-style: {value_count}, Comma-based: {comma_count}")
                    # If there's a significant difference, flag it as a potential issue
                    # Use the minimum to be conservative and catch edge cases
                    if abs(value_count - comma_count) > 1:
                        # This suggests a parsing issue - use the more conservative count
                        value_count = min(value_count, comma_count)
                
                if self.verbose and table_name == 'weenie_properties_emote_action':
                    print(f"[VERBOSE] {table_name} Row {row_num}: {value_count} values (expected {column_count})")
                
                # Store details for export (always, so we can help identify issues)
                # Note: insert_number is the global count, which helps identify which INSERT MySQL is referring to
                detail = {
                    'insert_num': insert_number,
                    'table': table_name,
                    'line': line_num,
                    'row': row_num,
                    'columns': column_count,
                    'values': value_count,
                    'match': value_count == column_count,
                    'snippet': row_content[:100],
                    'insert_snippet': statement[:150].replace('\n', ' ')
                }
                self._insert_details.append(detail)
                
                if value_count != column_count:
                    # Use row_content for snippet (first 150 chars)
                    row_snippet = row_content[:150] if len(row_content) > 150 else row_content
                    
                    # MySQL-style error message with INSERT statement context
                    # MySQL reports "row X" within the INSERT statement, not the file
                    # This matches the exact MySQL error format: "Column count doesn't match value count at row 2"
                    error_msg = (
                        f"Column count doesn't match value count at row {row_num} "
                        f"in INSERT #{insert_number} (Line ~{line_num}) for table `{table_name}`. "
                        f"Expected {column_count} columns, found {value_count} values. "
                        f"({abs(column_count - value_count)} value(s) {'missing' if value_count < column_count else 'extra'})"
                    )
                    errors.append(error_msg)
                    
                    # Add context to help identify which INSERT this is
                    # Extract a snippet of the INSERT statement to help locate it
                    insert_snippet = statement[:200].replace('\n', ' ').strip()
                    errors.append(
                        f"  -> INSERT statement context: {insert_snippet}..."
                    )
                    
                    # Add detailed row info
                    errors.append(
                        f"  -> Row {row_num} content: ({row_snippet}...)"
                    )
                    
                    # Special check for emote_action (most common issue)
                    if table_name == 'weenie_properties_emote_action':
                        diff = abs(40 - value_count)
                        errors.append(
                            f"  -> `weenie_properties_emote_action` requires exactly 40 values. "
                            f"Found: {value_count}. {'Missing' if value_count < 40 else 'Extra'} {diff} value(s)."
                        )
                    
                    # Helpful hint about MySQL error messages
                    errors.append(
                        f"  -> NOTE: MySQL error 'row {row_num}' refers to row {row_num} within THIS INSERT statement (#{insert_number}), "
                        f"not row {row_num} of the file. This is INSERT statement #{insert_number} in the file."
                    )
                    
                    # Special emphasis for row 2 (most common error location)
                    if row_num == 2:
                        errors.append(
                            f"  -> *** ROW 2 ERROR DETECTED *** This matches the MySQL error format exactly."
                        )
        
        return errors
    
    def _extract_value_rows(self, text: str) -> List[str]:
        """Extract all value rows from VALUES clause - handles multi-row VALUES correctly"""
        rows = []
        depth = 0
        in_string = False
        string_char = None
        in_comment = False
        comment_type = None  # '/*' or '--'
        row_start = -1
        i = 0
        
        # Skip leading whitespace
        while i < len(text) and text[i] in (' ', '\t', '\n', '\r'):
            i += 1
        
        while i < len(text):
            char = text[i]
            
            # Handle escaped characters (including escaped quotes)
            if char == '\\' and i + 1 < len(text) and not in_comment:
                i += 2
                continue
            
            # Handle SQL comments - must check before other parsing
            if not in_string and not in_comment:
                # Check for /* comment start
                if char == '/' and i + 1 < len(text) and text[i+1] == '*':
                    in_comment = True
                    comment_type = '/*'
                    i += 2
                    continue
                # Check for -- comment start
                elif char == '-' and i + 1 < len(text) and text[i+1] == '-':
                    in_comment = True
                    comment_type = '--'
                    i += 2
                    continue
            
            if in_comment:
                if comment_type == '/*':
                    # Check for */ comment end
                    if char == '*' and i + 1 < len(text) and text[i+1] == '/':
                        in_comment = False
                        comment_type = None
                        i += 2
                        continue
                elif comment_type == '--':
                    # -- comments end at newline
                    if char == '\n':
                        in_comment = False
                        comment_type = None
                        i += 1
                        continue
                
                # Skip comment content
                i += 1
                continue
            
            # Handle string literals (only when not in comment)
            if char in ("'", '"'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
            
            # Handle parentheses (only when not in comment or string)
            elif char == '(' and not in_string:
                if depth == 0:
                    row_start = i
                depth += 1
            elif char == ')' and not in_string:
                depth -= 1
                if depth == 0 and row_start != -1:
                    # Complete row found
                    rows.append(text[row_start+1:i])  # Exclude outer parentheses
                    row_start = -1
                elif depth < 0:
                    # Mismatched parentheses - shouldn't happen but handle gracefully
                    break
            
            # Handle semicolon (end of statement) - but only if we're at depth 0
            elif char == ';' and not in_string and depth == 0:
                break
            
            i += 1
        
        return rows
    
    
    def _count_values_mysql_style(self, text: str) -> int:
        """
        Count values MySQL-style by actually parsing them as MySQL would.
        MySQL is very strict about value boundaries.
        MySQL strips comments before parsing, so we need to do the same.
        """
        # First, strip SQL comments (both /* */ and -- style)
        # This is critical because MySQL strips comments before parsing VALUES
        # MySQL strips comments BEFORE parsing, so we need to do it carefully
        import re
        
        # Remove /* */ comments - but we need to be careful not to break inside strings
        # We'll do a simple regex replace for /* */ comments (MySQL handles this)
        # Note: This regex doesn't handle nested comments, but MySQL doesn't either
        text = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', text)
        
        # Remove -- style comments line by line (but preserve strings)
        lines = text.split('\n')
        cleaned_lines = []
        for line in lines:
            cleaned_line = []
            i = 0
            in_string = False
            string_char = None
            while i < len(line):
                char = line[i]
                # Handle escaped characters in strings
                if char == '\\' and i + 1 < len(line) and in_string:
                    cleaned_line.append(char)
                    cleaned_line.append(line[i+1])
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
                    cleaned_line.append(char)
                # Handle comment start (-- ) only if not in string
                elif char == '-' and i + 1 < len(line) and line[i+1] == '-' and not in_string:
                    # Rest of line is comment, stop here
                    break
                else:
                    cleaned_line.append(char)
                i += 1
            cleaned_lines.append(''.join(cleaned_line))
        text = '\n'.join(cleaned_lines)
        
        values = []
        current_value = []
        depth = 0
        in_string = False
        string_char = None
        i = 0
        
        while i < len(text):
            char = text[i]
            
            # Handle escaped characters (MySQL handles these specially)
            if char == '\\' and i + 1 < len(text):
                current_value.append(char)
                current_value.append(text[i+1])
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
                current_value.append(char)
            
            # Handle parentheses
            elif char == '(' and not in_string:
                depth += 1
                current_value.append(char)
            elif char == ')' and not in_string:
                depth -= 1
                current_value.append(char)
            
            # Handle commas (value separators)
            elif char == ',' and not in_string and depth == 0:
                # End of current value
                value_str = ''.join(current_value).strip()
                if value_str or len(values) == 0:  # Allow empty values
                    values.append(value_str)
                current_value = []
            else:
                current_value.append(char)
            
            i += 1
        
        # Add final value
        if current_value:
            value_str = ''.join(current_value).strip()
            if value_str or len(values) == 0:
                values.append(value_str)
        
        return len(values)
    
    def _count_top_level_commas(self, text: str) -> int:
        """Count commas at top level (not inside strings or nested parentheses)"""
        count = 0
        depth = 0
        in_string = False
        string_char = None
        i = 0
        
        while i < len(text):
            char = text[i]
            
            # Handle escaped characters (including escaped quotes)
            if char == '\\' and i + 1 < len(text):
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
                depth += 1
            elif char == ')' and not in_string:
                depth -= 1
            
            # Count top-level commas
            elif char == ',' and not in_string and depth == 0:
                count += 1
            
            i += 1
        
        return count
    
    def validate_directory(self, directory: str) -> bool:
        """Validate all SQL files in a directory"""
        dir_path = Path(directory)
        sql_files = list(dir_path.glob('**/*.sql'))
        
        if not sql_files:
            print(f"No SQL files found in {directory}")
            return False
        
        print(f"Validating {len(sql_files)} SQL files...")
        print()
        
        all_valid = True
        for sql_file in sorted(sql_files):
            is_valid = self.validate_file(str(sql_file))
            if not is_valid:
                all_valid = False
        
        return all_valid
    
    def validate_bulk_upload(self, file_path: str, validate_individual_files: bool = True) -> bool:
        """
        Validate the bulk upload SQL file.
        
        Args:
            file_path: Path to bulk upload SQL file
            validate_individual_files: If True, validate individual files first, then bulk upload
        """
        import os
        full_path = os.path.abspath(file_path)
        print(f"Validating bulk upload file: {full_path}")
        if not os.path.exists(full_path):
            print(f"[ERROR] File not found: {full_path}")
            return False
        print(f"File exists: Yes")
        print(f"File size: {os.path.getsize(full_path)} bytes")
        print()
        
        # If requested, validate individual files first
        if validate_individual_files:
            base_dir = os.path.dirname(full_path)
            print("=" * 80)
            print("STEP 1: Validating individual SQL files")
            print("=" * 80)
            print()
            
            # Import get_sql_files to find individual files
            try:
                # Try to import from create_bulk_upload
                sys.path.insert(0, base_dir)
                from create_bulk_upload import get_sql_files
                
                sql_files = get_sql_files(base_dir)
                if sql_files:
                    print(f"Found {len(sql_files)} individual SQL files to validate...")
                    print()
                    
                    individual_errors = 0
                    for relative_path, full_file_path in sql_files:
                        if os.path.exists(full_file_path):
                            print(f"Validating: {relative_path}")
                            file_valid = self.validate_file(full_file_path)
                            if not file_valid:
                                individual_errors += 1
                                print(f"  [FAILED] {relative_path}")
                            else:
                                print(f"  [OK] {relative_path}")
                    
                    print()
                    if individual_errors > 0:
                        print(f"[WARNING] Found {individual_errors} individual file(s) with errors.")
                        print("          These errors will also appear in the bulk upload validation.")
                        print()
                    else:
                        print("[SUCCESS] All individual files validated successfully.")
                        print()
                else:
                    print("[NOTE] Could not find individual SQL files to validate separately.")
                    print("       Proceeding with bulk upload validation only.")
                    print()
            except Exception as e:
                print(f"[NOTE] Could not validate individual files: {e}")
                print("       Proceeding with bulk upload validation only.")
                print()
        
        # Now validate the bulk upload file itself
        print("=" * 80)
        print("STEP 2: Validating bulk upload file")
        print("=" * 80)
        print()
        
        result = self.validate_file(file_path)
        
        # If validation passes but user reports server errors, suggest detailed check
        if result and self.error_count == 0:
            print("[NOTE] Validation passed, but if you're still getting server errors,")
            print("      please provide the exact MySQL error message (table name and row number)")
            print("      so we can identify the specific issue.")
            print()
        
        return result
    
    def print_report(self):
        """Print validation report"""
        print("=" * 80)
        print("SQL VALIDATION REPORT")
        print("=" * 80)
        print(f"Files checked: {self.file_count}")
        print(f"INSERT statements validated: {self._insert_count}")
        print(f"Errors found: {self.error_count}")
        print(f"Warnings: {len(self.warnings)}")
        print()
        
        # Check for row 2 errors specifically (most common issue)
        row2_errors = []
        if self._insert_details:
            for detail in self._insert_details:
                if detail['row'] == 2 and not detail['match']:
                    row2_errors.append(detail)
        
        if row2_errors:
            print("=" * 80)
            print("*** ROW 2 ERRORS DETECTED ***")
            print("=" * 80)
            print(f"Found {len(row2_errors)} INSERT statement(s) with row 2 column/value mismatches.")
            print("These match the MySQL error: 'Column count doesn't match value count at row 2'")
            print()
            for detail in row2_errors:
                print(f"  INSERT #{detail['insert_num']} in table `{detail['table']}` (Line ~{detail['line']})")
                print(f"    Expected: {detail['columns']} columns, Found: {detail['values']} values")
                print(f"    Row 2 snippet: {detail['snippet'][:100]}...")
                print()
            print("=" * 80)
            print()
        
        if self.errors:
            print("ERRORS:")
            print("-" * 80)
            for error in self.errors:
                print(f"  [ERROR] {error}")
            print()
        
        if self.warnings:
            print("WARNINGS:")
            print("-" * 80)
            for warning in self.warnings:
                print(f"  [WARN] {warning}")
            print()
        
        if self.export_mode:
            export_file = "validation_export.txt"
            if self._insert_details:
                with open(export_file, 'w', encoding='utf-8') as f:
                    f.write("=" * 80 + "\n")
                    f.write("DETAILED VALIDATION EXPORT\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(f"Total INSERT statements: {self._insert_count}\n")
                    f.write(f"Total rows checked: {len(self._insert_details)}\n\n")
                    f.write("IMPORTANT: MySQL error messages report 'row X' within a specific INSERT statement,\n")
                    f.write("not row X of the file. Use the INSERT # to identify which statement failed.\n\n")
                    
                    current_table = None
                    current_insert = None
                    for detail in self._insert_details:
                        # Group by INSERT statement number for clarity
                        if detail['insert_num'] != current_insert:
                            current_insert = detail['insert_num']
                            if detail['table'] != current_table:
                                current_table = detail['table']
                                f.write(f"\n{'=' * 80}\n")
                                f.write(f"Table: `{current_table}`\n")
                                f.write(f"{'=' * 80}\n")
                            f.write(f"\nINSERT Statement #{current_insert} (Line ~{detail['line']})\n")
                            f.write(f"  Context: {detail['insert_snippet']}...\n")
                            f.write(f"  Rows in this INSERT:\n")
                        
                        status = "OK" if detail['match'] else "ERROR"
                        f.write(f"    Row {detail['row']}: {detail['values']}/{detail['columns']} values [{status}]\n")
                        if not detail['match']:
                            f.write(f"      Snippet: {detail['snippet']}...\n")
                            f.write(f"      NOTE: MySQL 'row {detail['row']}' error refers to row {detail['row']} in THIS INSERT (#{detail['insert_num']}), not the file!\n")
                
                print(f"\n[EXPORT] Detailed report exported to: {export_file}")
                print(f"         This report shows every INSERT statement and every row for debugging.")
                print()
            else:
                print(f"\n[EXPORT] No details to export (insert_details is empty)")
                print()
        
        if not self.errors and not self.warnings:
            print("[SUCCESS] All files validated successfully!")
            print()
            return True
        else:
            print("[FAILED] Validation failed. Please fix the errors above before uploading.")
            print()
            return False


def main():
    """Main entry point"""
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    export = '--export' in sys.argv or '-e' in sys.argv
    if verbose or export:
        sys.argv = [a for a in sys.argv if a not in ('--verbose', '-v', '--export', '-e')]
    
    if len(sys.argv) < 2:
        print("Usage: python validate_sql.py <file_or_directory> [--verbose] [--export]")
        print("  Example: python validate_sql.py event_hub_random_event_20260110_204544.sql")
        print("  Example: python validate_sql.py Low Event Sequence/")
        print("  Example: python validate_sql.py . --verbose")
        print("  Example: python validate_sql.py file.sql --export  (exports detailed report)")
        sys.exit(1)
    
    target = sys.argv[1]
    validator = SQLValidator()
    validator.verbose = verbose
    validator.export_mode = export
    
    if os.path.isfile(target):
        if target.endswith('.sql'):
            is_valid = validator.validate_bulk_upload(target)
        else:
            print(f"Error: {target} is not a SQL file")
            sys.exit(1)
    elif os.path.isdir(target):
        is_valid = validator.validate_directory(target)
    else:
        print(f"Error: {target} not found")
        sys.exit(1)
    
    success = validator.print_report()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
