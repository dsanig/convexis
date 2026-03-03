from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from sqlalchemy.orm import Session

from .config import get_settings
from .db import get_db

settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.get('/api/health')
def health() -> dict[str, str]:
    return {"status": "ok", "app": settings.app_name, "env": settings.environment}


@app.get('/api/health/db')
def health_db(db: Session = Depends(get_db)) -> dict[str, str]:
    db.execute(text('SELECT 1'))
    return {"status": "ok", "database": settings.db_name}


web_dist = Path(__file__).resolve().parents[2] / 'web' / 'dist'
if web_dist.exists():
    app.mount('/assets', StaticFiles(directory=web_dist / 'assets'), name='assets')

    @app.get('/{full_path:path}')
    def serve_spa(full_path: str) -> FileResponse:
        target = web_dist / full_path
        if target.exists() and target.is_file():
            return FileResponse(target)
        return FileResponse(web_dist / 'index.html')
