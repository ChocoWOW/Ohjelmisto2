from flask import Flask, request

app = Flask(__name__)
@app.route('/summa/<num>')
def summa(num):
    numero = int(num)
    juu = True
    if numero == 1:
        print(numero, "ei ole alku numero")
        juu = False
    elif numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                print(numero, "ei ole alkunumero")
                juu = False
                break
        else:
            print(numero, "on alkunumero")
            juu = True


    else:
        print(numero, "ei ole alkunumero")
        juu = False

    vastaus = {
        "number":num,
        "IsPrime":juu

    }
    return vastaus



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)