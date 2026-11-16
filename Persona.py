class Persona: 
    def __init__ (self, nombre, apellido, documento):
        self.nombre = nombre 
        self.apellido = apellido
        self.documento = documento

    def mostrar_datos (self):
        print("Persona nombre:" ,self.nombre, "Apellido" ,self.apellido, "Documento" ,self.documento)