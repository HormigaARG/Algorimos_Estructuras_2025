class Reporte:

    def __init__(self, general, fecha, codigo_blaster, fallo, tipo_soldado):
        self.general = general                    
        self.fecha = fecha                        # Fecha de la misión (máx. 20 distintas)
        self.codigo_blaster = codigo_blaster      # Código único de 8 dígitos
        self.fallo = fallo                        # True si falló, False si no
        self.tipo_soldado = tipo_soldado          # Tipo de soldado

    def __str__(self):
        return (f"General: {self.general} | "
                f"Fecha: {self.fecha} | "
                f"Código Blaster: {self.codigo_blaster} | "
                f"Fallo: {self.fallo} | "
                f"Soldado: {self.tipo_soldado}")