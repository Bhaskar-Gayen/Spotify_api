import requests

access_token = "BQAv57eWuJbveUEBUMbEFmw9PDmIhtkp1m8vFGhOnwyGK2Z9zOiNOZPWXtP8D_Mpn5TzDOmRr5D7iC5JiT37vkJI-GknZH7Vgu2ltOR6eu3ibs5k5UGs9no79JrGq5v41bzRfppu0S6lmeaDquYhBDt53goUow3BiP3s8avcHYdFbJFwyPJ434i-GlQVy45Csrn21lygkY1DdKuBLfkSsCC1vxasEcVYREzGfVyIXz_8b6SdKytk4zKh"
headers = {
    "Authorization": f"Bearer {access_token}"
}
params = {
    "limit": 10,
    "time_range": "short_term"
}

response = requests.get("https://api.spotify.com/v1/me/top/tracks", headers=headers, params=params)
print(response.json())
