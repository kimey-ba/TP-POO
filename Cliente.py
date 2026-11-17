from Persona import Persona 
class Cliente (Persona):
    def __init__ (self, nombre, apellido, documento, telefono, id = None):
        super ().__init__(nombre, apellido, documento)
        self.telefono = telefono
        self.id = id
    def mostrar_datos (self):
        print ("Cliente nombre" ,self.nombre, "apellido" ,self.apellido, "documento" ,self.documento, "telefono" ,self.telefono, "id" ,self.id,)
