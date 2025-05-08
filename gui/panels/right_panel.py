from gui.panels.panel import Panel
from drawing.colors import *

from gui.buttons.color_button import BotonColor
from gui.buttons.undo_button import BotonDeshacer
from gui.buttons.redo_button import BotonRehacer

class PanelDerecho(Panel):
    def crear_botones(self):
        colores = [
            ROJO, NARANJA, AMARILLO, VERDE_CLARO, VERDE, VERDE_OSCURO,
            AZUL_CLARO, AZUL, AZUL_OSCURO, ROSA, PURPURA, MORADO,
            MARRON_CLARO, MARRON_OSCURO, BLANCO, GRIS_CLARO, GRIS, NEGRO
        ]
        botones_colores = [
            BotonColor(850 + (i // 9) * 75, 25 + (i % 9) * 55, 50, 50, color)
            for i, color in enumerate(colores)
        ]
        botones_cambios = [
            BotonDeshacer(850, 575, 50, 50, BLANCO),
            BotonRehacer(925, 575, 50, 50, BLANCO)
        ]
        
        self.lista_botones = botones_colores + botones_cambios

    def dibujar_panel(self, pantalla):
        super().dibujar_panel(pantalla)
        self.lista_botones[-3].seleccionar_boton(pantalla)

    def actualizar_seleccion(self, pantalla, lienzo):
        for boton in self.lista_botones:
            boton.deseleccionar_boton(pantalla)
        for boton in self.lista_botones[:-2]:
            if lienzo is not None and boton.color == lienzo.color_dibujo:
                boton.seleccionar_boton(pantalla)
                break
