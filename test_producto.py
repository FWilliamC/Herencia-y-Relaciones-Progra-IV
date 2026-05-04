from modelo.producto import Producto

def test_crear_producto():
    p = Producto("Fertilizante A", 100)
    assert p.nombre == "Fertilizante A"
    assert p.precio == 100