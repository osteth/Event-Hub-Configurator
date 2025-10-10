# ACE Event Generator - Project Summary

## Overview
This Python CLI tool automatically generates SQL weenie files for Asheron's Call ACE server events. It takes a simple CSV configuration and produces all necessary controller and generator files for three-tier (Low/Mid/High) events.

## Key Features
✅ **CSV-based configuration** - Edit in any spreadsheet software  
✅ **Three-tier support** - Low, Mid, and High difficulty  
✅ **Fixed Weenie IDs** - Uses predefined IDs from Event Hub  
✅ **10 waves + boss per tier** - Each wave with 10 independent monster generators  
✅ **Proper SQL structure** - Matches ACE server requirements exactly  
✅ **Folder organization** - Maintains proper directory structure  
✅ **Overwrite-safe** - Includes DELETE statements for safe re-generation  

## Project Files

### Core Scripts
| File | Purpose |
|------|---------|
| `generate_event_files.py` | Main generator - creates all SQL files from CSV config |
| `create_csv_template.py` | Helper to create blank CSV templates |

### Documentation
| File | Purpose |
|------|---------|
| `README_GENERATOR.md` | Complete tool documentation |
| `USAGE_GUIDE.md` | Step-by-step usage examples and tips |
| `PROJECT_SUMMARY.md` | This file - project overview |
| `Event Hub Weenie ID's.md` | Reference for all Weenie IDs used |

### Configuration Files
| File | Purpose |
|------|---------|
| `example_event_config.csv` | Full example with all 3 tiers configured |
| `test_template.csv` | Generated test template (gitignore) |

### Reference Files (Original POC)
These are your original event files that serve as the template:

**Low Event Sequence/** - Complete reference implementation
- `694200293 Low Event Controller.sql`
- `694200310-694200319` Wave generator files
- `694200320 Low Event Boss.sql`

**Mid Event Sequence/** - Partial implementation
- `694200300 Mid Event Controller.sql`
- Various generator files

**High Event Sequence/** - Partial implementation
- `694200304 High Event Controller.sql`
- Partial wave files

## How It Works

### 1. Input (CSV Configuration)
```csv
tier,wave_number,slot,wcid
low,1,1,300101071
low,1,2,300101071
...
```

### 2. Processing
- Reads CSV and groups by tier and wave
- Maps to fixed Weenie IDs from Event Hub
- Uses Low Event files as SQL template
- Substitutes monster WCIDs based on config

### 3. Output (SQL Files)
```
Low Event Sequence/
├── 694200293 Low Event Controller.sql
├── 694200310 Low Event Wave 1.sql
├── ...
└── 694200320 Low Event Boss.sql
```

## Weenie Structure

### Event Controller (per tier)
- Generates Event Bell
- Generates Exit Controller
- Generates 10 Wave Generators
- Generates 1 Boss Generator

### Wave Generator (per wave)
- Exactly 10 independent monster generators
- Each generator spawns 1 monster of specified WCID
- Properties: regeneration, radius, spawn behavior

### Boss Generator
- Same structure as wave generator
- Can contain different/stronger monsters

## Typical Workflow

```
1. Edit CSV in spreadsheet
   ↓
2. Run: python generate_event_files.py config.csv
   ↓
3. Files generated in tier folders
   ↓
4. Upload SQL files to ACE server
   ↓
5. Test event in-game
   ↓
6. Adjust CSV and regenerate as needed
```

## Weenie ID Mapping

### Low Tier (694200293-694200320)
- Controller: 694200293
- Waves: 694200310-694200319
- Boss: 694200320

### Mid Tier (694200300, 694200321-694200331)
- Controller: 694200300
- Waves: 694200321-694200330
- Boss: 694200331

### High Tier (694200304, 694200332-694200342)
- Controller: 694200304
- Waves: 694200332-694200341
- Boss: 694200342

### Shared
- Event Bell: 694200294
- Exit Controller: 694200295

## Design Decisions

### Why CSV?
- Easy to edit in spreadsheet software
- Simple structure: tier, wave, slot, wcid
- Can use copy/paste, fill-down, find/replace
- Version control friendly

### Why Fixed IDs?
- Server expects specific Weenie IDs
- Matches your Event Hub documentation
- No risk of ID conflicts
- Allows file overwrites safely

### Why 10 Independent Generators?
- Server behavior: spawns max 10 at once
- Each generator = 1 monster spawn
- Gives precise control over monster mix
- Matches your original Low Event implementation

### Why Templates?
- Ensures consistent SQL structure
- Maintains all required properties
- Based on proven working implementation (Low Event)
- Reduces risk of SQL errors

## Example Use Cases

### Case 1: Seasonal Event
Create Halloween event with undead monsters:
```csv
low,1,1,undead_wcid_1
low,1,2,undead_wcid_1
...
```

### Case 2: Difficulty Progression
Low tier: weak monsters  
Mid tier: moderate monsters  
High tier: strong monsters  

### Case 3: Mixed Waves
Wave 1: 5 ranged + 5 melee  
Wave 2: 7 casters + 3 healers  
Boss: 3 mini-bosses + 7 adds  

### Case 4: Themed Events
Fire Event: Fire elementals all tiers  
Ice Event: Ice creatures all tiers  
Raid Event: Boss-level monsters even in low tier  

## Technical Details

### SQL Structure Generated
Each file contains proper INSERT statements for:
- `weenie` table
- `weenie_properties_int`
- `weenie_properties_bool`
- `weenie_properties_float`
- `weenie_properties_string`
- `weenie_properties_d_i_d`
- `weenie_properties_generator`

Controllers additionally include:
- `weenie_properties_attribute`
- `weenie_properties_attribute_2nd`
- `weenie_properties_skill`
- `weenie_properties_body_part`
- `weenie_properties_emote`
- `weenie_properties_emote_action`

### Generator Properties
- **probability**: -1 (always spawn)
- **delay**: 1 for waves, 1600 for controller
- **init_Create**: 1 (spawn on init)
- **max_Create**: 1 (one at a time)
- **when_Create**: 1 (regenerate on destruction)
- **where_Create**: 2 (scatter) or 4 (specific)

## Dependencies
- Python 3.6+
- Standard library only (csv, os, sys, datetime, collections)
- No external packages required

## Platform
- Linux/Unix/Mac compatible
- Windows compatible
- Runs anywhere Python 3.6+ is installed

## Future Enhancements (Optional)

Potential additions if needed:
- GUI interface for CSV editing
- Validation tool to check CSV before generation
- Diff tool to compare event configs
- Monster database lookup integration
- Batch processing for multiple events
- Export to different ACE server formats

## Credits
Based on original POC event files for Asheron's Call ACE server.  
Low Event Sequence used as reference template for SQL structure.

## Version
Initial Release - 2025-01-10

## License
Free to use for ACE server administration and event creation.
