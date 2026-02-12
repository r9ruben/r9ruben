import requests
import re

def update_stats():
    username = "r9ruben"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(f"https://tryhackme.com/p/{username}", headers=headers, timeout=20)
        html = response.text

        rank = re.search(r'rank[\s]+([\d,]+)', html)
        rooms = re.search(r'completedRooms[\s]+(\d+)', html)

        rank_val = rank.group(1) if rank else "N/A"
        rooms_val = rooms.group(1) if rooms else "N/A"

        new_stats = f"\n**Rank:** {rank_val}\n**Global Ranking:** #{rank_val}\n**Rooms Completed:** {rooms_val}\n"

        # ✅ CORRECCIÓN: sobrescribir directamente en lugar de usar regex
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_stats)

        print("✅ README actualizado correctamente.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_stats()
