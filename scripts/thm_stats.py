import requests
import re

def update_stats():
    username = "r9ruben"
    # Identidad de navegador para que THM no nos bloquee
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        print(f"Connecting to {username}'s profile...")
        response = requests.get(f"https://tryhackme.com/p/{username}", headers=headers, timeout=20)
        html = response.text
        
        # Valores de respaldo (tus datos reales actuales)
        rank = "847599"
        rooms = "9"
        
        # Buscamos los números en el código de la página
        r_match = re.search(r'rank["\s:]+([\d,]+)', html)
        rm_match = re.search(r'completedRooms["\s:]+(\d+)', html)
        
        if r_match: rank = r_match.group(1)
        if rm_match: rooms = rm_match.group(1)

        print(f"Stats found: Rank {rank}, Rooms {rooms}")

        # Bloque de texto final formateado
        new_stats = f"\n**Rank:** {rank}\n**Global Ranking:** #{rank}\n**Rooms Completed:** {rooms}\n"

        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Reemplazo estricto: esto evita que se duplique
        pattern = r".*?"
        replacement = f"{new_stats}"
        
        # Limpiamos posibles etiquetas duplicadas antes de escribir
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("✅ Success! README is now clean.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_stats()
