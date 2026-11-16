from Empleado import Empleado
from Cliente import Cliente 
from Producto import Producto 
from Cliente_model import ClienteModel 
from Empleado_model import EmpleadoModel 
from Producto_model import ProductoModel

def agregar_empleado():
    nombre = input("Agregue el nombre de su empleado:")
    apellido = input("Agregue el apellido de su empleado:")
    documento = input("Agregue el DNI de su empleado:")
    legajo = int(input("Agregue el legajo de su empleado:"))
    empleado = Empleado (nombre, apellido, documento, legajo)
    empleado_model = EmpleadoModel()
    empleado_model.guardar(empleado)

def eliminar_empleado():
    empleado_model = EmpleadoModel()
    id = int(input("Ingrese el id del empleado a eliminar:"))
    empleado_model.eliminar(id)
        
def ver_empleados():
    empleado_model = EmpleadoModel()
    lista_empleados = empleado_model.obtener_todos()
    if lista_empleados is not None and len(lista_empleados) > 0:
        for empleado in lista_empleados: 
            empleado.mostrar_datos()  
    else:
        print ("No hay empleados en la base de datos")

def agregar_cliente():
    nombre = input("Agregue el nombre de su cliente:")
    apellido = input("Agregue el apellido de su cliente:")
    documento = input("Agregue el dni de su cliente:")
    telefono = input("Agregue el telefono de su cliente:")
    cliente = Cliente (nombre, apellido, documento, telefono)
    cliente_model = ClienteModel()
    cliente_model.guardar(cliente)

def eliminar_cliente():
    cliente_model = ClienteModel()
    id = int(input("Ingrese el id del cliente a eliminar:"))
    cliente_model.eliminar(id)
def ver_clientes():
    cliente_model = ClienteModel()
    lista_clientes = cliente_model.obtener_todos()
    if lista_clientes is not None and len(lista_clientes) > 0:
        for cliente in lista_clientes:
            cliente.mostrar_datos()
    else:
        print ("No hay clientes en la base de datos")

def agregar_producto():
    producto_nombre = input("Ingrese el nombre del producto:")
    precio_producto = float(input("Ingrese el precio del producto:"))
    codigo_producto = float(input("Ingrese el codigo de su producto:"))
    producto = Producto (producto_nombre, precio_producto, codigo_producto)
    producto_model = ProductoModel()
    producto_model.guardar(producto)

def eliminar_producto():
      producto_model = ProductoModel()
      id = int(input("Ingrese el id del producto a eliminar:"))
      producto_model.eliminar(id)
   
def ver_productos():
   producto_model = ProductoModel()
   lista_productos = producto_model.obtener_todos()
   if lista_productos is not None and len(lista_productos) > 0:
        for producto in lista_productos:
            producto.mostrar_datos()
   else:
       print ("No hay productos en la base de datos")

def menu_empleados ():
    menu_empleado = True 
    while menu_empleado: 
        print ("---Menu Empleados---")
        print ("Opcion 1: agregar empleado")
        print ("Opcion 2: eliminar empleado")
        print ("Opcion 3: ver empleados")
        print ("Opcion 4: salir")
        menu = int(input("Ingrese una opcion del 1 al 4 por favor:"))
        if menu == 1:
            agregar_empleado()
        elif menu == 2:
            eliminar_empleado()
        elif menu == 3:
            ver_empleados ()
        elif menu == 4:
            menu_empleado = False 
#en el menu empleados el usuario podra elegir distintas opciones para trabajar con los empleados 
#tambien se decidio que cada funcionalidad este en otro metodo para que el codigo sea mas legible y facil de mantener 
def menu_clientes():
    menu_clientes = True
    while menu_clientes:
        print ("---Menu Clientes---")
        print ("Opcion 1: agregar cliente")
        print ("Opcion 2: eliminar un cliente") 
        print ("Opcion 3: ver clientes") 
        print ("Opcion 4: salir") 
        menu_clientes = int(input("Ingrese una opcion del 1 al 4 por favor: ")) 
        if menu_clientes == 1:
            agregar_cliente()
        elif menu_clientes == 2:
            eliminar_cliente()
        elif menu_clientes == 3:
            ver_clientes()
        elif menu_clientes == 4:
            menu_clientes = False

def menu_productos():
    menu_productos = True 
    while menu_productos:
        print ("---Menu Productos---")  
        print ("Opcion 1: agregar producto")
        print ("Opcion 2: eliminar producto")
        print ("Opcion 3: ver productos")
        print ("Opcion 4: salir")
        menu_productos = int(input("Ingrese una opcion del 1 al 4 por favor:"))
        if menu_productos == 1:
            agregar_producto()
        elif menu_productos == 2:
            eliminar_producto()
        elif menu_productos == 3:
            ver_productos()
        elif menu_productos == 4:
            menu_productos = False 
abierto = True    
while abierto:
    print ("---Menu principal---")
    print ("Opcion 1: empleados")
    print ("Opcion 2: clientes")
    print ("Opcion 3: productos")
    opciones_principal = int(input("Ingrese una opcion del 1 al 3 por favor:"))
    if opciones_principal == 1:
        menu_empleados () 
    elif opciones_principal == 2:
        menu_clientes()
    elif opciones_principal == 3:
        menu_productos()        