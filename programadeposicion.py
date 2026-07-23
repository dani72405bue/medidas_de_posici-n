"""Programa para calcular medidas de posición: cuartiles, percentiles y deciles."""

# Importa la función sys para poder salir del programa de forma controlada.
import sys


# Define una función que calcula un percentil usando interpolación lineal.
def calcular_percentil(datos, porcentaje):
    # Ordena los datos de menor a mayor para poder ubicar correctamente el percentil.
    datos_ordenados = sorted(datos)
    # Obtiene la cantidad total de datos.
    n = len(datos_ordenados)
    # Si no hay datos, devuelve None para evitar errores.
    if n == 0:
        return None
    # Si solo hay un dato, ese valor es el percentil solicitado.
    if n == 1:
        return datos_ordenados[0]
    # Calcula la posición del percentil dentro de la lista ordenada.
    posicion = (n - 1) * (porcentaje / 100)
    # Redondea hacia abajo para obtener el índice inferior.
    indice_inferior = int(posicion)
    # Redondea hacia arriba para obtener el índice superior.
    indice_superior = min(indice_inferior + 1, n - 1)
    # Calcula la fracción entre ambos índices para interpolar.
    fraccion = posicion - indice_inferior
    # Si ambos índices son iguales, no hay interpolación y se devuelve ese valor.
    if indice_inferior == indice_superior:
        return datos_ordenados[indice_inferior]
    # Devuelve el valor interpolado entre los dos datos cercanos.
    return datos_ordenados[indice_inferior] + (datos_ordenados[indice_superior] - datos_ordenados[indice_inferior]) * fraccion


# Define una función para mostrar los resultados de forma ordenada.
def mostrar_resultados(titulo, resultados):
    # Imprime el título del bloque de resultados.
    print(f"\n{titulo}")
    # Recorre cada clave y valor del diccionario para mostrarlos uno por uno.
    for clave, valor in resultados.items():
        # Imprime cada resultado con dos decimales para mejor lectura.
        print(f"{clave}: {valor:.2f}")


# Muestra el propósito del programa al usuario.
print("Bienvenido al programa de medidas de posición")
print("Este programa calcula cuartiles, percentiles y deciles desde datos ingresados por ti.")
print("Puedes ingresar hasta 150 datos.")

while True:
    # Solicita la cantidad de datos que el usuario desea ingresar.
    try:
        cantidad = int(input("\n¿Cuántos datos deseas ingresar? "))
    except ValueError:
        # Si el usuario no ingresa un número, termina el programa con un mensaje.
        print("Debes ingresar un número entero.")
        continue

    # Valida que la cantidad de datos sea válida.
    while cantidad < 1 or cantidad > 150:
        # Muestra un mensaje si la cantidad está fuera del rango permitido.
        print("La cantidad debe ser un número entre 1 y 150.")
        try:
            cantidad = int(input("¿Cuántos datos deseas ingresar? "))
        except ValueError:
            print("Debes ingresar un número entero.")
            break

    if cantidad < 1 or cantidad > 150:
        continue

    # Crea una lista vacía para guardar los datos ingresados.
    datos = []

    # Repite el proceso tantas veces como datos haya pedido el usuario.
    for i in range(1, cantidad + 1):
        # Solicita cada dato por separado.
        while True:
            try:
                valor = float(input(f"Ingresa el dato {i}: "))
                break
            except ValueError:
                # Si el dato no es numérico, avisa y vuelve a pedirlo.
                print("Debes ingresar un número válido. Inténtalo de nuevo.")
        # Agrega el valor ingresado a la lista.
        datos.append(valor)

    # Muestra los datos originales para que el usuario los pueda revisar.
    print("\nDatos ingresados:", datos)

    # Ordena los datos para trabajar con ellos de forma organizada.
    datos_ordenados = sorted(datos)
    # Muestra los datos ya ordenados.
    print("Datos ordenados:", datos_ordenados)

    # Muestra las opciones disponibles para que el usuario elija.
    print("\n¿Qué deseas calcular?")
    print("1. Cuartiles")
    print("2. Percentiles")
    print("3. Deciles")
    print("4. Todo")
    print("5. Salir")

    # Solicita la opción elegida por el usuario.
    try:
        opcion = int(input("Elige una opción (1-5): "))
    except ValueError:
        print("Debes ingresar un número entero.")
        continue

    # Si la opción elegida es cuartiles, calcula Q1, Q2 y Q3.
    if opcion == 1:
        resultados = {
            "Q1": calcular_percentil(datos_ordenados, 25),
            "Q2": calcular_percentil(datos_ordenados, 50),
            "Q3": calcular_percentil(datos_ordenados, 75),
        }
        mostrar_resultados("Resultados de cuartiles", resultados)

    # Si la opción elegida es percentiles, solicita los percentiles que quiere calcular.
    elif opcion == 2:
        cantidad_percentiles = int(input("¿Cuántos percentiles quieres calcular? "))
        resultados = {}
        for i in range(1, cantidad_percentiles + 1):
            try:
                porcentaje = float(input(f"Ingresa el percentil {i} (por ejemplo 20 para P20): "))
            except ValueError:
                print("Debes ingresar un número válido.")
                break
            resultados[f"P{int(porcentaje)}"] = calcular_percentil(datos_ordenados, porcentaje)
        mostrar_resultados("Resultados de percentiles", resultados)

    # Si la opción elegida es deciles, solicita los deciles que quiere calcular.
    elif opcion == 3:
        cantidad_deciles = int(input("¿Cuántos deciles quieres calcular? "))
        resultados = {}
        for i in range(1, cantidad_deciles + 1):
            try:
                decil = float(input(f"Ingresa el decil {i} (por ejemplo 2 para D2): "))
            except ValueError:
                print("Debes ingresar un número válido.")
                break
            resultados[f"D{int(decil)}"] = calcular_percentil(datos_ordenados, decil * 10)
        mostrar_resultados("Resultados de deciles", resultados)

    # Si la opción elegida es 4, calcula cuartiles, percentiles y deciles juntos.
    elif opcion == 4:
        cuartiles = {
            "Q1": calcular_percentil(datos_ordenados, 25),
            "Q2": calcular_percentil(datos_ordenados, 50),
            "Q3": calcular_percentil(datos_ordenados, 75),
        }
        mostrar_resultados("Resultados de cuartiles", cuartiles)

        percentiles = {}
        for valor in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            percentiles[f"P{valor}"] = calcular_percentil(datos_ordenados, valor)
        mostrar_resultados("Resultados de percentiles", percentiles)

        deciles = {}
        for valor in range(1, 10):
            deciles[f"D{valor}"] = calcular_percentil(datos_ordenados, valor * 10)
        mostrar_resultados("Resultados de deciles", deciles)

    elif opcion == 5:
        print("Gracias por usar el programa.")
        break

    # Si la opción no es válida, muestra un mensaje de error.
    else:
        print("Opción no válida.")
