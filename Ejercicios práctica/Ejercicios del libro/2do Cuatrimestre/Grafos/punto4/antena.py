class Antena:
    def __init__(self, codigo, lat, lon, velocidad):
        self.codigo = codigo
        self.lat = lat
        self.lon = lon
        self.velocidad = velocidad

    def __str__(self):
        return (f"Antena {self.codigo} | Ubicación: ({self.lat}, {self.lon}) | "
                f"Velocidad: {self.velocidad} Mb/s")
