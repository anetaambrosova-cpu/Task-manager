import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent 
sys.path.insert(0, str(ROOT))

import pytest
from db import pripojeni_db

@pytest.fixture(autouse=True)
def clean_table():
    conn, cursor = pripojeni_db()
    if conn is None:
        pytest.skip("DB nedostupná")
    try:
        cursor.execute("DELETE FROM ukoly")
        conn.commit()
        yield
    finally:
     
        cursor.execute("DELETE FROM ukoly")
        conn.commit()
        cursor.close()
        conn.close()
