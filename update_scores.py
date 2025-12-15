import requests
import os
from datetime import datetime

API_KEY = os.environ["FOOTBALL_API_KEY"]
URL = "https://api.football-data.org/v4/matches"

headers = {"X-Auth-Token": API_KEY}
response = requests.get(URL, headers=headers).json()

md_content = "# Voetbalplatform – Dagoverzicht\n\n"
md_content += "## Uitslagen\n"

for match in response.get("matches", [])[:5]:
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]
    score = match.get("score", {}).get("fullTime", {})
    home_score = score.get("home", "?")
    away_score = score.get("away", "?")
    md_content += f"- {home} – {away}: {home_score}–{away_score}\n"

md_content += "\n## Nieuws\n- Voorbeeldnieuws: API-feed nog niet gekoppeld.\n"
md_content += f"\n*Laatste update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

with open("sample_output.md", "w", encoding="utf-8") as f:
    f.write(md_content)
