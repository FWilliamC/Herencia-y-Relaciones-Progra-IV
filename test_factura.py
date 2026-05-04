from modelo.factura import Factura
from modelo.producto import Producto
from modelo.cliente import Cliente

def test_total_factura():
    cliente = Cliente("Juan", "123")

    factura = Factura("2026-01-01", cliente)

    p1 = Producto("Producto 1", 100)
    p2 = Producto("Producto 2", 200)

    factura.agregar_producto(p1)
    factura.agregar_producto(p2)

    assert factura.calcular_total() == 300