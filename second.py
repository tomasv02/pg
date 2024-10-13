def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    # 13/10/2024 VRBAT - fction implementation
       
    if cislo > 100 or cislo < 0: #kontrola intervalu <0;100>
        print("Vyberte prosím číslo od 0 do 100")
        exit
    else:
        def najdi_text(cislo)
            if cislo is 
        #return "dvacet pět"


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: ")) #kontrola, vstup pouze celé číslo
    text = cislo_text(cislo)
    print(text)