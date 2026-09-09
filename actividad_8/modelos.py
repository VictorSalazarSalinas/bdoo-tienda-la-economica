from persistent import Persistent
from datetime import datetime

class Categoria(Persistent):
    def __init__(self, id_categoria, nombre, descripcion):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion

class Producto(Persistent):
    def __init__(self, codigo, nombre, descripcion, precio, existencias, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.categoria = categoria

    def incrementar_existencias(self, cantidad):
        self.existencias += cantidad

    def disminuir_existencias(self, cantidad):
        if self.existencias >= cantidad:
            self.existencias -= cantidad
            return True
        return False

    def verificar_disponibilidad(self, cantidad):
        return self.existencias >= cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

class Proveedor(Persistent):
    def __init__(self, rfc, nombre, telefono, correo, direccion):
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.productos = []  # Referencias a objetos Producto

class Cliente(Persistent):
    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class LineaVenta(Persistent):
    def __init__(self, id_linea, producto, cantidad, precio_unitario):
        self.id_linea = id_linea
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.cantidad * self.precio_unitario

class Venta(Persistent):
    def __init__(self, folio, fecha, cliente):
        self.folio = folio
        self.fecha = fecha
        self.cliente = cliente
        self.lineas = []
        self.total = 0.0

    def agregar_producto(self, producto, cantidad):
        if not producto.verificar_disponibilidad(cantidad):
            return False
        linea = LineaVenta(len(self.lineas) + 1, producto, cantidad, producto.precio)
        self.lineas.append(linea)
        self.calcular_total()
        return True

    def calcular_total(self):
        self.total = sum(l.subtotal for l in self.lineas)
        return self.total

    def finalizar_venta(self):
        for linea in self.lineas:
            linea.producto.disminuir_existencias(linea.cantidad)