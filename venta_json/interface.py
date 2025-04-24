#!/usr/bin/env python3
from typing import List, TypedDict


class InterfaceProduct(TypedDict):
    id: int
    descripcion: str
    precio: float
    stock: int


class InterfaceVenta(TypedDict):
    factura: float
    Fecha: str
    cliente: str
    subtotal: float
    descuento: float
    iva: float
    total: float
    detalle: List


class InterfaceClient(TypedDict):
    dni: str
    nombre: str
    apellido: str
    valor: float
