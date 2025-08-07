import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Spotify API Configuration
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    # Music Library Configuration
    MUSIC_DIRECTORY = os.getenv('MUSIC_DIRECTORY', '~/Music')
    
    # Playlist Configuration
    OUTPUT_PLAYLIST_NAME = os.getenv('OUTPUT_PLAYLIST_NAME', 'spotify_playlist')
    
    # MPD Configuration
    MPD_PLAYLIST_DIR = os.getenv('MPD_PLAYLIST_DIR', '~/.mpd/playlists/')
    
    @classmethod
    def validate(cls):
        """Validate that all required configuration is present"""
        required_vars = [
            ('SPOTIFY_CLIENT_ID', cls.SPOTIFY_CLIENT_ID),
            ('SPOTIFY_CLIENT_SECRET', cls.SPOTIFY_CLIENT_SECRET),
            ('MUSIC_DIRECTORY', cls.MUSIC_DIRECTORY),
        ]
        
        missing_vars = []
        for var_name, var_value in required_vars:
            if not var_value:
                missing_vars.append(var_name)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
