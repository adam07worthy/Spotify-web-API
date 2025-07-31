import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import tkinter
from tkinter import ttk


# --- Connect with spotify ---

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
    scope="playlist-read-private"))


# --- Function to fetch songs and display ---
def get_playlist_songs():
    # Get the playlist URL
    playlist_url = url_entry.get()

    # Fetch the first page of songs and artists
    results = sp.playlist_items(url_entry.get())
    all_songs = results["items"]

    # Fetch the rest of the songs if there are more than 100 songs
    while results['next']:
        results = sp.next(results)
        all_songs.extend(results['items'])

    # Add songs and artists to the display area
    for item in all_songs:
        display_area.insert(tkinter.END, (item["track"]["artists"][0]["name"] + ": " + item["track"]["name"]) + "\n")


# --- GUI ---

# Create a window
window = tkinter.Tk()
window.title("Song List")
window.state('zoomed')
window.geometry("500x500")
window.configure(bg="#050214")

# Label saying "Enter playlist URL"
url_label = tkinter.Label(window,
                          text="Enter playlist URL",
                          font=("Arial", 14, "bold"),
                          fg="white",
                          bg="#050214")
url_label.pack(pady=(8, 5))

# Entry for playlist URL
url_entry = tkinter.Entry(window,
                          width=80,
                          bg="#37374C",
                          fg="white",
                          bd=0)
url_entry.pack()

# Button to enter playlist URL
url_button = tkinter.Button(window,
                            text="Enter",
                            font=("Arial", 10, "bold"),
                            command=get_playlist_songs,
                            activebackground="#2B00FF",
                            activeforeground="white",
                            bd=0)
url_button.pack(pady=(5, 8))

# Text widget displaying all songs and artists
display_area = tkinter.Text(window,
                            wrap=tkinter.WORD,
                            width=70,
                            height=25,
                            bg="#080419",
                            fg="white",
                            insertbackground="white")

# Style for scrollbar
style = ttk.Style()
style.theme_use('clam')
style.configure("Vertical.TScrollbar",
                gripcount=0,
                background="#FFFFFF",
                troughcolor="#080419",
                bordercolor="#050214",
                arrowcolor="#2B00FF")

# Scrollbar
scrollbar = ttk.Scrollbar(window,
                          orient="vertical",
                          command=display_area.yview,
                          style="Vertical.TScrollbar")
display_area.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
display_area.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)


# --- Run the GUI ---
window.mainloop()