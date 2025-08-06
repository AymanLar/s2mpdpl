#!/bin/bash

# s2mpdpl - MPD Playlist Loader
# This script loads the generated playlist into MPD

# Load environment variables
if [ -f "../.env" ]; then
    export $(cat ../.env | grep -v '^#' | xargs)
fi

# Default playlist name
PLAYLIST_NAME=${OUTPUT_PLAYLIST_NAME:-spotify_playlist}

echo "🎵 Loading playlist into MPD..."

# Check if playlist file exists
if [ ! -f "${PLAYLIST_NAME}.m3u" ]; then
    echo "❌ Error: ${PLAYLIST_NAME}.m3u not found"
    echo "Make sure you've run the conversion script first"
    exit 1
fi

# Copy playlist to MPD directory
MPD_DIR=${MPD_PLAYLIST_DIR:-~/.mpd/playlists/}
MPD_DIR=$(eval echo $MPD_DIR)

echo "📁 Copying playlist to MPD directory: $MPD_DIR"

# Create MPD directory if it doesn't exist
mkdir -p "$MPD_DIR"

# Copy the playlist
cp "${PLAYLIST_NAME}.m3u" "$MPD_DIR/"

if [ $? -eq 0 ]; then
    echo "✅ Playlist copied successfully"
else
    echo "❌ Failed to copy playlist"
    exit 1
fi

# Update MPD database
echo "🔄 Updating MPD database..."
mpc update

if [ $? -eq 0 ]; then
    echo "✅ MPD database updated"
else
    echo "❌ Failed to update MPD database"
    exit 1
fi

# Load the playlist
echo "📋 Loading playlist: $PLAYLIST_NAME"
mpc load "$PLAYLIST_NAME"

if [ $? -eq 0 ]; then
    echo "✅ Playlist loaded successfully!"
    echo ""
    echo "🎵 You can now play the playlist with:"
    echo "   mpc play"
    echo "   mpc next"
    echo "   mpc prev"
    echo "   mpc status"
else
    echo "❌ Failed to load playlist"
    exit 1
fi

