# Testing Instructions for Event Hub Improvements

## Step 1: Add the Custom Script

1. Copy `wave_completion_script.cs` to your ACE server's Scripts folder
   - Location: `[Your ACE Server]/Scripts/WorldObjects/wave_completion_script.cs`
   - Or wherever your server loads scripts from

2. **Restart your ACE server** to load the new script

## Step 2: Regenerate Event Files

1. **Backup your current event files** (just in case)

2. Run the generator with your event config:
   ```bash
   python generate_event_files.py your_event_config.csv
   ```

   This will regenerate:
   - All wave generator files (10 waves + boss per tier)
   - All controller files (Low, Mid, High)
   - With the new improvements:
     - Height-aware spawning
     - Signal-based wave progression
     - Kill detection system

## Step 3: Upload SQL Files to Server

Upload all regenerated SQL files to your server:

### Low Tier:
- `Low Event Sequence/694200293 Low Event Controller.sql`
- `Low Event Sequence/694200310 Low Event Wave 1.sql`
- `Low Event Sequence/694200311 Low Event Wave 2.sql`
- ... (all 10 waves)
- `Low Event Sequence/694200320 Low Event Boss.sql`

### Mid Tier:
- `Mid Event Sequence/694200300 Mid Event Controller.sql`
- `Mid Event Sequence/694200321 Mid Event Wave 1.sql`
- ... (all 10 waves)
- `Mid Event Sequence/694200331 Mid Event Boss.sql`

### High Tier:
- `High Event Sequence/694200304 High Event Controller.sql`
- `High Event Sequence/694200332 High Event Wave 1.sql`
- ... (all 10 waves)
- `High Event Sequence/694200342 High Event Boss.sql`

### Event Bell:
- `694200294 Event Bell.sql` (updated to send StartEvent signal)

## Step 4: Test in Game

1. **Start the event** by ringing the Event Bell
   - Should send `StartEvent` signal
   - Controller should receive it and send `Wave1` signal
   - Wave 1 should activate and spawn monsters

2. **Check spawn locations**
   - Monsters should spawn at specific locations (not random)
   - Tall monsters should spawn successfully (no height failures)

3. **Kill all Wave 1 monsters**
   - Wait a few seconds (heartbeat checks every 5 seconds)
   - Wave 2 should automatically start
   - Verify the completion signal was sent

4. **Continue through all waves**
   - Each wave should progress automatically when all monsters are killed
   - Boss wave should trigger after Wave 10

## Troubleshooting

### Waves don't progress:
- Check server logs for script errors
- Verify `wave_completion_script.cs` is in the correct location
- Check that server was restarted after adding script
- Verify heartbeat emote is working (check generator properties)

### Monsters don't spawn:
- Check that wave generators are receiving their activation signals
- Verify `InitGeneratedObjects` is being set to 8 when signal received
- Check spawn locations aren't blocked

### Tall monsters still fail:
- Adjust spawn offsets in `generate_event_files.py` (spawn_offsets array)
- Increase Z coordinates if needed
- Check room height at spawn locations

### Script not found errors:
- Verify script file is in correct location
- Check script name matches: `wave_completion_script`
- Ensure server has script loading enabled

## Quick Test Checklist

- [ ] Script added to server and server restarted
- [ ] Event files regenerated
- [ ] All SQL files uploaded to server
- [ ] Event Bell updated
- [ ] Event starts when bell is rung
- [ ] Wave 1 spawns correctly
- [ ] All Wave 1 monsters can be killed
- [ ] Wave 2 starts automatically after Wave 1 is cleared
- [ ] All waves progress sequentially
- [ ] Boss wave triggers after Wave 10

## Rollback Plan

If something goes wrong:
1. Restore your backed-up event files
2. Remove the custom script
3. Re-upload the old files

The old system should still work (just without the improvements).
