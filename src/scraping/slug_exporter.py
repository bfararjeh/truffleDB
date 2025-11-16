import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# List of Liquidpedia tournament URLs
urls = ['https://liquipedia.net/fighters/FightClub_Championship/6/Chengdu', 'https://liquipedia.net/fighters/Esports_World_Cup/2024/SF6', 'https://liquipedia.net/fighters/Street_Fighter_League/Japan/2025', 'https://liquipedia.net/fighters/Topanga_Championship/5', 'https://liquipedia.net/fighters/Evolution_Championship_Series/2025/SF6', 'https://liquipedia.net/fighters/Blink_Respawn/2024/SF6', 'https://liquipedia.net/fighters/Street_Fighter_League/Japan/2024', 'https://liquipedia.net/fighters/Street_Fighter_League/Japan/2023', 'https://liquipedia.net/fighters/The_MIXUP/2024/SF6', 'https://liquipedia.net/fighters/Street_Fighter_League/World_Championship/2023', 'https://liquipedia.net/fighters/Ultimate_Fighting_Arena/2024/SF6', 'https://liquipedia.net/fighters/Red_Bull_Kumite/2025', 'https://liquipedia.net/fighters/Street_Fighter_League/World_Championship/2024', 'https://liquipedia.net/fighters/Capcom_Cup/12', 'https://liquipedia.net/fighters/Topanga_Championship/6', 'https://liquipedia.net/fighters/Ultimate_Fighting_Arena/2023/SF6', 'https://liquipedia.net/fighters/Capcom_Cup/10/Last_Chance_Qualifier', 'https://liquipedia.net/fighters/Community_Effort_Orlando/2024/SF6', 'https://liquipedia.net/fighters/Community_Effort_Orlando/2025/SF6', 'https://liquipedia.net/fighters/Evolution_Championship_Series/2024/Japan/SF6', 'https://liquipedia.net/fighters/Street_Fighter_League/Europe/2024', 'https://liquipedia.net/fighters/Street_Fighter_League/United_States/2023', 'https://liquipedia.net/fighters/Evolution_Championship_Series/2023/SF6', 
'https://liquipedia.net/fighters/FAV_CUP/2023/Singles', 'https://liquipedia.net/fighters/Community_Effort_Orlando/2023/SF6', 'https://liquipedia.net/fighters/Evolution_Championship_Series/2025/France/SF6', 'https://liquipedia.net/fighters/Capcom_Pro_Tour/2023/Singapore_Offline', 'https://liquipedia.net/fighters/Street_Fighter_League/United_States/2024', 'https://liquipedia.net/fighters/Red_Bull_Kumite/2024/New_York', 'https://liquipedia.net/fighters/Street_Fighter_League/United_States/2025', 'https://liquipedia.net/fighters/Evolution_Championship_Series/2025/Japan/SF6', 'https://liquipedia.net/fighters/Combo_Breaker/2024/SF6', 'https://liquipedia.net/fighters/Red_Bull_Kumite/2023/South_Africa', 'https://liquipedia.net/fighters/Street_Fighter_League/Europe/2023', 'https://liquipedia.net/fighters/Capcom_Pro_Tour/2023/France_Offline', 'https://liquipedia.net/fighters/Capcom_Cup/10', 'https://liquipedia.net/fighters/Gamers8/2023/SF6', 'https://liquipedia.net/fighters/Capcom_Cup/11', 'https://liquipedia.net/fighters/Kings_of_the_World/2024', 'https://liquipedia.net/fighters/East_Coast_Throwdown/2024/SF6', 'https://liquipedia.net/fighters/DreamHack/2024/Dallas/SF6', 'https://liquipedia.net/fighters/Evolution_Championship_Series/2024/SF6', 'https://liquipedia.net/fighters/DreamHack/2024/Summer/SF6', 'https://liquipedia.net/fighters/Esports_World_Cup/2025/SF6', 
'https://liquipedia.net/fighters/Cream_City_Convergence/2024/SF6', 'https://liquipedia.net/fighters/Ultimate_Fighting_Arena/2025/SF6', 'https://liquipedia.net/fighters/Esports_World_Cup/2025/SF6/Last_Chance_Qualifier', 'https://liquipedia.net/fighters/Capcom_Pro_Tour/2024/Super_Premier/Singapore', 'https://liquipedia.net/fighters/Combo_Breaker/2025/SF6', 'https://liquipedia.net/fighters/Asian_Champions_League/2025', 'https://liquipedia.net/fighters/Capcom_Pro_Tour/2024/Super_Premier/Japan', 'https://liquipedia.net/fighters/Esports_World_Cup/2024/SF6/Last_Chance_Qualifier', 'https://liquipedia.net/fighters/Blink_Respawn/2025/SF6']

startgg_slugs = []

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all external links
    links = soup.select("a.external.text")
    slug_found = False

    for a in links:
        href = a.get("href", "")
        if "start.gg" in href:
            parsed = urlparse(href)
            path_parts = parsed.path.strip("/").split("/")
            if len(path_parts) > 1 and path_parts[0] == "tournament":
                startgg_slug = path_parts[1]  # second segment after 'tournament'
                startgg_slugs.append(startgg_slug)
                slug_found = True
                break

    if not slug_found:
        startgg_slugs.append(None)

# Print results
for url, slug in zip(urls, startgg_slugs):
    print(f"Liquidpedia URL: {url}")
    print(f"Start.gg slug: {slug}\n")

# Count how many slugs are None
none_count = sum(1 for slug in startgg_slugs if slug is None)
print(f"Number of Liquidpedia pages without a Start.gg slug: {none_count}")