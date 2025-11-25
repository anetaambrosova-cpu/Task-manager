from db import pripojeni_db

def zobrazit_ukoly():

    conn, cursor = pripojeni_db()
    if conn is None:
        print("Nelze zobrazit úkoly – připojení k DB selhalo.")
        return
    
    try:
        # Načtení všech úkolů z databáze
        cursor.execute("SELECT id, nazev, popis, stav, datum_vytvoreni FROM ukoly")
        ukoly = cursor.fetchall()

    #Zobrazí všechny úkoly
        if not ukoly:
            print("Žádné úkoly k zobrazení.")
            return

        print("\n Seznam úkolů:")
        for idx, ukol in enumerate(ukoly, start=1):
            print(f"{idx}. {ukol['nazev']}: {ukol['popis']} | Stav: {ukol['stav']} | Vytvořeno: {ukol['datum_vytvoreni']}")

    except Exception as e:
        print("Chyba při načítání úkolů z DB:", e)
    finally:
        cursor.close()
        conn.close()