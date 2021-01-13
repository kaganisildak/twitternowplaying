import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import time
import twitter

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="https://kaganisildak.com",
                                               scope="user-read-currently-playing"))

temp_song = ""

while True:
    cur_play = sp.current_user_playing_track()
    songname = cur_play["item"]["name"]
    artists = cur_play["item"]["artists"][0]["name"]
    title = "🎧 Şuan bunu dinliyor : {}-{}".format(songname,artists)
    if temp_song == songname:
        time.sleep(1)
    else:
        temp_song = songname
        twitter.change_desc(title)
        print(title)
    #
    time.sleep(3)
