import requests

def update_stats():
    username = "r9ruben"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        url = "https://tryhackme.com/api/user/rank/" + username
        response = requests.get(url, headers=headers, timeout=20)
        
        print("Status: " + str(response.status_code))
        print("Respuesta: " + response.text[:500])
        
        data = response.json()
        
        rank_val = str(data.get("userRank", "N/A"))
        rooms_val = str(data.get("completedRooms", "N/A"))

        readme = "**Rank:** " + rank_val + " | **Rooms Completed:** " + rooms_val + "\n"

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme)

        print("README actualizado correctamente")

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
