#tallennus
leiv = input("Anna leiviskät:")
nau = input("Anna naulat:")
luo = input("Anna luodit:")

#merkkijonot liukuluvuksi
leiv1 = float(leiv)
nau1 = float(nau)
luo1 = float(luo)

#kokonaismassa
mas = (leiv1*20*32*13.3+nau1*32*13.3+luo1*13.3)

#kokomassa kiloihin ja pyöristys kokonaislukuun
kilo = f'{mas/1000:.0f}'

#kiloissa oleva kokonaisluku kerrotaan tuhannella = massan pyör. tuhansiin
kokgra = float(kilo)*1000

#kokonaismassata pois tuhanneksen pyöristys = jäjelle jäävät grammat
gram = f'{mas - kokgra:.0f}'

#kilot int pyöristyksellä liukuluvusta kokonaislukuun
print(f"Annettujen arvojen maassa nykyaikaisilla mitoilla on: {kilo} kilogrammaa ja {gram} grammaa")
