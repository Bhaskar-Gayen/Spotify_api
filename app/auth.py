from spotipy.oauth2 import SpotifyOAuth
from app.core.config import Settings

settings=Settings()
scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing user-top-read"

sp_oauth = SpotifyOAuth(
    client_id=settings.SPOTIFY_CLIENT_ID,
    client_secret=settings.SPOTIFY_CLIENT_SECRET,
    redirect_uri=settings.SPOTIFY_REDIRECT_URI,
    scope=scope
)

def get_auth_url():
    return sp_oauth.get_authorize_url()

def get_token(code: str):
    token_info = sp_oauth.get_access_token(code)
    return token_info
