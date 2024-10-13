def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

    # 13/10/2024 VRBAT - fction implementation
    cislo = int(cislo)   

    if cislo < 0 or cislo > 100: #kontrola intervalu <0;100>
        return "Vyberte prosím číslo od 0 do 100"
    else:
      if cislo == 0: 
         return "nula"
      
      if cislo >= 1 and cislo <= 9:
         interval_1_az_9 = {1: "jedna", 2: "dva", 3: "tři", 4:"čtyři", 5:"pět", 6:"šest", 7:"sedm", 8:"osm", 9:"devět"}
         return interval_1_az_9[cislo]
      
      if cislo >= 11 and cislo <= 19:
         interval_11_az_19 = {11: "jedenáct", 12: "dvanáct", 13:"třináct", 14:"čtrnáct", 15:"patnáct", 16:"šestnáct", 17:"sedmnáct", 18:"osmnáct", 19:"devatenáct"}
         return interval_11_az_19[cislo]
      
      if cislo >= 11 and cislo <= 19:
         interval_11_az_19 = {11: "jedenáct", 12: "dvanáct", 13:"třináct", 14:"čtrnáct", 15:"patnáct", 16:"šestnáct", 17:"sedmnáct", 18:"osmnáct", 19:"devatenáct"}
         return interval_11_az_19[cislo]
      
      if cislo > 20 and cislo < 99: 
         intervaů = {2: "dvacet", 3: "třicet", 4: "čtyřicet", 5: "padesát", 6: "šedesát", 7: "sedmdesát", 8: "osmdesát", 9: "devadesát"}
      if cislo == 100:
         return "sto"
     


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)