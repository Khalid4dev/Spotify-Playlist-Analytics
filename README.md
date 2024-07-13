# Spotify Playlist to Excel Script

This Python script retrieves track details from a specified Spotify playlist and saves the information to an Excel file.

## Prerequisites

1. Python 3.6+
2. Required libraries:
   - `spotipy`
   - `pandas`
   - `openpyxl` (for saving to Excel)

## Setup

### Step 1: Create a Virtual Environment

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create the project.
3. Create a virtual environment:

```sh
python -m venv spotify_env
```

4. Activate the virtual environment:

   - **Windows:**
     ```sh
     spotify_env\Scripts\activate
     ```
   - **macOS/Linux:**
     ```sh
     source spotify_env/bin/activate
     ```

### Step 2: Install Required Libraries

With the virtual environment activated, install the necessary libraries using pip:

```sh
pip install spotipy pandas openpyxl
```

## Getting Started

1. **Spotify API Credentials:**
   - Register your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Obtain your `Client ID` and `Client Secret`.

2. **Set Up the Script:**
   - Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` in the script with your Spotify API credentials.
   - Replace `YOUR_PLAYLIST_ID` with the ID of the Spotify playlist you want to retrieve tracks from.

## Script Overview

### Import Libraries

```python
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
```

### Spotify API Setup

Set up Spotify API credentials using the `SpotifyClientCredentials` class from `spotipy`.

```python
SPOTIFY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))
```

### Retrieve Spotify Playlist Tracks

Define a function to retrieve track details from the specified Spotify playlist.

```python
def get_spotify_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    track_details = []
    for track in tracks:
        track_info = track['track']
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']
        popularity = track_info['popularity']
        explicit = track_info['explicit']
        track_id = track_info['id']
        
        track_details.append((track_name, artist_name, popularity, explicit, track_id))
    
    return track_details
```

### Save to Excel

Retrieve the tracks and save the details to an Excel file.

```python
# Test
playlist_id = 'YOUR_PLAYLIST_ID'
tracks = get_spotify_playlist_tracks(playlist_id)

# Create a DataFrame from the tracks list
df = pd.DataFrame(tracks, columns=['Track Name', 'Artist Name', 'Popularity', 'Explicit', 'Track ID'])

# Save the DataFrame to an Excel file
df.to_excel('spotify_tracks.xlsx', index=False)
```

## Usage

1. Replace `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_PLAYLIST_ID` with your actual Spotify credentials and playlist ID in the script.
2. Run the script to generate an Excel file (`spotify_tracks.xlsx`) containing the track details from the specified Spotify playlist.

## Deactivate the Virtual Environment

Once you are done, you can deactivate the virtual environment using:

```sh
deactivate
```
