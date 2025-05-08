from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonElipse(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_elipse(pantalla, NEGRO,
            self.x0 + self.ancho // 2,
            self.y0 + self.alto // 2,
            self.ancho // 2.3,
            self.alto // 3.5
        )

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 6
        print("Modo Dibujar Elipse")
        return lienzo
