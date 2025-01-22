import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa koneen arpoma kokonaisluku, \nlukujen 1 ja 10 väliltä:"))
while arvaus != luku:
    if arvaus < luku:
        print("Liian pieni arvaus!")
    if arvaus > luku:
        print("Liian suuri arvaus!")
    arvaus = int(input("Arvaa kokonaislukua uudelleen:"))
print("Oikein!")