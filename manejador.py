from contacto import Contacto
import os

class ManejadorContactos:
    def __init__(self, archivo):
        self.archivo = archivo

    def crear_contacto(self, contacto):
        with open(self.archivo, "a") as file:
            file.write(f"{contacto.nombre},{contacto.telefono}\n")

    def leer_contactos(self):
        contactos = []
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as file:
                for linea in file:
                    partes = linea.strip().split(",")
                    if len(partes) == 2:
                        contactos.append(Contacto(partes[0], partes[1]))
        return contactos

    def actualizar_contacto(self, nombre_antiguo, nuevo_contacto):
        actualizado = False
        contactos = self.leer_contactos()
        with open(self.archivo, "w") as file:
            for contacto in contactos:
                if contacto.nombre == nombre_antiguo:
                    file.write(f"{nuevo_contacto.nombre},{nuevo_contacto.telefono}\n")
                    actualizado = True
                else:
                    file.write(f"{contacto.nombre},{contacto.telefono}\n")
        return actualizado

    def eliminar_contacto(self, nombre):
        eliminado = False
        contactos = self.leer_contactos()
        with open(self.archivo, "w") as file:
            for contacto in contactos:
                if contacto.nombre != nombre:
                    file.write(f"{contacto.nombre},{contacto.telefono}\n")
                else:
                    eliminado = True
        return eliminado