import requests
import json

def update_stats():
    username = "r9ruben"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://tryhackme.com',
    }

    try:
        # API pública de TryHackMe - no requiere autenticación
        api_url = f"https://tryhackme.com/api/user/rank/{username}"
        response = requests.get(api_url, headers=headers, timeout=20)
        
        print(f"Status code: {response.status_code}")
        print(f"Respuesta: {response.text[:500]}")
        
        data = response.json()

        # La API devuelve los datos directamente
        rank_val = data.get("userRank", data.get("rank", "N/A"))
        rooms_val = data.get("completedRooms", data.get("rooms", "N/A"))

        # Si rooms no está en este endpoint, intentar otro
        if rooms_val == "N/A":
            rooms_url = f"https://tryhackme.com/api/user/rooms/{username}"
            r2 = requests.get(rooms_url, headers=headers, timeout=20)
            print(f"Rooms API respuesta: {r2.text[:300]}")
            d2 = r2.json()
            rooms_val = d2.get("completedRooms", d2.get("total", "N/A"))

        new_stats = (
            f"**Rank:** {rank_val} | "
            f"**Global Ranking:** #{rank_val} | "
            f"**Rooms Completed:** {rooms_val}\n"
        )

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_stats)

        print(f"✅ README actualizado: Rank={rank_val}, Rooms={rooms_val}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_stats()
```

---

## Lo más importante ahora: ver qué devuelve la API

El script ya tiene `print` de debug. Cuando lo ejecutes en Actions, el log te mostrará exactamente qué JSON devuelve la API. Comparte esa respuesta conmigo y en un segundo te digo exactamente qué campos usar.

También puedes verlo tú mismo yendo directamente a tu navegador a:
```
https://tryhackme.com/api/user/rank/r9ruben
