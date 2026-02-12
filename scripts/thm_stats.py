import requests
import re

def update_stats():
    username = "r9ruben"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(f"https://tryhackme.com/p/{username}", headers=headers, timeout=20)
        html = response.text
        
        # Buscamos los datos actuales
        rank = re.search(r'rank["\s:]+([\d,]+)', html)
        rooms = re.search(r'completedRooms["\s:]+(\d+)', html)
        
        rank_val = rank.group(1) if rank else "847599"
        rooms_val = rooms.group(1) if rooms else "9"

        # Formato limpio
        new_stats = f"\n**Rank:** {rank_val}\n**Global Ranking:** #{rank_val}\n**Rooms Completed:** {rooms_val}\n"

        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Esta es la parte de "seguridad": reemplaza SOLO una vez
        pattern = r".*?"
        replacement = f"{new_stats}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL, count=1)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✅ Success! README is now clean and updated.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_stats()
