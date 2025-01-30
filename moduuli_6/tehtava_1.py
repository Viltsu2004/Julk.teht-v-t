import random

print("Ohjelma heittää noppaa niin monta kertaa, että tulee numero 6.\n")

def silmaluku():
    luku = random.randint(1,6)
    print(luku)
    return int(luku)

def main():
    while True:
        if silmaluku() == 6:
            break

main()

