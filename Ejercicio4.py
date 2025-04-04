"""Ejercicio #4: Gestión de productos e inventario
Diseñar una clase Producto que incluya atributos como código, nombre, precio y cantidad en
stock. Además, los estudiantes deberán implementar una clase Inventario que administre una
colección de objetos Producto, incorporando métodos para agregar, buscar, actualizar y
eliminar productos. Este ejercicio permite modelar situaciones reales de gestión de ventas y
refuerza el concepto de encapsulación y manejo de colecciones en programación orientada a
objetos"""

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad
    
    def __str__(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto
    
    def buscar_producto(self, codigo):
        return self.productos.get(codigo, None)
    
    def actualizar_producto(self, codigo, nombre=None, precio=None, cantidad=None):
        if codigo in self.productos:
            if nombre:
                self.productos[codigo].nombre = nombre
            if precio is not None:
                self.productos[codigo].precio = precio
            if cantidad is not None:
                self.productos[codigo].cantidad = cantidad
        else:
            print("Producto no encontrado.")
    
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
        else:
            print("Producto no encontrado.")
    
    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            codigo = int(input("Ingrese código del producto: "))
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio del producto: "))
            cantidad = int(input("Ingrese cantidad en stock: "))
            producto = Producto(codigo, nombre, precio, cantidad)
            inventario.agregar_producto(producto)
            print("Producto agregado.")
        
        elif opcion == "2":
            codigo = int(input("Ingrese código del producto a buscar: "))
            producto = inventario.buscar_producto(codigo)
            print(producto if producto else "Producto no encontrado.")
        
        elif opcion == "3":
            codigo = int(input("Ingrese código del producto a actualizar: "))
            nombre = input("Nuevo nombre: ") or None
            precio = input("Nuevo precio: ")
            precio = float(precio) if precio else None
            cantidad = input("Nueva cantidad en stock: ")
            cantidad = int(cantidad) if cantidad else None
            inventario.actualizar_producto(codigo, nombre, precio, cantidad)
            print("Producto actualizado.")
        
        elif opcion == "4":
            inventario.mostrar_inventario()
        
        elif opcion == "5":
            codigo = int(input("Ingrese código del producto a eliminar: "))
            inventario.eliminar_producto(codigo)
            print("Producto eliminado.")
        
        elif opcion == "6":
            print("Adios...")
            break
        
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
