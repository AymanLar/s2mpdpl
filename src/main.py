#!/usr/bin/env python3
"""
s2mpdpl - Spotify to MPD Playlist Converter
Main script that orchestrates the entire conversion process
"""

import os
import sys
from fetch_pl import fetch_spotify_playlist
from mapper import map_playlist_to_local_files
from config import Config

def main():
    """Main function to run the complete conversion process"""
    print("🎵 s2mpdpl - Spotify to MPD Playlist Converter")
    print("=" * 50)
    
    try:
        # Step 1: Fetch playlist from Spotify
        print("\n📥 Step 1: Fetching playlist from Spotify...")
        tracks = fetch_spotify_playlist()
        
        if not tracks:
            print("❌ No tracks found in playlist")
            sys.exit(1)
        
        # Step 2: Map tracks to local files
        print("\n🔍 Step 2: Mapping tracks to local music files...")
        playlist = map_playlist_to_local_files()
        
        if not playlist:
            print("❌ No tracks could be matched to local files")
            sys.exit(1)
        
        # Step 3: Generate final output
        print("\n✅ Conversion complete!")
        print(f"Generated playlist: {Config.OUTPUT_PLAYLIST_NAME}.m3u")
        print(f"Tracks in playlist: {len(playlist)}")
        
        # Step 4: Instructions for MPD
        print("\n📋 To load in MPD:")
        print(f"1. Copy {Config.OUTPUT_PLAYLIST_NAME}.m3u to your MPD playlist directory")
        print("2. Run: mpc update")
        print(f"3. Run: mpc load {Config.OUTPUT_PLAYLIST_NAME}")
        
    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 