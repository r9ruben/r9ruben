from curl_cffi import requests
import json

def update_stats():
    username = "r9ruben"

    # Estas son las APIs internas que usa TryHackMe en el navegador
    endpoints = [
        "https://tryhackme.com/api/user/rank/" + username,
        "https://tryhackme.com/api/v2/user/profile/" + username,
        "https://tryhackme.com/api/no-auth/leaderboards?limit=1&username=" + username,
    ]

    try:
        for url in endpoints:
            print("Probando: " + url)
            r = requests.get(url, impersonate="chrome110", timeout=20)
            print("Status: " + str(r.status_code))
            print("Respuesta: " + r.text[:800])
            print("---")

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    update_stats()
