#Kysymys
sukupuoli = input(f"Kirjoita biologinen sukupuolesi vaihtoehdoilla M tai N,\nHUOMIO M=miest ja N=nainen:")

#Naisen arv.
if sukupuoli==str("N"):
    hem = float(input("Anna hemoglobiiniarvosi g/l:"))
    if 117 <= hem <= 175:
        print("Hemoglobiiniarvosi ovat normaalit.")
    if hem<117:
        print("Hemoglobiiniarvosi ovat liian alhaiset.")
    if hem>175:
        print("Hemoglobiiniarvosi ovat liian korkeat.")

#Miehen arv.
elif sukupuoli==str("M"):
    hem = float(input("Anna hemoglobiiniarvosi g/l:"))
    if 134 <= hem <= 195:
        print("Hemoglobiiniarvosi ovat normaalit.")
    if hem < 134:
        print("Hemoglobiiniarvosi ovat liian alhaiset.")
    if hem > 195:
        print("Hemoglobiiniarvosi ovat liian korkeat.")

#Ei anna oikeaa suk.puol
else:
    print("Et anatanut sukupuolta oikeassa muodossa.")