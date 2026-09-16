from persistent import Persistent

LIMITE_STOCK_BAJO = 5

class Producto(Persistent):
    """Representa un artículo disponible para la venta."""

    def __init__(self, codigo, nombre, descripcion, precio, existencias, categoria):
        """Inicializa un producto con sus datos principales.

        Args:
            codigo: Identificador único del producto.
            nombre: Nombre descriptivo.
            descripcion: Detalle adicional.
            precio: Precio unitario en pesos.
            existencias: Cantidad disponible en inventario.
            categoria: Objeto Categoria al que pertenece.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.categoria = categoria

    def incrementar_existencias(self, cantidad):
        """Aumenta el inventario en la cantidad indicada."""
        if cantidad < 0:
            raise ValueError("La cantidad a incrementar no puede ser negativa.")
        self.existencias += cantidad

    def disminuir_existencias(self, cantidad):
        """Reduce el inventario si hay suficiente stock.

        Returns:
            True si se pudo reducir, False si no hay suficientes existencias.
        """
        if cantidad < 0:
            raise ValueError("La cantidad a disminuir no puede ser negativa.")
        if self.existencias >= cantidad:
            self.existencias -= cantidad
            return True
        return False

    def verificar_disponibilidad(self, cantidad=1):
        """Verifica si hay existencias suficientes.

        Returns:
            True si hay al menos 'cantidad' unidades disponibles.
        """
        return self.existencias >= cantidad

    def actualizar_precio(self, nuevo_precio):
        """Cambia el precio del producto.

        Raises:
            ValueError: Si el nuevo precio es menor o igual a cero.
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.precio = nuevo_precio

    def tiene_bajo_stock(self):
        """Determina si el producto tiene existencias por debajo del límite."""
        return self.existencias < LIMITE_STOCK_BAJO
