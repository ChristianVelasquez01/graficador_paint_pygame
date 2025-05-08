from pygame.draw import circle

class Herramientas:
    @staticmethod
    def bresenham_linea(pantalla, color, x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        
        while True:
            circle(pantalla, color, (x0, y0), 1)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
    
    @staticmethod
    def spline_catmull_rom(p0, p1, p2, p3, num_puntos=1000):
        puntos = []
        for i in range(num_puntos):
            t = i / num_puntos
            t2 = t * t
            t3 = t2 * t

            x = 0.5 * ((2 * p1[0]) +
                    (-p0[0] + p2[0]) * t +
                    (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                    (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)

            y = 0.5 * ((2 * p1[1]) +
                    (-p0[1] + p2[1]) * t +
                    (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                    (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)

            puntos.append((int(x), int(y)))
        return puntos

    @staticmethod
    def linea_curva(self, pantalla, color, puntos, panel, num_puntos=1000):
        puntos = [puntos[0]] + puntos + [puntos[-1]]
        
        if len(puntos) < 4:
            return
        for i in range(1, len(puntos) - 2):
            segmento = self.spline_catmull_rom(puntos[i - 1], puntos[i], puntos[i + 1], puntos[i + 2], num_puntos)
            for punto in segmento:
                if panel:
                    circle(pantalla, color, punto, 1)
                else:
                    if 100 <= punto[0] <= 825:
                        circle(pantalla, color, punto, 1)
    
    @staticmethod
    def bresenham_circunferencia(pantalla, color, x_centro, y_centro, radio):
        x = 0
        y = radio
        d = 3 - 2 * radio
        while y >= x:
            circle(pantalla, color, (x_centro + x, y_centro + y), 1)
            circle(pantalla, color, (x_centro - x, y_centro + y), 1)
            circle(pantalla, color, (x_centro + x, y_centro - y), 1)
            circle(pantalla, color, (x_centro - x, y_centro - y), 1)
            circle(pantalla, color, (x_centro + y, y_centro + x), 1)
            circle(pantalla, color, (x_centro - y, y_centro + x), 1)
            circle(pantalla, color, (x_centro + y, y_centro - x), 1)
            circle(pantalla, color, (x_centro - y, y_centro - x), 1)
            if d < 0:
                d = d + 4 * x + 6
            else:
                d = d + 4 * (x - y) + 10
                y -= 1
            x += 1
    
    @staticmethod
    def bresenham_elipse(pantalla, color, x_centro, y_centro, radio_x, radio_y):
        x = 0
        y = radio_y
        d1 = (radio_y**2) - (radio_x**2 * radio_y) + (0.25 * radio_x**2)
        dx = 2 * radio_y**2 * x
        dy = 2 * radio_x**2 * y

        while dx < dy:
            circle(pantalla, color, (x_centro + x, y_centro + y), 1)
            circle(pantalla, color, (x_centro - x, y_centro + y), 1)
            circle(pantalla, color, (x_centro + x, y_centro - y), 1)
            circle(pantalla, color, (x_centro - x, y_centro - y), 1)
            if d1 < 0:
                x += 1
                dx += 2 * radio_y**2
                d1 += dx + radio_y**2
            else:
                x += 1
                y -= 1
                dx += 2 * radio_y**2
                dy -= 2 * radio_x**2
                d1 += dx - dy + radio_y**2

        d2 = ((radio_y**2) * ((x + 0.5)**2)) + ((radio_x**2) * ((y - 1)**2)) - (radio_x**2 * radio_y**2)
        while y >= 0:
            circle(pantalla, color, (x_centro + x, y_centro + y), 1)
            circle(pantalla, color, (x_centro - x, y_centro + y), 1)
            circle(pantalla, color, (x_centro + x, y_centro - y), 1)
            circle(pantalla, color, (x_centro - x, y_centro - y), 1)
            if d2 > 0:
                y -= 1
                dy -= 2 * radio_x**2
                d2 += radio_x**2 - dy
            else:
                y -= 1
                x += 1
                dx += 2 * radio_y**2
                dy -= 2 * radio_x**2
                d2 += dx - dy + radio_x**2
            
    @staticmethod
    def bresenham_rectangulo(self, pantalla, color, x0, y0, x1, y1):
        self.bresenham_linea(pantalla, color, x0, y0, x1, y0)
        self.bresenham_linea(pantalla, color, x1, y0, x1, y1)
        self.bresenham_linea(pantalla, color, x1, y1, x0, y1)
        self.bresenham_linea(pantalla, color, x0, y1, x0, y0)
    
    @staticmethod
    def bresenham_rellenar_rectangulo(self, pantalla, color, x0, y0, x1, y1):
        if y0 > y1:
            y0, y1 = y1, y0
        for y in range(y0, y1 + 1):
            self.bresenham_linea(pantalla, color, x0, y, x1, y)
    
    @staticmethod
    def bresenham_triangulo(self, pantalla, color, x0, y0, x1, y1, x2, y2):
        self.bresenham_linea(pantalla, color, x0, y0, x1, y1)
        self.bresenham_linea(pantalla, color, x1, y1, x2, y2)
        self.bresenham_linea(pantalla, color, x2, y2, x0, y0)
    
    @staticmethod
    def bresenham_poligono(self, pantalla, color, puntos):
        n = len(puntos)
        for i in range(n):
            x0, y0 = puntos[i]
            x1, y1 = puntos[(i + 1) % n]
            self.bresenham_linea(pantalla, color, x0, y0, x1, y1)
    
    @staticmethod
    def rellenar_area(pantalla, color, x, y, color_original):
        if color_original == color:
            return

        ancho, alto = pantalla.get_size()
        pila = [(x, y)]

        while pila:
            cx, cy = pila.pop()
            if cx < 0 or cy < 0 or cx >= ancho or cy >= alto:
                continue
            if pantalla.get_at((cx, cy)) != color_original:
                continue

            pantalla.set_at((cx, cy), color)

            pila.append((cx + 1, cy))
            pila.append((cx - 1, cy))
            pila.append((cx, cy + 1))
            pila.append((cx, cy - 1))
    
    @staticmethod
    def pincel(self, pantalla, color, x, y, ultimo_punto, limite_izq, limite_der, radio):
        if ultimo_punto is not None:
            x0, y0 = ultimo_punto
            if limite_izq <= x0 <= limite_der:
                self.dibujar_linea_dentro_limites(self, pantalla, color, limite_izq, limite_der, x0, y0, x, y)
            elif x0 < limite_izq and x >= limite_izq:
                self.bresenham_linea(pantalla, color, limite_izq, y0, x, y)
            elif x0 > limite_der and x <= limite_der:
                self.bresenham_linea(pantalla, color, limite_der, y0, x, y)
        elif limite_izq <= x <= limite_der:
            circle(pantalla, color, (x, y), radio)

        if limite_izq <= x <= limite_der:
            circle(pantalla, color, (x, y), radio)

        return (x, y)

    @staticmethod
    def dibujar_linea_dentro_limites(self, pantalla, color, limite_izq, limite_der, x0, y0, x, y):
        if x < limite_izq:
            self.bresenham_linea(pantalla, color, x0, y0, limite_izq, y)
        elif x > limite_der:
            self.bresenham_linea(pantalla, color, x0, y0, limite_der, y)
        else:
            self.bresenham_linea(pantalla, color, x0, y0, x, y)
