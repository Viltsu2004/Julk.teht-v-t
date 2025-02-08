
import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='villevaltteri',
        password='salasana',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )

def main():

    icao1 = input("Anna ensimmäinen ICAO-kidoodi:")
    icao2 = input("Anna toinen ICAO-koodi:")

    etaisyys(icao1, icao2)
    print(f'Kenttein etäisyys on {etaisyys(icao1, icao2)}.')

def etaisyys(icao1, icao2):
    sql1 = f"select longitude_deg, latitude_deg from airport where ident = '{icao1}'"
    sql2 = f"select longitude_deg, latitude_deg from airport where ident = '{icao2}'"

    kursori = yhteys.cursor()

    kursori.execute(sql1)
    koord1 = kursori.fetchall()

    kursori.execute(sql2)
    koord2 = kursori.fetchall()

    return geodesic(koord2, koord1)

main()
