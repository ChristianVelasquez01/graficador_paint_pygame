from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonTriangulo(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_triangulo(
            Herramientas, pantalla, NEGRO,
            self.x0 + self.ancho // 2,
            self.y0 + 5,
            self.x0 + 5,
            self.y0 + self.alto - 5,
            self.x0 + self.ancho - 5,
            self.y0 + self.alto - 5
        )

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 7
        print("Modo Dibujar Triangulo")
        return lienzo
