# Pure SQL Solution (No Custom Scripts Required)

## Solution: Timer-Based Wave Completion

Since we can't check generator state (`CurrentCreate`) in pure SQL emotes, we use a timer-based approach:

1. **Wave activates** when signal received
2. **Monsters spawn** immediately
3. **Timer starts** (3 minutes default)
4. **Completion signal** sent after timer expires
5. **Next wave** starts automatically

## How It Works

- **Generation Emote**: Fires when wave generator activates and spawns monsters
- **Timer Delay**: 180 seconds (3 minutes) after activation
- **Completion Signal**: Sent automatically after delay
- **No Scripts Required**: Pure SQL solution

## Configuration

The timer delay is set in `generate_event_files.py`:
- Default: 180 seconds (3 minutes)
- Adjustable per wave if needed

### Adjusting the Timer

Edit `generate_event_files.py` line ~118:
```python
VALUES (@parent_id,  0,  88 /* LocalSignal */, 180, 1, NULL, '{wave_signal}Complete', ...
```

Change `180` to your desired delay in seconds:
- **60** = 1 minute (faster, but may trigger before all monsters are killed)
- **180** = 3 minutes (default, reasonable for most waves)
- **300** = 5 minutes (slower, ensures all monsters are dead)

## Advantages

- ✅ **No custom scripts** - Pure SQL solution
- ✅ **Works on any server** - No special permissions needed
- ✅ **Simple and reliable** - Timer always fires
- ✅ **Easy to adjust** - Change delay in generator script

## Limitations

- ⚠️ **Not kill-based** - Timer-based, not triggered by actual kills
- ⚠️ **May trigger early** - If players kill monsters quickly
- ⚠️ **May trigger late** - If players take longer than timer

## Recommendations

1. **Set timer** to average expected clear time + buffer
2. **Test** with your typical group size
3. **Adjust** delay based on actual clear times
4. **Consider** different delays for different waves (boss waves might need longer)

## Alternative: Manual Wave Progression

If timer-based doesn't work well, you could:
- Have an admin manually trigger next wave via command
- Use a lever/switch that players can activate when wave is cleared
- Use a kill counter on a specific "wave completion" object

But the timer approach is the simplest pure SQL solution.
