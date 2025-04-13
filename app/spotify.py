import spotipy


def get_spotify_client(token):
    return spotipy.Spotify(auth=token)

def get_top_tracks(sp):
    try:
        top = sp.current_user_top_tracks(limit=10, time_range='short_term')
        tracks = top.get("items", [])
        print("Top Object: ", top)

        return [
            {
                "name": t.get("name"),
                "artist": t["artists"][0]["name"] if t.get("artists") else "Unknown",
                "id": t.get("id")
            }
            for t in tracks
        ]

    except Exception as e:
        print(f"[ERROR] Failed to fetch top tracks: {e}")
        return []


def now_playing(sp):
    track = sp.current_playback()
    if not track:
        return {"message": "Nothing is playing"}
    return {
        "name": track["item"]["name"],
        "artist": track["item"]["artists"][0]["name"],
        "is_playing": track["is_playing"]
    }

def pause_track(sp):
    sp.pause_playback()
    return {"message": "Playback paused"}

def play_track(sp, track_id: str):
    sp.start_playback(uris=[f"spotify:track:{track_id}"])
    return {"message": f"Started playing track {track_id}"}
