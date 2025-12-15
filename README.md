# Journalistieke Voetbalagent – Live Uitslagen & Nieuws

## Doel
Deze toepassing toont een journalistieke agentic AI die autonoom de nieuwste voetbaluitslagen en voetbalnieuws verzamelt, selecteert en samenvat voor lezers. 

Het platform fungeert als een mini-nieuwsfeed of -platform, ideaal voor sportjournalisten die dagelijkse updates nodig hebben.

---

## Werkwijze (agentic)

De agent werkt autonoom in meerdere stappen:

1. **Verzamelen van data**  
   - De agent haalt de laatste voetbaluitslagen op via een betrouwbare voetbal-API.
   - Nieuwsitems worden toegevoegd (kan in een echte toepassing automatisch worden gekoppeld).

2. **Selectie**  
   - Alleen relevante en actuele informatie wordt opgenomen.

3. **Analyse en samenvatting**  
   - De uitslagen en nieuwsitems worden samengevat in duidelijke journalistieke taal.

4. **Structurering van output**  
   - Output wordt geschreven naar `sample_output.md` in Markdown.
   - Structuur:
     - Uitslagen
     - Belangrijk nieuws
     - Korte duiding

---

## Live updates met GitHub Actions

- Het Python-script `update_scores.py` haalt automatisch de laatste data op en schrijft dit naar `sample_output.md`.
- Een **GitHub Action** draait dagelijks en commit automatisch de bijgewerkte Markdown.
- De API-key wordt veilig opgeslagen als **repository secret**.

---

## Bestanden in deze repository

| Bestand | Functie |
|---------|---------|
| `README.md` | Uitleg van het project, agentic workflow en live update systeem |
| `agent_prompt.md` | Instructies voor de agent |
| `sample_output.md` | Outputvoorbeeld van het platform |
| `update_scores.py` | Script dat uitslagen ophaalt en Markdown bijwerkt |
| `.github/workflows/update_scores.yml` | Automatisering van dagelijkse updates |

---

## Reflectie: waarom agentic AI?

Deze toepassing is agentic omdat de AI zelfstandig meerdere stappen doorloopt: verzamelen, selecteren, samenvatten en presenteren van informatie. Dit bootst de routine van een journalist na en levert een nuttig, automatisch bijgewerkt platform.

---

## Gebruik

- Bekijk `sample_output.md` voor het resultaat.
- Het platform wordt automatisch bijgewerkt via de GitHub Action en de voetbal-API.

