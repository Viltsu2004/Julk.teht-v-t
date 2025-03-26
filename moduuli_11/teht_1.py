class Julkaisu:
    def __init__(self, julkaisu):
        self.julkaisu = julkaisu

    def tulosta_tiedot(self):
        print(f'\nJulkaisun nimi: {self.julkaisu}')

class Kirja(Julkaisu):
    def __init__(self, julkaisu, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(julkaisu)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara}')


class Lehti(Julkaisu):
    def __init__(self, julkaisu, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(julkaisu)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Päätoimittaja: {self.paatoimittaja}')

julk = []
julk.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julk.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for l in julk:
    l.tulosta_tiedot()

