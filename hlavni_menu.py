from funkce_pridat import pridat_ukol
from funkce_zobrazit import zobrazit_ukoly
from funkce_odstranit import odstranit_ukol
from funkce_ukoncit import ukoncit_program

ukoly = []


def hlavni_menu():
    #Zobrazí hlavní menu a volá příslušné funkce.
    while True:
        print("\n📘 Správce úkolů")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1–4): ").strip()

        if volba == "1":
            pridat_ukol(ukoly)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
        elif volba == "3":
            odstranit_ukol(ukoly)
        elif volba == "4":
            ukoncit_program()
        else:
            print("Neplatná volba. Zadejte číslo 1–4.")


if __name__ == "__main__":
    hlavni_menu()
