#!/usr/bin/env python3
class Provedor:
    def __init__(self, id: str, nombre: str, ruc: str, direccion: str, email: str):
        activo: bool = True
        self.id: str = id
        self.nombre: str = nombre
        self._ruc: str = ruc
        self.direccion: str = direccion
        self.email: str = email

    @property
    def ruc(self) -> str:
        return self._ruc

    def getJson(self):
        provedor = {
            "id": self.id,
            "nombre": self.nombre,
            "ruc": self.ruc,
            "direccion": self.direccion,
            "email": self.email,
        }
        return provedor

    def show(self):
        print(
            f"""
        Nombre: {self.nombre}
        Ruc:{self.ruc}
        Direccion:{self.direccion}
        Correo:{self.email}
        """
        )
