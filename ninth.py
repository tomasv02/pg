  #10/12/2024 VRBAT - implementation - převod dec na bin

def dec_to_bin(cislo):
    cislo = int(cislo)
    if cislo < 0:
        return "-" + dec_to_bin(-cislo)  # Zpracování záporných čísel
    elif cislo == 0:
        return "0"
    else:
        bin_cislo = ""
        while cislo > 0:
            bin_cislo = str(cislo % 2) + bin_cislo
            cislo //= 2
        return bin_cislo # záznam z debuggingu: výstup fce dec_to_bin: 10100111

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

if __name__ == "__main__":
    dec_to_bin(167) #vstup, v zadání je číslo 167
  