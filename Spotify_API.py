import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load the hidden variables from .env
load_dotenv()

# Get the hidden variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# Create a Spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-read-private"
))

# Get the songs and artists from a given playlist
playlist_id = input("Enter playlist ID: ")
results = sp.playlist_items(playlist_id)
 
# Allows for playlists larger than 100 songs
while results['next']:
    results = sp.next(results)
    results['items'].extend(results['items'])

for item in results["items"]:
    print(item["track"]["artists"][0]["name"] + ": " + item["track"]["name"])