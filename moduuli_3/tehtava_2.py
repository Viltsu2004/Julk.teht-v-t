#Kysyy hyttiluokkaa
hytti = input("Anna hyttiluokkasi, LUX, A, B tai C:")

#Tulos = vastaus
if hytti==str("A"):
    print("Hyttiluokkasi on ikkunallinen hytti autokannen yläpuolella.")
elif hytti==str("B"):
    print("Hyttiluokkasi on ikkunaton hytti autokannen yläpuolella.")
elif hytti==str("C"):
    print("Hyttiluokkasi on ikkunaton hytti autokannen alapuolella.")
elif hytti==str("LUX"):
    print("Hyttiluokkasi on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka.")