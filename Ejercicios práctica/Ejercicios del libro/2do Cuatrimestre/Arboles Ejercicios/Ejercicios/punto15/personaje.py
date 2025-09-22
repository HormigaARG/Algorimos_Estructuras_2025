class Personaje:
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura  # en cm
        self.peso = peso      # en kilogramos

    def __str__(self):
        return f'{self.nombre} - Altura: {self.altura}cm - Peso: {self.peso}kg'
     
