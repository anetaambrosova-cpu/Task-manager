from app_crud import pridat_ukol, zobrazit_ukoly, aktualizovat_ukol, odstranit_ukol
from db import pripojeni_db

# -------------------- Přidání úkolu --------------------
def test_create_task_positive():
    tid = pridat_ukol("TestTitle", "TestDesc")
    assert isinstance(tid, int) and tid > 0
    row = zobrazit_ukoly(tid)
    assert row is not None
    assert row['nazev'] == "TestTitle"

def test_create_task_negative_db_unavailable(monkeypatch):
    import db
    monkeypatch.setattr(db, "pripojeni_db", lambda: (None, None))
    try:
        try:
            pridat_ukol("X","Y")
            assert False, "mělo vyhodit RuntimeError"
        except RuntimeError:
            pass
    finally:
        pass

# -------------------- Aktualizace úkolu --------------------
def test_update_task_positive():
    tid = pridat_ukol("UpTitle","UpDesc")
    ok = aktualizovat_ukol(tid, "hotovo")
    assert ok is True
    row = zobrazit_ukoly(tid)
    assert row['stav'] == "hotovo"

def test_update_task_negative_nonexistent():
    ok = aktualizovat_ukol(9999999, "hotovo")
    assert ok is False

# -------------------- Odstranění úkolu --------------------
def test_delete_task_positive():
    tid = pridat_ukol("DelTitle","DelDesc")
    ok = odstranit_ukol(tid)
    assert ok is True
    assert zobrazit_ukoly(tid) is None

def test_delete_task_negative_nonexistent():
    ok = odstranit_ukol(9999999)
    assert ok is False
