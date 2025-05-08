from pygame import init, quit, display, time

from gui.panels.left_panel import PanelIzquierdo
from gui.panels.right_panel import PanelDerecho
from gui.canvas import Lienzo
from core.event_manager import Click

class Ventana:
    def __init__(self, ancho=1000, alto=700, titulo="Graficador Paint PyGame by C. Velasquez & J. Rojas"):
        self.configurar_pygame(ancho, alto, titulo)
        self.inicializar_componentes()
        self.inicializar_estado()

    def ejecutar_ventana(self):
        self.inicializar_interfaz()
        while self.ejecutando:
            self.ejecutando = self.click.obtener_clicks(self.pantalla, self.lienzo, self.panel_izquierdo, self.panel_derecho)
            display.flip()
            self.reloj.tick(60)
        quit()

    def configurar_pygame(self, ancho, alto, titulo):
        init()
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.pantalla = display.set_mode((self.ancho, self.alto))
        display.set_caption(self.titulo)
        self.reloj = time.Clock()

    def inicializar_componentes(self):
        self.panel_izquierdo = PanelIzquierdo(0, 0, self.ancho - 900, self.alto)
        self.panel_derecho = PanelDerecho(self.ancho - 175, 0, self.ancho - 825, self.alto)
        self.lienzo = Lienzo(100, 0, self.ancho - 275, self.alto)
        self.lista_pixeles = []
        self.click = Click(0, 0)

    def inicializar_estado(self):
        self.ejecutando = True

    def inicializar_interfaz(self):
        self.panel_izquierdo.dibujar_panel(self.pantalla)
        self.panel_derecho.dibujar_panel(self.pantalla)
        self.lienzo.dibujar_lienzo(self.pantalla)
