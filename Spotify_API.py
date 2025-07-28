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

# Get the songs and artists from given playlist
playlist_id = input("Enter playlist ID: ")
songs = sp.playlist_items(playlist_id)["items"]
for item in songs:
    print(item["track"]["artists"][0]["name"] + ": " + item["track"]["name"])