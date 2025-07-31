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



# Create a window
window = tkinter.Tk()
window.title("Song List")
window.geometry("500x500")

# Get the songs and artists from a given playlist
def get_playlist_songs():
    # Get the playlist URL
    playlist_url = url_entry.get()
    # Get the playlist songs and artists
    results = sp.playlist_items(url_entry.get())
    all_songs = results["items"]
    # Allows for playlists larger than 100 songs
    while results['next']:
        results = sp.next(results)
        all_songs.extend(results['items'])
    # Add songs and artists to window
    for item in all_songs:
        display_area.insert(tkinter.END, (item["track"]["artists"][0]["name"] + ": " + item["track"]["name"]) + "\n")

# Get the playlist URL
url_label = tkinter.Label(window, text="Enter playlist URL")
url_label.pack()
url_entry = tkinter.Entry(window, width=50)
url_entry.pack()
url_button = tkinter.Button(window, text="enter", command=get_playlist_songs)
url_button.pack()


# Add scrollable text
display_area = scrolledtext.ScrolledText(window, wrap=tkinter.WORD, width=70, height=25)
display_area.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

window.mainloop()