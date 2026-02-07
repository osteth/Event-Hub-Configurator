#!/usr/bin/env python3
"""Test counting values in a specific row"""

row = "(@parent_id,  2,  77, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)"

# Remove outer parentheses
if row.startswith('(') and row.endswith(')'):
    row = row[1:-1]

# Count commas
commas = row.count(',')
print(f"Commas: {commas}, Values: {commas + 1}")

# Manual split (simple, won't work for strings with commas)
values = [v.strip() for v in row.split(',')]
print(f"Split count: {len(values)}")
print(f"First 5: {values[:5]}")
print(f"Last 5: {values[-5:]}")
