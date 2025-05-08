from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonLinea(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + 7,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto - 7)

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 2
        print("Modo Dibujar Linea")
        return lienzo
    
