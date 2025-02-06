
vuodenaika = ("talvi", "kevät", "kesä", "syksy")

kysymys = int(input("Anna kuukauden numero:"))
if kysymys == 12 or 1 <= kysymys <= 2:
    print(vuodenaika[0])
elif 3 <= kysymys <= 5:
    print(vuodenaika[1])
elif 6 <= kysymys <= 8:
    print(vuodenaika[2])
elif 9 <= kysymys <= 11:
    print(vuodenaika[3])

