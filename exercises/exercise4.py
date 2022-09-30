"""DataClasses y Sobrecarga de operadores."""

from dataclasses import dataclass
from typing import List

@dataclass
class Materia():
    nombre: str

@dataclass
class Carrera():                                
    lista_materias: list
    
    def __str__(self):
        return f"Carrera({self.lista_materias})"

matematica = Materia("Matemática")
estadistica = Materia("Estadística")
programacion = Materia("Programación")
ciclo_basico = Carrera([matematica, estadistica, programacion])
print(ciclo_basico)
print(len(ciclo_basico.lista_materias))



"""Una carrera tiene varias materias, la "longitud" de una carrera hace
referencia a cuantas materias tiene.

Cada materia tiene un nombre.

Escribir una estructura de clases que refleje lo anterior.

Restricciones:
    - Utilizar Dataclasses
    - Utilizar 2 clases
    - Utilizar 1 variables de instancia en cada clase
    - Utilizar 1 método mágico
    - No utilizar variables de clase
    - No utilizar métodos de clase
    - No utilizar métodos de instancia
    - No utilizar properties
    - Utilizar Type Hints en todos los métodos y variables
"""


# NO MODIFICAR - INICIO
# Test parámetro obligatorio
# try:
#     materia = Materia()
#     assert False, "No se puede instanciar sin nombre"
# except TypeError:
#     assert True

# try:
#     materia = Carrera()
#     assert False, "No se puede instanciar sin materias"
# except TypeError:
#     assert True

# # Test básico
# matematica = Materia("Matemática")
# assert matematica.nombre == "Matemática"

# estadistica = Materia(nombre="Estadística")
# assert estadistica.nombre == "Estadística"

# ciclo_basico = Carrera([matematica, estadistica])
# assert (
#     str(ciclo_basico)
#     == "Carrera(materias=[Materia(nombre='Matemática'), Materia(nombre='Estadística')])"  # noqa: 501
# )

# assert len(ciclo_basico.longitud) == 2
# # NO MODIFICAR - FIN
