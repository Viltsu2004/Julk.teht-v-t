print("Ohjelma kysyy sinulta bensan gallonien määrän ja se muuntaa sen litroiksi, \nkun haluat lopettaa anna negatiivinen arvo. ")

def main():
    kysymys = side(int(input("Anna polttoaineenmäärä gallonina:")))
    if kysymys < 0:
        print("Kiitos käytöstä")
    else:
        print(f'Annettu gallonan määrä on {kysymys} litraa.')
    while kysymys:
        kysymys = side(int(input("Anna polttoaineenmäärä gallonina:")))
        if kysymys < 0:
            break
        else:
            print(f'Annettu gallonan määrä on {kysymys} litraa.')
    print("Kiitos käytöstä.")

def side(gallona):
    bensiini = gallona*3.785
    return bensiini



main()
