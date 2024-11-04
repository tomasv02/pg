def je_tah_mozny(figurka, cilove_pole, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.
    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilove_pole: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    :return: True, pokud je tah možný, jinak False.
    """
    #03.11.2024 VRBAT - implementation

    #vstupní podmínky
    condition1 = 1 <= cilove_pole[0] <= 8 and 1 <= cilove_pole[1] <= 8
    condition2 = cilove_pole not in obsazene_pozice
    condition3 = True
    condition4 = True

    #Pěšák
    if figurka["typ"] == "pěšec":  
        if figurka["pozice"][0] == 2:
            l_value = 2
        else:
            l_value = 1
        condition3 = figurka["pozice"][0] < cilove_pole[0] <= figurka["pozice"][0] + l_value

        min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
        for i in range(min0 + 1, max0):
            if (i, cilove_pole[1]) in obsazene_pozice:
                condition4 = False

    #Střelec
    elif figurka["typ"] == "střelec": 
        if abs(figurka["pozice"][0] - cilove_pole[0]) == abs(figurka["pozice"][1] - cilove_pole[1]): #kontrola úhlopříčně (diagonálně)
            condition3 = True
            min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
            min1, max1 = sorted([cilove_pole[1], figurka["pozice"][1]])
            for i, j in zip(range(min0 + 1, max0), range(min1 + 1, max1)):
                if (i, j) in obsazene_pozice:
                    condition4 = False

        else:
            condition3 = False

    #Věž
    elif figurka["typ"] == "věž":
        # kontrola vertiálního pohybu
        if cilove_pole[0] == figurka["pozice"][0]:
            condition3 = True
            min0, max0 = sorted([cilove_pole[1], figurka["pozice"][1]])
            for i in range(min0 + 1, max0):
                if (cilove_pole[0], i) in obsazene_pozice:
                    condition4 = False

        # kontrola horizontálního pohybu
        elif cilove_pole[1] == figurka["pozice"][1]:
            condition3 = True
            min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
            for i in range(min0 + 1, max0):
                if (i, cilove_pole[1]) in obsazene_pozice:
                    condition4 = False
        else:
            condition3 = False

    #kůň 
    elif figurka["typ"] == "jezdec":
        osa1 = abs(cilove_pole[0] - figurka["pozice"][0])
        osa2 = abs(cilove_pole[1] - figurka["pozice"][1])
        condition3 = (osa1 == 2 and osa2 == 1) or (osa1 == 1 and osa2 == 2)

    #královna 
    elif figurka["typ"] == "dáma": 
        if cilove_pole[0] == figurka["pozice"][0]: #kontrola sloupec (vertikálně)
            condition3 = True
            min0, max0 = sorted([cilove_pole[1], figurka["pozice"][1]])
            for i in range(min0 + 1, max0):
                if (cilove_pole[0], i) in obsazene_pozice:
                    condition4 = False

        elif cilove_pole[1] == figurka["pozice"][1]: #kontrola řádek (horizontálně)
            condition3 = True
            min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
            for i in range(min0 + 1, max0):
                if (i, cilove_pole[1]) in obsazene_pozice:
                    condition4 = False

        elif abs(figurka["pozice"][0] - cilove_pole[0]) == abs(figurka["pozice"][1] - cilove_pole[1]): #kontrola úhlopříčně (diagonálně)
            condition3 = True
            min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
            min1, max1 = sorted([cilove_pole[1], figurka["pozice"][1]])
            for i, j in zip(range(min0 + 1, max0), range(min1 + 1, max1)):
                if (i, j) in obsazene_pozice:
                    condition4 = False
        else:
            condition3 = False

    #král 
    elif figurka["typ"] == "král":
        #kontrola sloupec (vertikálně)
        if cilove_pole[0] == figurka["pozice"][0] and abs(cilove_pole[0] - figurka["pozice"][0] <= 1):
            condition3 = True
            min0, max0 = sorted([cilove_pole[1], figurka["pozice"][1]])
            for i in range(min0 + 1, max0):
                if (cilove_pole[0], i) in obsazene_pozice:
                    condition4 = False

        #kontrola řádek (horizontálně)
        elif cilove_pole[1] == figurka["pozice"][1] and abs(cilove_pole[0] - figurka["pozice"][0] <= 1):
            condition3 = True
            min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
            for i in range(min0 + 1, max0):
                if (i, cilove_pole[1]) in obsazene_pozice:
                    condition4 = False

        #kontrola úhlopříčně (diagonálně)
        if abs(cilove_pole[0] - figurka["pozice"][0]) <= 1 and abs(cilove_pole[1] - figurka["pozice"][1]) <= 1:
            condition3 = True
            min0, max0 = sorted([cilove_pole[0], figurka["pozice"][0]])
            min1, max1 = sorted([cilove_pole[1], figurka["pozice"][1]])
            for i, j in zip(range(min0 + 1, max0), range(min1 + 1, max1)):
                if (i, j) in obsazene_pozice:
                    condition4 = False

        else:
            condition3 = False

    #výsledek
    return f"Tah {figurka["7p"]} z pole {figurka["pozice"]} na pole {cilove_pole} je {condition1 and condition2 and condition3 and condition4}"

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
