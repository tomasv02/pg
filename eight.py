def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5

    #10/12/2024 VRBAT
    vysledek = 0
    binarni_cislo = str(binarni_cislo)
    hodnota_bitu = 1
    for cislo in reversed(binarni_cislo):
        if cislo == "1":
            vysledek += hodnota_bitu
        hodnota_bitu *= 2
    print(vysledek)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

if __name__ == "__main__":
    bin_to_dec("10011101")