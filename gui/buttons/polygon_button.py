from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonPoligono(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        puntos = [
            (self.x0 + self.ancho // 2, self.y0 + 5),
            (self.x0 + self.ancho - 5, self.y0 + self.alto // 2.3),
            (self.x0 + self.ancho - self.ancho // 4, self.y0 + self.alto - 5),
            (self.x0 + self.ancho // 4, self.y0 + self.alto - 5),
            (self.x0 + 5, self.y0 + self.alto // 2.3)
        ]
        
        Herramientas.bresenham_poligono(Herramientas, pantalla, NEGRO, puntos)

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.modo = 8
        print("Modo Dibujar Poligono")
        return lienzo
