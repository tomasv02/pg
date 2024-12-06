from abc import ABC, abstractmethod

class figurka(ABC):
    def __init__(self, pozice):
        self.pozice = pozice
    @abstractmethod
    def je_pohyb_mozny(self, nova_pozice):
        pass

class Pesak(figurka):
    def je_pohyb_mozny(self, nova_pozice):
        return True

if __name__== "__main__":
    figurka = Pesak()