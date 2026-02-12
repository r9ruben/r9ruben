# This script fetches real stats from TryHackMe API and updates the README
import requests
import re

def main():
    # Your official public ID
    user_id = "6835034"
    url = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={user_id}"
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # Extracting real data from your profile
        rank = data.get("rank", "N/A")
        rooms = data.get("completedRooms", "N/A")
        username = data.get("username", "r9ruben")

        # Formatting the block
        stats_block = (
            f"\n**Rank:** {rank}\n"
            f"**Global Ranking:** #{rank}\n"
            f"**Rooms Completed:** {rooms}\n"
        )
        
        # Update README.md
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            
        # Regex to find the markers
        pattern = r".*?"
        replacement = f"{stats_block}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print("Stats updated successfully for " + username)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
