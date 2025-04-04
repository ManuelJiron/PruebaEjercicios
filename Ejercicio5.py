"""Ejercicio #5: Procesamiento de pedidos y clientes
Crear una clase Cliente con atributos básicos (por ejemplo, ID, nombre y contacto) y una clase
Pedido que contenga información sobre el cliente, la lista de productos solicitados y el total de
la venta. Se podrá incluir el uso de herencia para diferenciar entre tipos de clientes (por
ejemplo, cliente regular y cliente VIP) y aplicar descuentos especiales, demostrando el uso de la
herencia y el polimorfismo para adaptar el comportamiento de los objetos según el tipo de
cliente"""

class Cliente:
    def __init__(self, id_cliente, nombre, contacto):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.contacto = contacto
    
    def obtener_descuento(self, total):
        """Método que será sobrescrito por clases derivadas."""
        return 0  # Cliente base no tiene descuento
    
    def __str__(self):
        return f"Cliente {self.nombre} (ID: {self.id_cliente})"

class ClienteRegular(Cliente):
    def obtener_descuento(self, total):
        return total * 0.05  # 5% de descuento

class ClienteVIP(Cliente):
    def obtener_descuento(self, total):
        return total * 0.10  # 10% de descuento

class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos  
    
    def calcular_total(self):
        total = sum(precio for _, precio in self.productos)
        descuento = self.cliente.obtener_descuento(total)
        return total - descuento
    
    def mostrar_detalle(self):
        print(f"Pedido de: {self.cliente}")
        print("Productos:")
        for producto, precio in self.productos:
            print(f"- {producto}: ${precio:.2f}")
        print(f"Total con descuento: ${self.calcular_total():.2f}")

# Ejemplo de uso

cliente1 = ClienteRegular(1, "Manuel Jiron", "manueljiron@gmail.com")
cliente2 = ClienteVIP(2, "Gabriel Juarez", "gabrieljuarez@gmail.com")

pedido1 = Pedido(cliente1, [("Laptop", 5000), ("Mouse", 52)])
pedido2 = Pedido(cliente2, [("Smartphone", 800), ("Audífonos", 234)])

pedido1.mostrar_detalle()
pedido2.mostrar_detalle()