from funkce_zobrazit import zobrazit_ukoly

def odstranit_ukol(ukoly):
#Odstraní úkol podle čísla
    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return

    zobrazit_ukoly(ukoly)

    while True:
        vstup = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()

        if not vstup.isdigit():
            print("Zadejte platné číslo.")
            continue

        index = int(vstup) - 1
        if 0 <= index < len(ukoly):
            odstraneny = ukoly.pop(index)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
            break
        else:
            print("Neplatné číslo úkolu. Zkuste to znovu.")
