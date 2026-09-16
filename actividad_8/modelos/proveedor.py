from persistent import Persistent

class Proveedor(Persistent):
    """Representa un proveedor que suministra productos a la tienda."""

    def __init__(self, rfc, nombre, telefono, correo, direccion):
        """Inicializa un proveedor con sus datos de contacto.

        Args:
            rfc: Identificador fiscal del proveedor.
            nombre: Nombre o razón social.
            telefono: Número de contacto.
            correo: Dirección de correo electrónico.
            direccion: Dirección física.
        """
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.productos = []
