from flask import Flask, render_template, request, redirect

# Crear la aplicacion. __name__ representa el archivo actual
app = Flask(__name__)

# estudiantes es una lista(array) de diccionarios
estudiantes = [{"nombre":"Juan", "apellido":"Rodriguez", "edad":15, "id_estudiante":1}, {"nombre":"Maria", "apellido":"Rodriguez", "edad":12, "id_estudiante":3}, {"nombre":"Pedro", "apellido":"Pérez", "edad":26, "id_estudiante":2 }]

# rutas disponibles
# / quiere decir root
@app.route('/')
def index():
    # return str(personas)
    return render_template('index.html', estudiantes = estudiantes)

@app.route('/create', methods=["GET", "POST"])
def crear():
    if request.method == "GET":
        return render_template("formularioCreacion.html")
    else:
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        id_estudiante = obteneridSiguiente()
        nuevoEst = {"nombre":nombre, "apellido":apellido, "edad":edad, "id_estudiante":id_estudiante}
        estudiantes.append(nuevoEst)

        return redirect("/")
def obteneridSiguiente():
    return 5
