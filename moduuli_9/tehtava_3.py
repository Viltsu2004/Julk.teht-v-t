class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, muutos):
        for i in muutos:
            self.nopeus += i
            if self.nopeus < 0:
                self.nopeus = 0
            elif self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            Auto.kulje(mersu, 1.5)
            print(f"\nAuton rekisteritunnus on {mersu.rekisteritunnus:s}, sen huippunopeus on {mersu.huippunopeus} km/h, \ntämän hetkinen nopeus {mersu.nopeus} km/h ja kuljettu matka {mersu.kuljettumatka} km")

    def kulje(self, aika):
        self.kuljettumatka += mersu.nopeus * float(aika)

mersu = Auto("ABC-123", 142)


Auto.kiihdyta(mersu, (30, 70, 50, -200))

