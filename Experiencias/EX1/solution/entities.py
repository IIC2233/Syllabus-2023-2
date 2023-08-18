from __future__ import annotations

class Usuario:
    def __init__(self, sub: bool):
        self.sub = sub
        self.canasta = []
        self._puntos = 0

    @property
    def puntos(self):
        return self._puntos
    
    @puntos.setter
    def puntos(self, nuevos_puntos):
        self._puntos = nuevos_puntos

    def agregar_item(self, item: Item):
        if self.sub == True:
            item.precio *= 0.9
        self.canasta.append(item)
    
    def comprar(self):
        for item in self.canasta:
            self.puntos += item.puntos
        self.canasta = []

class Item:
    def __init__(self, nombre: str, precio: int, puntos: int):
        self.nombre = nombre
        self.puntos = puntos
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo_precio
