import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import Config
import sys

def fetch_spotify_playlist():
    """Fetch tracks from Spotify playlist"""
    try:
        # Validate configuration
        Config.validate()
        
        # Setup Spotify client
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=Config.SPOTIFY_CLIENT_ID,
            client_secret=Config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=Config.SPOTIFY_REDIRECT_URI,
            scope="playlist-read-private"
        ))
        
        # Extract playlist ID from URL
        playlist_url = Config.PLAYLIST_URL
        if "playlist/" not in playlist_url:
            raise ValueError("Invalid Spotify playlist URL")
        
        playlist_id = playlist_url.split("playlist/")[-1].split("?")[0]
        
        print(f"Fetching playlist: {playlist_id}")
        
        # Get playlist tracks
        results = sp.playlist_tracks(playlist_id)
        
        tracks = []
        for item in results['items']:
            track = item['track']
            if track:  # Skip null tracks
                artist = track['artists'][0]['name'] if track['artists'] else "Unknown Artist"
                title = track['name']
                tracks.append(f"{artist} - {title}")
        
        print(f"Found {len(tracks)} tracks in playlist")
        
        # Save to file
        with open("playlist.txt", "w", encoding="utf-8") as f:
            for track in tracks:
                f.write(track + "\n")
        
        print("Playlist saved to playlist.txt")
        return tracks
        
    except Exception as e:
        print(f"Error fetching playlist: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fetch_spotify_playlist()

