from drawing.tools import Herramientas
from gui.buttons.button import Boton
from drawing.colors import *

class BotonLimpiar(Boton):
    def dibujar_boton(self, pantalla):
        self.pantalla = pantalla
        self.dibujar_base_boton(pantalla)
        
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + 7,
            self.y0 + 7,
            self.x0 + self.ancho - 7,
            self.y0 + self.alto - 7
        )
        Herramientas.bresenham_linea(pantalla, NEGRO,
            self.x0 + self.ancho - 7,
            self.y0 + 7,
            self.x0 + 7,
            self.y0 + self.alto - 7
        )

    def presionar_boton(self, lienzo, pantalla):
        Herramientas.bresenham_rellenar_rectangulo(
            Herramientas, pantalla, BLANCO, 100, 0,
            lienzo.ancho + 100, lienzo.alto)
        print("Boton Limpiar Lienzo")
        lienzo.lista_cambios = []
        lienzo.agregar_cambio(pantalla)
        return lienzo
