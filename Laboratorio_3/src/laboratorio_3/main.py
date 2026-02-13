import random
import time


def repetidor(funcion):
    def wrapper(*args, **kwargs):
        intentos = 3
        for i in range(intentos):
            print(f"Intento: {i+1}")
            resultado = funcion(*args, **kwargs)
            # Si el número es mayor a 10 termina
            if resultado > 10:
                print(f"El numero {resultado} es mayor a 10.")
                return resultado
            print(f"El numero {resultado} es menor a 10")
            time.sleep(1)
        return "Todos son menores a 10"

    return wrapper



@repetidor
def validar_numero(n):
    return n


def generadordeNumeros(limite):
    numero = 1
    while numero <= limite:
        yield random.randint(1, 20)
        numero = numero + 1



prueba = generadordeNumeros(3)


for n in prueba:
    print(f"\nNuevo numero")
    validar_numero(n)

