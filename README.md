# Spotify Web API

## Description
A Python script that uses the Spotify Web API to retrieve every song and the artist from a given Spotify playlist.

## Setup

1. Create or log into your [Spotify Developer account](https://developer.spotify.com/dashboard).
2. Create a `.env` file in the root of the project directory.
3. Add the following variables to the `.env` file using your Spotify Developer credentials:

   ```env
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback

5. Install Python packages:

        pip install spotipy python-dotenv


## Example Output
When the program is run it will print song and the artist who made it, for example:

    Stevie Wonder: I Wish  
    The Cure: A Forest  
    The Beatles: Norwegian Wood (This Bird Has Flown) - Remastered 2009  
    Radiohead: Talk Show Host  
    Led Zeppelin: Dazed and Confused - Remaster  
