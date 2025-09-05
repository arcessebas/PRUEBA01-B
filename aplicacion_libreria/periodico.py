from Material import Material

class Periodico(Material):
    def __init__(self, nombre, autor, precio, dia_publicacion):
        super().__init__(nombre, autor, precio)
        self.dia_publicacion = dia_publicacion
    def mostrar_datos(self):
        super().mostrar_datos()  # Llama al método de la clase padre
        print(f"Día de publicación: {self.dia_publicacion}")

        
