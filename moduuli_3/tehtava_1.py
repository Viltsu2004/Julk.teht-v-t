kala1 = input("Anna kuhan pituus senttimetreinä:")
arv = float(kala1)
if arv<37:
    print(f"Päästä alimittainen kala takaisin järveen, kalasi on {37-arv} senttimetriä liian lyhyt.")
else:
    print("Mahtava saalis!")