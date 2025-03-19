class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka


auto1 = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on {auto1.rekisteritunnus:s}, sen huippunopeus on {auto1.huippunopeus} km/h, \ntämän hetkinen nopeus {auto1.nopeus:d} km/h ja kuljettu matka {auto1.kuljettumatka:d} km")

