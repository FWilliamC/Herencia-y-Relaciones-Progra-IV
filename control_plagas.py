from modelo.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)

        if periodo_carencia is None:
            raise ValueError("Todos los atributos son obligatorios")

        self.periodo_carencia = periodo_carencia