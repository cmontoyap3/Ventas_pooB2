from utilities import borrarPantalla, gotoxy
from typing import List
import time


class Menu:
    def __init__(
        self, titulo: str = "", opciones: List[str] = [], col: int = 6, fil: int = 1
    ) -> None:
        self.titulo: str = titulo
        self.opciones: List[str] = opciones
        self.col: int = col
        self.fil: int = fil

    def menu(self) -> str:
        gotoxy(self.col, self.fil)
        print(self.titulo)
        self.col -= 5
        for opcion in self.opciones:
            self.fil += 1
            gotoxy(self.col, self.fil)
            print(opcion)
        gotoxy(self.col + 5, self.fil + 2)
        opc = input(f"Elija opcion[1...{len(self.opciones)}]: ")

        return opc


class Valida:
    def solo_numeros(self, mensajeError: str, col: int, fil: int) -> str:
        while True:
            gotoxy(col, fil)
            valor: str | int = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col, fil)
                print(mensajeError)
                time.sleep(1)
                gotoxy(col, fil)
                print(" " * 20)
        return valor

    def solo_letras(self, mensaje: str, mensajeError: str) -> str:
        while True:
            valor: str = str(input("          ------>   | {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def solo_decimales(self, mensaje: str, mensajeError: str):
        while True:
            valor: str | float = str(input("          ------>   | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor

    def cedula(self) -> None:
        pass


if __name__ == "__main__":
    # instanciar el menu
    opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    opcion_elegida = menu.menu()
    print("Opción escogida:", opcion_elegida)
    valida = Valida()
    if opciones_menu == 1:
        numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
        print("Número validado:", numero_validado)

    numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    print("Número validado:", numero_validado)

    letra_validada = valida.solo_letras("Ingrese una letra:", "Mensaje de error")
    print("Letra validada:", letra_validada)

    decimal_validado = valida.solo_decimales("Ingrese un decimal:", "Mensaje de error")
    print("Decimal validado:", decimal_validado)
