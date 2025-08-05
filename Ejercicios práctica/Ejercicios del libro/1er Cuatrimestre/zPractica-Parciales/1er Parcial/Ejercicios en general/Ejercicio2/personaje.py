class Personaje:
    def __init__(self, nombrePJ, nombreSH, genero):
        self.nombrePJ = nombrePJ
        self.nombreSH = nombreSH
        self.genero = genero

    def __str__(self):
        return f"Modelo: {self.nombrePJ}, Película: {self.nombreSH}, Genero: {self.genero}"
    
    


