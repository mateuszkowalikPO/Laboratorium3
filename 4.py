przychody = []
wydatki = []

while True:
    stan_konta = sum(przychod['kwota'] for przychod in przychody) - sum(wydatek['kwota'] for wydatek in wydatki)

    print("========= MOJ BUDZET =========")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("6. Usun operacje")
    print("0. Zakoncz")
    print("==============================")

    opcja = int(input("Wybierz opcje: "))

    if opcja == 0:
        break

    elif opcja == 1:
        opis = input("Opis: ")
        kwota = float(input("Kwota: "))
        przychod = {"opis": opis, "kwota": kwota}
        przychody.append(przychod)
        print("Przychod dodany!")

    elif opcja == 2:
        opis = input("Opis: ")
        kwota = float(input("Kwota: "))
        wydatek = {"opis": opis, "kwota": kwota}
        wydatki.append(wydatek)
        print("Wydatek dodany!")

    elif opcja == 3:
        print("Historia operacji:")
        nr = 1
        for przychod in przychody:
            print(f"{nr}. Przychod: {przychod['opis']}, Kwota: {przychod['kwota']}")
            nr += 1
        for wydatek in wydatki:
            print(f"{nr}. Wydatek: {wydatek['opis']}, Kwota: {wydatek['kwota']}")
            nr += 1

    elif opcja == 4:
        print(f"Stan konta: {stan_konta}")

    elif opcja == 5:
        print("Podsumowanie finansowe:")
        print(f"Suma przychodow: {sum(przychod['kwota'] for przychod in przychody)}")
        print(f"Suma wydatkow: {sum(wydatek['kwota'] for wydatek in wydatki)}")
        print(f"bilans: {stan_konta}")
        if wydatki:
            print(f"Najwyzszy wydatek: {max(wydatek['kwota'] for wydatek in wydatki)}")
        else:
            print("Brak wydatkow do wyznaczenia najwyzszego.")

    elif opcja == 6:
        nr = 1
        wszystkie = []
        for przychod in przychody:
            print(f"{nr}. Przychod: {przychod['opis']}, Kwota: {przychod['kwota']}")
            wszystkie.append(("p", przychod))
            nr += 1
        for wydatek in wydatki:
            print(f"{nr}. Wydatek: {wydatek['opis']}, Kwota: {wydatek['kwota']}")
            wszystkie.append(("w", wydatek))
            nr += 1

        wybrany_nr = int(input("Podaj numer operacji do usuniecia: "))
        typ, operacja = wszystkie[wybrany_nr - 1]

        if typ == "p":
            przychody.remove(operacja)
        else:
            wydatki.remove(operacja)
        print("Operacja zostala usunieta.")

    else:
        print("Niepoprawna opcja.")
