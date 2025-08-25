class Personaje:

    def __init__(self, nombre, especie, año_nacimiento, color_sable, ranking, maestro):
        self.nombre = nombre 
        self.especie = especie  
        self.año_nacimiento = año_nacimiento  
        self.color_sable = color_sable   
        self.ranking = ranking
        self.maestro = maestro

    def __str__(self):
        return f'{self.nombre} ({self.especie}) - Año: {self.año_nacimiento} - Color: {self.color_sable} - Ranking: {self.ranking} - Maestro: {self.maestro}'
     
