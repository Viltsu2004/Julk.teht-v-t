#Luodaan lista, jotta tiedot jäävät muistiin
lista = []
num = input("Anna lukuja niin pitkään kuin tahdot, \nkun olet valmis poistu painamalla ENTRER painiketta:")

#Luodaan while-rakenne
while num != "":
    lista.append(float(num))
    num = input("Anna luku tai poistu painamalla ENTRER:")

#Tulos kun num != "" -> max(lista) min(lista)
print(f"Lopetit lukujen syötön, tässä pienin antamasi luku {min(lista)} \nja tässä suurin {max(lista)}.")