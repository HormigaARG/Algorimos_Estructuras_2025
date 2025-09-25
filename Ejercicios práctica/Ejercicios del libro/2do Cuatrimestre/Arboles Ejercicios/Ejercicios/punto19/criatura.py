class Criatura:

    def __init__(self, nombre, derrotado_por=None, descripcion="", capturada=None):
        self.nombre = nombre                  # Nombre de la criatura
        self.derrotado_por = derrotado_por    # Héroe/Dios que la derrotó
        self.descripcion = descripcion        # Breve descripción
        self.capturada = capturada            # Quién la capturó
        
    def __str__(self):
        return (f'Criatura: {self.nombre} | '
                f'Derrotado por: {self.derrotado_por} | '
                f'Capturada: {self.capturada} | '
                f'Descripción: {self.descripcion}')