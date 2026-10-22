while True:
    print("\n========== KALKULATOR ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("0. Zakoncz")
    print("================================")

    opcja = int(input("Wybierz opcje: "))

    if opcja == 0:
        break

    elif opcja == 1:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        wynik = liczba1 + liczba2
        print(f"{liczba1} + {liczba2} = {wynik}")

    elif opcja == 2:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        wynik = liczba1 - liczba2
        print(f"{liczba1} - {liczba2} = {wynik}")

    elif opcja == 3:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        wynik = liczba1 * liczba2
        print(f"{liczba1} * {liczba2} = {wynik}")

    elif opcja == 4:
        liczba1 = int(input("Pierwsza liczba: "))
        liczba2 = int(input("Druga liczba: "))
        wynik = liczba1 / liczba2
        print(f"{liczba1} / {liczba2} = {wynik}")

    elif opcja == 5:
        liczba1 = int(input("Podstawa: "))
        liczba2 = int(input("Wykladnik: "))
        wynik = liczba1 ** liczba2
        print(f"{liczba1} ^ {liczba2} = {wynik}")

    elif opcja == 6:
        ilosc_liczb = int(input("Ile liczb: "))
        liczby_srednia = []
        if ilosc_liczb > 0:
            for i in range(ilosc_liczb):
                liczba = int(input(f"Liczba {i+1}: "))
                liczby_srednia.append(liczba)

            wynik = sum(liczby_srednia) / len(liczby_srednia)
            print(f"Srednia z {ilosc_liczb} liczb = {wynik}")
        else:
            print("Bład")

