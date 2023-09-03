import post
import spotipy
from spotipy.oauth2 import SpotifyOAuth;
import base64;
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

#defining scopes
scope = "user-library-read"




def generate_token():
    auth_string = client_id + " : " +client_secret
    auth_bytes = auth.string.encode("utf-8")
    auth_base64_string = str(base64.b64encode(auth_bytes),"utf-8") 
    headers = {
        "Authorization" : "Basic" + auth_base64_string,
    }



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#listing the searched tracks from the artist
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " = ", track['name'])


# sp = spotipy.Spotify();
# artist = sp.artist(urn);
print("Name of the song you want to play")
with mic as source:
    song_name = r.recognize_google();
    r.adjust_for_ambient_noise(source)


print("The user is " + sp.current_user)
print("The track playing is " + sp.currently_playing)


  
