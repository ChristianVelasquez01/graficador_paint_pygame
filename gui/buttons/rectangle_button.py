from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonRectangulo(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_rectangulo(
            Herramientas, pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + 7,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto - 7
        )

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 4
        print("Modo Dibujar Rectangulo")
        return lienzo
