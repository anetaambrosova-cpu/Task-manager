from funkce_zobrazit import zobrazit_ukoly
from db import pripojeni_db

def odstranit_ukol():
    conn, cursor = pripojeni_db()

    if conn is None:
        print("Nelze odstranit úkol – připojení k DB selhalo.")
        return()

    try:
        # Načtení všech úkolů z databáze
        cursor.execute("SELECT id, nazev, popis, stav FROM ukoly")
        ukoly = cursor.fetchall()
 
#Odstraní úkol podle čísla
        if not ukoly:
            print("Žádné úkoly k odstranění.")
            return

# zobrazení úkolů s čísly
        zobrazit_ukoly()
    
# výběr úkolu k odstranění
        while True:
            vstup = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()

            if not vstup.isdigit():
                print("Zadejte platné číslo.")
                continue        

            index = int(vstup) - 1
            if 0 <= index < len(ukoly):
                sql = "DELETE FROM ukoly WHERE id=%s"
                cursor.execute(sql, (ukoly[index]['id'],))
                conn.commit()
                print(f"Úkol '{ukoly[index]['nazev']}' byl odstraněn z databáze.")
                break
            else:
                print("Neplatné číslo úkolu. Zkuste to znovu.")

    except Exception as e:
        print("Chyba při odstraňování úkolu:", e)
    finally:
        cursor.close()
        conn.close()