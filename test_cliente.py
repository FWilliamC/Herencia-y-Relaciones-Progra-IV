from modelo.cliente import Cliente
from modelo.factura import Factura

def test_cliente_facturas():
    cliente = Cliente("Ana", "456")

    factura = Factura("2026-01-01", cliente)

    cliente.agregar_factura(factura)

    assert len(cliente.facturas) == 1