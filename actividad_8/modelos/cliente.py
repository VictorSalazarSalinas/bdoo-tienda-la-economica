from persistent import Persistent

class Cliente(Persistent):
    """Representa un cliente que realiza compras en la tienda."""

    def __init__(self, id_cliente, nombre, telefono, correo):
        """Inicializa un cliente con sus datos personales.

        Args:
            id_cliente: Identificador único del cliente.
            nombre: Nombre completo.
            telefono: Número de contacto.
            correo: Dirección de correo electrónico.
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
