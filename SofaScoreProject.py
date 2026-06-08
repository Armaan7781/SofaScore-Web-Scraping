import os
import time
import pandas as pd
import ScraperFC as sfc

def run_pipeline():
    print("=" * 60)
    print(" 🚀 WELCOME TO THE HISTORICAL FOOTBALL DATA EXTRACTION PIPELINE 🚀")
    print("=" * 60)
    print("Note: Ensure league names match Sofascore formatting (e.g., 'Spain La Liga', 'England Premier League').\n")

    # 1. Interactive User Inputs
    leagues_input = input("⚽ Enter league(s) separated by commas: ")
    seasons_input = input("📅 Enter season(s) separated by commas (e.g., 23/24, 24/25): ")
    
    # Clean and parse inputs into lists
    leagues_to_pull = [l.strip() for l in leagues_input.split(",") if l.strip()]
    seasons_to_pull = [s.strip() for s in seasons_input.split(",") if s.strip()]

    if not leagues_to_pull or not seasons_to_pull:
        print("❌ Error: You must enter at least one league and one season to proceed.")
        return

    # Initialize Sofascore module
    try:
        sofascore = sfc.Sofascore()
    except Exception as e:
        print(f"❌ Failed to initialize ScraperFC: {e}")
        return

    all_data_frames = []

    print(f"\n🛫 Initializing pipeline for {len(leagues_to_pull)} league(s) across {len(seasons_to_pull)} season(s)...\n")

    # 2. Nested Loops for Multi-League & Multi-Season Processing
    for league in leagues_to_pull:
        print(f"🏆 Processing League: {league}")
        print("-" * 40)
        
        for season in seasons_to_pull:
            print(f"  📥 Pulling player stats for {season}...")
            
            try:
                # Scrape the seasonal totals
                df = sofascore.scrape_player_league_stats(
                    year=season, 
                    league=league, 
                    accumulation="total"
                )
                
                if df is None or df.empty:
                    print(f"  ⚠️ No data returned for {league} in {season}.")
                    continue
                
                # Clean duplicate columns out immediately to prevent reindexing crashes
                df = df.loc[:, ~df.columns.duplicated()]
                
                # CRITICAL: Track metadata so rows don't get mixed up after merging
                df["league_name"] = league
                df["season_year"] = season
                
                # Append to master accumulator list
                all_data_frames.append(df)
                print(f"  ✅ Successfully processed {len(df)} records.")
                
            except Exception as e:
                print(f"  ⚠️ Error pulling {league} for {season}: {e}")
                
            # Polite pause between requests to respect the API/Server
            time.sleep(3)
        print() # Newline for readability between leagues

    # 3. Master Consolidation and Export
    if all_data_frames:
        print("=" * 60)
        print("Merging all data into a single master historical database...")
        master_historical_df = pd.concat(all_data_frames, ignore_index=True)
        
        # Build a dynamic file name or ask user for save directory
        output_dir = "D:/Football Analytics/"
        if not os.path.exists(output_dir):
            print(f"📁 Target directory '{output_dir}' not found. Saving to current working directory instead.")
            output_dir = "./"
            
        output_file = os.path.join(output_dir, "Custom_Football_Historical_Data.csv")
        
        # Save using 'utf-8-sig' so Excel and Power BI parse foreign names perfectly
        master_historical_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print("\n🎉 --- PIPELINE EXECUTION SUCCESS --- 🎉")
        print(f"Master file saved directly to: {output_file}")
        print(f"Total dataset volume: {len(master_historical_df)} total player-season entries.")
        print("=" * 60)
    else:
        print("❌ Pipeline finished, but no data could be collected.")

if __name__ == "__main__":
    run_pipeline()