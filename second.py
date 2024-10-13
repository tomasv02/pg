def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # 13/10/2024 VRBAT - fction implementation
    if cislo == "": #kontrola, zda je vyplněn vstup
        print("Číslo nebylo zadáno.")
        exit
    elif cislo is not int: #kontrola dat. typu
        print("Špatný datový typ")
        exit
    elif cislo > 100 or cislo < 0: #kontrola intervalu <0;100>
        print("Vyberte prosím číslo od 0 do 100")
        exit
    else: #kontroly ok, provedení
        return "dvacet pět"


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)