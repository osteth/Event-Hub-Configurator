# Wave Progression System - Complete Flow

## Current Architecture

### Flow:
1. **Event Bell** (spawned by Controller) → Player rings it
2. **Event Bell** → Sends `StartEvent` signal → Deletes self
3. **Controller** → Receives `StartEvent` → Sends `Wave1` signal
4. **Wave 1 Generator** → Receives `Wave1` → Activates (sets InitGeneratedObjects to 8) → Spawns monsters
5. **Wave 1 Generator** → Needs to detect completion → Send `Wave1Complete` signal
6. **Controller** → Receives `Wave1Complete` → Sends `Wave2` signal
7. **Wave 2 Generator** → Receives `Wave2` → Activates → Spawns monsters
8. ... and so on

## What's Been Fixed

### ✅ Event Bell
- Now sends `StartEvent` signal when rung
- File: `694200294 Event Bell.sql`

### ✅ Controller
- Listens for `StartEvent` and sends `Wave1`
- Listens for `Wave1Complete`, `Wave2Complete`, etc. and sends next wave
- File: `generate_event_files.py` - `generate_controller()` function

### ✅ Wave Generators
- Start inactive (`InitGeneratedObjects = 0`)
- Listen for their specific wave signal (`Wave1`, `Wave2`, etc.)
- Activate when signal received (sets `InitGeneratedObjects = 8`)
- Use specific spawn locations (`where_Create = 4`) to avoid height issues
- File: `generate_event_files.py` - `generate_wave_generator()` function

## What Still Needs Implementation

### ⚠️ Wave Completion Detection

The wave generators need a way to detect when all monsters are dead and send a completion signal. There are several approaches:

#### Option 1: Timer-Based (Simplest)
Add a timer to each wave generator that sends completion signal after a delay:
```sql
-- After activating, wait X seconds then send completion
INSERT INTO `weenie_properties_emote` ...
VALUES (..., 9 /* Generation */, ...);

INSERT INTO `weenie_properties_emote_action` ...
VALUES (..., 88 /* LocalSignal */, 300, 1, NULL, 'Wave1Complete', ...);
```
**Pros**: Simple, reliable
**Cons**: Not based on actual completion, may trigger too early/late

#### Option 2: Kill Counter (Most Accurate)
Each monster sends a signal when killed, wave generator counts kills:
```sql
-- Wave generator listens for kill signals
-- When kill count = 10, send completion signal
```
**Pros**: Accurate, based on actual completion
**Cons**: Requires modifying monster weenies or using custom scripts

#### Option 3: Generator State Check (Complex)
Use generator's internal state to detect when all spawned objects are destroyed:
```sql
-- Check if MaxGeneratedObjects = GeneratedObjects (all spawned)
-- Check if all spawned objects are destroyed
```
**Pros**: Automatic
**Cons**: May not work reliably in ACE, requires testing

## Recommended Implementation

For now, **Option 1 (Timer-Based)** is the most practical:

1. Each wave generator activates and spawns monsters
2. After a reasonable delay (e.g., 5 minutes), send completion signal
3. Controller receives completion and triggers next wave

This can be refined later with kill counters if needed.

## Files That Need Updates

1. ✅ `generate_event_files.py` - Wave generator function (needs completion signal)
2. ✅ `generate_event_files.py` - Controller function (already handles signals)
3. ✅ `694200294 Event Bell.sql` - Already sends StartEvent

## Testing Checklist

- [ ] Event Bell spawns and can be rung
- [ ] Event Bell sends StartEvent signal
- [ ] Controller receives StartEvent and sends Wave1
- [ ] Wave 1 generator receives Wave1 and activates
- [ ] Wave 1 generator spawns monsters at correct locations
- [ ] Wave 1 generator sends Wave1Complete (when implemented)
- [ ] Controller receives Wave1Complete and sends Wave2
- [ ] Process repeats for all 10 waves + boss

## Next Steps

1. Add completion detection to wave generators (timer-based recommended)
2. Test the signal flow in-game
3. Adjust timers/delays as needed
4. Consider implementing kill counter system for more accuracy
