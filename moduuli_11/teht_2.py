class Auto:

    aika = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka_aika):
        self.matka_aika = matka_aika
        Auto.aika = matka_aika
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

        self.kuljettumatka = self.matka_aika * self.nopeus

    def tulosta_tilanne(self):
        print(f"\nRekisteritunnus: {self.rekisteritunnus:s}, Huippunopeus: {self.huippunopeus} km/h, \nNopeus: {self.nopeus:d} km/h, Matkamittari: {self.kuljettumatka:d} km.")


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, akkukapasiteetti, matka_aika):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka_aika)

    def tulosta_tilanne(self):
        super().tulosta_tilanne()
        print(f'Akkukaupasiteetti: {self.akkukapasiteetti}')

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, litrat, matka_aika):
        self.litrat = litrat
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka_aika)

    def tulosta_tilanne(self):
        super().tulosta_tilanne()
        print(f'Polttistankki: {self.litrat}')

auto = []
auto.append(Sahkoauto("ABC-123", 122, -4, 52.5, 3))
auto.append(Polttomoottoriauto("ABC-123", 142, 150, 32.3, 3))

for l in auto:
    l.tulosta_tilanne()