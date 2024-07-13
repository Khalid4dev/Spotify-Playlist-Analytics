import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import googleapiclient.discovery
import googleapiclient.errors
import pandas as pd



# Set up Spotify API credentials
SPOTIFY_CLIENT_ID = 'YOUR_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# Function to get Spotify playlist tracks
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

# Test
playlist_id = 'YOUR_PLAYLIST_ID'
tracks = get_spotify_playlist_tracks(playlist_id)
for track in tracks:
    # Create a DataFrame from the tracks list
    df = pd.DataFrame(tracks, columns=['Track Name', 'Artist Name', 'Popularity', 'Explicit', 'Track ID'])
    # Save the DataFrame to an Excel file
    df.to_excel('spotify_tracks.xlsx', index=False)
