from curl_cffi import requests

def update_stats():
    username = "r9ruben"

    # Headers que envía Chrome cuando hace una llamada API (fetch/XHR)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://tryhackme.com/p/" + username,
        "Origin": "https://tryhackme.com",
        "X-Requested-With": "XMLHttpRequest",
    }

    endpoints = [
        "https://tryhackme.com/api/user/rank/" + username,
        "https://tryhackme.com/api/v2/hackers/profile/" + username,
        "https://tryhackme.com/api/v2/user/" + username,
    ]

    try:
        for url in endpoints:
            print("Probando: " + url)
            r = requests.get(
                url,
                headers=headers,
                impersonate="chrome110",
                timeout=20
            )
            print("Status: " + str(r.status_code))
            print("Content-Type: " + r.headers.get("content-type", "N/A"))
            print("Respuesta: " + r.text[:500])
            print("---")

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
