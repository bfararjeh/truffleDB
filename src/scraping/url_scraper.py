import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL for Tier 1 SF6 tournaments
tier1_url = "https://liquipedia.net/fighters/Street_Fighter_6/Tier_1_Tournaments"

response = requests.get(tier1_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

tournament_links = []

# Find all <b> tags containing <a> links
for b_tag in soup.find_all("b"):
    a_tag = b_tag.find("a")
    if a_tag and a_tag.get("href"):
        href = a_tag["href"]
        full_url = urljoin("https://liquipedia.net", href)
        tournament_links.append(full_url)

# Remove duplicates
tournament_links = list(set(tournament_links))

print(f"Found {len(tournament_links)} tournament pages:")
# for link in tournament_links:
#     print(link)
print(tournament_links)