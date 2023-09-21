import math
import backend.logica as logica


def acotar_numero(numero: int, minimo: int, maximo: int) -> int:
    return max(min(numero, maximo), minimo)


def distancia(icono_1: logica.Icono, icono_2: logica.Icono) -> float:
    distancia_x = math.pow(icono_2.centro_x - icono_1.centro_x, 2)
    distancia_y = math.pow(icono_2.centro_y - icono_1.centro_y, 2)
    return math.sqrt(distancia_x + distancia_y)


def gano_yo(icono_1: logica.Icono, icono_2: logica.Icono) -> bool:
    if icono_1.tipo == "empanada" and icono_2.tipo == "choripan":
        return True
    if icono_1.tipo == "choripan" and icono_2.tipo == "anticucho":
        return True
    if icono_1.tipo == "anticucho" and icono_2.tipo == "empanada":
        return True
    return False
