from curl_cffi import requests
import os
import json

def update_stats():
    username = "r9ruben"
    cookie = os.environ.get("THM_COOKIE", "")

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://tryhackme.com/p/" + username,
        "Cookie": cookie,
    }

    try:
        url = "https://tryhackme.com/api/user/rank/" + username
        r = requests.get(url, headers=headers, impersonate="chrome110", timeout=20)

        print("Status: " + str(r.status_code))
        print("Respuesta: " + r.text[:500])

        data = r.json()
        rank_val = str(data.get("userRank", data.get("rank", "N/A")))
        rooms_val = str(data.get("completedRooms", "N/A"))

        readme = "**Rank:** " + rank_val + " | **Rooms Completed:** " + rooms_val + "\n"

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)

        print("README actualizado: Rank=" + rank_val + " Rooms=" + rooms_val)

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
