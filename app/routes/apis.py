from fastapi import APIRouter, Query
from app import auth, spotify
from fastapi.responses import RedirectResponse

router=APIRouter(
    responses={404:{"description":"Not Found"}}
)

# Store token in memory
user_token = {}


@router.get("/spotify/login")
def login():
    print(user_token)
    return RedirectResponse(auth.get_auth_url())

@router.get("/spotify/callback")
def callback(code: str):
    token_info = auth.get_token(code)
    user_token["access_token"] = token_info["access_token"]
    return {"message": "Authenticated successfully!"}

@router.get("/spotify/top-tracks")
def top_tracks():
    print(user_token)
    sp = spotify.get_spotify_client(user_token["access_token"])
    return spotify.get_top_tracks(sp)

@router.get("/spotify/now-playing")
def now_playing():
    sp = spotify.get_spotify_client(user_token["access_token"])
    return spotify.now_playing(sp)

@router.post("/spotify/pause")
def pause():
    sp = spotify.get_spotify_client(user_token["access_token"])
    return spotify.pause_track(sp)

@router.post("/spotify/play")
def play(track_id: str = Query(...)):
    sp = spotify.get_spotify_client(user_token["access_token"])
    return spotify.play_track(sp, track_id)