import csv
from . import FICHERO

class Movimientos():
    def __init__(self, fecha, concepto, es_ingreso, cantidad):
        self.fecha = fecha
        self.concepto = concepto
        self.es_ingreso = es_ingreso
        self.cantidad = cantidad

class ListaMovimientos():
    def __init__(self):
        self.movimientos = []

    def leer(self):
        self.movimientos = []
        fichero = open(FICHERO, "r", encoding="utf-8") #tenemos que codificar de la misma forma HTML y Python en UTF-8
        dreader = csv.DictReader(fichero)
        for linea in dreader:
            self.movimientos.append(linea)

        fichero.close()

    def escribir(self):
        if len(self.movimientos) == 0:
            return

        fichero = open(FICHERO, "w")
        #nombres_campo = ["fecha","campo","es_ingreso","cantidad"]
        nombres_campo = list(self.movimientos[0].keys())
        dwriter = csv.DictWriter(fichero, fieldnames=nombres_campo)
        
        for movimiento in self.movimientos:
            dwriter.writerow(movimiento)
        
        fichero.close()

    def anyadir(self, valor):
        movimiento = {}
        movimiento['fecha'] = valor['fecha']
        movimiento['concepto'] = valor['concepto']
        movimiento['ingreso_gasto'] = valor['ingreso_gasto']
        movimiento['cantidad'] = valor['cantidad']
        self.movimientos.append(movimiento)
 