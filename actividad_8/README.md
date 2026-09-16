# Sistema de Tienda - BDOO con Python y ZODB

Sistema desarrollado en Python para administrar una tienda utilizando una Base de Datos Orientada a Objetos (BDOO) con ZODB.

## Requisitos

- Python 3.10 o superior
- ZODB

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Estructura del proyecto

```
tienda_bdoo/
├── modelos/           # Clases del dominio
│   ├── producto.py
│   ├── cliente.py
│   ├── proveedor.py
│   ├── categoria.py
│   └── venta.py
├── persistencia/      # Conexión con ZODB
├── servicios/         # Lógica de negocio
├── consultas/         # Consultas del sistema
├── main.py            # Punto de entrada
├── README.md
├── requirements.txt
└── .gitignore
```

## Funcionalidades

- CRUD de productos
- Registro de ventas
- Control de inventario
- Consultas: disponibilidad, stock bajo, ventas por cliente, productos más vendidos
- Persistencia de datos con ZODB
