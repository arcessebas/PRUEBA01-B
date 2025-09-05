from Material import Material
from libro import Libro
from periodico import Periodico
from revista import Revista

class Libreria:
    def __init__(self):
        self.materiales = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def mostrar_catalogo(self):
        for material in self.materiales:
            material.mostrar_datos()
            print("-" * 40)

if __name__ == "__main__":
    # Instanciar materiales
    libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 15000, 471)
    revista = Revista("National Geographic", "Varios", 8000, "Ciencia")
    periodico = Periodico("El País", "Varios", 500, "2025-09-04")

    # Usar el setter para modificar el precio de la revista
    revista.set_precio(9000)

    # Crear la biblioteca y agregar materiales
    biblioteca = Libreria()
    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(periodico)

    # Mostrar el catálogo completo
    biblioteca.mostrar_catalogo()