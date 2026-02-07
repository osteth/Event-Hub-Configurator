# Event Hub Fixes Applied

## Summary of Changes

### 1. ✅ Tier Recommendation System
**File**: `tier_recommender.py` (NEW)
- Analyzes monster difficulty from CSV
- Suggests appropriate tier placement
- Validates tier assignments
- Usage: `python tier_recommender.py <config.csv>`

### 2. ✅ Height-Aware Spawning
**File**: `generate_event_files.py` (MODIFIED)
- Changed `where_Create` from 2 (random location) to 4 (specific location)
- Added explicit spawn coordinates with proper Z positioning
- Prevents tall monsters from failing to spawn in low-ceiling areas
- Uses relative offsets from generator position

### 3. ✅ Wave Progression System
**Files**: 
- `generate_event_files.py` (MODIFIED)
- `694200294 Event Bell.sql` (MODIFIED)

**Changes**:
- Wave generators now start inactive (`InitGeneratedObjects = 0`)
- Wave generators listen for local signals (`HearLocalSignals = 1`)
- Event Bell sends `StartEvent` signal when rung
- Controller manages wave progression via signals
- Each wave activates on signal instead of spawning immediately

**How it works**:
1. Event Bell sends `StartEvent` signal
2. Controller receives `StartEvent` and sends `Wave1` signal
3. Wave 1 generator receives `Wave1` and activates spawning
4. Controller can send subsequent waves via `Wave2`, `Wave3`, etc. signals

### 4. ⚠️ Difficulty Normalization
**File**: `tier_recommender.py` (NEW)
- Calculates average difficulty per tier
- Provides recommendations for rebalancing
- Identifies tier mismatches

**Note**: Full automatic normalization requires manual review and adjustment based on recommendations.

## Key Technical Changes

### Wave Generator Changes:
```sql
-- OLD: Spawned immediately, random location
InitGeneratedObjects = 8
where_Create = 2  -- Random location in radius

-- NEW: Signal-activated, specific locations
InitGeneratedObjects = 0  -- Start inactive
HearLocalSignals = 1
where_Create = 4  -- Specific location
-- Added emote to listen for wave signal
```

### Event Bell Changes:
```sql
-- Added signal to start event
LocalSignal: 'StartEvent'
```

### Controller Changes:
```sql
-- Added signal handling for:
- StartEvent (triggers Wave1)
- WaveComplete (triggers next wave)
```

## Usage

1. **Check tier placement**:
   ```bash
   python tier_recommender.py your_event.csv
   ```

2. **Generate improved event files**:
   ```bash
   python generate_event_files.py your_event.csv
   ```

3. **Upload to server**:
   - Upload all generated SQL files
   - Upload the updated Event Bell SQL

## Remaining Considerations

### Wave Completion Detection
The current system requires manual wave progression or a kill counter system. For automatic progression, you may need to:
- Add a kill counter to each wave generator
- Use timers between waves
- Implement a custom script to detect wave completion

### Spawn Location Tuning
The spawn offsets are set to relative positions. You may need to adjust:
- X/Y offsets based on your room layout
- Z offsets if height issues persist
- Spawn radius if monsters are too spread out

## Testing Checklist

- [ ] Verify Event Bell triggers first wave
- [ ] Check that tall monsters spawn successfully
- [ ] Verify waves progress sequentially
- [ ] Test that waves don't get stuck
- [ ] Confirm difficulty feels balanced across tiers
- [ ] Validate tier recommendations match expectations
