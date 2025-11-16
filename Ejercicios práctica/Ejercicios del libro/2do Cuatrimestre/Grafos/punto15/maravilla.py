class Maravilla:
    def __init__(self, nombre, paises, tipo):
        self.nombre = nombre
        self.paises = paises          # lista o string
        self.tipo = tipo              # "natural" o "arquitectonica"

    def __str__(self):
        return f"{self.nombre} | {self.paises} | Tipo: {self.tipo}"
