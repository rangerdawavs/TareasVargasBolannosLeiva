#   Tarea 1 v5.py


# modulo #1, toma dos operandos, y le aplica una de tres operaciones
# retorna el resultado de la operación


def basic_operations(op1, op2, OP):
    if (type(op1) != int):  # revisamos el tipo de los operandos,
        return "E22a"  # para estar seguro que son enteros
    if (type(op2) != int):
        return "E22a"
    if (type(OP) != int):
        return "E22a"
# revisamos que el código del operando esté entre 1 y 3
# además retornamos la operación correspondiente
    if (OP > 0 and OP < 4):
        if (OP == 1):
            return op1+op2
        if (OP == 2):
            return op1-op2
# revisamos la divión entre cero
        if (OP == 3):
            if (op2 == 0):
                return 'E1'
            else:
                return op1/op2
    else:
        return 'E3'


# modulo #2, toma un string, y retorna la cantidad de caracteres


def count_char(string):
    if (type(string) != str):  # revisamos que sea string
        return 'E22b'
    else:
        return len(string)  # retornamos la longitud del string
