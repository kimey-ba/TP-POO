import mysql.connector
class BD:
    def __init__ (self):#aca definimos una funcion que utiliza un constructor
        # que se recibe a si mismo por parametro luego con un nuevo self definimos la variable conexion 1 que guarda los datos de la conexion 
        #con la base de datos 
        self.conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="cafeteria")      
    def obtener_cursor(self):
        return self.conexion1.cursor()#aca devuelvo un cursor para que quien llame a este metodo pueda interactuar con la base de datos 
    def cerrar_conexion (self):
        self.conexion1.close()
    def guardar_cambios(self):
        self.conexion1.commit()