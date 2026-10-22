ksiazki = []

while True:
    print("\n========== BIBLIOTEKA ==========")
    print("1. Dodaj ksiazke")
    print("2. Wyswietl wszystkie ksiazki")
    print("3. Wypozycz ksiazke")
    print("4. Zwroc ksiazke")
    print("5. Usun ksiazke")
    print("0. Zakoncz")
    print("===============================")

    opcja = int(input("Wybierz opcje: "))

    if opcja == 0:
        break

    elif opcja == 1:
        tytul = input("Tytul: ")
        autor = input("Autor: ")
        ksiazka = {
            "indeks": len(ksiazki) + 1,
            "tytul": tytul,
            "autor": autor,
            "wypozyczona": False,
        }
        ksiazki.append(ksiazka)
        print("Ksiazka dodana.")

    elif opcja == 2:
        for ksiazka in ksiazki:
            status = (
                "wypozyczona" if ksiazka["wypozyczona"] else "dostepna"
            )
            print(
                f"{ksiazka['indeks']}. Tytul: {ksiazka['tytul']}, Autor: {ksiazka['autor']} - {status}"
            )

    elif opcja == 3:
        indeks = int(input("Numer ksiazki: "))
        for ksiazka in ksiazki:
            if ksiazka["indeks"] == indeks:
                if not ksiazka["wypozyczona"]:
                    ksiazka["wypozyczona"] = True
                    print(f"Wypozyczono: {ksiazka['tytul']}")
                else:
                    print("Ksiazka jest juz wypozyczona.")
                break
        else:
            print("Nie znaleziono ksiazki.")

    elif opcja == 4:
        indeks = int(input("Numer ksiazki: "))
        for ksiazka in ksiazki:
            if ksiazka["indeks"] == indeks:
                if ksiazka["wypozyczona"]:
                    ksiazka["wypozyczona"] = False
                    print(f"Zwrocono: {ksiazka['tytul']}")
                else:
                    print("Ksiazka nie byla wypozyczona.")
                break
        else:
            print("Nie znaleziono ksiazki.")

    elif opcja == 5:
        indeks = int(input("Numer ksiazki do usuniecia: "))
        for ksiazka in ksiazki:
            if ksiazka["indeks"] == indeks:
                ksiazki.remove(ksiazka)
                print("Ksiazka zostala usunieta.")
                break
        else:
            print("Nie znaleziono ksiazki.")

    else:
        print("Niepoprawna opcja.")
