from pygame import display
from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonRehacer(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + 7,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto // 2
        )
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto // 2,
            self.x0 + 7,
            self.y0 + self.alto - 7
        )
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + 7,
            self.x0 + 7,
            self.y0 + self.alto - 7
        )

    def presionar_boton(self, lienzo, pantalla):
        if len(lienzo.lista_rehacer) > 0:
            lienzo.lista_cambios.append(lienzo.lista_rehacer.pop())
            pantalla.blit(lienzo.lista_cambios[-1], (lienzo.x, lienzo.y))
            display.update(lienzo.x, lienzo.y, lienzo.ancho, lienzo.alto)
            print("Boton Rehacer")
        else:
            print("No hay cambios para rehacer")
        return lienzo
