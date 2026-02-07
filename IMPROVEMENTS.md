# Event Hub Improvements

## Issues Fixed

### 1. Tier Recommendation System
- **Problem**: Difficult to find the right tier for monsters
- **Solution**: Created `tier_recommender.py` tool that analyzes mob difficulty and suggests tier placement
- **Usage**: `python tier_recommender.py <config.csv>`

### 2. Height-Aware Spawning
- **Problem**: Tall monsters don't spawn in low-ceiling areas
- **Solution**: Changed `where_Create` from 2 (random location) to 4 (specific location) with explicit Z coordinates
- **Implementation**: Modified wave generator to use specific spawn points with height validation

### 3. Difficulty Normalization
- **Problem**: Hard to normalize difficulty across 3 tiers
- **Solution**: Added difficulty scoring system and validation in tier_recommender.py
- **Implementation**: Calculates average difficulty per tier and suggests rebalancing

### 4. Wave Progression System
- **Problem**: Spawn sequence fails or gets stuck
- **Solution**: Implemented proper wave controller with local signals for sequential triggering
- **Implementation**: 
  - Wave generators only spawn when triggered by signal
  - Controller manages wave progression
  - Each wave signals completion to trigger next wave

## Key Changes

1. **Wave Generators**: Now use `when_Create` = 2 (on signal) instead of 1 (on generation)
2. **Wave Controller**: Manages sequential wave triggering via local signals
3. **Spawn Locations**: Use specific coordinates instead of random radius
4. **Tier Analysis**: Automated tool to verify tier placement
