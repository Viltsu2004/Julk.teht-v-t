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
        self.kuljettumatka += self.nopeus*aika



mersu = Auto("ABC-123", 142)

mersu.kiihdyta(30)
mersu.kiihdyta(70)
mersu.kiihdyta(50)
mersu.kulje(2)

print(f"\nAuton rekisteritunnus on {mersu.rekisteritunnus:s}, sen huippunopeus on {mersu.huippunopeus} km/h, \ntämän hetkinen nopeus {mersu.nopeus:d} km/h ja kuljettu matka {mersu.kuljettumatka:d} km")

mersu.kiihdyta(-200)

print(f"\nAuton rekisteritunnus on {mersu.rekisteritunnus:s}, sen huippunopeus on {mersu.huippunopeus} km/h, \ntämän hetkinen nopeus {mersu.nopeus:d} km/h ja kuljettu matka {mersu.kuljettumatka:d} km")

#30,70, 50, nopeus, -200 uus.nop