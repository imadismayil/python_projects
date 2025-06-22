import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# Load environment variables
load_dotenv()

# Get credentials from .env
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Get date input
year = input("Which year would you like to travel to (YYYY-MM-DD format)? ")

# Scrape Billboard for songs
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/", headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
song_elements = soup.select("li ul li h3")
song_names_list = [song.getText().strip() for song in song_elements]
print(f"\n🎵 Found {len(song_names_list)} songs from Billboard for {year}.")

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
print(f"🔐 Authenticated as Spotify user: {user_id}")

# Search each song on Spotify
track_uris = []
not_found = []

for song in song_names_list:
    query = f"track:{song} year:{year[:4]}"
    result = sp.search(q=query, type="track", limit=1)

    try:
        uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    except IndexError:
        print(f"❌ Not found on Spotify: {song}")
        not_found.append(song)

# Create playlist
playlist_name = f"{year} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

print(f"\n✅ Created Playlist: {playlist_name}")
print(f"🎧 Spotify Playlist Link: {playlist['external_urls']['spotify']}")
print(f"✔️ {len(track_uris)} songs added.")
print(f"❌ {len(not_found)} songs not found.")
