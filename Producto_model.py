from bd import BD
from Producto import Producto
class ProductoModel:

    def obtener_todos (self) -> list[Producto]:
      lista_productos = []
      base = BD()
      cursor = base.obtener_cursor()
      sql = "select id, nombre, precio, codigo from productos"
      cursor.execute(sql)
      for fila in cursor:
         producto = Producto (fila[1], fila[2], fila[3], fila[0])
         lista_productos.append(producto)
      base.cerrar_conexion()
      return lista_productos
   
    def guardar (self,producto:Producto):
        base = BD()
        cursor = base.obtener_cursor()
        sql="insert into productos (nombre, precio, codigo) values (%s,%s,%s)"
        values = (producto.nombre,producto.precio,producto.codigo)
        cursor.execute (sql, values)
        if cursor.rowcount > 0:
          print("Producto guardado correctamente")
        else:
          print("No se pudo guardar ningun producto")
        base.guardar_cambios()
        base.cerrar_conexion()
    
    def eliminar (self,id:int):
        base = BD()
        cursor = base.obtener_cursor()
        sql = "delete from productos where id = %s"
        values = (id,)
        cursor.execute (sql,values)
        if cursor.rowcount > 0:
          print("Producto eliminado correctamente")
          base.guardar_cambios()
        else:
          print("No se encontró ningún producto con ese ID")
        base.cerrar_conexion()
            