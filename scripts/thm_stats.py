from curl_cffi import requests
import re

def update_stats():
    username = "r9ruben"

    try:
        url = "https://tryhackme.com/p/" + username
        response = requests.get(url, impersonate="chrome110", timeout=20)

        print("Status: " + str(response.status_code))
        
        html = response.text
        
        # Buscar la seccion con los datos del usuario
        # Imprimir 3000 caracteres alrededor de donde aparece el username
        idx = html.find(username)
        if idx != -1:
            print("=== CONTEXTO DEL USERNAME ===")
            print(html[idx-200:idx+2000])
        else:
            print("Username no encontrado en el HTML")
            
        # Imprimir primeros 500 chars del script de Next.js si existe
        next_idx = html.find("__NEXT_DATA__")
        if next_idx != -1:
            print("=== NEXT DATA ===")
            print(html[next_idx:next_idx+3000])

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
