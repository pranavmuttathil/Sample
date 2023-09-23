from flask import Flask
import urllib
import post
import spotipy
from spotipy.oauth2 import SpotifyOAuth;
from spotipy.oauth2 import SpotifyClientCredentials
import speech_recognition as sr;

# Establishment of the speech recognition tool
r=sr.Recognizer()
mic = sr.Microphone()
print("Speak something")
with mic as source:
    print("Listening...")
    r.pause_threshold = 1
    r.energy_threshold = 200
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    r.recognize_google(audio)
    print("user said:" + audio )
 
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
port_number = 3000;
spotify_client_id = "9d51ddbc07584c89b6f5419171bd5fa7";
spotify_client_secret = '927413202b5a4f4884cef2084b5c0467';
spotify_redicrt_url = 'http://localhost:3000'

def getaccesstoken(self):
 sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="spotify_client_id",
                                               client_secret="spotify_client_secret",
                                               redirect_uri="spotify_redicrt_url",
                                               scope="user-library-read"))

#getting access_token by POST request to Spotify API
response = requests.post(
                self.__url,
                data=self.__body_params,
                auth=(
                    self.__client_id,
                    self.__client_secret
                )
            ).json()

artist = sp.artist(urn);
print("Name of the song you want to play")
with mic as source:
    song_name = r.recognize_google();
    r.adjust_for_ambient_noise(source)

current_song_playing = sp.currently_playing;
last_songs = sp.current_user_recently_played;
for i in range(3):
    last_three_songs.append();
    last_three_songs = {last_songs}


print("The user is " + sp.current_user)
print("The track playing is " + current_song_playing);
  
