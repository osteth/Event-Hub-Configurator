// Custom script for wave generators to detect when all monsters are killed
// Place this in your ACE server's Scripts folder (e.g., Scripts/WorldObjects/)
// Usage: Set p_Script = 'wave_completion_script' in the heartbeat emote action
// The script will check if all spawned monsters are dead and send completion signal

using System;
using ACE.Entity;
using ACE.Server.WorldObjects;
using ACE.Server.Managers;

namespace ACE.Server.Entity
{
    public static class WaveCompletionScript
    {
        public static bool Execute(WorldObject source, WorldObject target)
        {
            if (source == null || !(source is Generator generator))
                return false;

            // Check if all spawned objects are destroyed
            // CurrentCreate tracks how many objects are currently spawned
            // InitCreate is the initial spawn count (8 in our case)
            if (generator.CurrentCreate == 0 && generator.InitCreate > 0)
            {
                // Extract wave signal from generator name (e.g., "Low Event Wave 1 Gen" -> "Wave1")
                var name = generator.Name ?? "";
                string waveSignal = "Wave1"; // Default
                
                if (name.Contains("Wave 1")) waveSignal = "Wave1";
                else if (name.Contains("Wave 2")) waveSignal = "Wave2";
                else if (name.Contains("Wave 3")) waveSignal = "Wave3";
                else if (name.Contains("Wave 4")) waveSignal = "Wave4";
                else if (name.Contains("Wave 5")) waveSignal = "Wave5";
                else if (name.Contains("Wave 6")) waveSignal = "Wave6";
                else if (name.Contains("Wave 7")) waveSignal = "Wave7";
                else if (name.Contains("Wave 8")) waveSignal = "Wave8";
                else if (name.Contains("Wave 9")) waveSignal = "Wave9";
                else if (name.Contains("Wave 10")) waveSignal = "Wave10";
                else if (name.Contains("Boss")) waveSignal = "Wave11";
                
                // All monsters are dead, send completion signal
                generator.EmitSound(ACE.Common.Sound.SoundType.LocalSignal, waveSignal + "Complete");
                return true;
            }

            return false;
        }
    }
}
