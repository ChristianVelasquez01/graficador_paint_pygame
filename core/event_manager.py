from pygame import QUIT, event
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION

from pygame.draw import circle
from drawing.tools import Herramientas

class Click:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lista_clicks = []

    def obtener_clicks(self, pantalla, lienzo, panel_izquierdo, panel_derecho):
        for evento in event.get():
            if evento.type == QUIT:
                return False
            elif evento.type == MOUSEBUTTONDOWN and evento.button == 1:
                self.x, self.y = evento.pos
                self.lista_clicks.append((self.x, self.y))
                print("Lista de clicks: " + str(self.lista_clicks))
                self.procesar_click_izquierdo(pantalla, lienzo, panel_izquierdo, panel_derecho)
            elif evento.type == MOUSEBUTTONDOWN and evento.button == 3:
                self.procesar_click_derecho(pantalla, lienzo)
        return True

    def procesar_click_izquierdo(self, pantalla, lienzo, panel_izquierdo, panel_derecho):
        if self.verificar_click_lienzo():
            if (lienzo.modo == 3 or 
                lienzo.modo == 7 or
                lienzo.modo == 8):
                circle(pantalla, lienzo.color_dibujo, (self.x, self.y), 1)

            if len(self.lista_clicks) == 1 and lienzo.modo == 1:
                lienzo.dibujar(pantalla)
                self.lista_clicks = []
            elif len(self.lista_clicks) == 1 and lienzo.modo == 9:
                lienzo.dibujar(pantalla, self.lista_clicks)
                self.lista_clicks = []
            elif len(self.lista_clicks) == 2 and (lienzo.modo == 2 or lienzo.modo == 4 or
                                                  lienzo.modo == 5 or lienzo.modo == 6):
                lienzo.dibujar(pantalla, self.lista_clicks)
                self.lista_clicks = []
            elif len(self.lista_clicks) == 3 and lienzo.modo == 7:
                lienzo.dibujar(pantalla, self.lista_clicks)
                self.lista_clicks = []
        else:
            self.procesar_click_panel(pantalla, lienzo, panel_izquierdo, panel_derecho)

    def procesar_click_derecho(self, pantalla, lienzo):
        if len(self.lista_clicks) >= 3 and (lienzo.modo == 3 or lienzo.modo == 8):
            lienzo.dibujar(pantalla, self.lista_clicks)
            self.lista_clicks = []

    def procesar_click_panel(self, pantalla, lienzo, panel_izquierdo, panel_derecho):
        if self.x < 100:
            lienzo = panel_izquierdo.obtener_boton(pantalla, lienzo, self.x, self.y)
            self.lista_clicks = []
        elif self.x > 825:
            lienzo = panel_derecho.obtener_boton(pantalla, lienzo, self.x, self.y)
            self.lista_clicks = []

    def verificar_click_lienzo(self):
        return all(100 <= click[0] <= 825 for click in self.lista_clicks)


class MovimientoCursor:
    def __init__(self, limite_izq, limite_der, radio):
        self.limite_izq = limite_izq
        self.limite_der = limite_der
        self.radio = radio
        self.ultimo_punto = None

    def movimiento_cursor_pincel(self, pantalla, color):
        for evento in event.get():
            if evento.type == MOUSEBUTTONUP:
                return False
            elif evento.type == MOUSEMOTION:
                self.x, self.y = evento.pos
                self.ultimo_punto = Herramientas.pincel(
                    Herramientas, pantalla, color, self.x, self.y,
                    self.ultimo_punto, self.limite_izq, self.limite_der, self.radio
                )
        return True
