import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to time travel? Enter date in (yyyy-mm-dd) format.\n")
print("Please wait while we travel back in time....")

# ---------------------------------------- Scraping Billboard ---------------------------------------- #

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(billboard_url)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
songs_name = soup.select(selector="li h3", class_="c-title")
songs = [song.text.strip() for song in songs_name[0:100]]

# ---------------------------------------- Scraping Billboard ---------------------------------------- #

client_id = "297f397617bd4b78ad76179c93fe59fe"
client_secret = "894db33a5cdb4b77b7b794a7c5bfbef6"

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri="http://example.com"))
user_id = sp.current_user()["id"]

year = date.split("-")[0]

uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(f"{song} song not found")


playlist_name = f"{date}Billboard Top 100"
playlist_id = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)["id"]
sp.playlist_add_items(playlist_id=playlist_id,items=uris,)
