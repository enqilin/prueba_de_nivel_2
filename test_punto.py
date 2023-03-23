from punto import Punto, Rectangulo
import unittest

class TestPunto(unittest.Testcase):
    def test_cuadrante(self):
        punto1 = Punto(3,4)
        punto2 = Punto(-3,4)
        punto3 = Punto(3,-4)
        punto4 = Punto(-3,-4)
        punto5 = Punto(0,4)
        punto6 = Punto(3,0)
        punto7 = Punto()

        self.assertEqual(Punto.cuadrante(punto1),"El punto P(3,4) esta en 1º cuatrante. ")
        self.assertEqual(Punto.cuadrante(punto2),"El punto P(-3,4) esta en 2º cuatrante. ")
        self.assertEqual(Punto.cuadrante(punto3),"El punto P(3,-4) esta en 3º cuatrante. ")
        self.assertEqual(Punto.cuadrante(punto4),"El punto P(-3,-4) esta en 4º cuatrante. ")
        self.assertEqual(Punto.cuadrante(punto5),"El punto P(0,4) esta sobre eje x. ")
        self.assertEqual(Punto.cuadrante(punto6),"El punto P(3,0) esta sobre eje y. ")
        self.assertEqual(Punto.cuadrante(punto7),"El punto P(0,0) esta en el punto de origen. ")
