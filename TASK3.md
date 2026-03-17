# P18 Everwien — TASK3: Alles fertig machen

Lies auch TASK2_EXTRA.md, CHRONIK.md und LEGAL.md!

## BUGS FIXEN (HÖCHSTE PRIORITÄT)

### SVG-Icons escaped (BEREITS GEFIXT in sonnenschutz, glasdaecher, insektenschutz, gartenmoebel, raumdesign)
- Prüfe ALLE Templates nochmal: Überall wo SVG über Jinja-Variable eingefügt wird MUSS `|safe` stehen
- Teste: curl localhost:3019/everwien/sonnenschutz | grep '<svg' (muss SVGs finden, nicht escaped)

## FEHLENDE SEITEN

### 1. Team-Seite (team.html) — NEU ERSTELLEN
- Route: /everwien/team
- Familienbetrieb mit ~40 Mitarbeitern
- **Folkert Everwien** = Geschäftsführer, 5. Generation, Foto: `static/img/folkert-everwien.jpg` (ECHTES Foto!)
- Aufklappbar nach Kategorien (Accordion):
  - Geschäftsführung (Folkert + 1 weitere Person)
  - Meister & Werkstattleitung (3-4 Personen)
  - Montage-Teams (15-20 Personen)
  - Beratung & Verkauf (5-6 Personen)
  - Verwaltung (4-5 Personen)
- Dummy-Bilder für alle außer Folkert: Lade 8-10 diverse Portraits von Pexels (Handwerker, Berater, mix aus Männer/Frauen)
- Jede Person: Foto (rund), Name (Platzhalter), Rolle, 1 Satz
- Oben: "Wir sind Everwien — ein Familienbetrieb seit 1880"

### 2. Über-uns / Chronik — KOMPLETT NEU
- Die aktuelle ueber-uns.html ist fast leer
- Lies CHRONIK.md — dort steht die komplette 145-jährige Geschichte
- Timeline-Design: Vertikale Linie mit Meilensteinen (1880, 1895, 1909, 1945, 1957, 1974, 1976, 1984, 1992, heute)
- 5 Generationen klar darstellen
- Ursprung: Sattlerei → Polstermöbel → Raumausstattung → Sonnenschutz → heute
- Werte-Sektion: Tradition, Qualität, Regionalität, Familie
- Link zu Team-Seite

### 3. FAQ — KOMPLETT NEU
- Die aktuelle faq.html ist fast leer (1.7KB)
- 15-20 Fragen in Accordion, kategorisiert:
  - Glasdächer & Überdachungen (4-5 Fragen)
  - Sonnenschutz (4-5 Fragen)  
  - Service & Beratung (4-5 Fragen)
  - Bestellung & Montage (3-4 Fragen)
- Typische Fragen: Kosten, Montagezeit, Finanzierung, Ausstellung, Liefergebiet, Garantie, Pflege, Nachrüstung, Smart Home

## SPRACHEN (3 Sprachen, Plattdeutsch = DEFAULT)

### Content-Dateien erstellen
- data/content_plt.json (Ostfriesisches Platt) — DEFAULT
- data/content_de.json (Hochdeutsch)
- data/content_en.json (Englisch)
- Alle Navigation, Footer, Buttons, Headlines, Fließtexte
- html lang="nds" als Default

### Sprachwechsel
- Route: /everwien/lang/{code} setzt Cookie, redirect zurück
- Sprachumschalter in Nav: PLT | DE | EN
- Cookie: "lang", default "plt"

### Plattdeutsch Easter Eggs
- Footer: wechselnder Plattdeutscher Spruch
- 404: "Dat hebbt wi nich funnen — is woll achter de Markise versteken!"
- Kontakt: "Wi snackt ok Platt!"
- Loading: "Tööv mal eeven..."

## DARK MODE
- CSS `prefers-color-scheme` als System-Default
- Toggle-Button in Nav (☀️/🌙)
- Dark: Background #1A1A2E, Text #E8E8E8, Cards #1E1E1E
- Kupfer #C67B5C bleibt (funktioniert auf dunkel)
- localStorage speichern
- Smooth transition 0.3s

## UX VERBESSERUNGEN
- Scroll-Progress-Bar oben (dünn, Kupfer)
- Back-to-Top Button
- Breadcrumbs auf Unterseiten
- "Verwandte Produkte" am Ende jeder Produktseite
- CTA "Kostenlose Beratung" auf JEDER Seite
- Trust-Bar: "Seit 1880 | 2.000 m² Ausstellung | Eigene Produktion"

## SERVER.PY AKTUALISIEREN
- Alle neuen Routes: /team, /lang/{code}
- Content-JSON laden nach Sprach-Cookie
- 404 Exception Handler
- Impressum, Datenschutz Routes prüfen

## NACH ABSCHLUSS:
1. systemctl --user restart everwien-server  
2. curl -s localhost:3019/everwien/ (testen dass es läuft)
3. curl -s localhost:3019/everwien/team (Team-Seite)
4. curl -s localhost:3019/everwien/ueber-uns (Chronik)
5. curl -s localhost:3019/everwien/faq (FAQ)
6. openclaw system event --text "Done: P18 Everwien TASK3 complete" --mode now
