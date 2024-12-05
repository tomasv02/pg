def je_tah_mozny(figurka, cilove_pole, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.
    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilove_pole: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    #03.11.2024 VRBAT - implementation

    def je_na_sachovnici(pozice):
        return 1 <= pozice[0] <= 8 and 1 <= pozice[1] <= 8

    def je_volna(pozice):
        return pozice not in obsazene_pozice

    def je_cesta_volna(start, konec, smer):
        # Generuje všechny pozice mezi start a konec a kontroluje, zda jsou volné
        radek_smer, sloupec_smer = smer
        pozice = (start[0] + radek_smer, start[1] + sloupec_smer)
        while pozice != konec:
            if pozice in obsazene_pozice:
                return False
            pozice = (pozice[0] + radek_smer, pozice[1] + sloupec_smer)
        return True

    typ = figurka["typ"]
    start_pozice = figurka["pozice"]

    # Ověření, že cílová pozice je na šachovnici
    if not je_na_sachovnici(cilove_pole):
        return False

    # Pěšec
    if typ == "pěšec":
        smer = 1  # Pěšec se pohybuje směrem "nahoru" (větší čísla řádků)
        start_radek, start_sloupec = start_pozice
        cil_radek, cil_sloupec = cilove_pole
        if start_sloupec == cil_sloupec:
            if cil_radek == start_radek + smer and je_volna(cilove_pole):
                return True
            if (
                start_radek == 2 and  # Pěšec na výchozí pozici
                cil_radek == start_radek + 2 * smer and
                je_volna((start_radek + 1 * smer, start_sloupec)) and
                je_volna(cilove_pole)
            ):
                return True
        return False

    # Jezdec
    if typ == "jezdec":
        rozdil_radku = abs(cilove_pole[0] - start_pozice[0])
        rozdil_sloupce = abs(cilove_pole[1] - start_pozice[1])
        if (rozdil_radku, rozdil_sloupce) in [(2, 1), (1, 2)]:
            return je_volna(cilove_pole)
        return False

    # Věž
    if typ == "věž":
        if start_pozice[0] == cilove_pole[0]:  # Pohyb horizontálně
            smer = (0, 1 if cilove_pole[1] > start_pozice[1] else -1)
        elif start_pozice[1] == cilove_pole[1]:  # Pohyb vertikálně
            smer = (1 if cilove_pole[0] > start_pozice[0] else -1, 0)
        else:
            return False
        return je_cesta_volna(start_pozice, cilove_pole, smer) and je_volna(cilove_pole)

    # Střelec
    if typ == "střelec":
        rozdil_radku = abs(cilove_pole[0] - start_pozice[0])
        rozdil_sloupce = abs(cilove_pole[1] - start_pozice[1])
        if rozdil_radku == rozdil_sloupce:  # Pohyb diagonálně
            smer = (
                1 if cilove_pole[0] > start_pozice[0] else -1,
                1 if cilove_pole[1] > start_pozice[1] else -1,
            )
            return je_cesta_volna(start_pozice, cilove_pole, smer) and je_volna(cilove_pole)
        return False

    # Dáma
    if typ == "dáma":
        if start_pozice[0] == cilove_pole[0] or start_pozice[1] == cilove_pole[1]:  # Horizontálně/vertikálně
            smer = (
                (0, 1 if cilove_pole[1] > start_pozice[1] else -1)
                if start_pozice[0] == cilove_pole[0]
                else (1 if cilove_pole[0] > start_pozice[0] else -1, 0)
            )
            return je_cesta_volna(start_pozice, cilove_pole, smer) and je_volna(cilove_pole)
        elif abs(cilove_pole[0] - start_pozice[0]) == abs(cilove_pole[1] - start_pozice[1]):  # Diagonálně
            smer = (
                1 if cilove_pole[0] > start_pozice[0] else -1,
                1 if cilove_pole[1] > start_pozice[1] else -1,
            )
            return je_cesta_volna(start_pozice, cilove_pole, smer) and je_volna(cilove_pole)
        return False

    # Král
    if typ == "král":
        rozdil_radku = abs(cilove_pole[0] - start_pozice[0])
        rozdil_sloupce = abs(cilove_pole[1] - start_pozice[1])
        if max(rozdil_radku, rozdil_sloupce) == 1:
            return je_volna(cilove_pole)
        return False

    return False

# Test fce; # = výsledky (ze zadání)
if __name__ == "__main__":
    jezdec = {"typ": "jezdec", "7p": "jezdcem", "pozice": (3, 3)}
    vez = {"typ": "věž", "7p": "věží", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "7p": "střelcem", "pozice": (6, 3)}
    dama = {"typ": "dáma", "7p": "dámou", "pozice": (8, 3)}
    kral = {"typ": "král", "7p": "králem", "pozice": (1, 4)}
    pesec = {"typ": "pěšec", "7p": "pěšcem", "pozice": (2, 2)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
