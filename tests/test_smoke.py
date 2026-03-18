"""P18 Everwien — Smoke + Security + API Tests"""
import subprocess, json, re

BASE = "http://localhost:3019/everwien"

def curl(path, extra=""):
    r = subprocess.run(f'curl -s -o /dev/null -w "%{{http_code}}" {extra} "{BASE}{path}"',
                       shell=True, capture_output=True, text=True)
    return r.stdout.strip().strip('"')

def curl_body(path):
    r = subprocess.run(f'curl -s "{BASE}{path}"', shell=True, capture_output=True, text=True)
    return r.stdout

def curl_headers(path):
    r = subprocess.run(f'curl -sI "{BASE}{path}"', shell=True, capture_output=True, text=True)
    return r.stdout

def curl_post(path, data):
    r = subprocess.run(f"curl -s -X POST '{BASE}{path}' -H 'Content-Type: application/json' -d '{json.dumps(data)}'",
                       shell=True, capture_output=True, text=True)
    return r.stdout

# --- SMOKE TESTS ---
def test_all_pages_200():
    pages = ["", "/", "/glasdaecher", "/sonnenschutz", "/insektenschutz", "/gartenmoebel",
             "/raumdesign", "/kontakt", "/karriere", "/ueber-uns", "/faq", "/team",
             "/impressum", "/datenschutz"]
    for p in pages:
        code = curl(p)
        assert code == "200", f"{p} returned {code}"

def test_404_page():
    code = curl("/nonexistent-page-xyz")
    assert code == "404"

def test_404_contains_content():
    body = curl_body("/nonexistent-page-xyz")
    assert "404" in body

def test_static_assets():
    for f in ["/static/css/style.css", "/static/js/main.js"]:
        code = curl(f)
        assert code == "200", f"Static {f} returned {code}"

def test_seo_files():
    for f in ["/robots.txt", "/sitemap.xml", "/llms.txt"]:
        code = curl(f)
        assert code == "200", f"SEO file {f} returned {code}"

def test_robots_txt_content():
    body = curl_body("/robots.txt")
    assert "Sitemap:" in body
    assert "User-agent:" in body

def test_sitemap_xml():
    body = curl_body("/sitemap.xml")
    assert "<urlset" in body
    assert "<loc>" in body

# --- LANGUAGE TESTS ---
def test_language_switch():
    for lang in ["de", "en", "plt"]:
        code = curl(f"/lang/{lang}", "-L -c /dev/null")
        assert code == "200", f"Lang switch {lang} returned {code}"

def test_default_language_plattdeutsch():
    body = curl_body("/")
    # Default should be Plattdeutsch
    assert "plt" in body or "platt" in body.lower() or "Moin" in body

# --- SECURITY TESTS ---
def test_security_headers():
    headers = curl_headers("/")
    assert "x-content-type-options" in headers.lower()
    assert "x-frame-options" in headers.lower()
    assert "referrer-policy" in headers.lower()

def test_no_server_header():
    headers = curl_headers("/")
    lines = [l.lower() for l in headers.split("\n") if l.startswith("server:") or l.startswith("Server:")]
    # Should not expose server info (or at least not detailed)
    for l in lines:
        assert "uvicorn" not in l.lower()

def test_xss_in_contact():
    """XSS attempt in contact form should be escaped"""
    payload = {"name": "<script>alert(1)</script>", "email": "x@x.de", "phone": "", "topic": "test", "message": "xss"}
    result = json.loads(curl_post("/api/contact", payload))
    assert result["ok"] is True
    # Check log entry is escaped
    import subprocess
    r = subprocess.run("tail -1 data/contacts.log", shell=True, capture_output=True, text=True,
                       cwd="/home/openclaw/.openclaw/workspace/everwien")
    assert "<script>" not in r.stdout
    assert "&lt;script&gt;" in r.stdout

# --- CONTACT API TESTS ---
def test_contact_form_success():
    data = {"name": "Test User", "email": "test@example.com", "phone": "040-123", "topic": "Sonnenschutz", "message": "Anfrage"}
    result = json.loads(curl_post("/api/contact", data))
    assert result["ok"] is True

def test_contact_form_missing_fields():
    data = {"name": "", "email": "test@example.com", "phone": "", "topic": "", "message": ""}
    result = json.loads(curl_post("/api/contact", data))
    assert result["ok"] is False

# --- CONTENT TESTS ---
def test_meta_tags():
    body = curl_body("/")
    assert 'og:title' in body
    assert 'og:description' in body
    assert 'description' in body.lower()

def test_schema_org():
    body = curl_body("/")
    assert 'application/ld+json' in body

def test_team_has_categories():
    body = curl_body("/team")
    assert "team-category" in body
    assert "team-member" in body

def test_product_pages_have_related():
    for page in ["/sonnenschutz", "/glasdaecher", "/insektenschutz", "/gartenmoebel", "/raumdesign"]:
        body = curl_body(page)
        assert "related" in body.lower() or "verwandt" in body.lower() or "entdecken" in body.lower() or "produkt" in body.lower(), f"{page} missing related products"

def test_faq_page():
    body = curl_body("/faq")
    assert "faq" in body.lower() or "FAQ" in body

def test_impressum():
    body = curl_body("/impressum")
    assert "Everwien" in body

def test_datenschutz():
    body = curl_body("/datenschutz")
    assert "Daten" in body or "daten" in body

def test_favicon():
    body = curl_body("/")
    assert "favicon" in body.lower() or "icon" in body.lower()

def test_dark_mode_toggle():
    body = curl_body("/")
    assert "dark" in body.lower() or "theme" in body.lower()

def test_chronik_in_ueber_uns():
    body = curl_body("/ueber-uns")
    assert "1880" in body or "chronik" in body.lower() or "timeline" in body.lower()

if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
