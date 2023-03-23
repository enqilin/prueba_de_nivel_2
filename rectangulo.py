
from punto import Punto

"""• Crea una clase llamada Rectangulo con dos puntos (inicial y final) 
que formarán la diagonal del rectángulo.
• Añade un método constructor para crear ambos puntos fácilmente, 
si no se envían se crearán dos puntos en el origen por defecto.
• Añade al rectángulo un método llamado base que muestre la base.
• Añade al rectángulo un método llamado altura que muestre la altura.
• Añade al rectángulo un método llamado area que muestre el area"""




class Rectangulo(Punto):
    def __init__(self):
        super().__init__(self)

    def base(self, punto):
        base = abs(self.x -punto.x)
        return "La base es {}".format(base)

    def altura(self,punto):
        altura = abs(self.y - punto.y)
        return "La altura es {}".format(altura)

    def area(self,punto):
        base = abs(self.x -punto.x)
        altura = abs(self.y - punto.y)
        area = base * altura
        return "El area es{} unidad al cuadrado".format(area)