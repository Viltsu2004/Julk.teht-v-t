import random
lista = []

kysym = int(input("Anna arpakuutioiden lukumäärä:"))

for i in range(kysym):
    luku = random.randint(1,6)
    lista.append(luku)
print(f"Arpakuutioiden sattumanvaraisten silmälukujen summa on {sum(lista)}.")


