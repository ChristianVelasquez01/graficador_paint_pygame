from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonCurva(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        p0 = (self.x0 + 7, self.y0 + self.alto - 7)
        p1 = (self.x0 + self.ancho // 2, self.y0 + 7)
        p2 = (self.x0 + self.ancho - 7, self.y0 + self.alto - 7)
        Herramientas.linea_curva(Herramientas, pantalla, NEGRO, [p0, p1, p2], True)

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 3
        print("Modo Dibujar Curva")
        return lienzo
