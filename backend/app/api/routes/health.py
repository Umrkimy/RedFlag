from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.core.db import check_db

router = APIRouter()


@router.get("/health")
def health():
    db = check_db()

    if not db:
        return JSONResponse(
            status_code=503,
            content={"status": "unhealthy", "db": "error"},
        )

    return {"status": "ok", "db": "ok"}
