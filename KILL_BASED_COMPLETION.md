# Kill-Based Wave Completion (No Monster Modifications Required)

## Solution Overview

This solution uses the generator's built-in tracking of spawned objects. When all monsters are killed, the generator's `CurrentCreate` property reaches 0. We use a heartbeat emote to periodically check this and send a completion signal.

## How It Works

1. **Wave Generator** spawns monsters when activated
2. **Heartbeat Emote** fires every few seconds
3. **Custom Script** checks if `CurrentCreate == 0` (all monsters dead)
4. **Completion Signal** is sent when all are killed
5. **Controller** receives signal and triggers next wave

## Implementation

### Option 1: Custom Script (Recommended)

Use a custom C# script that monitors the generator's `CurrentCreate` property:

**File**: `wave_completion_script.cs` (provided)
**Usage**: Set `p_Script = 'wave_completion_script'` in the heartbeat emote action

The script checks if `generator.CurrentCreate == 0` and sends the completion signal.

### Option 2: Pure SQL with Heartbeat

If you prefer pure SQL without scripts, you can use a heartbeat that fires periodically. However, this requires the generator to track its own state, which may not be directly accessible in SQL emotes.

**Note**: Pure SQL solution may be limited. The custom script approach is more reliable.

## Setup Instructions

1. **Add the script** to your ACE server's Scripts folder
2. **Regenerate event files** using the updated `generate_event_files.py`
3. **Test** that waves progress when monsters are killed

## Advantages

- ✅ No monster modifications required
- ✅ Uses generator's built-in tracking
- ✅ Automatic detection when all monsters are dead
- ✅ Works with any monster type

## Testing

1. Start an event
2. Kill all monsters in Wave 1
3. Verify Wave 2 starts automatically
4. Repeat for all waves
