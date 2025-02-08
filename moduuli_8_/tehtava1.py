import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='villevaltteri',
    password= 'salasana',
    autocommit =True,
    collation='utf8mb3_general_ci'
)

def main():
    icao = input("Anna lentokentän ICAO-koodi:")
    hae_kentta(icao)

def hae_kentta(icao):
    sql = (f"select name from airport where ident='{icao}'")
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        print(tulos[0])

main()



