import requests
import re

def update_stats():
    username = "r9ruben"
    url = f"https://tryhackme.com/p/{username}"
    # Engañamos al sitio para que piense que somos un navegador real
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        print(f"Conectando con el perfil de {username}...")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Buscamos tu Rank (847599) y Salas (9) directamente en el texto de la página
        html = response.text
        
        # Buscamos el número que está justo después de la palabra 'Rank'
        rank_match = re.search(r'Rank.*?(\d+)', html, re.DOTALL)
        # Buscamos el número de salas completadas
        rooms_match = re.search(r'Completed rooms.*?(\d+)', html, re.DOTALL)
        
        rank = rank_match.group(1) if rank_match else "N/A"
        rooms = rooms_match.group(1) if rooms_match else "N/A"

        stats_block = f"\n**Rank:** {rank}\n**Global Ranking:** #{rank}\n**Rooms Completed:** {rooms}\n"

        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r".*?"
        replacement = f"{stats_block}"

        if "" not in content:
            print("❌ Error: No encontré las etiquetas en el README")
            return

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(re.sub(pattern, replacement, content, flags=re.DOTALL))
            
        print(f"✅ ¡Éxito! Rank: {rank}, Salas: {rooms}")

    except Exception as e:
        print(f"❌ Falló el script: {e}")
        exit(1) # Esto hace que el círculo salga ROJO si falla, para que lo sepas

if __name__ == "__main__":
    update_stats()
