import requests
from datetime import datetime

# Test key
API_KEY = "123"

# Endpoint voor laatste 5 Premier League wedstrijden (voorbeeld)
# In real use: vervang competitie ID met gewenste league
URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventspastleague.php?id=4328"

response = requests.get(URL)
data = response.json()

md_content = "# Voetbalplatform – Dagoverzicht\n\n"
md_content += "## Uitslagen\n"

for match in data.get('events', [])[:5]:  # eerste 5 wedstrijden
    date_event = match.get('dateEvent', '?')
    home_team = match.get('strHomeTeam', '?')
    away_team = match.get('strAwayTeam', '?')
    home_score = match.get('intHomeScore', '?')
    away_score = match.get('intAwayScore', '?')
    md_content += f"- {date_event}: {home_team} – {away_team}: {home_score}–{away_score}\n"

md_content += "\n## Nieuws\n- Voorbeeldnieuws: agentic demo\n"
md_content += f"\n*Laatste update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

# Schrijf naar Markdown
with open("sample_output.md", "w", encoding="utf-8") as f:
    f.write(md_content)
