from Persona import Persona
class Empleado (Persona):
    
    def __init__ (self, nombre, apellido, documento, legajo, id):
        super ().__init__(nombre, apellido, documento)
        self.legajo = legajo
        self.id = id  
    
    def mostrar_datos (self):
        print("Empleado nombre:" ,self.nombre, "Apellido" ,self.apellido, "Documento" ,self.documento, "Legajo" ,self.legajo, "id" ,self.id,)