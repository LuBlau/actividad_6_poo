import tkinter as tk
from tkinter import messagebox
from manejador import ManejadorContactos
from contacto import Contacto

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Libreta de Contactos")
        self.root.geometry("385x410")
        self.root.configure(bg="#F1EDF5")

        self.manejador = ManejadorContactos("contactos.txt")

        tk.Label(root, text="Libreta de contactos", font=("Arial", 13, "bold")).grid(column=0, row=0, columnspan=2, pady=(20, 5))

        # Etiquetas y entradas
        tk.Label(root, text="Nombre:", bg="#F1EDF5").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entrada_nombre = tk.Entry(root, bg="#E4DBEE")
        self.entrada_nombre.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Teléfono:", bg="#F1EDF5").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entrada_telefono = tk.Entry(root, bg="#E4DBEE")
        self.entrada_telefono.grid(row=2, column=1, padx=10, pady=10)

        # Botones
        tk.Button(root, text="Crear", bg="#B198CE", command=self.crear_contacto, width=15).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Leer", bg="#B198CE",command=self.leer_contactos, width=15).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Actualizar", bg="#B198CE",command=self.actualizar_contacto, width=15).grid(row=4, column=0, pady=10)
        tk.Button(root, text="Eliminar", bg="#B198CE",command=self.eliminar_contacto, width=15).grid(row=4, column=1, pady=10)

        # Área de salida
        self.area_salida = tk.Text(root, height=10, width=45)
        self.area_salida.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def crear_contacto(self):
        nombre = self.entrada_nombre.get().strip()
        telefono = self.entrada_telefono.get().strip()
        if nombre and telefono:
            if not telefono.isdigit():
                messagebox.showerror("Error", "El teléfono debe contener solo números.")
                return
            else:
                contacto = Contacto(nombre, telefono)
                self.manejador.crear_contacto(contacto)
                messagebox.showinfo("Éxito", "Contacto creado")
                self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Completa todos los campos")

    def leer_contactos(self):
        contactos = self.manejador.leer_contactos()
        self.area_salida.delete("1.0", tk.END)
        if contactos:
            for contacto in contactos:
                self.area_salida.insert(tk.END, str(contacto) + "\n")
        else:
            self.area_salida.insert(tk.END, "No hay contactos registrados.")

    def actualizar_contacto(self):
        nombre_antiguo = self.entrada_nombre.get().strip()
        telefono_nuevo = self.entrada_telefono.get().strip()
        if nombre_antiguo and telefono_nuevo:
            nuevo_contacto = Contacto(nombre_antiguo, telefono_nuevo)
            if self.manejador.actualizar_contacto(nombre_antiguo, nuevo_contacto):
                messagebox.showinfo("Éxito", "Contacto actualizado")
            else:
                messagebox.showwarning("Error", "No se encontró el contacto")
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Completa todos los campos")

    def eliminar_contacto(self):
        nombre = self.entrada_nombre.get().strip()
        if nombre:
            if self.manejador.eliminar_contacto(nombre):
                messagebox.showinfo("Éxito", "Contacto eliminado")
            else:
                messagebox.showwarning("Error", "No se encontró el contacto")
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Ingresa un nombre")

    def limpiar_campos(self):
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_telefono.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()

if __name__ == "__main__":
    main()