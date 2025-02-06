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

sql = f"select name from airport limit 5"
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(tulos)


