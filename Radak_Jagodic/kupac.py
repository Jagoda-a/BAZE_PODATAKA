class Kupac:
    def __init__(self, ime_prezime, adresa, porucena_roba=[], otkazana_roba=[]):
        self.ime_prezime = ime_prezime
        self.adresa = adresa
        self.porucena_roba = porucena_roba
        self.otkazana_roba = otkazana_roba