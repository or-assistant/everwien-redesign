"""P18 — Everwien Sonnenschutz & Raumdesign Redesign — Port 3019"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import HTMLResponse
import uvicorn, os, json, datetime, html as html_mod, hashlib, secrets
from pydantic import BaseModel, EmailStr
from typing import Optional

SITE_PASSWORD = "everwien26"

BASE_PATH = os.environ.get("BASE_PATH", "/everwien")
app = FastAPI(docs_url=None, redoc_url=None)
app.mount(f"{BASE_PATH}/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Load content files ---
CONTENT = {}
for lang_code in ("plt", "de", "en"):
    with open(f"content_{lang_code}.json", "r", encoding="utf-8") as f:
        CONTENT[lang_code] = json.load(f)

DEFAULT_LANG = "plt"

def get_lang(request: Request) -> str:
    lang = request.cookies.get("lang", DEFAULT_LANG)
    if lang not in CONTENT:
        lang = DEFAULT_LANG
    return lang

def ctx(request, **kwargs):
    lang = get_lang(request)
    t = CONTENT[lang]
    return {"request": request, "base_path": BASE_PATH, "t": t, "lang": lang, **kwargs}

# --- Password Protection ---
AUTH_COOKIE = "everwien_auth"
AUTH_TOKEN = hashlib.sha256(SITE_PASSWORD.encode()).hexdigest()[:32]

LOGIN_HTML = """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Everwien — Zugang</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{min-height:100vh;display:flex;align-items:center;justify-content:center;
font-family:system-ui,sans-serif;background:#f5f0eb;color:#2D3436}.login{background:#fff;padding:48px 40px;border-radius:16px;
box-shadow:0 4px 24px rgba(0,0,0,.08);text-align:center;max-width:400px;width:90%}h1{font-size:1.5rem;margin-bottom:8px}
p{color:#666;margin-bottom:24px;font-size:.95rem}input{width:100%;padding:14px 16px;border:2px solid #e0d8d0;border-radius:8px;
font-size:1rem;margin-bottom:16px;outline:none;transition:border .2s}input:focus{border-color:#6B7F5E}
button{width:100%;padding:14px;background:#6B7F5E;color:#fff;border:none;border-radius:8px;font-size:1rem;font-weight:600;
cursor:pointer;transition:background .2s}button:hover{background:#5a6e4f}.error{color:#c0392b;font-size:.85rem;margin-bottom:12px;display:none}</style></head>
<body><div class="login"><h1>🔒 Zugang</h1><p>Diese Seite ist passwortgeschützt.</p>
<form method="POST"><div class="error" id="err">Falsches Passwort</div>
<input type="password" name="password" placeholder="Passwort eingeben" autofocus required>
<button type="submit">Eintreten</button></form></div>
<script>if(location.search.includes('wrong'))document.getElementById('err').style.display='block'</script></body></html>"""

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    path = request.url.path
    if path.startswith(f"{BASE_PATH}/static") or path == f"{BASE_PATH}/auth":
        return await call_next(request)
    if request.cookies.get(AUTH_COOKIE) == AUTH_TOKEN:
        return await call_next(request)
    if request.method == "POST" and "password" in (await request.form()):
        form = await request.form()
        if form.get("password") == SITE_PASSWORD:
            response = RedirectResponse(url=path or f"{BASE_PATH}/", status_code=303)
            response.set_cookie(AUTH_COOKIE, AUTH_TOKEN, max_age=60*60*24*30, path="/", samesite="lax", httponly=True)
            return response
        return RedirectResponse(url=f"{path}?wrong=1", status_code=303)
    return HTMLResponse(LOGIN_HTML)

# --- Security Headers Middleware ---
@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    response.headers["Server"] = "Everwien"
    return response

# --- Language switch ---
@app.get(f"{BASE_PATH}/lang/{{code}}")
async def switch_lang(request: Request, code: str):
    if code not in CONTENT:
        code = DEFAULT_LANG
    referer = request.headers.get("referer", f"{BASE_PATH}/")
    response = RedirectResponse(url=referer, status_code=303)
    response.set_cookie("lang", code, max_age=60*60*24*365, path="/", samesite="lax")
    return response

# --- Pages ---
@app.get(f"{BASE_PATH}/")
@app.get(f"{BASE_PATH}")
async def index(request: Request):
    return templates.TemplateResponse("index.html", ctx(request))

@app.get(f"{BASE_PATH}/glasdaecher")
async def glasdaecher(request: Request):
    return templates.TemplateResponse("glasdaecher.html", ctx(request))

@app.get(f"{BASE_PATH}/sonnenschutz")
async def sonnenschutz(request: Request):
    return templates.TemplateResponse("sonnenschutz.html", ctx(request))

@app.get(f"{BASE_PATH}/insektenschutz")
async def insektenschutz(request: Request):
    return templates.TemplateResponse("insektenschutz.html", ctx(request))

@app.get(f"{BASE_PATH}/gartenmoebel")
async def gartenmoebel(request: Request):
    return templates.TemplateResponse("gartenmoebel.html", ctx(request))

@app.get(f"{BASE_PATH}/raumdesign")
async def raumdesign(request: Request):
    return templates.TemplateResponse("raumdesign.html", ctx(request))

@app.get(f"{BASE_PATH}/kontakt")
async def kontakt(request: Request):
    return templates.TemplateResponse("kontakt.html", ctx(request))

@app.get(f"{BASE_PATH}/karriere")
async def karriere(request: Request):
    return templates.TemplateResponse("karriere.html", ctx(request))

@app.get(f"{BASE_PATH}/ueber-uns")
async def ueber_uns(request: Request):
    return templates.TemplateResponse("ueber-uns.html", ctx(request))

@app.get(f"{BASE_PATH}/team")
async def team(request: Request):
    return templates.TemplateResponse("team.html", ctx(request))

@app.get(f"{BASE_PATH}/faq")
async def faq(request: Request):
    return templates.TemplateResponse("faq.html", ctx(request))

@app.get(f"{BASE_PATH}/impressum")
async def impressum(request: Request):
    return templates.TemplateResponse("impressum.html", ctx(request))

@app.get(f"{BASE_PATH}/datenschutz")
async def datenschutz(request: Request):
    return templates.TemplateResponse("datenschutz.html", ctx(request))

# --- Contact Form ---
class ContactForm(BaseModel):
    name: str
    email: str
    phone: Optional[str] = ""
    topic: str
    message: str

CONTACTS_LOG = os.path.join(os.path.dirname(__file__), "data", "contacts.log")
os.makedirs(os.path.dirname(CONTACTS_LOG), exist_ok=True)

@app.post(f"{BASE_PATH}/api/contact")
async def contact_submit(form: ContactForm):
    # Sanitize
    safe = {k: html_mod.escape(str(v).strip())[:2000] for k, v in form.dict().items()}
    if not safe["name"] or not safe["email"] or not safe["message"]:
        return {"ok": False, "error": "Missing fields"}
    entry = {**safe, "ts": datetime.datetime.utcnow().isoformat()}
    with open(CONTACTS_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return {"ok": True}

# --- 404 Handler ---
@app.exception_handler(StarletteHTTPException)
async def custom_404(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("404.html", ctx(request), status_code=404)
    return Response(content=str(exc.detail), status_code=exc.status_code)

# --- SEO files ---
@app.get(f"{BASE_PATH}/robots.txt")
async def robots():
    with open("static/robots.txt") as f:
        return Response(content=f.read(), media_type="text/plain")

@app.get(f"{BASE_PATH}/sitemap.xml")
async def sitemap():
    with open("static/sitemap.xml") as f:
        return Response(content=f.read(), media_type="application/xml")

@app.get(f"{BASE_PATH}/llms.txt")
async def llms():
    with open("static/llms.txt") as f:
        return Response(content=f.read(), media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=3019, reload=True, server_header=False)
