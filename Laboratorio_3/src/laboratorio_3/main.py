import random
import time


class Temporizador:
    def __enter__(self):
        # Lo que pasa al abrir el 'with'
        self.inicio = time.perf_counter()
        return self

    def __exit__(self, tipo_error, valor_error, traza_error):
        # Lo que pasa al cerrar el 'with'
        fin = time.perf_counter()
        print(f"⏱️ Tardó {fin - self.inicio:.4f} segundos.")


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


# Recibe los numeros y los regresa al decorador
@repetidor
def validar_numero(n):
    return n


# Genera numeros aleatorios
def generadordeNumeros(limite):
    numero = 1
    while numero <= limite:
        yield random.randint(1, 20)
        numero = numero + 1


# Crea 3 numeros aleatorios
prueba = generadordeNumeros(3)

# Recorre los 3 numeros generados
for n in prueba:
    print(f"\nNuevo numero")
    validar_numero(n)


# Uso:
with Temporizador():
    time.sleep(1)
