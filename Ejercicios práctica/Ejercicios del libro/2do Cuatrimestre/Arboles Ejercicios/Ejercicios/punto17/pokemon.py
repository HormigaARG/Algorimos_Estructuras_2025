class Pokemon:

    def __init__(self, numero, nombre, tipos, debilidades):
        self.numero = numero              # Número en la Pokédex
        self.nombre = nombre              # Nombre del Pokémon
        self.tipos = tipos                # Lista de tipos (puede ser 1 o 2)
        self.debilidades = debilidades    # Lista de debilidades

    def __str__(self):
        return f'({self.numero}) {self.nombre} - Tipo/Tipos: {self.tipos} - Debilidades: {self.debilidades}'