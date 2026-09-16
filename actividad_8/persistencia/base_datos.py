"""Funciones para gestionar la conexión con la base de datos ZODB."""

import os
import ZODB
from ZODB.FileStorage import FileStorage
import transaction
from persistent.mapping import PersistentMapping

RUTA_BD = "./base_datos/tienda.fs"

COLECCIONES = ["categorias", "productos", "proveedores", "clientes", "ventas"]


def abrir_base_datos():
    """Abre la base de datos ZODB y retorna la conexión.

    Crea el directorio de la base de datos si no existe.
    """
    os.makedirs("./base_datos", exist_ok=True)
    storage = FileStorage(RUTA_BD)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    return db, connection, root


def inicializar(root):
    """Inicializa las colecciones en la raíz de ZODB si no existen."""
    for attr in COLECCIONES:
        if not hasattr(root, attr):
            setattr(root, attr, PersistentMapping())
    transaction.commit()


def cerrar_base_datos(db, connection):
    """Cierra la conexión y la base de datos ZODB."""
    connection.close()
    db.close()
