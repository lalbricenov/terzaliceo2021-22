from flask import Flask
import time

# Creamos la aplicación que va a escuchar
# las solicitudes del usuario
app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo"

@app.route('/hora')
def hora():
    seconds = time.time()
    return f"Los segundos desde epoch son: {seconds} y la hora actual es {time.ctime(seconds)}"