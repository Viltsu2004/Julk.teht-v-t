lista = []
luku = input("Anna luku tai poistu painamalla ENTER:")


while luku !="":
    lista.append(float(luku))
    luku = input("Anna luku tai poistu painamalla ENTER:")


lista.sort(reverse=True)
print(f'Viisi suurinta lukua suurimmasta pienimpään ovat {lista[0:5]}.')




