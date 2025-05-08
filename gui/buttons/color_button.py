from gui.buttons.button import Boton
from drawing.colors import *

class BotonColor(Boton):
    def dibujar_boton(self, pantalla):
        self.dibujar_base_boton(pantalla)

    def presionar_boton(self, lienzo, pantalla=None):
        lienzo.color_dibujo = self.color
        return lienzo
