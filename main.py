from modelo.cliente import Cliente
from modelo.factura import Factura
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante
from modelo.antibiotico import Antibiotico

def main():
    cliente = Cliente("William", "12345689")

    factura = Factura("2026-05-10", cliente)

    p1 = ControlPlagas("Insecticida X", 150, "ICA123", "15 dias", 7)
    p2 = Fertilizante("Fertilizante Y", 200, "ICA456", "30 dias", "2026-04-01")
    p3 = Antibiotico("Antibio Z", 500, "Bovino", 300)

    factura.agregar_producto(p1)
    factura.agregar_producto(p2)
    factura.agregar_producto(p3)

    cliente.agregar_factura(factura)

    print(cliente)
    print(factura)

    print("\nProductos:")
    for p in factura.productos:
        print(p)

if __name__ == "__main__":
    main()