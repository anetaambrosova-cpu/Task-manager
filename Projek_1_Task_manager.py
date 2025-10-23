ukoly = []

def hlavni_menu():
    while True:
        print("Správce úkolu - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()
        if volba not in ('1', '2', '3', '4'):
            print("Neplatná volba: zadejte prosím číslo 1-4.")
            continue

# Volba 1 přidání nového úkolu
        if volba == '1':   
            while True: 
                novy_ukol = input("Zadejte název úkolu: ").strip()
                if not novy_ukol:
                    print("Chyba: Název úkolu nesmí být prázdný. Zkuste to znovu.")
                    continue
                else:
                    break

            while True:
                popis_ukolu = input("Zadejte popis úkolu: ").strip()
                if not popis_ukolu:
                    print("Chyba: Popis úkolu nesmí být prázdný. Zkuste to znovu")
                    continue
                else:
                    break
            
            ukoly.append((novy_ukol, popis_ukolu))
            print(f"Úkol '{novy_ukol}' byl přidán.")
            

        elif volba == '2':
            if ukoly:
                print("Seznam úkolů:")
                for index, (novy_ukol, popis_ukolu) in enumerate(ukoly, start=1):
                    print(f"{index}. {novy_ukol}: {popis_ukolu}")
#            else:
#               print("Žádné úkoly k zobrazení.")


        elif volba == '3':
            if ukoly:
                print("Seznam úkolů:")
                for index, (novy_ukol, popis_ukolu) in enumerate(ukoly, start=1):
                    print(f"{index}. {novy_ukol}: {popis_ukolu}")
                index_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
                if 0 <= index_ukolu < len(ukoly):
                    odstraneny_ukol = ukoly.pop(index_ukolu)
                    print(f"Úkol '{odstraneny_ukol[0]}' byl odstraněn.")
                else:
                    print("Neplatné číslo úkolu.")
#            else:
#                print("Žádné úkoly k odstranění.")

        elif volba == '4':
            print("Konec programu.")
            break

hlavni_menu()
    