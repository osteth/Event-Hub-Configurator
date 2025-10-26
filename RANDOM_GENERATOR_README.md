# Random Event Configuration Generator

## Overview

`generate_random_event.py` is a powerful script that automatically creates randomized event configurations using the mobs from `Spawnable Mobs List.csv`. It intelligently selects appropriate mobs based on difficulty tiers and generates CSV files that can be used with `generate_event_files.py` to create SQL event files.

## Key Features

✅ **Difficulty Matching** - Automatically uses Low/Mid/High mobs for corresponding event tiers  
✅ **Smart Boss Waves** - Creates boss waves with configurable boss count + regular mob support  
✅ **Two Randomization Modes** - Same-mob waves (default) or fully mixed waves  
✅ **Flexible Configuration** - Command-line flags for full customization  
✅ **Reproducible Results** - Optional seed parameter for consistent output  
✅ **Safe & Validated** - Ensures all waves have exactly 10 slots

## Quick Start

### Basic Usage (Generate All Tiers)

```bash
python generate_random_event.py
```

This creates `random_event.csv` with:
- All 3 tiers (Low, Mid, High)
- 10 waves + 1 boss wave per tier
- Same mob per wave (your typical approach)
- 1 boss + 9 regular mobs in boss waves

### Generate SQL Files from Random Config

```bash
python generate_random_event.py -o my_event.csv
python generate_event_files.py my_event.csv
```

## Command-Line Options

### `--tiers` / `-t` (Choose Tiers)

Generate specific tiers only:

```bash
# Generate only low tier
python generate_random_event.py -t low

# Generate low and mid tiers
python generate_random_event.py -t low mid

# Generate all tiers (default)
python generate_random_event.py -t all
```

### `--mixed-waves` / `-m` (Randomization Mode)

**Default (without flag)**: All 10 slots spawn the same mob (your typical approach)
```bash
python generate_random_event.py
# Wave 1: 10x Death Dillo
# Wave 2: 10x Huge Scarecrow
# etc.
```

**Mixed mode (with flag)**: Each slot can spawn a different mob
```bash
python generate_random_event.py --mixed-waves
# Wave 1: Death Dillo, Scarecrow, Dillo, Mini-Undead, Scarecrow, etc.
```

### `--output` / `-o` (Output Filename)

Specify custom output filename:

```bash
python generate_random_event.py -o halloween_event.csv
python generate_random_event.py -o raid_event.csv
```

### `--boss-count` (Bosses in Boss Wave)

Control how many bosses appear in the boss wave:

```bash
# Default: 1 boss + 9 regular mobs
python generate_random_event.py

# 3 bosses + 7 regular mobs
python generate_random_event.py --boss-count 3

# 5 bosses + 5 regular mobs (intense!)
python generate_random_event.py --boss-count 5
```

### `--seed` (Reproducible Randomization)

Generate the same random event every time:

```bash
# Same seed = same output
python generate_random_event.py --seed 12345
python generate_random_event.py --seed 12345  # Identical to above

# Different seed = different output
python generate_random_event.py --seed 67890
```

Useful for:
- Testing specific configurations
- Sharing event designs with team
- Version control and debugging

### `--mobs-file` (Custom Mob List)

Use a different spawnable mobs CSV:

```bash
python generate_random_event.py --mobs-file custom_mobs.csv
```

## Usage Examples

### Example 1: Quick Random Event (Your Typical Style)

Generate a random event with same-mob waves:

```bash
python generate_random_event.py -o quick_event.csv
python generate_event_files.py quick_event.csv
```

**Result**: 
- Low tier wave 1: 10 identical mobs (e.g., all Death Dillos)
- Low tier wave 2: 10 identical mobs (e.g., all Huge Scarecrows)
- Boss wave: 1 boss + 9 identical support mobs

### Example 2: Experimental Mixed Event

Try fully randomized waves for variety:

```bash
python generate_random_event.py --mixed-waves -o experimental_event.csv
python generate_event_files.py experimental_event.csv
```

**Result**: Each wave has 10 different mobs mixed together

### Example 3: High-Intensity Boss Event

Create challenging high-tier with multiple bosses:

```bash
python generate_random_event.py -t high --boss-count 5 -o intense_high.csv
python generate_event_files.py intense_high.csv
```

**Result**: High tier boss wave has 5 bosses + 5 regular mobs

### Example 4: Specific Tiers with Custom Names

Generate only mid and high for end-game content:

```bash
python generate_random_event.py -t mid high -o endgame_event.csv
python generate_event_files.py endgame_event.csv
```

### Example 5: Reproducible Test Event

Create a test event you can regenerate exactly:

```bash
python generate_random_event.py --seed 42 -o test_event.csv
# Later, regenerate identical event:
python generate_random_event.py --seed 42 -o test_event.csv
```

## How It Works

### 1. Mob Categorization

The script reads `Spawnable Mobs List.csv` and categorizes mobs:

```
Low Difficulty:
  Regular: [Death Dillo, Dire Carenzi, Mini-Undead, ...]
  Boss: [Delacim, Big Boss Moss, My Buddy Doll, ...]

Mid Difficulty:
  Regular: [Rage Rabbit, Angry Beaver, Dark Entity, ...]
  Boss: [King of the Garden, The Forgotten One, ...]

High Difficulty:
  Regular: [Molten Menace, Titan Margul, Ancient Oak, ...]
  Boss: [Charred Benedino, Enlightened Jester, ...]
```

### 2. Wave Generation

**Same-Mob Mode (Default)**:
- Randomly picks ONE mob from the tier's regular mobs
- Uses that mob for all 10 slots in the wave

**Mixed Mode**:
- Randomly picks a different mob for EACH of the 10 slots
- More variety, more chaos!

### 3. Boss Wave Generation

Always follows this pattern:
- Slots 1 to N: Boss mobs (N = boss-count)
- Remaining slots: Regular mobs
- Default: 1 boss + 9 regular mobs

### 4. Output Format

Generates CSV compatible with `generate_event_files.py`:

```csv
tier,wave_number,slot,wcid
low,1,1,500116
low,1,2,500116
...
low,boss,1,2001004
low,boss,2,300101050
...
```

## Integration with Existing Workflow

The random generator fits seamlessly into your existing workflow:

### Old Workflow:
1. Manually create CSV with monster IDs
2. Run `generate_event_files.py`
3. Upload SQL files to server

### New Workflow:
1. Run `generate_random_event.py` (auto-generates CSV)
2. Run `generate_event_files.py` (same as before)
3. Upload SQL files to server

You can still manually edit the generated CSV if you want to tweak specific waves!

## Statistics

Based on your `Spawnable Mobs List.csv`:

| Tier | Regular Mobs | Boss Mobs |
|------|--------------|-----------|
| Low  | 31 mobs      | 5 bosses  |
| Mid  | 59 mobs      | 16 bosses |
| High | 16 mobs      | 14 bosses |

**Total**: 106 regular mobs + 35 boss mobs = **141 spawnable creatures**

## Tips & Best Practices

### 1. Start with Default Settings
Your typical approach works great for most events:
```bash
python generate_random_event.py
```

### 2. Experiment with Mixed Waves
Try mixed mode for special/holiday events:
```bash
python generate_random_event.py --mixed-waves -o special_event.csv
```

### 3. Save Multiple Versions
Generate several random events and pick the best:
```bash
python generate_random_event.py -o option1.csv
python generate_random_event.py -o option2.csv
python generate_random_event.py -o option3.csv
```

### 4. Manual Tweaking
Generated CSV is editable - open in spreadsheet and adjust specific waves:
```bash
python generate_random_event.py -o base_event.csv
# Edit base_event.csv in Excel/Sheets
python generate_event_files.py base_event.csv
```

### 5. Version Control
Keep your generated CSVs in version control:
```bash
python generate_random_event.py -o v1_event.csv
git add v1_event.csv
git commit -m "Random event v1"
```

## Troubleshooting

### "No regular mobs found for tier"

**Problem**: The Spawnable Mobs List doesn't have non-boss mobs for that difficulty.

**Solution**: Check your CSV file or generate a different tier.

### "No boss mobs found for tier"

**Problem**: The Spawnable Mobs List doesn't have boss mobs for that difficulty.

**Solution**: Check your CSV file or generate a different tier.

### Generated event feels repetitive

**Problem**: Same mobs appearing in multiple waves.

**Solution**: This is expected with small mob pools. Try:
- Mixed-waves mode: `--mixed-waves`
- Manually edit the CSV to adjust
- Add more mobs to your Spawnable Mobs List

### Want identical events on multiple servers

**Problem**: Need same random event on dev and production.

**Solution**: Use the `--seed` parameter:
```bash
python generate_random_event.py --seed 12345
```
Run with same seed on all servers.

## Advanced Usage

### Generate Multiple Events in Bulk

```bash
#!/bin/bash
# Generate 5 different random events
for i in {1..5}; do
  python generate_random_event.py --seed $i -o event_$i.csv
done
```

### Create Difficulty-Specific Events

```bash
# Easy mode - only low tier
python generate_random_event.py -t low -o easy_mode.csv

# Normal mode - low and mid
python generate_random_event.py -t low mid -o normal_mode.csv

# Hard mode - all tiers, mixed waves
python generate_random_event.py -t all --mixed-waves -o hard_mode.csv

# Insane mode - high tier only, 5 bosses
python generate_random_event.py -t high --boss-count 5 -o insane_mode.csv
```

### Testing Different Configurations

```bash
# Test same-mob waves
python generate_random_event.py -o test_same.csv
python generate_event_files.py test_same.csv

# Test mixed-mob waves
python generate_random_event.py --mixed-waves -o test_mixed.csv
python generate_event_files.py test_mixed.csv

# Compare results in-game
```

## File Structure

After running the complete workflow:

```
/your/directory/
├── Spawnable Mobs List.csv         # Your mob database
├── generate_random_event.py        # NEW: Random generator
├── random_event.csv                # Generated config
├── generate_event_files.py         # Existing SQL generator
├── Low Event Sequence/
│   ├── 694200293 Low Event Controller.sql
│   ├── 694200310-694200319 (Wave files)
│   └── 694200320 Low Event Boss.sql
├── Mid Event Sequence/
│   └── (Similar structure)
└── High Event Sequence/
    └── (Similar structure)
```

## Summary

The random event generator adds a powerful new capability to your ACE event creation toolkit:

**Before**: Manual CSV creation → SQL generation → Upload  
**After**: Automatic CSV generation → SQL generation → Upload

This saves time and introduces fun variety to your server events while maintaining full compatibility with your existing workflow!

---

**Ready to generate your first random event?**

```bash
python generate_random_event.py
python generate_event_files.py random_event.csv
# Upload generated SQL files to your server!
```
