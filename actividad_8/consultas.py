from base_datos import abrir_base_datos, cerrar_base_datos

def consulta_1_mostrar_productos():
    """Mostrar todos los productos registrados."""
    db, conn, root = abrir_base_datos()
    print("\n=== CONSULTA 1: TODOS LOS PRODUCTOS ===")
    for p in root.productos.values():
        print(f"  {p.codigo} | {p.nombre} | ${p.precio:.2f} | Stock: {p.existencias} | Categoria: {p.categoria.nombre}")
    cerrar_base_datos(db, conn)

def consulta_2_productos_precio_superior(precio_min):
    """Productos cuyo precio sea superior a determinada cantidad."""
    db, conn, root = abrir_base_datos()
    print(f"\n=== CONSULTA 2: PRODUCTOS CON PRECIO > ${precio_min:.2f} ===")
    for p in root.productos.values():
        if p.precio > precio_min:
            print(f"  {p.codigo} | {p.nombre} | ${p.precio:.2f}")
    cerrar_base_datos(db, conn)

def consulta_3_productos_disponibles_o_limite(limite=10):
    """Productos disponibles o con existencias menores a cierto limite."""
    db, conn, root = abrir_base_datos()
    print(f"\n=== CONSULTA 3: PRODUCTOS CON EXISTENCIAS < {limite} ===")
    for p in root.productos.values():
        if p.existencias < limite:
            print(f"  {p.codigo} | {p.nombre} | Stock: {p.existencias} {'(BAJO STOCK!)' if p.existencias < 5 else ''}")
    cerrar_base_datos(db, conn)

def consulta_4_productos_por_proveedor(rfc_proveedor):
    """Mostrar los productos proporcionados por un determinado proveedor."""
    db, conn, root = abrir_base_datos()
    print(f"\n=== CONSULTA 4: PRODUCTOS DEL PROVEEDOR {rfc_proveedor} ===")
    prov = root.proveedores.get(rfc_proveedor)
    if prov:
        for p in prov.productos:
            if p.codigo in root.productos:  # Solo mostrar productos que siguen en el inventario
                print(f"  {p.codigo} | {p.nombre} | ${p.precio:.2f}")
    else:
        print("  Proveedor no encontrado")
    cerrar_base_datos(db, conn)

def consulta_5_total_ventas():
    """Total de ventas."""
    db, conn, root = abrir_base_datos()
    print("\n=== CONSULTA 5: TOTAL DE VENTAS ===")
    total_general = 0
    for v in root.ventas.values():
        print(f"  Folio: {v.folio} | Fecha: {v.fecha} | Cliente: {v.cliente.nombre} | Total: ${v.total:.2f}")
        total_general += v.total
    print(f"  TOTAL GENERAL: ${total_general:.2f}")
    cerrar_base_datos(db, conn)