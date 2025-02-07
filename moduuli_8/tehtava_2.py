import mysql.connector


def main():

    maakoodi = input("Anna lentokentän maakoodi:")
    heliportit(maakoodi)
    print(f'Pineiä lentokenttiä on {heliportit(maakoodi)[0]}.')
    print(f'Keskikokoisia lentokenttiä on {heliportit(maakoodi)[1]}.')
    print(f'Isoja lentokenttiä on {heliportit(maakoodi)[2]}.')
    print(f'Helikopteri kenttiä on {heliportit(maakoodi)[3]}.')
    print(f'Muita on {heliportit(maakoodi)[4]}.')



def heliportit(maakoodi):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='villevaltteri',
        password='salasana',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )

    sql = f"SELECT type from airport where iso_country='{maakoodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    heli = 0
    small = 0
    medium = 0
    large = 0
    muut = 0

    for lentokentta in tulos:
        if lentokentta[0] == 'small_airport':
            small += 1
        elif lentokentta[0] == 'medium_airport':
            medium += 1
        elif lentokentta[0] == 'large_airport':
            large += 1
        elif lentokentta[0] == 'heliport':
            heli += 1
        else:
            muut += 1
    return small, medium, large, heli, muut


main()

