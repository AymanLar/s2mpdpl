# s2mpdpl

Convert Spotify playlists (not limited to it, you can use it for albums ...)  to MPD-compatible M3U playlists.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   ```bash
   cp env.example .env
   ```
   Edit `.env` with your Spotify API credentials and music directory.

3. **Convert a playlist:**
   ```bash
   python convert.py "https://open.spotify.com/playlist/your_playlist_id"
   ```

## Usage

```bash
# Basic usage
python convert.py "playlist_url"

# Custom options
python convert.py "playlist_url" --output "my_playlist" --music-dir "/path/to/music"

# Load in MPD
mpc load spotify_playlist
mpc play
```

## Configuration

Required environment variables in `.env`:
- `SPOTIFY_CLIENT_ID` - Your Spotify API Client ID
- `SPOTIFY_CLIENT_SECRET` - Your Spotify API Client Secret  
- `MUSIC_DIRECTORY` - Path to your music library

## How it works

1. Fetches track info from Spotify API
2. Matches tracks to local files using fuzzy matching
3. Generates M3U playlist with absolute paths
4. Optionally copies to MPD playlist directory

## Supported formats
``MP3, FLAC, M4A, OGG, WAV, AAC``