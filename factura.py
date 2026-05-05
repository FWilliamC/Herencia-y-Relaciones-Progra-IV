class Factura:
    def __init__(self, fecha, cliente):
        if not fecha or cliente is None:
            raise ValueError("Todos los atributos son obligatorios")

        self.fecha = fecha
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for p in self.productos:
            total += p.precio
        return total

    def __str__(self):
        return f"Factura {self.fecha} - Total: ${self.calcular_total()}"