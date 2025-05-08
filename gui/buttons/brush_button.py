from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonPincel(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_linea(pantalla, AZUL,
            self.x0 + self.ancho - 20,
            self.y0 + 20,
            self.x0 + 7,
            self.y0 + self.alto - 7)
        Herramientas.bresenham_triangulo(
            Herramientas, pantalla, MARRON_CLARO,
            self.x0 + self.ancho - 20, self.y0 + 20,
            self.x0 + self.ancho - 5, self.y0 + 15,
            self.x0 + self.ancho - 15, self.y0 + 5
        )
        Herramientas.rellenar_area(pantalla, MARRON_CLARO, self.x0 + self.ancho - 17, self.y0 + 17, BLANCO)

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 1
        print("Modo Dibujar Con Pincel")
        return lienzo
