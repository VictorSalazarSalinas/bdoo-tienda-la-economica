"""Servicios relacionados con el control de inventario."""

import transaction


class InventarioService:
    """Operaciones de negocio para el inventario."""

    @staticmethod
    def actualizar_inventario(root, codigo_producto, cantidad):
        """Incrementa las existencias de un producto.

        Args:
            root: Raíz de ZODB.
            codigo_producto: Código del producto.
            cantidad: Cantidad a incrementar. Debe ser positiva.

        Returns:
            True si se actualizó correctamente.

        Raises:
            ValueError: Si el producto no existe o la cantidad es inválida.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        producto = root.productos.get(codigo_producto)
        if not producto:
            raise ValueError(f"Producto {codigo_producto} no encontrado.")
        producto.incrementar_existencias(cantidad)
        transaction.commit()
        return True
