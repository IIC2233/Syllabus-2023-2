import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import separar_mensaje


class TestSepararMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = bytearray(b"Hola Mundo")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [b"Hauo", b"o n", b"lMd"])

    def test_1(self):
        mensaje = bytearray(b"\xc2\xb4+{}[]\xc2\xa8*!#$%&/()")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(
            respuesta, [b"\xc2{]*$/", b"\xb4}\xc2!%(", b"+[\xa8#&)"])

    def test_2(self):
        mensaje = bytearray(b"A\xc3\xb1o nuevo, vida nueva")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(
            respuesta, [b"Aouovaua", b"\xc3 e,i e", b"\xb1nv dnv"])

    def test_3(self):
        mensaje = bytearray(b"\xc3\xb1a\xc3\xb1e\xc3\xb1i\xc3\xb1d\xc3\xb1r\xc3"
                            b"\xb1t\xc3\xb1ch\xc3\xb1h\xc3\xb1l\xc3\xb1\xc3\xb1"
                            b"\xc2\xb4\xc2\xb4\xc3\xb1\xc3\xb1\xc2\xb4\xc2\xb4\xc3\xb1")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"\xc3\xc3\xc3\xc3\xc3\xc3\xc3hhl\xc3\xb4\xc3\xb1\xc2\xb1",
            b"\xb1\xb1\xb1\xb1\xb1\xb1\xb1\xc3\xc3\xc3\xb1\xc2\xb1\xc2\xb4",
            b"aeidrtc\xb1\xb1\xb1\xc2\xb4\xc3\xb4\xc3"
        ])

    def test_4(self):
        mensaje = bytearray(
            b"{}\xc2\xb4+[]\xc2\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1\\\xc2\xb8\xc2"
            b"\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1\\\xc2\xb8|\xc2\xb0\xc2"
            b"\xac!#$%&/()=|@\xc2\xb7~\xc2\xbd\xc2\xac{[]}")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"{\xb4]*\xc2\'?\\\xc2^\xa8\xc2\xc2\xc2\xc2\xac$/=\xc2\xc2\xac]",
            b"}+\xc2^\xa8\xc2\xc2\xc2\xa8`~\xbf\xa1\xb8\xb0!%(|\xb7\xbd{}",
            b"\xc2[\xa8`~\xbf\xa1\xb8*\xc2\'?\\|\xc2#&)@~\xc2["
        ])

    def test_5(self):
        mensaje = bytearray(
            b"\xe2\x80\xa1\xe2\x80\xa0\xc6\x92\xe2\x82\xac\xe2\x80\xb0\xc5\xa0\xc5\x92\xc5\xbd")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"\xe2\xe2\xc6\x82\x80\xa0\xc5",
            b"\x80\x80\x92\xac\xb0\xc5\xbd",
            b"\xa1\xa0\xe2\xe2\xc5\x92"
        ])

    def test_6(self):
        mensaje = bytearray(b"\t\n\r\x0b\x0c")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"\t\x0b",
            b"\n\x0c",
            b"\r"
        ])

    def test_7(self):
        mensaje = bytearray(b"Hola Mundo\nHola Mundo\nHola Mundo\n")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"Hauoo n\nlMd",
            b"o n\nlMdHauo",
            b"lMdHauoo n\n"
        ])

    def test_8(self):
        mensaje = bytearray(b"                               ")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"           ",
            b"          ",
            b"          "
        ])

    def test_9(self):
        mensaje = bytearray(b"1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1")
        respuesta = separar_mensaje(mensaje)
        self.assertIsInstance(respuesta, list)
        for n in respuesta:
            self.assertIsInstance(n, bytearray)
        self.assertEqual(respuesta, [
            b"1 1 1 1 1 1 1 1",
            b" 1 1 1 1 1 1 1 ",
            b"1 1 1 1 1 1 1 1"
        ])


if __name__ == "__main__":
    unittest.main(verbosity=2)
