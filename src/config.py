import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for s2mpdpl"""
    
    # Spotify API Configuration
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8888/callback')
    
    # Music Library Configuration
    MUSIC_DIRECTORY = os.getenv('MUSIC_DIRECTORY')
    
    # MPD Configuration
    MPD_PLAYLIST_DIR = os.getenv('MPD_PLAYLIST_DIR', '~/.mpd/playlists/')
    
    # Playlist Configuration
    PLAYLIST_URL = os.getenv('PLAYLIST_URL')
    OUTPUT_PLAYLIST_NAME = os.getenv('OUTPUT_PLAYLIST_NAME', 'spotify_playlist')
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        required_vars = [
            'SPOTIFY_CLIENT_ID',
            'SPOTIFY_CLIENT_SECRET',
            'MUSIC_DIRECTORY',
            'PLAYLIST_URL'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True 