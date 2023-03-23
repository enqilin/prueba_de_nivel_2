import punto as pt
import rectangulo as rt
import unittest

class TestPunto(unittest.Testcase):
    def test_cuadrante(self):
        punto1 = pt.Punto(3,4)
        punto2 = pt.Punto(-3,4)
        punto3 = pt.Punto(3,-4)
        punto4 = pt.Punto(-3,-4)
        punto5 = pt.Punto(0,4)
        punto6 = pt.Punto(3,0)
        punto7 = pt.Punto()

        self.assertEqual(pt.Punto.cuadrante(punto1),"El punto P(3,4) esta en 1º cuatrante. ")
        self.assertEqual(pt.Punto.cuadrante(punto2),"El punto P(-3,4) esta en 2º cuatrante. ")
        self.assertEqual(pt.Punto.cuadrante(punto3),"El punto P(3,-4) esta en 3º cuatrante. ")
        self.assertEqual(pt.Punto.cuadrante(punto4),"El punto P(-3,-4) esta en 4º cuatrante. ")
        self.assertEqual(pt.Punto.cuadrante(punto5),"El punto P(0,4) esta sobre eje x. ")
        self.assertEqual(pt.Punto.cuadrante(punto6),"El punto P(3,0) esta sobre eje y. ")
        self.assertEqual(pt.Punto.cuadrante(punto7),"El punto P(0,0) esta en el punto de origen. ")

    def test_vector(self):
        punto = pt.Punto(4,5)
        punto1 = pt.Punto(3,4)
        self.assertEqual(pt.Punto.vector(punto,punto1), "El vector es V(-1,-1)")

    def test_distancia(self):
        self.assertEqual(pt.Punto.distancia((pt.Punto(4,4),(4,5)), "La distancia es 1"))

    def test_base(self):
        self.assertEqual(rt.Rectangulo.base((3,4),(4,5)),"La base es 1")

    def test_altura(self):
        self.assertEqual(rt.Rectangulo.altura((3,4),(4,5)),"La altura es 1")

    def test_area(self):
        self.assertEqual(rt.Rectangulo.area((3,4),(4,5)),"El area es 1 unidad al cuadrado")