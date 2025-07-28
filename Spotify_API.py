import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import tkinter
from tkinter import scrolledtext

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
playlist_url = input("Enter playlist URL: ")
results = sp.playlist_items(playlist_url)
all_songs = results["items"]
 
# Allows for playlists larger than 100 songs
while results['next']:
    results = sp.next(results)
    all_songs.extend(results['items'])

# Create a window
window = tkinter.Tk()
window.title("Song List")
window.geometry("500x500")

# Add scrollable text
display_area = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=70, height=25)
display_area.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

# Add songs and artists to window
for item in all_songs:
    display_area.insert(tkinter.END, (item["track"]["artists"][0]["name"] + ": " + item["track"]["name"]) + "\n")

window.mainloop()