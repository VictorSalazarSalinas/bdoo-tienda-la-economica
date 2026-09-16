"""Servicios relacionados con la gestión de productos."""

import transaction
from modelos.producto import Producto


class ProductoService:
    """Operaciones de negocio para productos: CRUD y consultas."""

    @staticmethod
    def registrar_producto(root, codigo, nombre, descripcion, precio, existencias, categoria):
        """Registra un nuevo producto en la base de datos.

        Args:
            root: Raíz de ZODB.
            codigo: Identificador único del producto.
            nombre: Nombre del producto.
            descripcion: Descripción detallada.
            precio: Precio unitario. Debe ser mayor a cero.
            existencias: Cantidad inicial. No puede ser negativa.
            categoria: Objeto Categoria al que pertenece.

        Returns:
            El objeto Producto creado.

        Raises:
            ValueError: Si el precio o las existencias no son válidos.
        """
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if existencias < 0:
            raise ValueError("Las existencias no pueden ser negativas.")
        if codigo in root.productos:
            raise ValueError(f"El código {codigo} ya está registrado.")

        producto = Producto(codigo, nombre, descripcion, precio, existencias, categoria)
        root.productos[codigo] = producto
        transaction.commit()
        return producto

    @staticmethod
    def consultar_producto(root, codigo):
        """Busca un producto por su código.

        Returns:
            El objeto Producto si existe, None en caso contrario.
        """
        return root.productos.get(codigo)

    @staticmethod
    def modificar_precio(root, codigo, nuevo_precio):
        """Modifica el precio de un producto existente.

        Args:
            root: Raíz de ZODB.
            codigo: Código del producto a modificar.
            nuevo_precio: Nuevo precio. Debe ser mayor a cero.

        Returns:
            True si se modificó correctamente.

        Raises:
            ValueError: Si el producto no existe o el precio no es válido.
        """
        producto = root.productos.get(codigo)
        if not producto:
            raise ValueError(f"Producto {codigo} no encontrado.")
        producto.actualizar_precio(nuevo_precio)
        transaction.commit()
        return True

    @staticmethod
    def eliminar_producto(root, codigo):
        """Elimina un producto de la base de datos.

        Args:
            root: Raíz de ZODB.
            codigo: Código del producto a eliminar.

        Returns:
            True si se eliminó correctamente.

        Raises:
            ValueError: Si el producto no existe.
        """
        if codigo not in root.productos:
            raise ValueError(f"Producto {codigo} no encontrado.")
        del root.productos[codigo]
        transaction.commit()
        return True
