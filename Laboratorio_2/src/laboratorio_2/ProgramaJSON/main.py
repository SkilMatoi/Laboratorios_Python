import json


def mascotas(rutaDelArchivo):

    try:
        # Aqui se abre el archivo JSON
        with open(
            rutaDelArchivo,
            "r",
        ) as archivo:
            datosMacotas = json.load(archivo)

        perros = []
        hamsters = []

        for item in datosMacotas:
            # eL Pattern Matching es el Match y Case
            match item:
                case {"especie": especie, "nombre": nombre, "edad": edad}:

                    if especie == "Perro":
                        perros.append(item)
                        if edad <= 1:
                            print(f"El perro {nombre} es un cachorro")

                    elif especie == "Hamster":
                        hamsters.append(item)

                        if edad <= 1:
                            print(f"El hámster {nombre} es un hamster adulto")

        return perros, hamsters

    except Exception as e:
        print(f"Hay un error al momento de abrir el archivo {e}")
        return


rutaArchivo = r"C:\Users\BBVA\OneDrive - Axity US\Escritorio\Laboratorios_python\Laboratorio_2\src\laboratorio_2\ProgramaJSON\Mascotas.json"


perros, hamsters = mascotas(rutaArchivo)

print(f"Lista de mascotas:")
print(f"Cantidad total de Perros: {len(perros)}")
print(f"Cantidad total de Hámsters: {len(hamsters)}")


if perros:
    print("Perros encontrados:")
    print(perros)
