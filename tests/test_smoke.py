"""P18 Everwien — Smoke + Security Tests"""
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

# --- SMOKE TESTS ---
def test_all_pages_200():
    pages = ["", "/glasdaecher", "/sonnenschutz", "/insektenschutz", "/gartenmoebel",
             "/raumdesign", "/kontakt", "/karriere", "/ueber-uns", "/faq", "/team",
             "/impressum", "/datenschutz"]
    for p in pages:
        code = curl(p)
        assert code == "200", f"{p} returned {code}"

def test_404_page():
    code = curl("/nonexistent-page-xyz")
    assert code == "404"

def test_language_switch():
    for lang in ["plt", "de", "en"]:
        code = curl(f"/lang/{lang}", "-L")
        assert code == "200", f"Language switch {lang} failed"

def test_default_language_plattdeutsch():
    body = curl_body("/")
    assert 'lang="nds"' in body, "Default should be Plattdeutsch (nds)"

def test_static_files():
    assert curl("/static/css/style.css") == "200"
    assert curl("/static/js/main.js") == "200"
    assert curl("/static/img/favicon.svg") == "200"
    assert curl("/static/img/logo.svg") == "200"

def test_seo_files():
    assert curl("/robots.txt") == "200"
    assert curl("/sitemap.xml") == "200"
    assert curl("/llms.txt") == "200"

def test_meta_tags():
    body = curl_body("/")
    assert '<meta property="og:title"' in body or "og:title" in body
    assert '<meta property="og:image"' in body
    assert 'schema.org' in body.lower() or 'json-ld' in body.lower() or 'application/ld+json' in body

def test_favicon():
    body = curl_body("/")
    assert "favicon" in body

# --- SECURITY TESTS ---
def test_security_headers():
    headers = curl_headers("/")
    assert "x-content-type-options" in headers.lower()
    assert "x-frame-options" in headers.lower()
    assert "referrer-policy" in headers.lower()

def test_no_directory_listing():
    code = curl("/static/")
    assert code in ["404", "403", "405"]

def test_path_traversal():
    code = curl("/static/../../etc/passwd")
    assert code != "200"

def test_xss_in_lang():
    code = curl('/lang/<script>alert(1)</script>')
    body = curl_body('/lang/<script>alert(1)</script>')
    assert "<script>alert" not in body

def test_no_server_version():
    headers = curl_headers("/")
    assert "uvicorn" not in headers.lower()

if __name__ == "__main__":
    import sys
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"  ✅ {t.__name__}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {t.__name__}: {e}")
            failed += 1
    print(f"\n{'='*40}\n  {passed} passed, {failed} failed / {passed+failed} total")
    sys.exit(1 if failed else 0)
