from modelo.producto_control import ProductoControl

class Fertilizante(ProductoControl):
    def __init__(self, nombre, precio, registro_ica, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, precio, registro_ica, frecuencia_aplicacion)

        if not fecha_ultima_aplicacion:
            raise ValueError("Todos los atributos son obligatorios")

        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion