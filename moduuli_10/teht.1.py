class Hissi:
    def __init__(self, kerros = 0):
        self.alin_kerros = 0
        self.ylin_kerros = 10
        self.kerros = kerros

    def siirry_kerrokseen(self, siirtyma):
        if siirtyma > self.ylin_kerros or siirtyma < self.alin_kerros:
            print("Kerrosta ei ole olemassa")

        else:
            if siirtyma > self.kerros:
                h.kerros_ylos(siirtyma)

            elif siirtyma < self.kerros:
                h.kerros_alas(siirtyma)

            else:
                print(f'Olet jo kerroksessa {siirtyma}.')

    def kerros_ylos(self, siirtyma):
        for i in range(siirtyma - self.kerros):
            h.kerros += 1
            print(f'Olet kerroksessa {self.kerros}')

    def kerros_alas(self, siirtyma):
        for i in range(self.kerros - siirtyma):
            h.kerros -= 1
            print(f'Olet kerroksessa {self.kerros}')


h = Hissi(5)
h.siirry_kerrokseen(11)
h.siirry_kerrokseen(0)