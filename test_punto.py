from punto import Punto
from rectangulo import Rectangulo
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

    def test_vector(self):
        punto = Punto(4,5)
        punto1 = Punto(3,4)
        self.assertEqual(Punto.vector(punto,punto1), "El vector es V(-1,-1)")

    def test_distancia(self):
        self.assertEqual(Punto.distancia((Punto(4,4),(4,5)), "La distancia es 1"))

    def test_base(self):
        self.assertEqual(Rectangulo.base((3,4),(4,5)),"La base es 1")

    def test_altura(self):
        self.assertEqual(Rectangulo.altura((3,4),(4,5)),"La altura es 1")

    def test_area(self):
        self.assertEqual(Rectangulo.area((3,4),(4,5)),"El area es 1 unidad al cuadrado")