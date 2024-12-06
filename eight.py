def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    cislo = int(cislo)
    if cislo == 0:
        return "0"
    vysledek = ""
    while cislo > 0:
        if cislo % 2 == 0:
            vysledek += "0"
        else:
            vysledek += "1"
        cislo = cislo // 2

    return "".join(reversed(vysledek))

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128