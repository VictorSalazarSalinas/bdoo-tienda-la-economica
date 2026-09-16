"""Consultas del sistema para recuperar información de la tienda."""

from persistencia import abrir_base_datos, cerrar_base_datos
from datetime import date


def mostrar_todos_los_productos():
    """Muestra todos los productos registrados en la tienda."""
    db, conn, root = abrir_base_datos()
    print("\n=== TODOS LOS PRODUCTOS ===")
    for producto in root.productos.values():
        categoria = producto.categoria.nombre if producto.categoria else "Sin categoría"
        stock = producto.existencias
        indicador = " (BAJO STOCK)" if producto.tiene_bajo_stock() else ""
        print(f"  {producto.codigo} | {producto.nombre} | ${producto.precio:.2f} | "
              f"Stock: {stock}{indicador} | {categoria}")
    cerrar_base_datos(db, conn)


def productos_disponibles():
    """Muestra únicamente los productos con existencias mayores a cero."""
    db, conn, root = abrir_base_datos()
    print("\n=== PRODUCTOS DISPONIBLES ===")
    for producto in root.productos.values():
        if producto.existencias > 0:
            print(f"  {producto.codigo} | {producto.nombre} | Stock: {producto.existencias}")
    cerrar_base_datos(db, conn)


def productos_bajo_stock(limite=5):
    """Muestra productos con existencias menores al límite establecido.

    Args:
        limite: Cantidad mínima de existencias considerada como stock bajo.
    """
    db, conn, root = abrir_base_datos()
    print(f"\n=== PRODUCTOS BAJO STOCK (< {limite}) ===")
    for producto in root.productos.values():
        if producto.existencias < limite:
            print(f"  {producto.codigo} | {producto.nombre} | Stock: {producto.existencias}")
    cerrar_base_datos(db, conn)


def productos_precio_superior(precio_minimo):
    """Muestra productos cuyo precio sea superior a una cantidad determinada.

    Args:
        precio_minimo: Precio mínimo para filtrar.
    """
    db, conn, root = abrir_base_datos()
    print(f"\n=== PRODUCTOS CON PRECIO > ${precio_minimo:.2f} ===")
    for producto in root.productos.values():
        if producto.precio > precio_minimo:
            print(f"  {producto.codigo} | {producto.nombre} | ${producto.precio:.2f}")
    cerrar_base_datos(db, conn)


def productos_por_proveedor(rfc_proveedor):
    """Muestra los productos que suministra un proveedor específico.

    Args:
        rfc_proveedor: RFC del proveedor a consultar.
    """
    db, conn, root = abrir_base_datos()
    proveedor = root.proveedores.get(rfc_proveedor)
    print(f"\n=== PRODUCTOS DEL PROVEEDOR {rfc_proveedor} ===")
    if proveedor:
        for producto in proveedor.productos:
            if producto.codigo in root.productos:
                print(f"  {producto.codigo} | {producto.nombre} | ${producto.precio:.2f}")
    else:
        print("  Proveedor no encontrado.")
    cerrar_base_datos(db, conn)


def ventas_cliente(id_cliente):
    """Muestra todas las ventas realizadas por un cliente específico.

    Args:
        id_cliente: Identificador del cliente a consultar.
    """
    db, conn, root = abrir_base_datos()
    print(f"\n=== VENTAS DEL CLIENTE {id_cliente} ===")
    for venta in root.ventas.values():
        if venta.cliente.id_cliente == id_cliente:
            print(f"  Folio: {venta.folio} | Fecha: {venta.fecha.date()} | Total: ${venta.total:.2f}")
    cerrar_base_datos(db, conn)


def productos_mas_vendidos():
    """Muestra los productos más vendidos ordenados por cantidad."""
    db, conn, root = abrir_base_datos()
    print("\n=== PRODUCTOS MÁS VENDIDOS ===")
    conteo = {}
    for venta in root.ventas.values():
        for linea in venta.lineas:
            codigo = linea.producto.codigo
            conteo[codigo] = conteo.get(codigo, 0) + linea.cantidad
    ordenados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    for codigo, cantidad in ordenados:
        producto = root.productos.get(codigo)
        nombre = producto.nombre if producto else "Eliminado"
        print(f"  {codigo} | {nombre} | {cantidad} vendido(s)")
    cerrar_base_datos(db, conn)


def total_ventas():
    """Muestra el total acumulado de todas las ventas registradas."""
    db, conn, root = abrir_base_datos()
    print("\n=== TOTAL DE VENTAS ===")
    total_general = 0.0
    for venta in root.ventas.values():
        print(f"  Folio: {venta.folio} | {venta.cliente.nombre} | ${venta.total:.2f}")
        total_general += venta.total
    print(f"  TOTAL GENERAL: ${total_general:.2f}")
    cerrar_base_datos(db, conn)


def venta_diaria():
    """Muestra las ventas realizadas durante el día actual."""
    db, conn, root = abrir_base_datos()
    hoy = date.today()
    print(f"\n=== VENTAS DEL DÍA {hoy} ===")
    total_dia = 0.0
    for venta in root.ventas.values():
        if venta.fecha.date() == hoy:
            print(f"  Folio: {venta.folio} | {venta.cliente.nombre} | ${venta.total:.2f}")
            total_dia += venta.total
    print(f"  TOTAL DEL DÍA: ${total_dia:.2f}")
    cerrar_base_datos(db, conn)
