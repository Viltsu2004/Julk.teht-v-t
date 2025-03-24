class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros


    def siirry_kerrokseen(self, siirtyma):
        if siirtyma > self.ylin_kerros or siirtyma < self.alin_kerros:
            print("Kerrosta ei ole olemassa")

        else:
            if siirtyma > self.kerros:
                Hissi.kerros_ylos(self, siirtyma)

            elif siirtyma < self.kerros:
                Hissi.kerros_alas(self, siirtyma)

            else:
                print(f'Olet jo kerroksessa {siirtyma}.')

    def kerros_ylos(self, siirtyma):
        for i in range(siirtyma - self.kerros):
            self.kerros += 1
            print(f'Olet kerroksessa {self.kerros}')


    def kerros_alas(self, siirtyma):
        for i in range(self.kerros - siirtyma):
            self.kerros -= 1
            print(f'Olet kerroksessa {self.kerros}')


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.maara = maara
        self.hissit = []
        for i in range(maara):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissia(self, siirtyma, hissi_n):
        if 0 <= hissi_n < len(self.hissit):
            self.hissit[hissi_n].siirry_kerrokseen(siirtyma)

        else:
            print("Hissiä ei ole.")


talo = Talo(-2, 15, 4)

talo.aja_hissia(8, 2)
print("\n")
talo.aja_hissia(3,2)
print("\n")




#talo.aja_hissia(3, talo.hissit[1], 0)







