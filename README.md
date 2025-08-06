# s2mpdpl

Spotify to MPD Playlist Converter

This project converts Spotify playlists into MPD-compatible playlists (.m3u).

## Features

- Export any private or public Spotify playlist
- Automatic search & match with your local music library using fuzzy matching
- Outputs an MPD-compatible .m3u playlist
- Configuration management with environment variables
- Detailed progress reporting and match statistics
- Support for multiple audio formats (MP3, FLAC, M4A, OGG, WAV, AAC)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AymanLar/s2mpdpl
   cd s2mpdpl
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Spotify API credentials:**
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Create a new application
   - Copy your Client ID and Client Secret

4. **Configure the application:**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` with your settings:
   ```env
   # Spotify API Credentials
   SPOTIFY_CLIENT_ID=your_spotify_client_id_here
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   
   # Music Library Configuration
   MUSIC_DIRECTORY=/path/to/your/music/library
   
   # MPD Configuration
   MPD_PLAYLIST_DIR=~/.mpd/playlists/
   
   # Playlist Configuration
   PLAYLIST_URL=https://open.spotify.com/playlist/your_playlist_id_here
   OUTPUT_PLAYLIST_NAME=spotify_playlist
   ```

## Usage

### Quick Start

Run the complete conversion process:

```bash
cd src
python main.py
```

This will:
1. Fetch your Spotify playlist
2. Match tracks to your local music library
3. Generate an MPD-compatible .m3u playlist

### Step-by-Step Process

You can also run each step individually:

1. **Fetch Spotify playlist:**
   ```bash
   cd src
   python fetch_pl.py
   ```

2. **Map to local files:**
   ```bash
   python mapper.py
   ```

3. **Load into MPD:**
   ```bash
   bash loader.sh
   ```

### MPD Integration

After running the conversion:

1. The playlist will be saved as `spotify_playlist.m3u` (or your custom name)
2. Use the loader script to automatically copy it to your MPD playlist directory
3. Load and play in MPD:
   ```bash
   mpc load spotify_playlist
   mpc play
   ```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SPOTIFY_CLIENT_ID` | Your Spotify API Client ID | Yes |
| `SPOTIFY_CLIENT_SECRET` | Your Spotify API Client Secret | Yes |
| `MUSIC_DIRECTORY` | Path to your local music library | Yes |
| `PLAYLIST_URL` | Spotify playlist URL to convert | Yes |
| `OUTPUT_PLAYLIST_NAME` | Name for the output playlist | No |
| `MPD_PLAYLIST_DIR` | MPD playlist directory | No |

### Supported Audio Formats

The converter supports these audio formats:
- MP3
- FLAC
- M4A
- OGG
- WAV
- AAC

## How It Works

1. **Playlist Fetching**: Uses Spotify API to retrieve track information from your playlist
2. **Track Matching**: Uses fuzzy string matching to find corresponding files in your local music library
3. **Playlist Generation**: Creates an MPD-compatible .m3u playlist with absolute file paths
4. **MPD Integration**: Provides scripts to load the playlist directly into MPD

## Troubleshooting

### Common Issues

1. **"Missing required environment variables"**
   - Make sure you've created a `.env` file with all required variables
   - Check that your Spotify API credentials are correct

2. **"Music directory does not exist"**
   - Verify the `MUSIC_DIRECTORY` path in your `.env` file
   - Use absolute paths for best results

3. **Low match rate**
   - The fuzzy matching requires at least 70% similarity
   - Ensure your local files have similar naming to Spotify track names
   - Check that your music files are in supported formats

4. **MPD connection issues**
   - Make sure MPD is running: `mpc status`
   - Verify your MPD playlist directory path

### Debug Mode

For more detailed output, you can run individual scripts:

```bash
python fetch_pl.py  # See Spotify API responses
python mapper.py    # See detailed matching process
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
