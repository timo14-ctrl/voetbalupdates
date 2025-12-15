# Journalistieke Voetbalagent – Demo met SportDB.dev

## Doel
Autonoom platform dat actuele voetbaluitslagen en nieuws presenteert.
Demo gebruikt de gratis "123" API-key van SportDB.dev.

## Werkwijze
1. Script `update_scores.py` haalt laatste wedstrijden op.
2. Markdown-output (`sample_output.md`) toont uitslagen en nieuws.
3. GitHub Actions draait dagelijks om updates automatisch te committen.
4. Agentic workflow: ophalen → selecteren → samenvatten → publiceren.

## Bestanden
- `update_scores.py` – Python-script voor uitslagen
- `sample_output.md` – gegenereerde Markdown-feed
- `agent_prompt.md` – instructies voor agent
- `.github/workflows/update_scores.yml` – automatische workflow
- `README.md` – uitleg en reflectie

## Reflectie
Agentic AI: workflow werkt autonoom met meerdere stappen.  
Uitkomst: een automatisch bijgewerkt, journalistiek relevant platform.


