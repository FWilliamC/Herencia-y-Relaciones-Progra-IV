class Cliente:
    def __init__(self, nombre, cedula):
        if not nombre or not cedula:
            raise ValueError("Todos los atributos son obligatorios")

        self.nombre = nombre
        self.cedula = cedula
        self.facturas = []

    def agregar_factura(self, factura):
        self.facturas.append(factura)

    def __str__(self):
        return f"{self.nombre} - {self.cedula}"