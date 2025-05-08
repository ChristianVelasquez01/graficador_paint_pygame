from gui.panels.panel import Panel
from drawing.colors import *

from gui.buttons.brush_button import BotonPincel
from gui.buttons.line_button import BotonLinea
from gui.buttons.curved_line_button import BotonCurva
from gui.buttons.rectangle_button import BotonRectangulo
from gui.buttons.circumference_button import BotonCircunferencia
from gui.buttons.ellipse_button import BotonElipse
from gui.buttons.triangle_button import BotonTriangulo
from gui.buttons.polygon_button import BotonPoligono
from gui.buttons.fill_button import BotonRellenar
from gui.buttons.clear_button import BotonLimpiar

class PanelIzquierdo(Panel):
    def crear_botones(self):
        botones_config = [
            (BotonPincel, 25, 25, BLANCO),
            (BotonLinea, 25, 80, BLANCO),
            (BotonCurva, 25, 135, BLANCO),
            (BotonRectangulo, 25, 190, BLANCO),
            (BotonCircunferencia, 25, 245, BLANCO),
            (BotonElipse, 25, 300, BLANCO),
            (BotonTriangulo, 25, 355, BLANCO),
            (BotonPoligono, 25, 410, BLANCO),
            (BotonRellenar, 25, 465, BLANCO),
            (BotonLimpiar, 25, 575, BLANCO),
        ]
        self.lista_botones = [boton_cls(x, y, 50, 50, color) for boton_cls, x, y, color in botones_config]

    def dibujar_panel(self, pantalla):
        super().dibujar_panel(pantalla)
        self.lista_botones[0].seleccionar_boton(pantalla)

    def actualizar_seleccion(self, pantalla, lienzo):
        for boton in self.lista_botones:
            boton.deseleccionar_boton(pantalla)
        if 1 <= lienzo.modo <= len(self.lista_botones):
            self.lista_botones[lienzo.modo - 1].seleccionar_boton(pantalla)
