#!/usr/bin/env python3
"""
CSV Template Generator for ACE Event Configuration
Creates a blank CSV template for easy editing in spreadsheets
"""

import csv
import sys


def create_template(output_file='event_template.csv', default_wcid=300101071):
    """Create a CSV template with default monster IDs."""
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['tier', 'wave_number', 'slot', 'wcid'])
        
        # Generate template for all three tiers
        for tier in ['low', 'mid', 'high']:
            # 10 regular waves
            for wave_num in range(1, 11):
                for slot in range(1, 11):
                    writer.writerow([tier, wave_num, slot, default_wcid])
            
            # Boss wave
            for slot in range(1, 11):
                writer.writerow([tier, 'boss', slot, default_wcid])
    
    print(f"✅ Created template: {output_file}")
    print(f"   - All slots filled with default WCID: {default_wcid}")
    print(f"   - Edit in spreadsheet software (Excel, Google Sheets)")
    print(f"   - Change WCIDs to your monster IDs")
    print(f"   - Run: python generate_event_files.py {output_file}")


def main():
    output_file = sys.argv[1] if len(sys.argv) > 1 else 'event_template.csv'
    default_wcid = int(sys.argv[2]) if len(sys.argv) > 2 else 300101071
    
    create_template(output_file, default_wcid)


if __name__ == '__main__':
    main()
