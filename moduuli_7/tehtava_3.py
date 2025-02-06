koodi={"":""}

while True:
    icao = input("Jos haluat antaa uuden lentoaseman nimen kirjoita K, \njos haluat etsiä olemassa olevaa lentoasemaa kirjoita E, \nja jos lopettaa paina ENTER:")
    if icao == "K":
        annakood = input("Annna ICAO-koodi:")
        nimi = input("Anna lentoaseman nimi:")
        koodi[annakood]=nimi
    elif icao == "E":
        etsi = input("Anna ICAO-koodi:")
        if etsi in koodi:
            print(koodi[etsi])
    elif icao == "":
        break
