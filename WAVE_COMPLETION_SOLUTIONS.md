# Wave Completion Solutions

## Problem
Waves need to progress when all monsters are killed, but we don't want to modify every monster weenie.

## Solution: Generator State Monitoring

The generator tracks how many objects are currently spawned via `CurrentCreate`. When all monsters are killed, `CurrentCreate` becomes 0.

### Option 1: Custom Script (Recommended) ✅

**File**: `wave_completion_script.cs`

**How it works**:
- Heartbeat emote fires every few seconds
- Script checks if `generator.CurrentCreate == 0`
- If true, sends completion signal
- No monster modifications needed

**Setup**:
1. Copy `wave_completion_script.cs` to your ACE server's `Scripts/WorldObjects/` folder
2. Regenerate event files - they'll include the script reference
3. Restart server to load the script

**Advantages**:
- ✅ No monster modifications
- ✅ Automatic detection
- ✅ Reliable
- ✅ Works with any monster

### Option 2: Pure SQL (Alternative)

If you can't use scripts, you could:
- Use a timer-based approach (less accurate)
- Or manually trigger waves (not automatic)

**Note**: Pure SQL detection of generator state is limited in ACE. The script approach is recommended.

## Current Implementation

The generator now includes:
- Heartbeat emote that fires periodically
- Script reference to check completion
- Automatic signal sending when all monsters are dead

## Testing

1. Start event
2. Kill all monsters in Wave 1
3. Wave 2 should start automatically within a few seconds
4. Repeat for all waves
