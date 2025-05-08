from drawing.tools import Herramientas
from drawing.colors import *

class Boton:
    def __init__(self, x0, y0, ancho, alto, color):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + ancho
        self.y1 = y0 + alto
        self.ancho = ancho
        self.alto = alto
        self.color = color

    def dibujar_base_boton(self, pantalla):
        Herramientas.bresenham_rellenar_rectangulo(Herramientas, pantalla, self.color,
            self.x0, self.y0, self.x0 + self.ancho, self.y0 + self.alto
        )
        Herramientas.bresenham_rectangulo(Herramientas, pantalla, NEGRO,
            self.x0, self.y0, self.x0 + self.ancho, self.y0 + self.alto
        )

    def presionar_boton(self):
        pass

    def seleccionar_boton(self, pantalla):
        Herramientas.bresenham_rectangulo(
            Herramientas, pantalla, BLANCO,
            self.x0 - 1, self.y0 - 1, self.x0 + self.ancho + 1, self.y0 + self.alto + 1
        )
        Herramientas.bresenham_rectangulo(
            Herramientas, pantalla, GRIS_CLARO,
            self.x0 - 2, self.y0 - 2, self.x0 + self.ancho + 2, self.y0 + self.alto + 2
        )

    def deseleccionar_boton(self, pantalla):
        Herramientas.bresenham_rectangulo(
            Herramientas, pantalla, NEGRO,
            self.x0, self.y0, self.x0 + self.ancho, self.y0 + self.alto
        )
        Herramientas.bresenham_rectangulo(
            Herramientas, pantalla, BACKGROUND,
            self.x0 - 2, self.y0 - 2, self.x0 + self.ancho + 2, self.y0 + self.alto + 2
        )
