"""Variables de Instancia y Métodos de instancia."""

from math import pi

class Circle:

    def __init__(self, radio: float):
        self.radio = radio

    def calculos(self):
        area = (pi * (self.radio ** 2))
        perimetro = (pi * 2 * self.radio)
        return print("El área es:", area,"y el perímetro es:", perimetro)

circle = Circle(1)
print(circle.radio)
circle.calculos()


    
    
"""Todo círculo tiene un radio y se desea conocer tanto el área como el
    perímetro (longitud de circunferencia).

    Reportar los números redondeados a dos decimales

    Restricciones:
        - Utilizar 1 variable de instancia
        - Utilizar 2 métodos de instancia
        - No utilizar variable de clase
        - No utilizar Dataclasses
        - No utilizar Properties
        - Utilizar Type Hints en todos los métodos y variables
    """


# NO MODIFICAR - INICIO
# Test básico
circle = Circle(1)
assert circle.radio == 1
assert circle.area() == 3.14
assert circle.perimetro() == 6.28

# Test palabra clave
circle = Circle(radio=1)
assert circle.radio == 1
assert circle.area() == 3.14
assert circle.perimetro() == 6.28

# Test parámetro obligatorio
try:
    circle = Circle()
    assert False, "No se puede instanciar sin radio"
except TypeError:
    assert True

# Test invocación encadenada
assert Circle(1).area() == 3.14
assert Circle(1).perimetro() == 6.28
# NO MODIFICAR - FIN
