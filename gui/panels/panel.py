from drawing.tools import Herramientas
from drawing.colors import *

class Panel:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.lista_botones = []
        self.crear_botones()

    def crear_botones(self):
        pass

    def dibujar_panel(self, pantalla):
        Herramientas.bresenham_rellenar_rectangulo(Herramientas, pantalla, BACKGROUND, self.x, self.y, self.x + self.ancho, self.y + self.alto)
        for boton in self.lista_botones:
            boton.dibujar_boton(pantalla)

    def obtener_boton(self, pantalla, lienzo, x, y):
        for boton in self.lista_botones:
            if boton.x0 < x < boton.x1 and boton.y0 < y < boton.y1:
                lienzo = boton.presionar_boton(lienzo, pantalla)
                break
        self.actualizar_seleccion(pantalla, lienzo)
        return lienzo

    def actualizar_seleccion(self, pantalla, lienzo):
        pass
