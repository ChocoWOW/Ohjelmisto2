from flask import Flask, request

app = Flask(__name__)
@app.route('/summa/<num>')
def summa(num):