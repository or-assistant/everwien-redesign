# TASK2 Ergänzungen (WICHTIG — zusätzlich zu TASK2.md!)

## Plattdeutsch ist DEFAULT-Sprache
- Plattdeutsch (Ostfriesisches Platt) ist die AUSGANGS-Sprache, nicht Deutsch!
- Sprachreihenfolge: PLT (Default) | DE | EN
- html lang="nds" als Default
- Seite öffnet sich standardmäßig auf Plattdeutsch

## Mobile MUSS perfekt sein
- Mobile-first Design (touch targets min 44px)
- Hamburger-Menü smooth
- Cards stapeln sich sauber
- Bilder responsive (srcset wenn möglich)
- Kein horizontales Scrollen

## 404-Seite
- Eigenes Template: 404.html
- Handwerkliches Thema (Sonnenschutz/Raumausstattung)
- Frecher Plattdeutscher Spruch (z.B. "Dat hebbt wi nich funnen — is woll achter de Markise versteken!")
- Kleines Mini-Game dazu:
  - Idee: "Fang die Sonne" — eine CSS/JS Sonne bewegt sich, man muss sie mit einer Markise/Sonnenschutz einfangen
  - Oder: Drag & Drop Markise über ein Fenster ziehen
  - Simpel, lustig, on-brand
- CTA zurück zur Startseite
- Dreisprachig (PLT/DE/EN), jeweils mit passendem Spruch
- In server.py als Exception Handler registrieren

## Firmengeschichte korrigieren
- Everwien wurde vor 145 Jahren gegründet (1880)
- Ursprung: Zaumzeug und Lederzeug (Sattlerei/Riemer)
- Dann Entwicklung zu Sonnenschutz & Raumdesign
- Timeline auf Über-uns-Seite entsprechend anpassen: Sattlerei → Polsterei/Raumausstattung → Sonnenschutz → heute

## Team-Seite (team.html)
- Familienbetrieb mit ~40 Mitarbeitern
- Geschäftsführung: Folkert Everwien (+ ggf. weitere Familienmitglieder)
- Sektionen: Geschäftsführung, Meister/Werkstattleitung, Montage-Teams, Beratung/Verkauf, Verwaltung
- Dummy-Bilder (Pexels: Handwerker-Portraits, diverse, sympathisch)
- Jede Person: Foto, Name (Platzhalter), Rolle, kurzer Satz
- Teamfoto-Bereich oben (Gruppenbild)
- "Wir sind ein Familienbetrieb" Storytelling
- Verlinken von Karriere-Seite ("Werde Teil unseres Teams")
- In Navigation einbauen

## Freche Plattdeutsche Sprüche
- Überall auf der Seite kleine Plattdeutsche Easter Eggs einbauen
- Footer: wechselnder Plattdeutscher Spruch
- 404: lustiger Spruch
- Kontaktseite: "Wi snackt ok Platt!"
- Loading-States: "Tööv mal eeven..."
