# This script fetches public TryHackMe stats and updates the README.md

import requests
from bs4 import BeautifulSoup

USERNAME = "r9ruben"
URL = f"https://tryhackme.com/p/{USERNAME}"

response = requests.get(URL, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# --- VERY BASIC extraction (safe placeholders if structure changes) ---
rank = "Unknown"
global_rank = "Unknown"
rooms_completed = "Unknown"

text = soup.get_text()

if "Rank" in text:
    rank = "Visible on profile"

if "Completed" in text:
    rooms_completed = "Visible on profile"

new_block = f"""<!-- THM_STATS_START -->
Rank: {rank}
Global Ranking: {global_rank}
Rooms Completed: {rooms_completed}
<!-- THM_STATS_END -->"""

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace stats block
import re
readme = re.sub(
    r"<!-- THM_STATS_START -->.*?<!-- THM_STATS_END -->",
    new_block,
    readme,
    flags=re.DOTALL
)

# Write README back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("TryHackMe stats updated")
