"""P18 — Everwien Sonnenschutz & Raumdesign Redesign — Port 3019"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn, os

BASE_PATH = os.environ.get("BASE_PATH", "/everwien")
app = FastAPI(docs_url=None, redoc_url=None)
app.mount(f"{BASE_PATH}/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def ctx(request, **kwargs):
    return {"request": request, "base_path": BASE_PATH, **kwargs}

@app.get(f"{BASE_PATH}/")
@app.get(f"{BASE_PATH}")
async def index(request: Request):
    return templates.TemplateResponse("index.html", ctx(request))

# Sub-pages will be added by the agent

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=3019, reload=True)
