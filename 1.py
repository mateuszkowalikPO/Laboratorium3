kontakty = []
while True:
    print("\n========== KSIAZKA KONTAKTOW ==========")
    print("1. Dodaj kontakt")
    print("2. Wyświetl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("=======================================")
    opcja = int(input("Wybierz opcje: "))

    if opcja == 0:
        break

    elif opcja == 1:
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        telefon = input("Telefon: ")
        kontakt = {"imie": imie, "nazwisko": nazwisko, "telefon": telefon}
        kontakty.append(kontakt)
        print("Kontakt dodany")

    elif opcja == 2:
        for kontakt in kontakty:
            print(f"Imie: {kontakt['imie']}")
            print(f"Nazwisko: {kontakt['nazwisko']}")
            print(f"Telefon: {kontakt['telefon']}")
            print("=======================================")

    elif opcja == 3:
        telefon = input("Telefon: ")
        for kontakt in kontakty:
            if kontakt["telefon"] == telefon:
                print(f"Imie: {kontakt['imie']}")
                print(f"Nazwisko: {kontakt['nazwisko']}")
                print(f"Telefon: {kontakt['telefon']}")
                print("=======================================")
            else:
                print("Nie znaleziono kontaktu")

    elif opcja == 4:
        telefon = input("Telefon: ")
        for kontakt in kontakty:
            if kontakt["telefon"] == telefon:
                imie = input("Imie: ")
                nazwisko = input("Nazwisko: ")
                kontakt["imie"] = imie
                kontakt["nazwisko"] = nazwisko
                print("Kontakt edytowany")
            else:
                print("Nie znaleziono kontaktu")

    elif opcja == 5:
        telefon = input("Telefon: ")
        for kontakt in kontakty:
            if kontakt["telefon"] == telefon:
                kontakty.remove(kontakt)
                print("Kontakt usuniety")
            else:
                print("Nie znaleziono kontaktu")

    else:
        print("Niepoprawna opcja")
