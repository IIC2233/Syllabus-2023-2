from PyQt6.QtCore import QObject, pyqtSignal


class ControladorLogico(QObject):

    senal_volumen = pyqtSignal(int)
    senal_canal = pyqtSignal(int)
    senal_encendido = pyqtSignal(bool)
    senal_empezar = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        self._volumen = 20
        self._canal = 1
        self.prendido = True

    @property
    def volumen(self) -> int:
        return self._volumen

    @volumen.setter
    def volumen(self, valor: int) -> None:
        if valor < 0:
            valor = 0
        elif valor > 100:
            valor = 100

        self._volumen = valor

    @property
    def canal(self) -> int:
        return self._canal

    @canal.setter
    def canal(self, valor: int) -> None:
        if (valor < 1) or (valor > 9):
            valor = 1 + (valor - 1) % 9

        self._canal = valor

    def cambiar_volumen(self, cambio: str) -> None:
        if not self.prendido:
            print('La tele está apagada, no se puede cambiar el volumen')
            return

        print('Cambiando volumen:', cambio)
        if cambio == '+':
            self.volumen += 10
        elif cambio == '-':
            self.volumen -= 10
        self.actualizar_volumen()

    def cambiar_canal(self, cambio: str) -> None:
        if not self.prendido:
            print('La tele está apagada, no se puede cambiar el canal')
            return

        print('Cambiando canal:', cambio)
        if cambio == '+':
            self.canal += 1
        elif cambio == '-':
            self.canal -= 1
        else:
            self.canal = int(cambio)

        self.actualizar_canal()

    def actualizar_volumen(self) -> None:
        print('Avisando nuevo volumen:', self.volumen)
        self.senal_volumen.emit(self.volumen)

    def actualizar_canal(self) -> None:
        print('Avisando nuevo canal:', self.canal)
        self.senal_canal.emit(self.canal)

    def prender_apagar(self) -> None:
        self.prendido = not self.prendido
        if self.prendido:
            print('Prendiendo tele')
        else:
            print('Apagando tele')
        self.senal_encendido.emit(self.prendido)

    def empezar(self) -> None:
        self.actualizar_canal()
        self.actualizar_volumen()
        self.senal_empezar.emit()
