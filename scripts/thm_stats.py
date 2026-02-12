import requests
import re
import os

def main():
    user_id = "6835034"
    url = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={user_id}"
    
    try:
        print(f"Buscando datos para el usuario {user_id}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        rank = data.get("rank", "N/A")
        rooms = data.get("completedRooms", "N/A")
        
        stats_block = f"\n**Rank:** {rank}\n**Global Ranking:** #{rank}\n**Rooms Completed:** {rooms}\n"
        
        # Leemos el README
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Buscamos las etiquetas (esta vez de forma más flexible)
        pattern = r".*?"
        replacement = f"{stats_block}"
        
        if not re.search(pattern, content, flags=re.DOTALL):
            print("❌ ERROR: No encontré las etiquetas en tu README.md")
            return

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print("✅ ¡README actualizado con éxito!")
        
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
