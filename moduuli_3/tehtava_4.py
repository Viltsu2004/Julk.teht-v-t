vuosi = float(input("Kirjoita vuosiluku:"))
jakojaannos = float(f'{vuosi/4:.0f}')
if vuosi/4==jakojaannos or vuosi/100==jakojaannos and vuosi/400==jakojaannos:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
