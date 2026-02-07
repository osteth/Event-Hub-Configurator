#!/usr/bin/env python3
"""
Tier Recommendation Tool for Event Hub
Analyzes monster difficulty and suggests appropriate tier placement
"""

import csv
import sys
from collections import defaultdict
from typing import Dict, List, Tuple, Optional


def load_mob_list(csv_file: str = 'Spawnable Mobs List.csv') -> Dict[int, Dict]:
    """Load mob list with difficulty ratings."""
    mobs = {}
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                wcid = row.get('ID', '').strip()
                if not wcid or not wcid.isdigit():
                    continue
                
                wcid = int(wcid)
                name = row.get('Name', 'Unknown').strip()
                difficulty = row.get('Difficulty', '').strip().lower()
                is_boss = row.get('Difficulty (eg: boss)', '').strip().upper() == 'TRUE'
                
                mobs[wcid] = {
                    'name': name,
                    'difficulty': difficulty,
                    'is_boss': is_boss
                }
    except FileNotFoundError:
        print(f"Warning: {csv_file} not found. Tier recommendations will be limited.")
    
    return mobs


def get_tier_score(difficulty: str, is_boss: bool) -> Tuple[int, str]:
    """
    Calculate tier score and recommended tier.
    Returns: (score, recommended_tier)
    """
    difficulty_map = {
        'low': 1,
        'mid': 2,
        'high': 3
    }
    
    base_score = difficulty_map.get(difficulty.lower(), 2)  # Default to mid
    
    # Bosses get +1 tier boost
    if is_boss:
        base_score = min(3, base_score + 1)
    
    # Map score to tier
    if base_score == 1:
        return (base_score, 'low')
    elif base_score == 2:
        return (base_score, 'mid')
    else:
        return (base_score, 'high')


def analyze_config(config_file: str, mob_list: Dict[int, Dict]) -> Dict:
    """Analyze event config and provide tier recommendations."""
    tier_analysis = defaultdict(lambda: {
        'waves': defaultdict(list),
        'issues': [],
        'recommendations': []
    })
    
    with open(config_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tier = row['tier'].lower()
            wave_num = row['wave_number']
            wcid = int(row['wcid'])
            
            tier_analysis[tier]['waves'][wave_num].append(wcid)
    
    # Analyze each tier
    for tier in ['low', 'mid', 'high']:
        if tier not in tier_analysis:
            continue
        
        analysis = tier_analysis[tier]
        all_wcids = []
        
        for wave_wcids in analysis['waves'].values():
            all_wcids.extend(wave_wcids)
        
        # Check for tier mismatches
        tier_scores = []
        for wcid in set(all_wcids):
            if wcid in mob_list:
                mob = mob_list[wcid]
                score, recommended = get_tier_score(mob['difficulty'], mob['is_boss'])
                tier_scores.append((wcid, score, recommended, mob['name']))
                
                if recommended != tier:
                    analysis['issues'].append(
                        f"WCID {wcid} ({mob['name']}) is rated '{mob['difficulty']}' "
                        f"but placed in '{tier}' tier. Recommended: '{recommended}'"
                    )
            else:
                analysis['issues'].append(
                    f"WCID {wcid} not found in mob list - cannot verify tier placement"
                )
        
        # Calculate average difficulty
        if tier_scores:
            avg_score = sum(score for _, score, _, _ in tier_scores) / len(tier_scores)
            analysis['avg_difficulty'] = avg_score
            
            # Normalize recommendations
            if tier == 'low' and avg_score > 1.5:
                analysis['recommendations'].append(
                    f"Average difficulty ({avg_score:.2f}) is high for Low tier. "
                    "Consider moving some monsters to Mid tier."
                )
            elif tier == 'mid' and (avg_score < 1.3 or avg_score > 2.5):
                analysis['recommendations'].append(
                    f"Average difficulty ({avg_score:.2f}) may be unbalanced. "
                    "Consider redistributing monsters."
                )
            elif tier == 'high' and avg_score < 2.0:
                analysis['recommendations'].append(
                    f"Average difficulty ({avg_score:.2f}) is low for High tier. "
                    "Consider moving some monsters to Mid tier."
                )
    
    return tier_analysis


def print_recommendations(config_file: str, mob_list_file: str = 'Spawnable Mobs List.csv'):
    """Print tier recommendations for a config file."""
    print(f"Analyzing {config_file}...\n")
    
    mob_list = load_mob_list(mob_list_file)
    analysis = analyze_config(config_file, mob_list)
    
    for tier in ['low', 'mid', 'high']:
        if tier not in analysis:
            continue
        
        print(f"\n{'='*60}")
        print(f"{tier.upper()} TIER ANALYSIS")
        print(f"{'='*60}")
        
        tier_data = analysis[tier]
        
        if tier_data['issues']:
            print(f"\n⚠️  ISSUES FOUND ({len(tier_data['issues'])}):")
            for issue in tier_data['issues']:
                print(f"  • {issue}")
        else:
            print("\n✅ No tier placement issues found!")
        
        if tier_data.get('avg_difficulty'):
            print(f"\n📊 Average Difficulty Score: {tier_data['avg_difficulty']:.2f}")
        
        if tier_data['recommendations']:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in tier_data['recommendations']:
                print(f"  • {rec}")
    
    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*60}\n")


def suggest_tier_for_mob(wcid: int, mob_list: Dict[int, Dict]) -> Optional[str]:
    """Suggest tier for a specific mob WCID."""
    if wcid not in mob_list:
        return None
    
    mob = mob_list[wcid]
    _, recommended = get_tier_score(mob['difficulty'], mob['is_boss'])
    return recommended


def main():
    if len(sys.argv) < 2:
        print("Usage: python tier_recommender.py <config.csv> [mob_list.csv]")
        print("\nAnalyzes event configuration and suggests tier placements.")
        sys.exit(1)
    
    config_file = sys.argv[1]
    mob_list_file = sys.argv[2] if len(sys.argv) > 2 else 'Spawnable Mobs List.csv'
    
    print_recommendations(config_file, mob_list_file)


if __name__ == '__main__':
    main()
