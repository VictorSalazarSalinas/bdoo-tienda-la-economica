from modelos import LineaVenta
from base_datos import abrir_base_datos, cerrar_base_datos
import transaction

# ===== ALTA =====
def alta_producto(root, codigo, nombre, descripcion, precio, existencias, categoria):
    from modelos import Producto
    p = Producto(codigo, nombre, descripcion, precio, existencias, categoria)
    root.productos[codigo] = p
    transaction.commit()
    return p

def alta_cliente(root, id_cliente, nombre, telefono, correo):
    from modelos import Cliente
    c = Cliente(id_cliente, nombre, telefono, correo)
    root.clientes[id_cliente] = c
    transaction.commit()
    return c

def alta_proveedor(root, rfc, nombre, telefono, correo, direccion):
    from modelos import Proveedor
    p = Proveedor(rfc, nombre, telefono, correo, direccion)
    root.proveedores[rfc] = p
    transaction.commit()
    return p

def alta_categoria(root, id_cat, nombre, descripcion):
    from modelos import Categoria
    c = Categoria(id_cat, nombre, descripcion)
    root.categorias[id_cat] = c
    transaction.commit()
    return c

# ===== CONSULTA =====
def consultar_producto(root, codigo):
    return root.productos.get(codigo)

def consultar_cliente(root, id_cliente):
    return root.clientes.get(id_cliente)

def consultar_proveedor(root, rfc):
    return root.proveedores.get(rfc)

# ===== MODIFICACION =====
def modificar_precio_producto(root, codigo, nuevo_precio):
    p = root.productos.get(codigo)
    if p:
        p.actualizar_precio(nuevo_precio)
        transaction.commit()
        return True
    return False

def incrementar_existencias(root, codigo, cantidad):
    p = root.productos.get(codigo)
    if p:
        p.incrementar_existencias(cantidad)
        transaction.commit()
        return True
    return False

# ===== ELIMINACION =====
def eliminar_producto(root, codigo):
    if codigo in root.productos:
        del root.productos[codigo]
        transaction.commit()
        return True
    return False

# ===== LOGICA DE NEGOCIO =====
def registrar_venta(root, folio, cliente):
    from modelos import Venta
    from datetime import datetime
    v = Venta(folio, datetime.now(), cliente)
    root.ventas[folio] = v
    transaction.commit()
    return v

def agregar_producto_a_venta(root, folio_venta, codigo_producto, cantidad):
    venta = root.ventas.get(folio_venta)
    producto = root.productos.get(codigo_producto)
    if not venta or not producto:
        return False
    resultado = venta.agregar_producto(producto, cantidad)
    if resultado:
        transaction.commit()
    return resultado

def finalizar_venta(root, folio_venta):
    venta = root.ventas.get(folio_venta)
    if not venta:
        return False
    venta.finalizar_venta()
    transaction.commit()
    return True