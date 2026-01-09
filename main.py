from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  titulo = "IDGS 802-Flask"
  lista = ['Juan', 'Karla', 'Miguel','Ana']
  return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formularios')
def formularios():
  return render_template("formularios.html")

@app.route('/reportes')
def reportes():
  return render_template("reportes.html")

@app.route('/')
def home():
  return "Hello word IDGS802!"

@app.route('/hola')
def hola():
  return "Hola, hola!"


@app.route('/user/<string:user>')
def user(user):
  return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
  return "Numero:{}".format(n)

@app.route("/user/<int:n>/<string:username>")
def user(id, username):
  return "ID: {} nombre: {}".format(id, username)

@app.route("/user/<float:n1>/<float:n2>")
def func(n1, n2):
  return "lasuma es: {}".format(n1+n2)

@app.route("/default/")
@app.router("/default/<string:param>")
def func2(param="juan"):
  return f"<h1>!hola,{param}!</h1>"


@app.route("/operas")
def operas():
  return '''

    <form>
      <label for ="name">Name:</label>
      <input type="text" id="name" name="name" required>

      <label for ="name">apaterno:</label>
      <input type="text" id="name" name="name" required>
  </form>

          '''

if __name__ == "__main__":
  app.run(debug=True)