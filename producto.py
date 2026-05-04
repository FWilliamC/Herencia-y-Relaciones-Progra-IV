class Producto:
    def __init__(self, nombre, precio):
        if not nombre or precio is None:
            raise ValueError("Todos los atributos son obligatorios")
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"