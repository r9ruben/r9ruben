from curl_cffi import requests
import re

def update_stats():
    username = "r9ruben"

    try:
        url = "https://tryhackme.com/p/" + username
        response = requests.get(url, impersonate="chrome110", timeout=20)

        print("Status: " + str(response.status_code))
        
        html = response.text
        
        rank = re.search(r'"userPoints"\s*:\s*(\d+)', html)
        rooms = re.search(r'"completedRooms"\s*:\s*(\d+)', html)
        
        rank_val = rank.group(1) if rank else "N/A"
        rooms_val = rooms.group(1) if rooms else "N/A"
        
        print("Rank encontrado: " + rank_val)
        print("Rooms encontrado: " + rooms_val)

        readme = "**Rank:** " + rank_val + " | **Rooms Completed:** " + rooms_val + "\n"

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)

        print("README actualizado correctamente")

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
