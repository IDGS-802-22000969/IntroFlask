import math
from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)
app.secret_key='clave screta'
csrf=CSRFProtect()


@app.route('/')
def index():
    titulo = "IDGS 802-Flask"
    lista = ['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/usuarios', methods =["GET", "POST"])
def usuarios():
    mat=0
    nom=""
    apa=''
    ama=''
    email=''

    usuarios_class=forms.UserForm(request.form)
    if request.method=='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data

        mensaje="Bienvenido {}".format(nom)
        flash(mensaje)

    return render_template('usuarios.html', form=usuarios_class, 
                           mat=mat, nom=nom, apa=apa, ama=ama, email=email)

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

@app.route("/operasBass",  methods=["GET", "POST"])
def operas1():
    operacion=""
    n1=0
    n2=0
    res=0
    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        operacion=request.form.get("opera")

    if operacion == "suma":
        res = float(n1) + float(n2)
    elif operacion == "resta":
        res = float(n1) - float(n2)
    elif operacion == "multip":
        res = float(n1) * float(n2)
    elif operacion == "division":
        res = float(n1) / float(n2)
    else:
        res = 0
    return render_template("operasBass.html",n1=n1,n2=n2,res=res)


   
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


@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1=0
    x2=0
    y1=0
    y2=0
    res=0
    cine_form=forms.CinepolisForm(request.form)
    if request.method == "POST":
        x1 = float(request.form.get("x1"))
        y1 = float(request.form.get("y1"))
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))
        res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    return render_template("distancia.html",form=cine_form, x1=x1, x2=x2, y1=y1, y2=y2, res=res)

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepoli():
    nombre="" 
    total=0
    mensaje =""
    compradores=0
    boletos = 0
    tarjeta = ""

    cine_form=forms.CinepolisForm(request.form)
    if request.method == "POST" and cine_form.validate():
        nombre = cine_form.nombre.data
        compradores = cine_form.compradores.data
        boletos = cine_form.boletos.data
        tarjeta = cine_form.tarjeta.data
        
        maximopermitido = compradores * 7

        if boletos > maximopermitido:
            mensaje = f"No se pueden comprar más de 7 boletos por persona"
            total = 0
        else: 
            subtotal = boletos * 12
            if boletos > 5:
                subtotal *= 0.85  
            elif 3 <= boletos <= 5:
                subtotal *= 0.90 
            if tarjeta=="true":
                subtotal *= 0.90  
            total = subtotal
    return render_template("cinepolis.html", form=cine_form,
                            nombre=nombre, 
                            compradores=compradores,
                            boletos=boletos, 
                            total=total, 
                            mensaje=mensaje)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True) 