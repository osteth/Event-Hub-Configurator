# Asheron's Call ACE Event Generator

A Python CLI tool to automatically generate SQL weenie files for multi-tier events on Asheron's Call ACE servers.

## Overview

This tool generates all necessary event files (controllers, wave generators, and boss generators) for three difficulty tiers (Low, Mid, High) based on a simple CSV configuration file.

## Features

- ✅ Generates event controllers for all three tiers
- ✅ Creates 10 wave generators per tier
- ✅ Creates boss wave generators
- ✅ Uses fixed Weenie IDs from Event Hub
- ✅ Maintains proper folder structure
- ✅ Easy CSV configuration (edit in spreadsheet)
- ✅ Generates proper SQL with all required properties

## Quick Start

### 1. Edit the Configuration File

Open `example_event_config.csv` in your favorite spreadsheet editor (Excel, Google Sheets, etc.)

The CSV format is:
```
tier,wave_number,slot,wcid
low,1,1,300101071
low,1,2,300101071
...
```

**Columns:**
- `tier`: Event difficulty (low, mid, or high)
- `wave_number`: Wave number (1-10) or "boss" for boss wave
- `slot`: Monster slot in that wave (1-10)
- `wcid`: Weenie Class ID of the monster to spawn

### 2. Run the Generator

```bash
python generate_event_files.py example_event_config.csv
```

Or with your own config file:
```bash
python generate_event_files.py my_event.csv
```

### 3. Files Generated

The tool creates/overwrites files in the proper folder structure:

```
Low Event Sequence/
├── 694200293 Low Event Controller.sql
├── 694200310 Low Event Wave 1.sql
├── 694200311 Low Event Wave 2.sql
├── ...
├── 694200319 Low Event Wave 10.sql
└── 694200320 Low Event Boss.sql

Mid Event Sequence/
├── 694200300 Mid Event Controller.sql
├── 694200321 Mid Event Wave 1.sql
├── ...
└── 694200331 Mid Event Boss.sql

High Event Sequence/
├── 694200304 High Event Controller.sql
├── 694200332 High Event Wave 1.sql
├── ...
└── 694200342 High Event Boss.sql
```

## Weenie ID Mapping

All Weenie IDs are fixed based on the Event Hub documentation:

### Low Tier
- Controller: 694200293
- Waves 1-10: 694200310-694200319
- Boss: 694200320

### Mid Tier
- Controller: 694200300
- Waves 1-10: 694200321-694200330
- Boss: 694200331

### High Tier
- Controller: 694200304
- Waves 1-10: 694200332-694200341
- Boss: 694200342

## CSV Configuration Tips

### Example: All Same Monster
```csv
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

### Example: Mixed Monsters
```csv
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

### Example: Boss Wave
```csv
low,boss,1,300101090
low,boss,2,300101090
low,boss,3,300101090
low,boss,4,300101091
low,boss,5,300101091
low,boss,6,300101091
low,boss,7,300101092
low,boss,8,300101092
low,boss,9,300101092
low,boss,10,300101093
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Workflow

1. **Edit CSV in spreadsheet** - Easy to manage monster spawns
2. **Run generator** - Creates all SQL files
3. **Upload to server** - Files overwrite existing event files
4. **Test in game** - Verify monster spawns

## File Structure

Each generated file includes:
- Proper DELETE statement (safe to re-run)
- Weenie basic properties
- Generator properties
- Exactly 10 monster generator entries per wave
- All necessary SQL tables and relationships

## Troubleshooting

### Error: "Wave must have exactly 10 monsters"
Make sure each wave has all 10 slots (1-10) configured in the CSV.

### Warning: "No configuration found for [tier]"
Add entries for that tier in your CSV file, or it will be skipped.

### Wave files not generating
Check that wave_number is between 1-10 or "boss" exactly.

## Advanced Usage

### Skipping a Tier
Simply don't include rows for that tier in your CSV. The generator will skip it.

### Partial Updates
You can include only the tiers/waves you want to regenerate. Missing waves won't be generated.

### Monster Distribution
You have full control over which monster appears in which slot (1-10) of each wave.

## Support

For questions about:
- **Weenie IDs**: Check `Event Hub Weenie ID's.md`
- **Monster WCIDs**: Refer to your ACE server's weenie database
- **Generator issues**: Verify CSV format matches the examples

## License

This tool is provided as-is for Asheron's Call ACE server administration.
