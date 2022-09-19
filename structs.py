


class Point():
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.z = 1

class Line():
    def __init__(self, pi, pf):
        self.xi = pi.x
        self.xf = pf.x
        self.yi = pi.y
        self.yf = pf.y
        self.zi = pi.z
        self.zf = pf.z

class Wireframe():
    def __init__(self):
        self.pontos = []

    def add_ponto(self, p):
        self.pontos.append(p)


