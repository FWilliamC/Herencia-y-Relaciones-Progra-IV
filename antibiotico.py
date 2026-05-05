class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, precio):
        if not nombre or dosis is None or not tipo_animal or precio is None:
            raise ValueError("Todos los atributos son obligatorios")

        if dosis < 400 or dosis > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg")

        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} ({self.tipo_animal}) - ${self.precio}"