import db

def pridat_ukol(title: str, description: str) -> int:
    conn, cursor = db.pripojeni_db()
    if conn is None:
        raise RuntimeError("Nelze se připojit k DB")
    try:
        cursor.execute(
            "INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)",
            (title, description)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()


def zobrazit_ukoly(task_id: int):
    conn, cursor = db.pripojeni_db()
    if conn is None:
        raise RuntimeError("Nelze se připojit k DB")
    try:
        cursor.execute("SELECT * FROM ukoly WHERE id = %s", (task_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


def aktualizovat_ukol(task_id: int, new_status: str) -> bool:
    conn, cursor = db.pripojeni_db()
    if conn is None:
        raise RuntimeError("Nelze se připojit k DB")
    try:
        cursor.execute("UPDATE ukoly SET stav = %s WHERE id = %s", (new_status, task_id))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()


def odstranit_ukol(task_id: int) -> bool:
    conn, cursor = db.pripojeni_db()
    if conn is None:
        raise RuntimeError("Nelze se připojit k DB")
    try:
        cursor.execute("DELETE FROM ukoly WHERE id = %s", (task_id,))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()
