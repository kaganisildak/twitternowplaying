import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from os import environ

auth_token = "" #twitter
ct0 = "" #twitter
client_id = "" #spotify
client_secret = "" #spotify

if auth_token == "" or ct0 == "" or client_id == "" or client_secret == "":
    try:
        auth_token = environ.get('auth_token')
        ct0 = environ.get('ct0')
        client_id = environ.get('clientid')
        client_secret = environ.get('clientsecret')
    except TypeError:
        print("auth_token, ct0, client_id ve client_secret değerlerini yazınız!")
        sleep(5)
        exit()
    
def desc(text):
    url = "https://twitter.com:443/i/api/1.1/account/update_profile.json"
    cookies = {"auth_token": auth_token, "ct0": ct0}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA", "X-Twitter-Auth-Type": "OAuth2Session", "X-Twitter-Client-Language": "en", "X-Twitter-Active-User": "yes", "Content-Type": "application/x-www-form-urlencoded", "X-Csrf-Token": ct0, "Origin": "https://twitter.com", "Dnt": "1", "Referer": "https://twitter.com/settings/profile", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
    data = {"description": text}
    requests.post(url, headers=headers, cookies=cookies, data=data)
    
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="https://www.google.com/callback", scope="user-read-currently-playing"))
temp = ""
while 1:
    try:
        resp = sp.current_user_playing_track()
        songname, artists = resp["item"]["name"], resp["item"]["artists"][0]["name"]
        if temp == songname:
            continue
        temp = ""
        temp+=songname
        playing = (f"🎧 Şu an bunu dinliyor: {songname} -- {artists}")
        desc(playing)
        print(playing)
        sleep(10)
    except:
        sleep(30)
