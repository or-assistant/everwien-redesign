"""P18 — Everwien Sonnenschutz & Raumdesign Redesign — Port 3019"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import uvicorn, os, json

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

# --- Security Headers Middleware ---
@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
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
    uvicorn.run("server:app", host="0.0.0.0", port=3019, reload=True)
