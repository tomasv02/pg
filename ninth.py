def dec_to_bin2(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    vysledek = ""
    while cislo > 0:
        if cislo % 2 == 0:
            vysledek += "0"
        else:
            vysledek = str(cislo % 2) + vysledek 
        cislo = cislo // 2

    return vysledek

def dec_to_bin(cislo):
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    elif cislo == 1:
        return "1"
    else:
        return dec_to_bin(cislo // 2) + str(cislo % 2)


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


if __name__ == "__main__":
    dec_to_bin(120)