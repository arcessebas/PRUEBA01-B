class Material():
   def __init__(self,nombre,autor,precio):
        self.nombre = nombre
        self.autor = autor
        self.__precio=precio
   def get_precio(self):
       return self.__precio
   def set_precio(self,nuevo_precio):#se crea una variable para setear la variable precio
       if nuevo_precio<0:
           self.__precio=nuevo_precio#se inserta el nuevo valor si es mayor a 0 
       else:
           raise ValueError("error en el valor tiene que ser mayo a 0 ")
   def mostrar_datos(self):
        print(f"material:titulo={self.nombre,},el autor es={self.autor},y el precio es={self.get_precio()}")

       
       