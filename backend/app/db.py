from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

from app.config import settings

engine = create_engine(settings.database_url, connect_args={"connect_timeout": 3})


def check_db() -> bool:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except OperationalError:
        return False
