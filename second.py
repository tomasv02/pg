def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # 13/10/2024 VRBAT - fction implementation
    if cislo is None: 
        raise Exception("Číslo nebylo zadáno.")
    elif cislo is not int: 
        raise Exception("Špatný datový typ")
    elif cislo > 100 or cislo < 0: 
        raise Exception("Vyberte prosím číslo od 0 do 100")
    else:
        return "dvacet pět"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)