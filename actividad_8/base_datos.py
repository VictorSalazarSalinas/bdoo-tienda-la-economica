import ZODB
from ZODB.FileStorage import FileStorage
import transaction
from persistent.mapping import PersistentMapping
import os

def abrir_base_datos():
    os.makedirs("./base_datos", exist_ok=True)
    storage = FileStorage("./base_datos/tienda.fs")
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root()
    return db, connection, root

def inicializar(root):
    for attr in ["categorias", "productos", "proveedores", "clientes", "ventas"]:
        if not hasattr(root, attr):
            setattr(root, attr, PersistentMapping())
    transaction.commit()

def cerrar_base_datos(db, connection):
    connection.close()
    db.close()