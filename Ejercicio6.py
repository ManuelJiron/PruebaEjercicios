"""Ejercicio #6 Facturación y reportes de ventas
Crear una clase Factura que simule el proceso de facturación de una venta. Los estudiantes
deberán encapsular los datos internos de la factura (como los detalles de los productos,
cantidades, precios y descuentos) y proveer métodos para calcular el total de la venta, generar
reportes simples y validar la integridad de la información. Este ejercicio enfatiza la importancia
de ocultar la implementación interna y de diseñar interfaces claras y seguras para la gestión de
transacciones comerciales.
"""

class Factura:
    def __init__(self, numero_factura, cliente):
        self.__numero_factura = numero_factura  
        self.__cliente = cliente  
        self.__items = []  # Lista privada de ítems en la factura

    def agregar_item(self, descripcion, cantidad, precio_unitario, descuento=0):
        if cantidad <= 0 or precio_unitario < 0 or descuento < 0:
            raise ValueError("Cantidad, precio y descuento deben ser valores positivos.")
        item = {
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "descuento": descuento,
            "subtotal": (cantidad * precio_unitario) - descuento
        }
        self.__items.append(item)

    def calcular_total(self):
        return sum(item["subtotal"] for item in self.__items)

    def generar_reporte(self):
        reporte = f"Factura N° {self.__numero_factura}\nCliente: {self.__cliente}\n"
        reporte += "=" * 40 + "\n"
        for item in self.__items:
            reporte += (f"{item['descripcion']} - Cantidad: {item['cantidad']} - "
                        f"Precio: {item['precio_unitario']:.2f} - "
                        f"Descuento: {item['descuento']:.2f} - "
                        f"Subtotal: {item['subtotal']:.2f}\n")
        reporte += "=" * 40 + "\n"
        reporte += f"Total a pagar: {self.calcular_total():.2f}\n"
        return reporte

    def validar_factura(self):
        return len(self.__items) > 0 and self.calcular_total() > 0

# Ejemplo de uso
factura = Factura("80003400", "Manuel Jiron")
factura.agregar_item("Laptop", 1, 1200.00, 50.00)
factura.agregar_item("Mouse", 2, 25.00)
print(factura.generar_reporte())
print("Factura válida:", factura.validar_factura())
