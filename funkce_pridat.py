from db import pripojeni_db


def pridat_ukol():

    conn, cursor = pripojeni_db()
    if conn is None:
        print("Nelze přidat úkol – připojení k DB selhalo.")
        return

    #Přidá nový úkol do seznamu.
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný.")
            continue
        break

    while True:
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný.")
            continue
        break

    try:
        sql = "INSERT INTO ukoly (nazev, popis, stav) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nazev, popis, 'nezahájeno'))
        conn.commit()
        print(f"Úkol '{nazev}' byl úspěšně přidán do databáze.")
    except Exception as e:
        print("Chyba při přidávání úkolu do DB:", e)
    finally:
        cursor.close()
        conn.close()