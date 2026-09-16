"""Servicios relacionados con la gestión de ventas."""

from datetime import datetime
import transaction
from modelos.venta import Venta


class VentaService:
    """Operaciones de negocio para ventas."""

    @staticmethod
    def registrar_venta(root, folio, cliente):
        """Registra una nueva venta.

        Args:
            root: Raíz de ZODB.
            folio: Identificador único de la venta.
            cliente: Objeto Cliente que realiza la compra.

        Returns:
            El objeto Venta creado.

        Raises:
            ValueError: Si el folio ya existe.
        """
        if folio in root.ventas:
            raise ValueError(f"El folio {folio} ya está registrado.")
        venta = Venta(folio, datetime.now(), cliente)
        root.ventas[folio] = venta
        transaction.commit()
        return venta

    @staticmethod
    def agregar_producto(root, folio_venta, codigo_producto, cantidad):
        """Agrega un producto a una venta existente.

        Args:
            root: Raíz de ZODB.
            folio_venta: Folio de la venta.
            codigo_producto: Código del producto a agregar.
            cantidad: Número de unidades.

        Returns:
            True si se agregó correctamente.

        Raises:
            ValueError: Si la venta o el producto no existen, o cantidad inválida.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        venta = root.ventas.get(folio_venta)
        if not venta:
            raise ValueError(f"Venta {folio_venta} no encontrada.")
        producto = root.productos.get(codigo_producto)
        if not producto:
            raise ValueError(f"Producto {codigo_producto} no encontrado.")
        resultado = venta.agregar_producto(producto, cantidad)
        if resultado:
            transaction.commit()
        return resultado
