import random
kokolista = []
ympyralis = []

#Arvo inpu("Arvo
luku = float(input("Anna arvottavien pisteiden lukumäärä:"))


#Toisto kunnes pisteitä arvottu = luku
while len(kokolista) != luku:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    piste = (x, y)
    kokolista.append(piste)

#Piste listaan jos toteuttaa yhtälön
    if (x**2+y**2)<1:
        ympyralis.append(piste)

#(4*ympyrän pisteiden.luk)/kokoalueen pisteiden.luk
print(f'Piin likiarvo on noin {4*(len(ympyralis))/len(kokolista)} saatujen pisteiden perusteella.')


