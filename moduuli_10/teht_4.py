
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettumatka=0,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def kulje(self, aika):
        self.kuljettumatka += self.nopeus * aika



class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.osallistuvat_autot = []
        self.autot = autot

        for i in range(self.autot):
            uusi_auto = Auto(f'ABC-{i + 1}', random.randint(100, 200), 0, 0)
            self.osallistuvat_autot.append(uusi_auto)

    tunti_mennyt = 0
    def tunti_kuluu(self):
        while self.kilpailuohi() != True:
            for l in self.osallistuvat_autot:
                l.kiihdyta(random.randint(-10, 15))
                l.kulje(1)
                self.tunti_mennyt += 1
                if self.tunti_mennyt % 10 == 0:
                    print(f'\nAikaa on kulunut {self.tunti_mennyt} h.')
                    self.tulostatilanne()



    def tulostatilanne(self):
        print(f"""*-----------------*--------------*--------*----------------*
| Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka |""")

        for auto in self.osallistuvat_autot:
            print(f"""*-----------------*--------------*--------*----------------*
| {auto.rekisteritunnus.ljust(16)}| {(str(auto.huippunopeus) + " km/h").ljust(13)}| {str(auto.nopeus).ljust(7)}| {(str(auto.kuljettumatka) + " km").ljust(15)}|
*-----------------*--------------*--------*----------------*""")

    def kilpailuohi(self):
        for auto in self.osallistuvat_autot:
            if auto.kuljettumatka >= self.kilpailun_pituus:
                return True





aloitus = Kilpailu("Suuri romuralli", 8000, 10)
print(f'\nKilpailun nimi on "{aloitus.kilpailun_nimi}", ja kisan pituus on {aloitus.kilpailun_pituus} km')

aloitus.tunti_kuluu()