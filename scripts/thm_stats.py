from curl_cffi import requests
import re

def update_stats():
    username = "r9ruben"

    try:
        url = "https://tryhackme.com/p/" + username
        response = requests.get(url, impersonate="chrome110", timeout=20)
        html = response.text
        
        # Buscar todas las etiquetas <script> y mostrar su contenido
        scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
        
        print("Total de scripts encontrados: " + str(len(scripts)))
        
        for i, script in enumerate(scripts):
            # Solo mostrar scripts que tengan datos relevantes
            if any(word in script.lower() for word in ["rank", "room", "point", "complete", "r9ruben"]):
                print("=== SCRIPT " + str(i) + " ===")
                print(script[:2000])
                print("---")

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
