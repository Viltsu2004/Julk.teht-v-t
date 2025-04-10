import json

from flask import Flask, Response

app = Flask(__name__)
@app.route('/alkuluku/<luku1>')
def summa(luku1):
    try:
        lista = []
        alkuluku = float(luku1)
        aloitus = 1
        lista.append(alkuluku)

        while aloitus != alkuluku:
            if (alkuluku/aloitus) == int(alkuluku/aloitus):
                lista.append(aloitus)
            aloitus += 1
        if len(lista)<=2:
            luku = True
        else:
            luku = False
        print(lista)




        tilakoodi = 200
        vastaus = {
            'status': tilakoodi,
            'Number': alkuluku,
            'isPrime': luku
        }
        json_vastaus = json.dumps(vastaus)
        return Response(response=json_vastaus, status=tilakoodi, mimetype='application/json')

    except ValueError:
        tilakoodi = 400
        vastaus = {
        'status' : tilakoodi,
        'kuvaus' : 'Virheellinen yhteenlaskettava'
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
