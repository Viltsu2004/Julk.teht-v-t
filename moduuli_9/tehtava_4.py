
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

autot = []

for l in range(10):
    u_auto = Auto(f'ABC-{l+1}', random.randint(100, 200))
    autot.append(u_auto)

while True:
    for i in autot:
        i.kulje(1)
        i.kiihdyta(random.randint(-10, 15))
        if i.kuljettumatka >= 10000:
            break
    else:
        continue
    break


print(f"""*-----------------*--------------*--------*----------------*
| Rekisteritunnus | Huippunopeus | Nopeus | Kuljettu matka |""")

for auto in autot:
    print(f"""*-----------------*--------------*--------*----------------*
| {auto.rekisteritunnus.ljust(16)}| {(str(auto.huippunopeus)+" km/h").ljust(13)}| {str(auto.nopeus).ljust(7)}| {(str(auto.kuljettumatka) + " km").ljust(15)}|
*-----------------*--------------*--------*----------------*""")
