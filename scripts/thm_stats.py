import requests
import re

def update_stats():
    # Usamos tu ID público oficial para una conexión limpia
    user_id = "6835034"
    url = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={user_id}"

    try:
        print(f"Conectando a la API oficial para el ID {user_id}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        # Obtenemos los datos limpios directamente en formato JSON
        data = response.json()
        
        # Extraemos solo los números que necesitamos
        rank = data.get("rank", "N/A")
        rooms = data.get("completedRooms", "N/A")

        print(f"Datos limpios encontrados -> Rank: {rank}, Salas: {rooms}")

        # Creamos el bloque de texto bonito y limpio
        stats_block = f"\n**Rank:** {rank}\n**Global Ranking:** #{rank}\n**Rooms Completed:** {rooms}\n"

        # Leemos el README
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazamos el contenido entre las marcas
        pattern = r".*?"
        replacement = f"{stats_block}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Guardamos el archivo limpio
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print("✅ README actualizado con éxito y SIN basura.")

    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    update_stats()
