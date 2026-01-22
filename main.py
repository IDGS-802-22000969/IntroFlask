from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    titulo = "IDGS 802-Flask"
    lista = ['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formularios')
def formularios():
    return render_template("formularios.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")

@app.route('/hola') 
def home():
    return "Hello word IDGS802!"

@app.route('/hola')
def hola():
    return "Hola, hola!"


@app.route('/user/<string:user>')
def user_nombre(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)


@app.route("/user/<int:n>/<string:username>")
def user_id(n, username):
    return "ID: {} nombre: {}".format(n, username)

@app.route("/user/<float:n1>/<float:n2>")
def func_suma(n1, n2):
    return "la suma es: {}".format(n1 + n2)


@app.route("/default/")
@app.route("/default/<string:param>")
def func_default(param="juan"):
    return f"<h1>!hola, {param}!</h1>"

# --- RUTAS CON HTML DIRECTO ---

@app.route("/operas")
def operas():
    return '''
    <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="apaterno">apaterno:</label>
        <input type="text" id="apaterno" name="apaterno" required><br><br>
        
        <input type="submit" value="Enviar">
    </form>
    '''

@app.route("/operasBass")
def operas1():
    return render_template("operasBass.html")
   
@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        op = request.form.get("opciones")

        if n1 and n2:
            num1 = float(n1)
            num2 = float(n2)
            
            if op == 'sumar':
                res = num1 + num2
                msg = "suma"
            elif op == 'restar':
                res = num1 - num2
                msg = "resta"
            elif op == 'multiplicar':
                res = num1 * num2
                msg = "multiplicación"
            elif op == 'dividir':
                res = num1 / num2 if num2 != 0 else "Error (división por cero)"
                msg = "división"
            
            return f"<h1>El resultado de la {msg} es: {res}</h1> <a href='/'>Volver</a>"
        
        return "Error: Faltan datos por llenar."

if __name__ == "__main__":
    app.run(debug=True)