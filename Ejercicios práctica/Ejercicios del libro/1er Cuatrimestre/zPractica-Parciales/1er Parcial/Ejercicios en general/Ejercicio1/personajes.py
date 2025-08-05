class Personaje:
    def __init__(self, nombre, cantPelicula):
        self.nombre = nombre
        self.cantPelicula = cantPelicula

    def __str__(self):
        return f"Modelo: {self.nombre}, Película: {self.cantPelicula}"
    

