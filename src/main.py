import heapq

def leerMatrices(archivo):
    matrices = []
    while True:
        # Leer la primera línea del bloque
        primeraLinea = archivo.readline().strip()
        if not primeraLinea:  # Si no hay más líneas, salir del bucle
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

def initialSearch(matriz, filaInicio, columnaInicio):
    if 0 <= filaInicio < len(matriz) and 0 <= columnaInicio < len(matriz[0]):
        return matriz[filaInicio][columnaInicio]
def finialSearch(matriz, filaFinal, columnaFinal):
    if 0 <= filaFinal < len(matriz) and 0 <= columnaFinal < len(matriz[0]):    
        return matriz[filaFinal][columnaFinal]

def dfs(matriz, fila, columna, visitados, valorFinal, pasos, caminoMinimo):
    # Verificar límites y si ya fue visitado
    if (fila < 0 or fila >= len(matriz) or
        columna < 0 or columna >= len(matriz[0]) or
        (fila, columna) in visitados):
        return False
    
    if pasos >= caminoMinimo[0]:
        return False
    # Marcar la celda como visitada
    visitados.add((fila, columna))
    
    # Verificar si se encontró el valor final
    if matriz[fila][columna] == valorFinal:
        if pasos < caminoMinimo[0]:
           caminoMinimo[0] = pasos
        visitados.remove((fila,columna))                        
        return True
    
    # Desplazamientos en las direcciones: arriba, abajo, izquierda, derecha
    valorActual = matriz[fila][columna]
    direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
    for df, dc in direcciones:
        dfs(matriz, fila + df, columna + dc, visitados, valorFinal, pasos + 1, caminoMinimo)

    visitados.remove((fila, columna))
    return False  # Retornar False si no se encuentra el valor final en este camino

def ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal):
    filas, columnas = len(matriz), len(matriz[0])
    visitados = set()
    priorityQueue = []
    pasos = 0
    heapq.heappush(priorityQueue, (0, filaInicio, columnaInicio))

    while priorityQueue:
        costoActual, fila, columna = heapq.heappop(priorityQueue)
        pasos += 1
        if(fila, columna) in visitados:
            continue
        visitados.add((fila, columna))
        
        if(fila, columna) == (filaFinal, columnaFinal):
           return costoActual, pasos
        valorActual = matriz[fila][columna]
        direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
        for df, dc in direcciones:
            nuevaFila, nuevaColumna = fila + df, columna + dc
            if 0 <= nuevaFila < filas and 0 <= nuevaColumna < columnas and (nuevaFila, nuevaColumna) not in visitados:
                nuevoCosto = costoActual + matriz[nuevaFila][nuevaColumna]        
                heapq.heappush(priorityQueue, (nuevoCosto, nuevaFila, nuevaColumna))
    
    return -1, pasos
    
if __name__ == "__main__":
    with open("src/input.txt", "r") as archivo:
        # Leer todas las matrices del archivo
        matrices = leerMatrices(archivo)

    # Procesar cada matriz
    for i, (filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal, matriz) in enumerate(matrices):
        print(f"\nProcesando matriz {i + 1}:")
        print("Matriz:")
        for fila in matriz:
            print(fila)

        valorInicio = initialSearch(matriz, filaInicio, columnaInicio)
        valorFinal = finialSearch(matriz, filaFinal, columnaFinal)
        visitados = set()


        caminoMinimo = []
        caminoMinimo.append(1e9)

        # Ejecutar DFS
        print("Buscando el camino más corto hacia el valor final...")
        dfs(matriz, filaInicio, columnaInicio, visitados, valorFinal, 0, caminoMinimo)

        # Mostrar el resultado
        if caminoMinimo[0] < 1e9:
            print(f"Se llegó a destino en: {caminoMinimo[0]} pasos.")
        else:
            print("No se encontró un camino hacia el valor final.")
        # Ejecutar UCS
        print("\nBuscando el camino más corto hacia el valor final con UCS...")
        costo, pasos = ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal)

        # Mostrar el resultado de UCS
        if costo != -1:
            print(f"UCS: Se llegó a destino con un costo total de: {costo}. Con un total de: {pasos} pasos")
        else:
            print("UCS: No se encontró un camino hacia el valor final.")