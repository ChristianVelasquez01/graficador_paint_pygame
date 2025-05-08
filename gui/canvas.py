from core.event_manager import MovimientoCursor

from drawing.tools import Herramientas
from drawing.colors import *

class Lienzo:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.modo = 1
        self.color_dibujo = NEGRO
        self.lista_cambios = []
        self.lista_rehacer = []

    def cambiar_color(self, color):
        self.color = color

    def dibujar_lienzo(self, pantalla):
        Herramientas.bresenham_rellenar_rectangulo(
            Herramientas, pantalla, BLANCO,
            self.x,
            self.y,
            self.x + self.ancho,
            self.y + self.alto)
        self.agregar_cambio(pantalla)

    def agregar_cambio(self, pantalla):
        superficie_lienzo = pantalla.subsurface(
            self.x, self.y, self.ancho, self.alto
        ).copy()
        self.lista_cambios.append(superficie_lienzo)
        if len(self.lista_cambios) > 10:
            self.lista_cambios.pop(0)
        self.lista_rehacer.clear()

    def dibujar(self, pantalla, lista_clicks=None):
        if self.modo == 1:
            movimiento_cursor = MovimientoCursor(100, 825, 1)
            dibujando = True
            while dibujando:
                dibujando = movimiento_cursor.movimiento_cursor_pincel(
                    pantalla, self.color_dibujo
                )
        elif self.modo == 2:
            Herramientas.bresenham_linea(
                pantalla, self.color_dibujo,
                lista_clicks[0][0], lista_clicks[0][1],
                lista_clicks[1][0], lista_clicks[1][1]
            )
        elif self.modo == 3:
            Herramientas.linea_curva(
                Herramientas, pantalla, self.color_dibujo, lista_clicks, False
            )
        elif self.modo == 4:
            Herramientas.bresenham_rectangulo(
                Herramientas, pantalla, self.color_dibujo,
                lista_clicks[0][0], lista_clicks[0][1],
                lista_clicks[1][0], lista_clicks[1][1]
            )
        elif self.modo == 5:
            Herramientas.bresenham_circunferencia(
                pantalla, self.color_dibujo,
                (lista_clicks[0][0] + lista_clicks[1][0]) // 2,
                (lista_clicks[0][1] + lista_clicks[1][1]) // 2,
                abs(lista_clicks[0][0] - lista_clicks[1][0]) // 2
            )
        elif self.modo == 6:
            Herramientas.bresenham_elipse(
                pantalla, self.color_dibujo,
                (lista_clicks[0][0] + lista_clicks[1][0]) // 2,
                (lista_clicks[0][1] + lista_clicks[1][1]) // 2,
                abs(lista_clicks[0][0] - lista_clicks[1][0]) // 2,
                abs(lista_clicks[0][1] - lista_clicks[1][1]) // 2
            )
        elif self.modo == 7:
            Herramientas.bresenham_triangulo(
                Herramientas, pantalla, self.color_dibujo,
                lista_clicks[0][0], lista_clicks[0][1],
                lista_clicks[1][0], lista_clicks[1][1],
                lista_clicks[2][0], lista_clicks[2][1]
            )
        elif self.modo == 8:
            Herramientas.bresenham_poligono(
                Herramientas, pantalla, self.color_dibujo, lista_clicks
            )
        elif self.modo == 9:
            Herramientas.rellenar_area(
                pantalla, self.color_dibujo,
                lista_clicks[0][0], lista_clicks[0][1],
                pantalla.get_at((lista_clicks[0][0], lista_clicks[0][1]))
            )       
        else:
            print("Modo no válido")

        self.agregar_cambio(pantalla)
