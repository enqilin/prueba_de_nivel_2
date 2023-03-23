""""Crea una clase llamada Punto con sus dos coordenadas X e Y.

• Añade un método constructor para crear puntos fácilmente. Si no se 
reciben una coordenada, su valor será cero.

• Sobreescribe el método string, para que al imprimir por pantalla un 
punto aparezca en formato (X,Y)

• Añade un método llamado cuadrante que indique a qué cuadrante 
pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa 
sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y 
== 0 está sobre el origen.

• Añade un método llamado vector, que tome otro punto y calcule el 
vector resultante entre los dos puntos.

• (Optativo) Añade un método llamado distancia, que tome otro punto 
y calcule la distancia entre los dos puntos y la muestre por pantalla."""




import 

class Punto:
    def __init__(self, x = 0 , y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "el punto es P({},{}).".format(self.x , self.y)

    def cuadrante(self):
        if (self.x > 0 and self.y > 0):
            print("El punto P({},{}) esta en 1º cuatrante. ".format(self.x , self.y))
        elif(self.x < 0 and self.y > 0):
            print("El punto P({},{}) esta en 2º cuatrante. ".format(self.x , self.y))
        elif(self.x < 0 and self.y < 0):
            print("El punto P({},{}) esta en 3º cuatrante. ".format(self.x , self.y))
        elif(self.x > 0 and self.y < 0):
            print("El punto P({},{}) esta en 4º cuatrante. ".format(self.x , self.y))
        elif(self.x == 0 and self.y != 0):
            print("El punto P({},{}) esta sobre eje x. ".format(self.x , self.y))
        elif(self.x != 0 and self.y == 0):
            print("El punto P({},{}) esta sobre eje y. ".format(self.x , self.y))
        elif(self.x== 0 and self.y == 0):
            print("El punto P({},{}) esta en punto del origen. ".format(self.x , self.y))

    def vector(self , punto):
        punto_x = punto.x - self.x
        punto_y = punto.y - self.y
        return "El vector es V({},{})".format(punto_x, punto_y)

    def distancia(self, punto):
        punto_x = punto.x - self.x
        punto_y = punto.y - self.y
    