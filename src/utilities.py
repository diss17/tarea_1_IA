def leerMatrices(archivo):
    matrices = []
    while True:
        # Leer la primera línea del bloque
        primeraLinea = archivo.readline().strip()
        if not primeraLinea or primeraLinea == "0": #más líneas, salir del bucle
            break

        # Extraer dimensiones y posiciones iniciales/finales
        filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal = map(int, primeraLinea.split())

        # Leer la matriz
        matriz = []
        for _ in range(filas):
            fila = list(map(int, archivo.readline().strip().split()))
            matriz.append(fila)

        # Agregar la matriz y su configuración a la lista
        matrices.append((filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal, matriz))

    return matrices