import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# get the client id and client secret from spotify
# https://developer.spotify.com/dashboard/applications/

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

# get the date from the user
date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# get the data from the website
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=url)
response.raise_for_status()

# scrape the data from the website
soup = bs4.BeautifulSoup(response.text, "html.parser")
songs_element = soup.select("li > ul > li > h3#title-of-a-story")

# get the text of the song from the html element
songs = [song.get_text(strip=True) for song in songs_element]

# get the spotify token for the user to create a playlist
# when open the link, it will ask you to login to spotify and give permission to the app to create a playlist
# after you login, it will redirect you to the url you set in the redirect_uri on spotify developer dashboard (https://example.com)
# copy the url and paste it in the terminal
# it will create a token.txt file in the same folder
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri="https://example.com",scope="playlist-modify-private",show_dialog=True,cache_path="token.txt"))

# get the user id
user_id = sp.current_user()["id"]
print(user_id)

# search for the song in spotify
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# create a playlist in spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# add songs into the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
