"""Punto de entrada del sistema de tienda BDOO.

Ejecuta la población de datos de ejemplo y todas las consultas.
"""

from persistencia import abrir_base_datos, inicializar, cerrar_base_datos
from modelos.categoria import Categoria
from servicios.producto_service import ProductoService
from servicios.venta_service import VentaService
from servicios.inventario_service import InventarioService
from consultas.consultas import (
    mostrar_todos_los_productos,
    productos_disponibles,
    productos_bajo_stock,
    productos_precio_superior,
    productos_por_proveedor,
    ventas_cliente,
    productos_mas_vendidos,
    total_ventas,
    venta_diaria,
)


def poblar_datos():
    """Crea datos de ejemplo en la base de datos."""
    db, connection, root = abrir_base_datos()
    inicializar(root)

    producto_service = ProductoService()
    venta_service = VentaService()

    categoria_abarrotes = Categoria(1, "Abarrotes", "Productos de despensa")
    categoria_bebidas = Categoria(2, "Bebidas", "Refrescos y jugos")
    categoria_limpieza = Categoria(3, "Limpieza", "Artículos de limpieza")

    from modelos.proveedor import Proveedor
    from modelos.cliente import Cliente

    root.categorias[1] = categoria_abarrotes
    root.categorias[2] = categoria_bebidas
    root.categorias[3] = categoria_limpieza

    producto_service.registrar_producto(root, "P001", "Arroz 1kg", "", 25.50, 50, categoria_abarrotes)
    producto_service.registrar_producto(root, "P002", "Frijol 1kg", "", 30.00, 40, categoria_abarrotes)
    producto_service.registrar_producto(root, "P003", "Azúcar 1kg", "", 28.00, 35, categoria_abarrotes)
    producto_service.registrar_producto(root, "P004", "Coca-Cola 2L", "", 32.00, 20, categoria_bebidas)
    producto_service.registrar_producto(root, "P005", "Jugo de naranja 1L", "", 18.50, 15, categoria_bebidas)
    producto_service.registrar_producto(root, "P006", "Cloro 1L", "", 22.00, 25, categoria_limpieza)
    producto_service.registrar_producto(root, "P007", "Jabón líquido", "", 35.00, 10, categoria_limpieza)
    producto_service.registrar_producto(root, "P008", "Lavalozas", "", 28.00, 18, categoria_limpieza)

    proveedor = Proveedor("PROV001", "Distribuidora Xalapa", "2281112233",
                          "ventas@dx.com", "Av. Xalapa 123")
    proveedor.productos = [
        root.productos["P001"], root.productos["P002"], root.productos["P003"],
        root.productos["P006"], root.productos["P007"], root.productos["P008"],
    ]
    root.proveedores["PROV001"] = proveedor

    cliente_uno = Cliente(1, "Juan Pérez", "2283334455", "juan@gmail.com")
    cliente_dos = Cliente(2, "María López", "2284445566", "maria@gmail.com")
    root.clientes[1] = cliente_uno
    root.clientes[2] = cliente_dos

    venta_001 = venta_service.registrar_venta(root, "V001", cliente_uno)
    venta_service.agregar_producto(root, "V001", "P001", 3)
    venta_service.agregar_producto(root, "V001", "P004", 2)

    venta_002 = venta_service.registrar_venta(root, "V002", cliente_dos)
    venta_service.agregar_producto(root, "V002", "P005", 5)
    venta_service.agregar_producto(root, "V002", "P007", 2)

    cerrar_base_datos(db, connection)
    print("Datos de ejemplo creados correctamente.\n")


def ejecutar_consultas():
    """Ejecuta todas las consultas del sistema."""
    mostrar_todos_los_productos()
    productos_disponibles()
    productos_bajo_stock()
    productos_precio_superior(30.0)
    productos_por_proveedor("PROV001")
    ventas_cliente(1)
    productos_mas_vendidos()
    total_ventas()
    venta_diaria()


def main():
    """Función principal del programa."""
    print("=" * 60)
    print("   SISTEMA DE TIENDA LA ECONÓMICA - BDOO")
    print("   Versión refactorizada")
    print("=" * 60)
    poblar_datos()
    ejecutar_consultas()
    print("\n" + "=" * 60)
    print("   PROGRAMA FINALIZADO CORRECTAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    main()
