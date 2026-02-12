import requests
import re
import json

def update_stats():
    username = "r9ruben"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(
            f"https://tryhackme.com/p/{username}",
            headers=headers,
            timeout=20
        )
        html = response.text

        # TryHackMe usa Next.js, los datos están en __NEXT_DATA__
        match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)

        if not match:
            raise Exception("No se encontró __NEXT_DATA__ en la página")

        data = json.loads(match.group(1))

        # Navegar por el JSON para obtener los datos del usuario
        props = data.get("props", {}).get("pageProps", {})
        
        # Intentar diferentes rutas posibles dentro del JSON
        user_data = props.get("user", props.get("userData", props.get("profileData", {})))
        
        rank_val = user_data.get("userPoints", user_data.get("points", "N/A"))
        rooms_val = user_data.get("completedRooms", user_data.get("rooms", "N/A"))
        
        # Si no encontramos los datos, buscar en todo el JSON
        if rank_val == "N/A":
            json_str = match.group(1)
            rank_search = re.search(r'"userPoints"\s*:\s*(\d+)', json_str)
            rank_val = rank_search.group(1) if rank_search else "N/A"
        
        if rooms_val == "N/A":
            json_str = match.group(1)
            rooms_search = re.search(r'"completedRooms"\s*:\s*(\d+)', json_str)
            rooms_val = rooms_search.group(1) if rooms_search else "N/A"

        new_stats = f"**Rank:** {rank_val}\n**Global Ranking:** #{rank_val}\n**Rooms Completed:** {rooms_val}\n"

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_stats)

        print(f"✅ README actualizado: Rank={rank_val}, Rooms={rooms_val}")

    except Exception as e:
        print(f"❌ Error: {e}")
        # Imprimir parte del HTML para debug
        try:
            print(f"Primeros 2000 chars del HTML: {html[:2000]}")
        except:
            pass

if __name__ == "__main__":
    update_stats()
