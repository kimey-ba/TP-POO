class Producto:
    def __init__ (self, nombre, precio, codigo, id):
        self.nombre = nombre 
        self.precio = precio 
        self.codigo = codigo
        self.id = id
    def mostrar_datos (self):
            print ("Producto nombre" ,self.nombre, "precio" ,self.precio, "codigo" ,self.codigo, "id" ,self.id,)