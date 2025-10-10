# ACE Event Generator - Usage Guide

## Quick Start

### Step 1: Create Your Configuration

**Option A: Start with a template**
```bash
python create_csv_template.py my_event.csv
```

**Option B: Use the example**
```bash
cp example_event_config.csv my_event.csv
```

### Step 2: Edit in Spreadsheet

Open `my_event.csv` in:
- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Any spreadsheet editor

The CSV has 4 columns:
- **tier**: low, mid, or high
- **wave_number**: 1-10, or "boss"
- **slot**: 1-10 (which monster slot in the wave)
- **wcid**: The Weenie Class ID of the monster to spawn

### Step 3: Generate Files

```bash
python generate_event_files.py my_event.csv
```

### Step 4: Upload to Server

Upload the generated files from these folders to your ACE server:
- `Low Event Sequence/`
- `Mid Event Sequence/`
- `High Event Sequence/`

## Examples

### Example 1: All Same Monster
Want all 10 slots in Wave 1 to spawn Death Dillo (WCID 300101071)?

```csv
tier,wave_number,slot,wcid
low,1,1,300101071
low,1,2,300101071
low,1,3,300101071
low,1,4,300101071
low,1,5,300101071
low,1,6,300101071
low,1,7,300101071
low,1,8,300101071
low,1,9,300101071
low,1,10,300101071
```

### Example 2: Mixed Monsters
Want 5 of one type, 5 of another?

```csv
tier,wave_number,slot,wcid
low,2,1,300101072
low,2,2,300101072
low,2,3,300101072
low,2,4,300101072
low,2,5,300101072
low,2,6,300101073
low,2,7,300101073
low,2,8,300101073
low,2,9,300101073
low,2,10,300101073
```

### Example 3: Varied Boss Wave
Want different boss monsters in the boss wave?

```csv
tier,wave_number,slot,wcid
low,boss,1,300101090
low,boss,2,300101090
low,boss,3,300101090
low,boss,4,300101091
low,boss,5,300101091
low,boss,6,300101091
low,boss,7,300101092
low,boss,8,300101092
low,boss,9,300101093
low,boss,10,300101093
```

## Spreadsheet Editing Tips

### Fill Down Technique
1. Type the WCID in the first cell
2. Select cells you want to fill
3. Use Ctrl+D (Windows) or Cmd+D (Mac) to fill down

### Copy-Paste Blocks
1. Create one complete wave (10 rows)
2. Copy the entire block
3. Paste and change wave_number and WCIDs as needed

### Filter by Tier
Most spreadsheet apps let you filter by tier to work on one difficulty at a time.

### Find and Replace
Use Find/Replace to quickly change all instances of a WCID across multiple waves.

## File Output

The generator creates these files for each tier:

### Low Tier
- `694200293 Low Event Controller.sql` - Main controller
- `694200310 Low Event Wave 1.sql` - Wave 1 generator
- `694200311 Low Event Wave 2.sql` - Wave 2 generator
- ... (waves 3-9)
- `694200319 Low Event Wave 10.sql` - Wave 10 generator
- `694200320 Low Event Boss.sql` - Boss generator

### Mid Tier
- `694200300 Mid Event Controller.sql` - Main controller
- `694200321 Mid Event Wave 1.sql` - Wave 1 generator
- ... (waves 2-10)
- `694200331 Mid Event Boss.sql` - Boss generator

### High Tier
- `694200304 High Event Controller.sql` - Main controller
- `694200332 High Event Wave 1.sql` - Wave 1 generator
- ... (waves 2-10)
- `694200342 High Event Boss.sql` - Boss generator

## Common Workflows

### Creating a New Event
1. Run `python create_csv_template.py new_event.csv`
2. Open in spreadsheet
3. Replace placeholder WCIDs with your monsters
4. Save
5. Run `python generate_event_files.py new_event.csv`
6. Upload generated SQL files to server

### Updating Existing Event
1. Open your existing CSV (or create from scratch)
2. Modify monster WCIDs as desired
3. Run generator again (overwrites old files)
4. Upload updated SQL files to server

### Creating Only One Tier
Only include rows for that tier in your CSV:

```csv
tier,wave_number,slot,wcid
high,1,1,500101071
high,1,2,500101071
...
```

The generator will only create High tier files.

### Testing on Development Server
1. Generate test files with placeholder WCIDs
2. Upload to dev server
3. Test event in-game
4. Adjust WCIDs in CSV
5. Regenerate and re-upload

## Troubleshooting

### Error: "Wave must have exactly 10 monsters"
**Problem**: A wave doesn't have all 10 slots filled.

**Solution**: Check your CSV - each wave must have slots 1-10 with WCIDs.

### Error: "Config file not found"
**Problem**: Wrong file path or filename.

**Solution**: Check the filename and run from correct directory.

### Warning: "No configuration found for tier"
**Problem**: CSV is missing entries for that tier.

**Solution**: Either add entries for that tier, or it will be skipped (which is fine if you only want to generate some tiers).

### Generated Files Look Wrong
**Problem**: Wrong WCIDs in CSV.

**Solution**: Open the generated .sql file and check the `weenie_Class_Id` values in the `weenie_properties_generator` section.

## Advanced Tips

### Version Control
Keep your CSV files in version control (git) to track event changes over time:
```bash
git add my_event.csv
git commit -m "Updated low tier wave 3 monsters"
```

### Multiple Events
Create separate CSV files for different events:
```
halloween_event.csv
winter_event.csv
raid_event.csv
```

### Batch Generation
Generate multiple events at once:
```bash
python generate_event_files.py event1.csv
python generate_event_files.py event2.csv
python generate_event_files.py event3.csv
```

### Backup Before Overwriting
The generator overwrites existing files. Keep backups:
```bash
cp -r "Low Event Sequence" "Low Event Sequence.backup"
```

## Getting Help

### Check Your CSV Format
Make sure:
- First row is the header: `tier,wave_number,slot,wcid`
- tier is one of: low, mid, high
- wave_number is 1-10 or "boss"
- slot is 1-10
- wcid is a valid monster weenie ID number

### Verify Generated SQL
Open a generated SQL file and look for:
- Correct weenie_Class_Id in the generator entries
- Exactly 10 generator entries per wave
- Proper SQL syntax (no missing semicolons)

### Test Individual Waves
You can test by uploading just one wave file and controller to see if monsters spawn correctly before generating all files.

## Command Reference

### Generate from CSV
```bash
python generate_event_files.py <config.csv>
```

### Create blank template
```bash
python create_csv_template.py [output_file] [default_wcid]
```

Examples:
```bash
# Creates event_template.csv with default WCID 300101071
python create_csv_template.py

# Creates custom_event.csv with WCID 999999
python create_csv_template.py custom_event.csv 999999
```

## File Locations

After generation, files are organized as:
```
/your/directory/
├── Low Event Sequence/
│   ├── 694200293 Low Event Controller.sql
│   ├── 694200310-694200319 (Wave files)
│   └── 694200320 Low Event Boss.sql
├── Mid Event Sequence/
│   └── (Similar structure)
└── High Event Sequence/
    └── (Similar structure)
```

Upload these entire folders to your ACE server's weenie directory.
