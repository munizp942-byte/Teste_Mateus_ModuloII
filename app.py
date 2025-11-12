from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/adicao/<numero1>/<numero2>", methods=['GET'])
def adição(numero1, numero2):
    resultado = float(numero1) + float(numero2)
    return f'<h1> o resultado da soma é: { resultado } </h1>'

  
@app.route("/multiplicacao/<numero1>/<numero2>", methods=['GET'])
def multiplicação(numero1, numero2):
    resultado = float(numero1) * float(numero2)
    return f'<h1> o resultado da multiplicação é: { resultado } </h1>'


@app.route("/divisao/<numero1>/<numero2>", methods=['GET'])
def divisão(numero1, numero2):
    resultado = float(numero1) / float(numero2)
    return f'<h1> o resultado da divisão é: { resultado } </h1>'


@app.route("/subtracao/<numero1>/<numero2>", methods=['GET'])
def subtração(numero1, numero2):
    resultado = float(numero1) - float(numero2)
    return f'<h1> o resultado da subtração é: { resultado } </h1>' 

if __name__ == "__main__":
    app.run(debug=True)