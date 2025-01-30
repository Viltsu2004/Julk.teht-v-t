import random

print("\nOhjelma heittää noppaa niin kauan, \nettä se saa nopan suurimman silmäluvun.")


def silmaluku(tahko):
    luku = random.randint(1, tahko)
    print(luku)
    return int(luku)

def main():
    tahko = int(input("\nAnna nopan tahkojen lukumäärä:"))
    while True:
        if silmaluku(tahko) == tahko:
            break

main()