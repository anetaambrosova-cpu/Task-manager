ukoly = []

def pridat_ukol(ukoly):
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

    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl úspěšně přidán.")
