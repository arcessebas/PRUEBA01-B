from Material import Material
class libro(Material):
  def __init__(self,nombre,autor,precio,paginas):
      super().__init__(nombre,autor,precio)
      self.paginas=paginas
  def mostrar_datos(self):
        super().mostrar_datos()  # Llama al método de la clase padre
        print(f"Día de publicación: {self.paginas}")
