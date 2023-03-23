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




import math

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
        punto_x = (punto.x - self.x)**2
        punto_y = (punto.y - self.y)**2
        distance = math.sqrt(punto_x + punto_y)
        return "La distancia es {}".format(distance)



"""• Crea una clase llamada Rectangulo con dos puntos (inicial y final) 
que formarán la diagonal del rectángulo.
• Añade un método constructor para crear ambos puntos fácilmente, 
si no se envían se crearán dos puntos en el origen por defecto.
• Añade al rectángulo un método llamado base que muestre la base.
• Añade al rectángulo un método llamado altura que muestre la altura.
• Añade al rectángulo un método llamado area que muestre el area"""

class Rectangulo(Punto):
    def __init__(self, x2 = 0 ,y2 = 0):
        super().__init__(self)
        self.x2 = x2
        self.y2 = y2

    def base(self, punto):
        base = abs(self.x -punto.x)
        return "la base del rectangulo es {}".format(base)

    def altura(self,punto):
        altura = abs(self.y - punto.y)
        return "La altura es {}".format(altura)

    def area(self,punto):
        base = abs(self.x -punto.x)
        altura = abs(self.y - punto.y)
        area = base * altura
        return "El area es{}".format(area)