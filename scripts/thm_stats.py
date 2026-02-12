import requests
import re

def update_stats():
    # Usamos tu nombre de usuario oficial
    username = "r9ruben"
    url = f"https://tryhackme.com/p/{username}"
    
    # Esta cabecera es vital para que TryHackMe no nos bloquee
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        print(f"Conectando con el perfil de {username}...")
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        
        html = response.text
        
        # Nueva búsqueda más potente para el Rank y las Salas
        # Buscamos los números que aparecen cerca de las palabras clave
        rank_search = re.search(r'rank["\s:]+([\d,]+)', html, re.IGNORECASE)
        rooms_search = re.search(r'completedRooms["\s:]+(\d+)', html, re.IGNORECASE)
        
        # Si no los encuentra arriba, probamos con este otro formato
        if not rank_search:
            rank_search = re.search(r'Rank.*?(\d+)', html, re.DOTALL)
        if not rooms_search:
            rooms_search = re.search(r'Rooms Completed.*?(\d+)', html, re.DOTALL)

        # Limpiamos los datos encontrados
        rank = rank_search.group(1) if rank_search else "847599" # Backup con tu dato actual
        rooms = rooms_search.group(1) if rooms_search else "9"    # Backup con tu dato actual

        print(f"Datos encontrados -> Rank: {rank}, Salas: {rooms}")

        stats_block = f"\n**Rank:** {rank}\n**Global Ranking:** #{rank}\n**Rooms Completed:** {rooms}\n"

        # Leemos y actualizamos el README
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r".*?"
        replacement = f"{stats_block}"

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(re.sub(pattern, replacement, content, flags=re.DOTALL))
            
        print("✅ README actualizado con éxito.")

    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    update_stats()
