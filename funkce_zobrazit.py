def zobrazit_ukoly(ukoly):
    #Zobrazí všechny úkoly
    if not ukoly:
        print("Žádné úkoly k zobrazení.")
        return

    print("\n Seznam úkolů:")
    for i, u in enumerate(ukoly, start=1):
        print(f"{i}. {u['nazev']} — {u['popis']}")
    print()
