class Tarea:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo       

    def __str__(self):
        return f'Nombre: {self.nombre} - Tipo: {self.tipo}'