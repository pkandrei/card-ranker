from fastapi import FastAPI

from app.settings import get_settings

title = get_settings().app_name
app = FastAPI(title=title)


@app.get("/health")
def health():
    return {"status": "ok"}
