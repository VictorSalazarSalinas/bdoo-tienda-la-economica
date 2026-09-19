# Sistema de gestión de tienda BDOO

## Descripción

Sistema desarrollado en Python para administrar una tienda utilizando una Base de Datos Orientada a Objetos (BDOO) con ZODB. Permite gestionar productos, clientes, proveedores y ventas, con consultas y control de inventario.

## Objetivo

Resolver los problemas de administración de una tienda pequeña que actualmente lleva sus registros en hojas de cálculo y papel, migrando a un sistema con persistencia de datos y consultas automatizadas.

## Tecnologías utilizadas

- Python
- ZODB
- Git

## Estructura del proyecto

```
tienda_bdoo/
├── modelos/           # Clases del dominio
│   ├── categoria.py
│   ├── cliente.py
│   ├── producto.py
│   ├── proveedor.py
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

- Gestión de productos (CRUD)
- Gestión de clientes
- Gestión de proveedores
- Registro de ventas
- Consultas de disponibilidad, stock, ventas por cliente, productos más vendidos
- Control de inventario

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Integrantes

- Víctor Miguel Salazar Salinas

## Versión

v1.0.0 — Versión inicial del proyecto.