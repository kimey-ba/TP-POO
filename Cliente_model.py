from bd import BD
from Cliente import Cliente  
class ClienteModel:
    
    def obtener_todos (self):
        lista_clientes = []
        base = BD()
        cursor = base.obtener_cursor()
        sql = "select id, nombre, apellido, documento, telefono from clientes"
        cursor.execute(sql)
        for fila in cursor:
            cliente = Cliente (fila[1], fila[2], fila[3], fila[4], fila[0])
            lista_clientes.append(cliente)
        base.cerrar_conexion()
        return lista_clientes
    
    def guardar(self,cliente:Cliente):
        base = BD()
        cursor = base.obtener_cursor()
        sql="insert into clientes(nombre, apellido, documento, telefono) values (%s,%s,%s,%s)"
        values = (cliente.nombre,cliente.apellido,cliente.documento,cliente.telefono)
        cursor.execute (sql, values)
        base.guardar_cambios()
        if cursor.rowcount > 0:
            print("Cliente guardado correctamente")
        else:
            print("No se pudo guardar ningun cliente")
        base.cerrar_conexion()
    
    def eliminar(self,id:int):
        base = BD()
        cursor = base.obtener_cursor()
        sql = "delete from clientes where id = %s"
        values = (id,)
        cursor.execute (sql,values)
        if cursor.rowcount > 0:
            print("Cliente eliminado correctamente")
        else:
            print("No se encontró ningún cliente con ese ID")

        base.guardar_cambios()
        base.cerrar_conexion()
