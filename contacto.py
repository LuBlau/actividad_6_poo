class Contacto:
    def __init__(self, nombre, telefono:int):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"