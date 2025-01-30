lista = []
print("Ohjelma kysyy sinulta viisi kertaa kaupungin nimeä.")

for kaupunki in range(1,6):
    nimi = input("Anna kaupungin nimi:")
    lista.append(nimi)

for paikat in lista:
    print(paikat)