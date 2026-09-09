from base_datos import abrir_base_datos, inicializar, cerrar_base_datos
from operaciones import *
from consultas import *

def poblar():
    """Crear datos de ejemplo y cerrar para demostrar persistencia."""
    db, conn, root = abrir_base_datos()
    inicializar(root)

    # Categorias
    c1 = alta_categoria(root, 1, "Abarrotes", "Productos de despensa")
    c2 = alta_categoria(root, 2, "Bebidas", "Refrescos, jugos, aguas")
    c3 = alta_categoria(root, 3, "Limpieza", "Productos de limpieza del hogar")

    # Productos
    alta_producto(root, "P001", "Arroz 1kg", "Arroz blanco de grano largo", 25.50, 50, c1)
    alta_producto(root, "P002", "Frijol 1kg", "Frijol negro", 30.00, 40, c1)
    alta_producto(root, "P003", "Azucar 1kg", "Azucar refinada", 28.00, 35, c1)
    alta_producto(root, "P004", "Coca-Cola 2L", "Refresco de cola 2 litros", 32.00, 20, c2)
    alta_producto(root, "P005", "Jugo de naranja 1L", "Jugo natural 1 litro", 18.50, 15, c2)
    alta_producto(root, "P006", "Agua purificada 1L", "Agua embotellada", 12.00, 60, c2)
    alta_producto(root, "P007", "Cloro 1L", "Cloro liquido para limpieza", 22.00, 25, c3)
    alta_producto(root, "P008", "Jabon liquido 500ml", "Jabon antibacterial", 35.00, 10, c3)
    alta_producto(root, "P009", "Lavalozas 500ml", "Detergente para trastes", 28.00, 18, c3)
    alta_producto(root, "P010", "Escoba", "Escoba de plastico", 45.00, 12, c3)

    # Proveedores
    prov1 = alta_proveedor(root, "PROV001", "Distribuidora Xalapa", "2281112233", "ventas@dxalapa.com", "Av. Xalapa 123")
    prov2 = alta_proveedor(root, "PROV002", "Bebidas del Golfo", "2282223344", "pedidos@bebidasgolfo.com", "Av. Veracruz 456")

    # Asignar productos a proveedores
    prov1.productos = [root.productos["P001"], root.productos["P002"], root.productos["P003"],
                       root.productos["P007"], root.productos["P008"], root.productos["P009"], root.productos["P010"]]
    prov2.productos = [root.productos["P004"], root.productos["P005"], root.productos["P006"]]

    # Clientes
    alta_cliente(root, 1, "Juan Perez", "2283334455", "juan@gmail.com")
    alta_cliente(root, 2, "Maria Lopez", "2284445566", "maria@gmail.com")

    # Venta 1
    v1 = registrar_venta(root, "V001", root.clientes[1])
    agregar_producto_a_venta(root, "V001", "P001", 3)
    agregar_producto_a_venta(root, "V001", "P004", 2)
    finalizar_venta(root, "V001")

    # Venta 2
    v2 = registrar_venta(root, "V002", root.clientes[2])
    agregar_producto_a_venta(root, "V002", "P005", 5)
    agregar_producto_a_venta(root, "V002", "P008", 2)
    finalizar_venta(root, "V002")

    cerrar_base_datos(db, conn)
    print("✅ Datos creados y guardados en ZODB. Cerrando conexion...\n")

def demostrar_persistencia():
    """Volver a abrir para demostrar que los datos siguen ahi."""
    print("Reabriendo la base de datos para demostrar persistencia...\n")

    # Modificar un precio
    db, conn, root = abrir_base_datos()
    p = root.productos.get("P004")
    if p:
        print(f"  Producto recuperado: {p.nombre} - ${p.precio:.2f}")
        print("  Modificando precio de P004 de $32.00 a $35.00...")
        modificar_precio_producto(root, "P004", 35.00)
    cerrar_base_datos(db, conn)

    # Volver a abrir y verificar el cambio
    db, conn, root = abrir_base_datos()
    p = root.productos.get("P004")
    if p:
        print(f"  Precio modificado correctamente: ${p.precio:.2f} (LOS DATOS PERSISTEN)\n")

    # Eliminar un producto
    print("  Eliminando producto P010 (Escoba)...")
    eliminar_producto(root, "P010")
    cerrar_base_datos(db, conn)

    # Reabrir para consultas finales
    db, conn, root = abrir_base_datos()
    print(f"  Producto P010 {'aun existe' if 'P010' in root.productos else 'eliminado correctamente'}")
    cerrar_base_datos(db, conn)

# ===== EJECUCION =====
print("=" * 60)
print("   ACTIVIDAD 8 - BDOO TIENDA LA ECONOMICA (PARTE 2)")
print("=" * 60)

poblar()

print("=" * 60)
print("   DEMOSTRACION DE PERSISTENCIA")
print("=" * 60)
demostrar_persistencia()

print("=" * 60)
print("   CONSULTAS")
print("=" * 60)

consulta_1_mostrar_productos()
consulta_2_productos_precio_superior(30)
consulta_3_productos_disponibles_o_limite(15)
consulta_4_productos_por_proveedor("PROV001")
consulta_5_total_ventas()

print("\n" + "=" * 60)
print("   CODIGO COMPLETO - LISTO PARA SUBIR A GITHUB")
print("=" * 60)