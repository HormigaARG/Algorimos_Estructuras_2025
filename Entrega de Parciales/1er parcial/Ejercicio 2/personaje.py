class Personaje:

    def __init__(self, nombre, nombre_real, es_villano, año_aparicion, biografia):
        self.nombre = nombre 
        self.nombre_real = nombre_real  
        self.año_aparicion = año_aparicion  
        self.es_villano = es_villano  
        self.biografia = biografia  

    def __str__(self):
        return f'{self.nombre} ({self.nombre_real}) - Año: {self.año_aparicion} - {"Villano" if self.es_villano else "Héroe"}'
    
    
def order_by_nombre(pj):
    return pj.nombre

def order_by_nombre_real(pj):
    return pj.nombre_real

def order_by_año_aparicion(pj):
    return pj.año_aparicion
