from db import pripojeni_db

def aktualizovat_ukol():
   
   
    conn, cursor = pripojeni_db()
    if conn is None:
        print("Nelze aktualizovat úkol – připojení k DB selhalo.")
        return

    try:
        # Načteme aktuální úkoly (id, nazev, stav)
        cursor.execute("SELECT id, nazev, stav FROM ukoly ORDER BY id")
        ukoly = cursor.fetchall()

        if not ukoly:
            print("Žádné úkoly k aktualizaci.")
            return

        # Vypíšeme úkoly pro přehled (id, název, stav)
        print("\nSeznam úkolů:")
        for u in ukoly:
            print(f"{u['id']}. {u['nazev']} | Stav: {u['stav']}")

        # Výběr ID úkolu
        while True:
            vstup = input("\nZadejte ID úkolu, který chcete aktualizovat: ").strip()
            if not vstup.isdigit():
                print("Chyba: zadejte platné číselné ID.")
                continue

            id_zvolene = int(vstup)
            # ověření, že ID existuje v poli ukoly
            vybrany = None
            for u in ukoly:
                if u['id'] == id_zvolene:
                    vybrany = u
                    break

            if vybrany is None:
                print("Úkol s tímto ID neexistuje. Zkuste to znovu.")
                continue
            break

        # Nabídka nového stavu
        print("\nVyberte nový stav úkolu:")
        print("1) Probíhá")
        print("2) Hotovo")

        while True:
            volba = input("Volba (1-2): ").strip()
            if volba == "1":
                novy_stav = "probíhá"
                break
            elif volba == "2":
                novy_stav = "hotovo"
                break
            else:
                print("Neplatná volba. Zadejte 1 nebo 2.")

        # Potvrzení změny
        potvrzeni = input(f"Opravdu změnit stav úkolu '{vybrany['nazev']}' (ID {vybrany['id']}) na '{novy_stav}'? (a/n): ").strip().lower()
        if potvrzeni not in ("a", "y", "ano", "yes"):
            print("Aktualizace zrušena uživatelem.")
            return

        # Provedeme update
        sql = "UPDATE ukoly SET stav = %s WHERE id = %s"
        cursor.execute(sql, (novy_stav, id_zvolene))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Úspěšně aktualizováno: '{vybrany['nazev']}' nyní má stav '{novy_stav}'.")
        else:
            print("Aktualizace se nezdařila (řádek nebyl nalezen nebo nebyla změna).")

    except Exception as e:
        print("Chyba při aktualizaci úkolu:", e)
    finally:
        cursor.close()
        conn.close()
