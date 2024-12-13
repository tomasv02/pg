# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

# 13/12/2024 VRBAT
#pokud je číslo větší než 10, ukončí loop pro daný seznam 
def process_numbers(numbers):
    result = []  # Výsledný seznam
    for num in numbers:
        if num == 10:  # Pokud je číslo 10, ukončíme zpracování
            break
        if num > 5:  # Pokud je číslo větší než 5
            result.append(num * 2)  # Vynásobíme číslo 2 a přidáme do výsledku
    return result

# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]