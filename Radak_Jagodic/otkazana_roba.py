from roba import Roba

class OtkazanaRoba(Roba):
    def __init__(self, adresa, velicina = "", broj_felera = 1):
        super().__init__(adresa, velicina = velicina)
        self.broj_felera = broj_felera