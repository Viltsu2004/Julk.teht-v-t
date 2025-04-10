
import mysql.connector
import json
from flask import Flask, Response

yhteys = mysql.connector.connect (
    host='127.0.0.1',
    port= 3306,
    database='rahtipeli',
    user='villevaltteri',  # HUOM käyttäjä: pythonuser
    password='salasana',  #HUOM salasana
    autocommit=True,
    collation='utf8mb3_general_ci'
    )
kursori = yhteys.cursor()

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def haku(icao):
    try:
        kentta = icao
        sql = (f"select name, municipality from airport where ident='{kentta}'")
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        vastaus = {
            'icao': kentta,
            'Name': tulos[0],
            'Municipality': tulos[1]
        }
        json_vastaus = json.dumps(vastaus)
        return Response(response=json_vastaus, mimetype='application/json')

    except TypeError:
        tilakoodi = 400
        vastaus = {
            'status': tilakoodi,
            'kuvaus': 'Virheellinen icao-koodi'
        }
        json_vastaus = json.dumps(vastaus)
        return Response(response=json_vastaus, status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(virhe):
    tilakoodi = 404
    vastaus = {
        'status' : tilakoodi,
        'kuvaus' : 'Virheellinen paatepiste'
    }
    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype='application/json')


if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)