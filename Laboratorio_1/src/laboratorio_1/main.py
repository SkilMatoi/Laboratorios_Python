import sys
import os  # Imports desordenados y en líneas que no corresponden


def mi_funcion_con_errores(a, b):  # Falta espacio tras la coma
    x = 10  # Demasiados espacios en la asignación
    print(f"Resultado: {a+b+x}")  # Espacio innecesario antes del paréntesis
    return x
    # Uso de punto y coma
