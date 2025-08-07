import os
import re
from fuzzywuzzy import fuzz
from config import Config
import sys

def normalize_string(s):
    """Normalize string for better matching"""
    # Remove special characters and convert to lowercase
    s = re.sub(r'[^\w\s]', '', s.lower())
    # Remove extra whitespace
    s = ' '.join(s.split())
    return s

def find_music_file(track_name, music_dir):
    """Find a music file that matches the track name"""
    track_normalized = normalize_string(track_name)
    best_match = None
    best_score = 0
    
    # Supported audio file extensions
    audio_extensions = {'.mp3', '.flac', '.m4a', '.ogg', '.wav', '.aac'}
    
    for root, _, files in os.walk(music_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in audio_extensions):
                file_path = os.path.join(root, file)
                file_name = os.path.splitext(file)[0]  # Remove extension
                file_normalized = normalize_string(file_name)
                
                # Calculate similarity score
                score = fuzz.ratio(track_normalized, file_normalized)
                
                if score > best_score and score > 70:  # Minimum 70% similarity
                    best_score = score
                    best_match = file_path
    
    return best_match, best_score

def get_mpd_path(file_path, music_dir):
    """Convert absolute file path to MPD-compatible path"""
    # Get relative path from music directory
    try:
        relative_path = os.path.relpath(file_path, music_dir)
        # Convert to forward slashes for MPD (works on all platforms)
        mpd_path = relative_path.replace(os.sep, '/')
        return mpd_path
    except ValueError:
        # If file is not in music directory, return absolute path
        return file_path.replace(os.sep, '/')

def map_playlist_to_local_files():
    """Map Spotify playlist tracks to local music files"""
    try:
        # Validate configuration
        Config.validate()
        
        music_dir = os.path.expanduser(Config.MUSIC_DIRECTORY)
        if not os.path.exists(music_dir):
            raise ValueError(f"Music directory does not exist: {music_dir}")
        
        playlist = []
        matched_tracks = 0
        total_tracks = 0
        
        print(f"Searching for tracks in: {music_dir}")
        
        with open("playlist.txt", "r", encoding="utf-8") as f:
            tracks = [line.strip() for line in f if line.strip()]
        
        total_tracks = len(tracks)
        
        for track in tracks:
            file_path, score = find_music_file(track, music_dir)
            if file_path:
                # Convert to MPD-compatible path
                mpd_path = get_mpd_path(file_path, music_dir)
                playlist.append(mpd_path)
                matched_tracks += 1
                print(f"✓ Matched: {track} -> {os.path.basename(file_path)} ({score}%)")
                print(f"  Path: {mpd_path}")
            else:
                print(f"✗ No match found: {track}")
        
        # Save MPD playlist
        output_file = f"{Config.OUTPUT_PLAYLIST_NAME}.m3u"
        with open(output_file, "w", encoding="utf-8") as f:
            for path in playlist:
                f.write(path + "\n")
        
        print(f"\nSummary:")
        print(f"Total tracks: {total_tracks}")
        print(f"Matched tracks: {matched_tracks}")
        print(f"Match rate: {(matched_tracks/total_tracks)*100:.1f}%")
        print(f"Playlist saved to: {output_file}")
        
        return playlist
        
    except Exception as e:
        print(f"Error mapping playlist: {e}")
        sys.exit(1)

if __name__ == "__main__":
    map_playlist_to_local_files()

