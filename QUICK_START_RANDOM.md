# 🎲 Random Event Generator - Quick Start

## The Fastest Way to Create Events

### 1️⃣ Generate Random Configuration
```bash
python generate_random_event.py
```
✅ Creates `random_event.csv` with all 3 tiers  
✅ Uses mobs from `Spawnable Mobs List.csv`  
✅ Matches mob difficulty to event tier  
✅ Boss waves: 1 boss + 9 support mobs  

### 2️⃣ Create SQL Files
```bash
python generate_event_files.py random_event.csv
```
✅ Generates all SQL files in tier folders

### 3️⃣ Upload to Server
Upload these folders to your ACE server:
- `Low Event Sequence/`
- `Mid Event Sequence/`
- `High Event Sequence/`

**Done!** 🎉

---

## Common Variations

### Generate Only Specific Tiers
```bash
# Low tier only
python generate_random_event.py -t low -o low_only.csv

# Mid and high only
python generate_random_event.py -t mid high -o endgame.csv
```

### Mixed Mobs per Wave (Experimental)
```bash
python generate_random_event.py --mixed-waves -o mixed.csv
```
Instead of 10 identical mobs per wave, each slot gets a different random mob!

### Multiple Bosses in Boss Wave
```bash
# 3 bosses + 7 support mobs
python generate_random_event.py --boss-count 3 -o intense.csv

# 5 bosses + 5 support mobs
python generate_random_event.py --boss-count 5 -o ultra_hard.csv
```

### Custom Output Filename
```bash
python generate_random_event.py -o halloween_event.csv
python generate_random_event.py -o winter_raid.csv
```

---

## Examples

### Example 1: Quick Random Event
```bash
python generate_random_event.py
python generate_event_files.py random_event.csv
# Upload and done!
```

### Example 2: High-Level Content Only
```bash
python generate_random_event.py -t high -o highlevel.csv
python generate_event_files.py highlevel.csv
```

### Example 3: Experimental Mixed Event
```bash
python generate_random_event.py --mixed-waves -o experimental.csv
python generate_event_files.py experimental.csv
```

### Example 4: Boss Rush Mode
```bash
python generate_random_event.py --boss-count 5 -o boss_rush.csv
python generate_event_files.py boss_rush.csv
```

---

## What Gets Generated

| Item | Details |
|------|---------|
| **Tiers** | Low, Mid, High (or your selection) |
| **Waves per tier** | 10 regular + 1 boss = 11 total |
| **Mobs per wave** | 10 monsters |
| **Mob selection** | Random from appropriate difficulty tier |
| **Boss wave** | 1 boss + 9 regulars (configurable) |
| **Output format** | CSV compatible with generate_event_files.py |

---

## Your Spawnable Mobs

Based on `Spawnable Mobs List.csv`:

- **Low tier**: 31 regular mobs + 5 bosses
- **Mid tier**: 59 regular mobs + 16 bosses  
- **High tier**: 16 regular mobs + 14 bosses

**Total pool**: 106 regular mobs + 35 bosses = **141 creatures**

---

## Tips

💡 **Generate multiple options and pick the best**:
```bash
python generate_random_event.py -o option1.csv
python generate_random_event.py -o option2.csv
python generate_random_event.py -o option3.csv
```

💡 **You can still edit the generated CSV manually** before running generate_event_files.py

💡 **Use `--seed` for reproducible results**:
```bash
python generate_random_event.py --seed 12345
```

---

## Full Documentation

📖 See **[RANDOM_GENERATOR_README.md](RANDOM_GENERATOR_README.md)** for:
- Detailed flag documentation
- Advanced usage examples
- Troubleshooting
- Best practices

📖 See **[README.md](README.md)** for:
- Overview of the complete event system
- Manual CSV editing guide
- SQL generation details

---

## Workflow Comparison

### Old Workflow:
1. Create blank template
2. Manually fill in 330 rows with monster IDs
3. Run generate_event_files.py
4. Upload SQL files

### New Workflow:
1. Run generate_random_event.py ⚡
2. Run generate_event_files.py
3. Upload SQL files

**Time saved**: 95% 🚀

---

**Ready to create your first random event?**

```bash
python generate_random_event.py
```
