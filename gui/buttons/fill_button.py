from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonRellenar(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_rellenar_rectangulo(
            Herramientas, pantalla, AZUL,
            self.x0 + 7,
            self.y0 + 22,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto - 7
        )
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + 7,
            self.x0 + 7,
            self.y0 + self.alto - 7
        )
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + self.alto - 7,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto - 7
        )
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + self.ancho - 7,
            self.y0 + 7,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto - 7
        )

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 9
        print("Modo Rellenar Area")
        return lienzo
