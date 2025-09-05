from Material import Material
class revista(Material):
  def __init__(self,nombre,autor,precio,num_edicion):
      super().__init__(nombre,autor,precio)
      self.num_edicion=num_edicion
  def mostrar_datos(self):
        super().mostrar_datos()  # Llama al método de la clase padre
        print(f"Día de publicación: {self.num_edicion}")