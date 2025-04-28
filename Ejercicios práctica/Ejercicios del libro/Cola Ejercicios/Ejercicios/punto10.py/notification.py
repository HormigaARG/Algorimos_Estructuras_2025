class Notification:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"Hora: [{self.hora}], Aplicacion: {self.aplicacion}, Mensaje: {self.mensaje}"
