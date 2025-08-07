#!/usr/bin/env python3
"""
Spotify to MPD Playlist Converter
Converts Spotify playlists to MPD-compatible M3U playlists
"""

import os
import sys
import argparse
from fetch import get_playlist_tracks
from mapper import map_playlist_to_local_files
from config import Config

def main():
    parser = argparse.ArgumentParser(
        description="Convert Spotify playlist to MPD-compatible M3U playlist"
    )
    parser.add_argument(
        "playlist_url", 
        help="Spotify playlist URL to convert"
    )
    parser.add_argument(
        "--output", "-o",
        default=Config.OUTPUT_PLAYLIST_NAME,
        help="Output playlist name (default: spotify_playlist)"
    )
    parser.add_argument(
        "--music-dir", "-m",
        default=Config.MUSIC_DIRECTORY,
        help="Path to your music library directory"
    )
    
    args = parser.parse_args()
    
    # Update config with command line arguments
    Config.OUTPUT_PLAYLIST_NAME = args.output
    Config.MUSIC_DIRECTORY = args.music_dir
    
    try:
        print("🎵 Spotify to MPD Playlist Converter")
        print("=" * 40)
        
        # Step 1: Fetch Spotify playlist
        print("\n📥 Fetching Spotify playlist...")
        tracks = get_playlist_tracks(args.playlist_url)
        
        if not tracks:
            print("❌ No tracks found in playlist")
            sys.exit(1)
        
        # Step 2: Map to local files and create M3U
        print("\n🔍 Mapping tracks to local music library...")
        playlist = map_playlist_to_local_files()
        
        if playlist:
            print(f"\n✅ Successfully created M3U playlist: {args.output}.m3u")
            print(f"📁 Found {len(playlist)} matching tracks")
            
            # Optional: Copy to MPD playlist directory
            mpd_dir = os.path.expanduser(Config.MPD_PLAYLIST_DIR)
            if os.path.exists(mpd_dir):
                import shutil
                source = f"{args.output}.m3u"
                destination = os.path.join(mpd_dir, f"{args.output}.m3u")
                shutil.copy2(source, destination)
                print(f"📋 Copied to MPD playlist directory: {destination}")
            else:
                print(f"ℹ️  MPD playlist directory not found: {mpd_dir}")
                print("   You can manually copy the .m3u file to your MPD playlist directory")
        else:
            print("❌ No tracks could be mapped to local files")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
