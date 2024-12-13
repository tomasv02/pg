# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

#13/12/2024 VRBAT - ověření, zda se provede přenos z hlavní třídy do podtříd. Testování pomocí metody test_shapes
#do terminalu: pytest zkouska3.py => return musi byt bez chyb

from abc import ABC, abstractmethod

class Shape(ABC): #nemůže být inicializována, slouží jako základna
    @abstractmethod
    def area(self):
        pass

# Třída Rectangle, která dědí po Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Třída Circle, která dědí po Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert circle.area() == 28.26

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass