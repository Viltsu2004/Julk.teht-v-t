lista =[]

kayttajatunnus = "python"
salasana = "rules"


while len(lista)!=5:
    tunnus = input("\nAnna käyttäjätunnus:")
    koodi = input("Anna salasana:")
    lista.append(tunnus and koodi)
    oikeat = (tunnus == kayttajatunnus)
    oikeas = (koodi == salasana)
    if oikeat and oikeas:
        print("Tervetuloa")
        break
else:
    print("Pääsy evätty.")



