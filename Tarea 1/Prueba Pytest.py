
# Las siguientes funciones permiten probar
# las funciones basic_operations y count_char.
# Se usa pytest 7.1.2 para las pruebas.

from Tarea_1_v6 import basic_operations
# se importa la función basic_operations .

from Tarea_1_v6 import count_char  # se importa la función count_char.


# Pruebas para el metodo basic_operations.

def testsum():  # Prueba de suma
    assert basic_operations(4, 4, 1) == 8
# El assert permite verificar que una condicion sea verdadera,
# si no lo es dara una excepcion como resultado.


def testres():  # Prueba resta
    assert basic_operations(4, 1, 2) == 3


def testdiv():  # Prueba la division
    assert basic_operations(4, 2, 3) == 2


def testdivbyzero():
    # Prueba la division por cero que debe retornar un Cod. de Error.
    assert basic_operations(4, 0, 3) == 'E1'


def testoutrange():
    # Prueba el codigo de error
    # al ingrasar al sistema una opcion que no existe.
    assert basic_operations(4, 4, 4) == 'E3'


def testnotintbutstr():  # Prueba el codigo de error cuando se ingresa un STR.
    assert basic_operations('t', 't', 't') == 'E22a'


def testnotintbutfloat():
    # Prueba el codigo de error cuando se ingresa un FLOAT.
    assert basic_operations(3.14, 3.14, 3.14) == 'E22a'


# Puebas para el metodo count_char.


def testnotstrint():  # Prueba el codigo de error cuando se ingresa un INT.
    assert count_char(40) == 'E22b'


def testnotstrbool():  # Prueba el codigo de error cuando se ingresa un FLOAT.
    assert count_char(3.14) == 'E22b'


def testforstr():  # Prueba de la lectura de caracteres de un STR
    assert count_char('Hola Mundo') == 10

#    Para las pruebas se necesita tener instalado pytest,
#    ademas se necesita que el archivo.py del programa principal
#    y el programa de testeo esten en la misma carpeta.
#
#    Para iniciar la prueba se abre el Command Prompt, se busca la ruta
#    en la que se localizan ambos archivos y por ultimo se ejecuta el
#    comando:
#            pytest "nombre del .py de testeo"
#
#            pytest PruebaPytest.py
