class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros


    def siirry_kerrokseen(self, siirtyma, hissi_n):
        if siirtyma > self.ylin_kerros or siirtyma < self.alin_kerros:
            print("Kerrosta ei ole olemassa")

        else:
            if siirtyma > self.kerros:
                Hissi.kerros_ylos(self, siirtyma, hissi_n)

            elif siirtyma < self.kerros:
                Hissi.kerros_alas(self, siirtyma, hissi_n)

            else:
                print(f'Hissi "{hissi_n}" on kerroksessa {siirtyma}.')

    def kerros_ylos(self, siirtyma, hissi_n):
        for i in range(siirtyma - self.kerros):
            self.kerros += 1
            print(f'Hissi "{hissi_n}" on kerroksessa {self.kerros}')


    def kerros_alas(self, siirtyma, hissi_n):
        for i in range(self.kerros - siirtyma):
            self.kerros -= 1
            print(f'Hissi "{hissi_n}" on kerroksessa {self.kerros}')


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
            self.hissit[hissi_n].siirry_kerrokseen(siirtyma, hissi_n)

        else:
            print("Hissiä ei ole.")

    def palohalytys(self):
        for l in range(len(self.hissit)):
            talo.aja_hissia(self.alin_kerros, l)
            print('\n')


talo = Talo(-2, 15, 4)

talo.aja_hissia(8, 2)
print('\n')
talo.aja_hissia(3,2)
print('\n')

talo.palohalytys()



#talo.aja_hissia(3, talo.hissit[1], 0)







