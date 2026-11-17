from fastapi import FastAPI

from app.settings import get_settings
from app.version import get_version

title = get_settings().app_name
version = get_version()
app = FastAPI(title=title, version=version)


@app.get("/health")
def health():
    return {"status": "ok"}
