import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from config import Config

def get_playlist_tracks(playlist_url):
    """Fetch tracks from Spotify playlist and save to file"""
    # Validate configuration
    Config.validate()
    
    # Authenticate using Client Credentials Flow
    auth_manager = SpotifyClientCredentials(
        client_id=Config.SPOTIFY_CLIENT_ID, 
        client_secret=Config.SPOTIFY_CLIENT_SECRET
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Extract playlist ID from URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    try:
        results = sp.playlist_tracks(playlist_id)
        tracks = results['items']

        # Pagination: continue if there are more tracks
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        print(f"\nTotal Tracks: {len(tracks)}\n")
        
        # Save tracks to file for mapping
        with open("playlist.txt", "w", encoding="utf-8") as f:
            for i, item in enumerate(tracks):
                track = item['track']
                name = track['name']
                artists = ', '.join([artist['name'] for artist in track['artists']])
                track_info = f"{name} — {artists}"
                print(f"{i+1}. {track_info}")
                f.write(f"{track_info}\n")
        
        print(f"\nPlaylist saved to playlist.txt")
        return tracks
        
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch.py <playlist_url>")
        sys.exit(1)

    playlist_url = sys.argv[1]
    get_playlist_tracks(playlist_url)
