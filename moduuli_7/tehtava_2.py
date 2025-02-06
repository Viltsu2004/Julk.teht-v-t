nimi = {""}

while True:
    kysym = input("Anna nimi tai poistu painamalla ENTER:")
    if kysym == "":
        for n in nimi:
            print(n)
        break
    if kysym in nimi:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimi.add(kysym)

