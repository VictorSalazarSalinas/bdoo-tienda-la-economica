from persistent import Persistent

class Categoria(Persistent):
    """Representa una categoría de productos."""

    def __init__(self, id_categoria, nombre, descripcion):
        """Inicializa una categoría con identificador, nombre y descripción."""
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
