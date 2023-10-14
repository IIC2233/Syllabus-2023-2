import sys
import unittest

# Advertencia, la siguiente línea solo es utiliza por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from funciones_servidor import encriptar_mensaje


class TestEncriptarMensaje(unittest.TestCase):

    def test_0(self):
        mensaje = bytearray(b"Hola Mundo")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(b'1HMuladoo n'))

    def test_1(self):
        mensaje = bytearray(b"\xc2\xb4+{}[]\xc2\xa8*!#$%&/()")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(b'0\xb4}\xc2!%(\xc2[]#$)+{\xa8*&/'))

    def test_2(self):
        mensaje = bytearray(b"A\xc3\xb1o nuevo, vida nueva")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(
            b'0\xc3 e,i eAnu vnu\xb1ovodava'))

    def test_3(self):
        mensaje = bytearray(b"\xc3\xb1a\xc3\xb1e\xc3\xb1i\xc3\xb1d\xc3\xb1r\xc3"
                            b"\xb1t\xc3\xb1ch\xc3\xb1h\xc3\xb1l\xc3\xb1\xc3\xb1"
                            b"\xc2\xb4\xc2\xb4\xc3\xb1\xc3\xb1\xc2\xb4\xc2\xb4\xc3\xb1")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(
            b"1\xc3e\xc3d\xc3t\xc3\xb1h\xb1\xc3\xb4\xc3\xb4\xc2a\xc3i\xc3r"
            b"\xc3ch\xb1l\xc2\xb4\xc3\xb1\xc3\xb1\xb1\xb1\xb1\xb1\xb1\xb1"
            b"\xb1\xc3\xc3\xc3\xb1\xc2\xb1\xc2\xb4"))

    def test_4(self):
        mensaje = bytearray(
            b"{}\xc2\xb4+[]\xc2\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1\\\xc2\xb8"
            b"\xc2\xa8*^`\xc2\xa8~\'\xc2\xbf?\xc2\xa1\\\xc2\xb8|\xc2\xb0\xc2"
            b"\xac!#$%&/()=|@\xc2\xb7~\xc2\xbd\xc2\xac{[]}")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(
            b"1{[]`\xc2\xbf?\xb8\xc2\xc2\xa8?\xc2|\xc2#$)=~"
            b"\xc2[]\xc2\xb4\xa8*~\'\xa1\\*^\'\xc2\\\xc2\xc2"
            b"\xac&/@\xc2\xc2\xac}+\xc2^\xa8\xc2\xc2\xc2\xa8`~"
            b"\xbf\xa1\xb8\xb0!%(|\xb7\xbd{}"))

    def test_5(self):
        mensaje = bytearray(
            b"\xe2\x80\xa1\xe2\x80\xa0\xc6\x92\xe2\x82\xac\xe2\x80\xb0\xc5\xa0\xc5\x92\xc5\xbd")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(
            b'1\xe2\xa0\xc6\xe2\x80\x92\xc5\xa1\xe2\xe2\x82\xc5\xa0\x80\x80\x92\xac\xb0\xc5\xbd'))

    def test_6(self):
        mensaje = bytearray(b"\xc2\xb4+{}[]\xc2\xa8*!#$%&/()")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(b'0\xb4}\xc2!%(\xc2[]#$)+{\xa8*&/'))

    def test_7(self):
        mensaje = bytearray(b"a b c")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(b'1ab  c'))

    def test_8(self):
        mensaje = bytearray(b"11 1 1 1 1 1 1 1 1 1 1 11")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(b'01 1 1 1 11 1 1 11 1 1 1 1'))

    def test_9(self):
        mensaje = bytearray(b"abcdefghijklmnopqrstuvwxyz")
        respuesta = encriptar_mensaje(mensaje)
        self.assertIsInstance(respuesta, bytearray)
        self.assertEqual(respuesta, bytearray(b'1afglmrsxycdijopuvbehknqtwz'))


if __name__ == "__main__":
    unittest.main(verbosity=2)
