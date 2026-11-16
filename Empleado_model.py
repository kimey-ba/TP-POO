from bd import BD
from Empleado import Empleado 
class EmpleadoModel: 
    
    def obtener_todos(self):
        lista_empleados = []
        base = BD()
        cursor = base.obtener_cursor()
        sql = "select id, nombre, apellido, documento, legajo from empleados"
        cursor.execute(sql)
        for fila in cursor:
           empleado = Empleado (fila[1], fila[2], fila[3], fila[4], fila[0])
           lista_empleados.append(empleado)
        base.cerrar_conexion()
        return lista_empleados
         
   
    def guardar (self,empleado:Empleado):
        base = BD()
        cursor = base.obtener_cursor()#devuelve un cursor para interactuar con la base de datos 
        sql="insert into empleados (nombre, apellido, documento, legajo) values (%s,%s,%s,%s)"
        values =  (empleado.nombre,empleado.apellido,empleado.documento,empleado.legajo)
        cursor.execute (sql, values)
        base.guardar_cambios()
        if cursor.rowcount > 0:
           print("Empleado guardado correctamente")
        else:
           print("No se pudo guardar ningun empleado")
        base.cerrar_conexion()
    
    def eliminar (self,id:int):
        base = BD()
        cursor = base.obtener_cursor()
        sql = "delete from empleados where id = %s"
        values = (id,)
        cursor.execute (sql,values)
        if cursor.rowcount > 0:
         print("Empleado eliminado correctamente")
         base.guardar_cambios()
        else:
         print("No se encontró ningún empleado con ese ID")
        base.cerrar_conexion()
                    