def konwerter_jednostek():
    jednostki = {
        "dlugosc": {
            "metry": 1,
            "centymetry": 0.01,
            "milimetry": 0.001,
            "cale": 0.0254,
            "stopy": 0.3048,
            "jardy": 0.9144,
            "kilometry": 1000,
            "mile": 1609.34
        },
        "waga": {
            "kilogramy": 1,
            "dekagramy": 0.1,
            "gramy": 0.001,
            "miligramy": 0.000001,
            "uncje": 0.0283495,
            "funty": 0.453592,
            "tony": 1000
        }
    }

    kategoria = input("Podaj kategorię jednostek (np. 'dlugosc', 'waga'): ")
    if kategoria not in jednostki:
        print("Nieprawidłowa kategoria")
        return

    jednostka_wejsciowa = input("Podaj jednostkę wejściową: ")
    if jednostka_wejsciowa not in jednostki[kategoria]:
        print("Nieprawidłowa jednostka wejściowa")
        return

    jednostka_wyjsciowa = input("Podaj jednostkę wyjściową: ")
    if jednostka_wyjsciowa not in jednostki[kategoria]:
        print("Nieprawidłowa jednostka wyjściowa")
        return

    wartosc_wejsciowa = float(input("Podaj wartość wejściową: "))

    wartosc_wyjsciowa = wartosc_wejsciowa * jednostki[kategoria][jednostka_wejsciowa] / jednostki[kategoria][jednostka_wyjsciowa]
    print(f"{wartosc_wejsciowa} {jednostka_wejsciowa} to {wartosc_wyjsciowa} {jednostka_wyjsciowa}")


if __name__ == "__main__":
    konwerter_jednostek()