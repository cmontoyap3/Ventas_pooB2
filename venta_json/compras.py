from typing import List
from calculos import Icalculo
from datetime import date
import os
from interface import InterfaceVenta
from product import Product
from customer import RegularClient
from company import Company
from provedor import Provedor

# Colores en formato ANSI escape code
reset_color = "\033[0m"
red_color = "\033[91m"
green_color = "\033[92m"
yellow_color = "\033[93m"
blue_color = "\033[94m"
purple_color = "\033[95m"
cyan_color = "\033[96m"


class comPraDetail:
    _line: int = 0

    def __init__(self, product: Product, quantity: int):
        comPraDetail._line += 1
        self.__id: int = comPraDetail._line
        self.product: Product = product
        self.preci: float = product.preci
        self.quantity: int = quantity

    @property
    def id(self) -> int:
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__id

    def __repr__(self) -> str:
        # Método especial para representar la clase Cliente como una cadena
        return f"{self.id} {self.product.descrip} {self.preci} {self.quantity}"


class Compra(Icalculo):
    next = 0
    FACTOR_IVA: float = 0.12

    def __init__(self, provedor: Provedor) -> None:
        Compra.next += 1
        self.__invoice: float = Compra.next
        self.date: date = date.today()
        self.provedor: Provedor = provedor
        self.subtotal: float = 0
        self.iva: float = 0
        self.total: float = 0
        self.sale_detail: List = []

    @property
    def invoice(self) -> float:
        # Getter para obtener el valor del límite de crédito del cliente VIP
        return self.__invoice

    def __repr__(self) -> str:
        # Método especial para representar la clase Cliente como una cadena
        return (
            f"Factura# {self.invoice} {self.date} {self.provedor.nombre} {self.total}"
        )

    def cal_iva(self, iva: float = 0.12, valor: float = 0):
        return round(valor * iva, 2)

    def cal_discount(self, valor: float = 0, discount: float = 0) -> float:
        return valor * discount

    def add_detail(self, prod, qty):
        # composicion entre detventa y venta
        detail = comPraDetail(prod, qty)
        self.subtotal += round(detail.preci * detail.quantity, 2)
        # self.discount = self.subtotal*self.percentage_discount
        # self.iva = round((self.subtotal-self.discount)*Sale.FACTOR_IVA,2)
        self.iva = self.cal_iva(Compra.FACTOR_IVA, self.subtotal)
        self.total = round(self.subtotal + self.iva, 2)
        self.sale_detail.append(detail)

    def print_invoice(self, company: Company):

        os.system("cls")
        print("\033c", end="")
        print(green_color + "*" * 70 + reset_color)
        print(
            blue_color + f"Empresa: {company.business_name} Ruc: {company.ruc}", end=""
        )
        print(" Factura#:{:7}Fecha:{}".format(self.invoice, self.date))
        self.provedor.show()
        print(green_color + "*" * 70 + reset_color)
        print(purple_color + "Linea Articulo Precio Cantidad Subtotal")
        for det in self.sale_detail:
            print(
                blue_color
                + f"{det.id:5} {det.product.descrip:6} {det.preci:7} {det.quantity:2} {det.preci*det.quantity:14}"
            )
        print(green_color + "*" * 70 + reset_color)
        print(purple_color + " " * 23, "Subtotal:  ", str(self.subtotal))
        print(" " * 23, "Iva:       ", str(self.iva))
        print(" " * 23, "Total:     ", str(self.total) + reset_color)

    def getJson(self):
        # Método especial para representar la clase venta como diccionario
        invoice = {
            "factura": self.invoice,
            "Fecha": self.date.strftime("%Y-%m-%d"),
            "ruc": self.provedor.nombre,
            "subtotal": self.subtotal,
            "iva": self.iva,
            "total": self.total,
            "detalle": [],
        }
        for det in self.sale_detail:
            invoice["detalle"].append(
                {
                    "poducto": det.product.descrip,
                    "precio": det.preci,
                    "cantidad": det.quantity,
                }
            )
        return invoice
