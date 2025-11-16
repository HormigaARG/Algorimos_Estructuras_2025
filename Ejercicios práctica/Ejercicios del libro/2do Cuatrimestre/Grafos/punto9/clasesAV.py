class Aeropuerto:
    def __init__(self, nombre, lat, lon, pistas):
        self.nombre = nombre
        self.lat = lat
        self.lon = lon
        self.pistas = pistas

    def __str__(self):
        return f"{self.nombre} | ({self.lat},{self.lon}) | Pistas: {self.pistas}"

class Vuelo:
    def __init__(self, salida, arribo, empresa, costo, duracion, distancia):
        self.salida = salida
        self.arribo = arribo
        self.empresa = empresa
        self.costo = costo
        self.duracion = duracion
        self.distancia = distancia

    def __str__(self):
        return (f"{self.empresa} | {self.salida} → {self.arribo} | "
                f"Costo: {self.costo} | Duración: {self.duracion} | "
                f"Distancia: {self.distancia} km")
