from flask import Flask
FICHERO = "data/movimientos.csv"

app = Flask(__name__)

from . import views #se tiene que importar despues de crear la variable app         


