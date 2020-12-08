from roba import Roba 

class PorucenaRoba(Roba):
    def __init__(self, adresa, velicina = "", cena = 2000):
        super().__init__(adresa, velicina = velicina)
        self.cena = cena
