# P18 — Everwien Sonnenschutz & Raumdesign — Komplettes Redesign

## Firmen-Daten (aus Analyse)
- **Name:** Sonnenschutz & Raumdesign Everwien
- **Standort:** Norden (Ostfriesland), Niedersachsen
- **Gegründet:** 1880 (145+ Jahre Tradition!)
- **Ausstellung:** 2.000 m² Musterausstellung
- **Slogan aktuell:** "Ihr Hersteller aus Norden seit 1880"
- **Branche:** Sonnenschutz, Glasdächer, Terrassenüberdachungen, Raumdesign, Gartenmöbel
- **Typ:** Handwerksbetrieb mit eigener Produktion
- **Hosting aktuell:** CM4all/web4business Baukasten (komplett JS-gerendert, kein SSR, schlechtes SEO)
- **Zielgruppe:** Hauseigentümer + kleine Firmen, mittleres bis hohes Preissegment

## Produktkategorien (32 Seiten in Sitemap)

### Glasdächer & Überdachungen
- Terrassendächer
- Sommergärten
- Glas-Windschutz
- Haustürvordächer

### Sonnenschutz
- Markisen
- Rollläden
- Innenlösungen (Plissees, Jalousien)
- Raffstore
- Steuerungen (Smart Home Integration)

### Insektenschutz
- Verschiedene Modelle für Fenster und Türen

### Gartenmöbel
- Metall, Holz & Kunststoff
- Outdoormöbel
- Loungemöbel
- Indoormöbel
- Strandkörbe (Ostfriesland!)
- Sonnenschirme

### Raum & Design
- Gardinen
- Flächenvorhänge
- Wohnaccessoires

### Service
- Partner-Seite
- Kontakt
- Karriere
- Rückrufservice
- Anfrage-Formular
- Anfahrt
- Chronik (Firmengeschichte)
- Downloads

## Bilder (in static/img/)
- hero-terrace.jpg (1920px, Hero Terrasse)
- glasdach.jpg (Wintergarten/Glasdach)
- markise.jpg (Markise)
- terrasse.jpg (elegante Terrasse)
- gartenmoebel.jpg (Gartenmöbel)
- raumdesign.jpg (Interior Design)
- fenster.jpg (Fenster/Insektenschutz)
- team.jpg (Handwerker/Team)
- strandkorb.jpg (Strandkorb)

## Design-Anforderungen

### Farbkonzept (NEU — Premium Handwerk)
- **Primary:** Warmes Anthrazit #2D3436 (Eleganz, Handwerk)
- **Accent:** Warmes Kupfer/Terrakotta #C67B5C (Wärme, Handwerk, Erde)
- **Secondary:** Olivgrün #6B7F5E (Natur, Garten, Nachhaltigkeit)
- **Background:** Warmes Off-White #FAF8F5 (nicht kalt-weiß)
- **Text:** #1A1A1A (Haupttext), #6B7280 (Sekundärtext)
- **Akzent-Hell:** #F5EDE8 (Kupfer-tint Background)

### Typografie
- Headlines: "Outfit" oder "Plus Jakarta Sans" (modern, warm, nicht kalt-technisch)
- Body: Inter (bewährt, lesbar)
- Lokal laden (DSGVO!)

### Logo-Entwurf (SVG)
Erstelle ein neues, modernes Logo:
- "EVERWIEN" als Wortmarke (clean, spacious letter-spacing)
- Darunter kleiner: "Sonnenschutz & Raumdesign · seit 1880"
- Optionales Icon: abstrahiertes Dach/Sonnenstrahlen (geometrisch, minimal)
- Farben: Anthrazit + Kupfer-Akzent

## Seitenstruktur

### 1. Startseite (index.html)
- **Hero:** Vollbild-Foto (hero-terrace.jpg) mit Overlay
  - "Ihr Zuhause. Perfekt geschützt." (Headline)
  - "Sonnenschutz, Glasdächer & Raumdesign aus Ostfriesland. Seit 1880." (Subtitle)
  - CTA: "Kostenlose Beratung anfragen" + "Ausstellung besuchen"
- **Vertrauensleiste:** "Seit 1880 | 2.000 m² Ausstellung | Eigene Produktion | Kostenlose Beratung"
- **Leistungen:** Bento-Grid mit 5 Hauptkategorien (Glasdächer, Sonnenschutz, Insektenschutz, Gartenmöbel, Raum & Design)
- **Warum Everwien:** 3 Spalten (Eigene Produktion, 145 Jahre Erfahrung, Beratung vor Ort)
- **Referenz-Galerie:** 4-6 Projekt-Bilder als Grid
- **FAQ-Section:** 8-10 häufige Fragen (Accordion)
- **Kontakt-Teaser:** Karte + Schnellkontakt + Öffnungszeiten
- **Karriere-Teaser:** "Werde Teil unseres Teams" Banner

### 2. Unterseiten (jeweils eigenes Template)

**Produktseiten** (glasdaecher.html, sonnenschutz.html, insektenschutz.html, gartenmoebel.html, raumdesign.html):
- Sub-Hero mit Kategorie-Bild
- Produktübersicht als Cards
- Vorteile/Features als Icons
- CTA: "Jetzt beraten lassen"
- Verwandte Kategorien

**kontakt.html:**
- Kontaktformular mit: Name, E-Mail, Telefon, **Thema-Dropdown** (Glasdächer, Sonnenschutz, Insektenschutz, Gartenmöbel, Raumdesign, Karriere, Sonstiges), Nachricht, Datei-Upload
- Karte (Openstreetmap Embed oder statisch)
- Öffnungszeiten
- Rückrufservice-Option
- Anfahrtsbeschreibung

**karriere.html:**
- "Handwerk mit Zukunft" — Storytelling
- Vorteile als Arbeitgeber (Tradition + Innovation, Teamgröße, Region Ostfriesland)
- Aktuelle Stellen (Platzhalter: Monteur/in, Auszubildende/r, Verkaufsberater/in)
- Initiativbewerbung-Formular
- Team-Foto

**ueber-uns.html:**
- Chronik: Timeline von 1880 bis heute
- Werte: Qualität, Regionalität, Nachhaltigkeit
- Team / Musterausstellung
- Partner / Hersteller

**faq.html:**
- Umfassende FAQ-Seite (15-20 Fragen)
- Kategorisiert: Glasdächer, Sonnenschutz, Service, Bestellung
- Typische Fragen:
  - "Was kostet eine Terrassenüberdachung?"
  - "Wie lange dauert die Montage?"
  - "Bieten Sie Finanzierung an?"
  - "Kann ich die Ausstellung ohne Termin besuchen?"
  - "Liefern Sie auch außerhalb Ostfrieslands?"
  - "Welche Garantie erhalte ich?"
  - "Wie pflege ich meine Markise?"
  - "Kann ich Sonnenschutz nachrüsten?"
  - "Bieten Sie Smart-Home-Steuerungen an?"
  - "Was ist der Unterschied zwischen Wintergarten und Sommergarten?"

### 3. Interaktive Features
- Smooth scroll
- Intersection Observer Fade-in
- FAQ Accordion (pure CSS/JS)
- Sticky Nav mit Blur
- Kontaktformular mit Validierung
- Lazy Loading auf allen Bildern
- Mobile: Hamburger-Menü mit Slide-in

### 4. SEO (Goldene Regeln!)
- Title: "Everwien Sonnenschutz & Raumdesign | Glasdächer, Markisen & mehr | Norden/Ostfriesland"
- Meta Description mit lokalen Keywords
- Schema.org: LocalBusiness + Product
- Geo-Tags: Norden, Niedersachsen
- hreflang: de
- Sitemap.xml
- robots.txt
- llms.txt
- OG-Image (1200x630)

## Technische Regeln
- FastAPI + Jinja2 SSR, Port 3019, BASE_PATH=/everwien
- Deutsche Umlaute IMMER korrekt (ä ö ü ß) — GOLDENE REGEL
- Fonts lokal (NICHT Google CDN)
- Keine externen JS-Libraries
- Mobile-first responsive
- Alle Bilder: loading="lazy"
- Security Headers

NACH ABSCHLUSS:
1. systemctl --user restart everwien-server
2. openclaw system event --text "Done: P18 Everwien Redesign complete — 7 Seiten, Logo, FAQ, Kontaktformular, Karriere, Bento-Grid" --mode now
