# P18 Everwien — Runde 2: Deep Polish & Features

## Deine Aufgaben (ALLE erledigen!)

### 1. Bilder-Audit: Passen Bilder zu den Themen?
- Geh JEDE Seite durch und prüfe: Passt das Bild zum Inhalt?
- Besonders: Glasdächer, Sonnenschutz, Insektenschutz — brauchen die bessere Bilder?
- Wenn ein Bild nicht passt: Lade ein besseres von Pexels (curl, wie die bestehenden)
- Bilder sollen Premium-Gefühl vermitteln (Zielgruppe: mittleres bis hohes Preissegment)
- hero-terrace.jpg, glasdach.jpg, markise.jpg, terrasse.jpg, gartenmoebel.jpg, raumdesign.jpg, fenster.jpg, team.jpg, strandkorb.jpg

### 2. Interaktive Kacheln / Cards auf Unterseiten
- Produktkarten müssen INTERAKTIV sein
- Option A: Aufklappbar (Accordion-Style mit Details, Maßen, Vorteilen)
- Option B: Klick führt zu Detail-Abschnitt oder Modal
- Jede Produktkategorie braucht mindestens 3-4 Unterpunkte mit echten Inhalten
- Beispiel Glasdächer: Terrassendächer, Sommergärten, Glas-Windschutz, Haustürvordächer
- Beispiel Sonnenschutz: Markisen, Rollläden, Innenlösungen, Raffstore, Steuerungen

### 3. Dark Mode / Light Mode Toggle
- CSS `prefers-color-scheme` als Default
- Manueller Toggle-Button (Sonne/Mond Icon) in der Navigation
- Dark Mode Farben:
  - Background: #1A1A2E oder #0F0F0F
  - Text: #E8E8E8
  - Cards: #2D2D3F oder #1E1E1E
  - Accent bleibt Kupfer #C67B5C (funktioniert auf dunkel gut)
- Preference in localStorage speichern
- Smooth transition (0.3s)

### 4. Dreisprachig: Deutsch, Englisch, Plattdeutsch
- Cookie-basierter Sprachwechsel (wie andere Projekte)
- Sprachumschalter in der Navigation (DE | EN | PLT)
- Content-Dateien: content_de.json, content_en.json, content_plt.json
- Plattdeutsch (Ostfriesisches Platt) für alle Hauptseiten:
  - "Willkommen" → "Moin un welkamen"
  - "Kontakt" → "Kontakt"
  - "Über uns" → "Över uns"
  - "Karriere" → "Karriere bi uns"
  - etc.
- Navigation, Footer, alle Buttons, alle Headlines, alle Fließtexte
- Plattdeutsch soll authentisch Ostfriesisch klingen, NICHT Hamburger Platt

### 5. Impressum & Datenschutz (aus LEGAL.md)
- Lies LEGAL.md — dort stehen die echten Firmendaten
- impressum.html: Vollständiges Impressum (§5 TMG)
- datenschutz.html: Vollständige DSGVO-konforme Datenschutzerklärung
- Beide Seiten im Design der restlichen Seite
- Im Footer verlinken
- Dreisprachig (DE komplett, EN komplett, PLT: mindestens Überschriften)

### 6. Roter Faden / User Journey optimieren
- Was will der Nutzer? → Lösung für sein Zuhause finden → Beratung anfragen
- JEDE Seite braucht einen klaren CTA: "Kostenlose Beratung anfragen" oder "Rückruf vereinbaren"
- Trust-Signale auf jeder Seite: "Seit 1880 | Eigene Produktion | 2.000 m² Ausstellung"
- Breadcrumbs auf Unterseiten
- "Verwandte Produkte" am Ende jeder Produktseite
- Social Proof wo möglich (ohne Fake-Testimonials)

### 7. Moderne UX-Features
- Scroll-Progress-Bar (oben, dünn, Kupfer-Farbe)
- Back-to-Top Button (erscheint nach Scroll)
- Smooth Scroll für alle Anchor-Links
- Intersection Observer Fade-in Animationen
- Kontaktformular: Inline-Validierung, Erfolgs-Animation
- Bildergalerie auf Produktseiten mit Lightbox-Effekt (pure CSS/JS)

### 8. Server-Routes aktualisieren
- Alle neuen Seiten in server.py registrieren
- Sprachwechsel-Route: /lang/{code} setzt Cookie
- Content-JSON Dateien laden und an Templates übergeben

## Technische Regeln
- Deutsche Umlaute IMMER korrekt (ä ö ü ß) — GOLDENE REGEL
- Fonts lokal (NICHT Google CDN)
- Keine externen JS-Libraries
- Mobile-first responsive
- Alle Bilder: loading="lazy"
- Kein Hardcoding von Texten in Templates — alles aus Content-JSON
- Impressum/Datenschutz darf statisch sein (rechtliche Texte ändern sich selten)

## NACH ABSCHLUSS:
1. systemctl --user restart everwien-server
2. openclaw system event --text "Done: P18 Everwien Runde 2 complete — Dark Mode, 3 Sprachen, interaktive Cards, Impressum, Datenschutz" --mode now
