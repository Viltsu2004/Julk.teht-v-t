#Pää
import math

def main():
    koko = float(input("Anna ensimmäisen pitsan halkaisija senttimetreinä: "))
    hinta = float(input("Anna ensimmäisen pitsan hinta euroina: "))
    neljhint = side(koko, hinta)

    koko = float(input("Anna toisen pitsan halkaisija senttimetreinä: "))
    hinta = float(input("Anna toisen pitsan hinta euroina: "))
    neljhint2 = side(koko, hinta)

    if neljhint > neljhint2:
        print(f'Jälkimmäisenä annettu pitsa on neljö hinnaltaan huokeampi, ja se maksoi \n{neljhint2:.2f} €/m^2')
        
    else:
        print(f'Ensimmäinen pitsa oli neljöhinnaltaan huokeampi ja se maksoi {neljhint:.2f} €/m^2')


def side(koko, hinta):
    koko = koko*1/100
    neljo = hinta/(math.pi*(koko/2)**2)
    return neljo

main()