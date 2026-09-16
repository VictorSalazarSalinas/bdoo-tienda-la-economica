from persistent import Persistent

class LineaVenta(Persistent):
    """Representa un producto específico dentro de una venta, con cantidad y subtotal."""

    def __init__(self, id_linea, producto, cantidad, precio_unitario):
        """Inicializa una línea de venta.

        Args:
            id_linea: Identificador único dentro de la venta.
            producto: Objeto Producto vendido.
            cantidad: Número de unidades.
            precio_unitario: Precio al momento de la venta.
        """
        self.id_linea = id_linea
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self):
        """Calcula el subtotal multiplicando cantidad por precio unitario."""
        return self.cantidad * self.precio_unitario


class Venta(Persistent):
    """Representa una transacción de compra realizada por un cliente."""

    def __init__(self, folio, fecha, cliente):
        """Inicializa una venta.

        Args:
            folio: Identificador único de la venta.
            fecha: Fecha y hora en que se realizó.
            cliente: Objeto Cliente que realizó la compra.
        """
        self.folio = folio
        self.fecha = fecha
        self.cliente = cliente
        self.lineas = []
        self.total = 0.0

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la venta y actualiza el inventario.

        Args:
            producto: Objeto Producto a agregar.
            cantidad: Número de unidades.

        Returns:
            True si se agregó correctamente, False si no hay stock suficiente.
        """
        if not producto.verificar_disponibilidad(cantidad):
            return False
        linea = LineaVenta(len(self.lineas) + 1, producto, cantidad, producto.precio)
        self.lineas.append(linea)
        producto.disminuir_existencias(cantidad)
        self.calcular_total()
        return True

    def calcular_total(self):
        """Calcula el total de la venta sumando los subtotales de cada línea."""
        self.total = sum(linea.subtotal for linea in self.lineas)
        return self.total
