from list_ import List

class Entrenador:
    def __init__(self, nombre, cantTorneosGanados, cantBP, cantBG):
        self.nombre= nombre
        self.cantTorneosGanados = cantTorneosGanados
        self.cantBP = cantBP
        self.cantBG = cantBG
        self.pokemones = List()
        
    def __str__(self):
        return f"{self.nombre}, T.ganados:{self.cantTorneosGanados}, C. batallas perdidas: {self.cantBP}, C. batallas ganadas: {self.cantBG}"
        
class Pokemon:
    
    def __init__(self, nombre, nivel, tipo, subtipo, nombreEntrenador):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo
        self.nombreEntrenador = nombreEntrenador 
    
    def __str__(self):
        return f"Materia: {self.nombre}, Nota: {self.nivel}, Fecha: {self.tipo}"
    
def order_by_nombre(entrenador):
    return entrenador.nombre
