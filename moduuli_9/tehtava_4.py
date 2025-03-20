
import random

def main():
    auto = []
    for autot in range(10):
        auto.append(f"ABC-{autot},  {random.randint(100, 200)}")

class Auto:
    def __init__(self, rekisteri, maksiminopeus, nopeus, matka):
        self.rekisteri = rekisteri
        self.maksiminopaus = maksiminopeus
        self.nopeus = nopeus
        self.matka = matka

main()jeajaje