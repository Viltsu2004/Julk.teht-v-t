
n1 = float(input("Anna tuumamäärä:"))
while n1:
    if n1 < 0:
        break
    print(f"Annettu tuuma on {n1*2.54} cm.")
    n1 = float(input("Anna tuumamäärä:"))
print("Nähdään taas!")