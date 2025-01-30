
#Pää ohjelma
def main():
    lista = []
    print("Anna kokonaislukuja, \nja kun haluat lopettaa paina ENTER")
    while True:
        i = input("Anna kokonaislukuja:")
        if i == "":
            side(lista)
            print(f'Antamistasi luvuista parillisia ovat {side(lista)}.')
            print(f'Kaikki antamasi kokonaisluvut {lista}.')
        else:
            i = int(i)
            lista.append(i)

#Sivu ohjelma
def side(lista):
    lista2 = []
    for l in lista:
        if l % 2 == 0:
            lista2.append(l)
    return lista2

main()