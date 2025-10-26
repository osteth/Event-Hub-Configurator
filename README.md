# Asheron's Call ACE Event Generator

**Automatically generate SQL weenie files for multi-tier server events**

## What This Does

This Python CLI tool generates all SQL files needed for Asheron's Call ACE server events with three difficulty tiers (Low, Mid, High). Each tier has:
- 1 Event Controller
- 10 Wave Generators (10 monsters each)
- 1 Boss Wave Generator (10 monsters)

Instead of manually creating and editing 33+ SQL files, you can:
- 🎲 **Auto-generate random events** from your spawnable mobs list (NEW!)
- ✏️ Edit a CSV file in a spreadsheet and run the generator
- 📋 Use pre-made templates

## Quick Start

### 1. Create a Configuration File

**Option A: 🎲 Generate a random event (NEW!)**
```bash
python generate_random_event.py -o my_event.csv
```
This automatically creates a random event using mobs from `Spawnable Mobs List.csv`, matching difficulty tiers appropriately!

**Option B: Use the example**
```bash
cp example_event_config.csv my_event.csv
```

**Option C: Generate a blank template**
```bash
python create_csv_template.py my_event.csv
```

### 2. Edit in Your Favorite Spreadsheet

Open `my_event.csv` in Excel, Google Sheets, or any spreadsheet editor.

The file has 4 columns:
- `tier` - low, mid, or high
- `wave_number` - 1 through 10, or "boss"
- `slot` - 1 through 10 (which monster in the wave)
- `wcid` - The Weenie Class ID of the monster to spawn

### 3. Generate the Files

```bash
python generate_event_files.py my_event.csv
```

### 4. Upload to Server

Upload the generated files to your ACE server:
- `Low Event Sequence/` folder
- `Mid Event Sequence/` folder  
- `High Event Sequence/` folder

## Example Configuration

Here's what the CSV looks like:

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
low,2,1,300101072
low,2,2,300101072
...
```

**Each wave needs exactly 10 rows** (one for each monster slot).

## Files Generated

For **each tier**, the tool generates:

### Low Tier Example
```
Low Event Sequence/
├── 694200293 Low Event Controller.sql
├── 694200310 Low Event Wave 1.sql
├── 694200311 Low Event Wave 2.sql
├── 694200312 Low Event Wave 3.sql
├── 694200313 Low Event Wave 4.sql
├── 694200314 Low Event Wave 5.sql
├── 694200315 Low Event Wave 6.sql
├── 694200316 Low Event Wave 7.sql
├── 694200317 Low Event Wave 8.sql
├── 694200318 Low Event Wave 9.sql
├── 694200319 Low Event Wave 10.sql
└── 694200320 Low Event Boss.sql
```

Similar files are generated for Mid and High tiers.

## Features

✅ **Easy Configuration** - Edit CSV in any spreadsheet software  
✅ **Consistent Output** - Generates proper SQL every time  
✅ **Fixed Weenie IDs** - Uses IDs from Event Hub Weenie ID's.md  
✅ **Safe Overwrites** - Includes DELETE statements  
✅ **Flexible Monster Mix** - Each wave can have different monsters  
✅ **Three Difficulty Tiers** - Low, Mid, High  
✅ **No Dependencies** - Python 3.6+ standard library only  

## Common Use Cases

### All Same Monster in a Wave
Perfect for swarm waves:
```csv
low,1,1,300101071
low,1,2,300101071
low,1,3,300101071
...all 10 slots...
```

### Mixed Monsters in a Wave
Create variety:
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

### Boss Wave with Multiple Boss Types
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

## Commands

### Generate Event Files
```bash
python generate_event_files.py <config.csv>
```

### Create Template
```bash
# Default template with WCID 300101071
python create_csv_template.py

# Custom template
python create_csv_template.py my_event.csv 999999
```

## Documentation

- **[README_GENERATOR.md](README_GENERATOR.md)** - Complete tool documentation
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Step-by-step examples and tips
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Technical details and architecture
- **[Event Hub Weenie ID's.md](Event%20Hub%20Weenie%20ID's.md)** - Weenie ID reference

## Requirements

- Python 3.6 or higher
- No external dependencies
- Works on Windows, Mac, Linux

## Workflow

```
Edit CSV → Run Generator → Upload SQL Files → Test In-Game → Iterate
```

## Weenie ID Reference

All Weenie IDs are fixed and documented in `Event Hub Weenie ID's.md`:

### Low Tier
- Controller: 694200293
- Waves: 694200310-694200319
- Boss: 694200320

### Mid Tier
- Controller: 694200300
- Waves: 694200321-694200330
- Boss: 694200331

### High Tier
- Controller: 694200304
- Waves: 694200332-694200341
- Boss: 694200342

## Tips for Spreadsheet Editing

1. **Fill Down**: Type WCID once, select cells, Ctrl+D to fill
2. **Copy Blocks**: Copy entire wave (10 rows), paste for other waves
3. **Find & Replace**: Quickly change monster types across waves
4. **Filter by Tier**: Work on one difficulty at a time
5. **Save Often**: Keep backups of working configurations

## Troubleshooting

**Error: "Wave must have exactly 10 monsters"**
- Make sure each wave has rows for slots 1-10

**Warning: "No configuration found for tier"**
- Add entries for that tier, or it will be skipped

**Files not generating**
- Check CSV format matches example
- Verify wave_number is 1-10 or "boss"
- Ensure slot numbers are 1-10

## Support

For questions about:
- **Weenie IDs**: Check `Event Hub Weenie ID's.md`
- **Usage Examples**: See `USAGE_GUIDE.md`
- **Technical Details**: See `PROJECT_SUMMARY.md`

## Credits

Based on the Low Event Sequence POC implementation for Asheron's Call ACE servers.

## License

Free to use for ACE server administration and event creation.

---

**Ready to create your event?**

```bash
python create_csv_template.py my_event.csv
# Edit my_event.csv in your spreadsheet
python generate_event_files.py my_event.csv
# Upload generated files to server
```
