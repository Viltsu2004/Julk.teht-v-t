lista = []
luku = int(input("Anna kokonaisluku niin kerron onko se alkuluku:"))

testi = 1
lista.append(testi)

while testi != luku:
    ensimmainen = luku/testi
    if ensimmainen == int(ensimmainen):
        lista.append(ensimmainen)
    testi = testi + 1
if len(lista)<=2:
    print("Antamasi luku on alkuluku")
else:
    print("Antamasi luku ei ole alkuluku")

