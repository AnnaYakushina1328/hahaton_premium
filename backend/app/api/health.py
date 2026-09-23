from fastapi import APIRouter
from sqlalchemy import text

from app.config import settings
from app.database.db import engine


router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("")
def health():
    return {
        "ok": True,
        "service": "arena-negotiations",
        "version": settings.app_version,
    }


@router.get("/database")
def database_health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "ok": True,
        "database": "connected",
    }
