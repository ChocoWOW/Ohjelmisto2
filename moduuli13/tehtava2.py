from flask import Flask, request
import mysql.connector




yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='lentopeli',
    user='root',
    password='lolmol123',
    autocommit=True
)
app = Flask(name)
@app.route('/summa/<icao>')
def summa(icao):
    sql = f"SELECT name FROM airport WHERE ident = '{icao}'"
    sql2 = f"SELECT municipality FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            i = 0
            i = i + 1
            print(rivi[0])
    kursori = yhteys.cursor()
    kursori.execute(sql2)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi1 in tulos:
            i = 0
            i = i + 1
            print(rivi1[0])

    vastaus = {
        "ICAO":icao,
        "Name":rivi[0],
        "Municipality":rivi1[0]
    }

    return vastaus

if name == 'main':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)