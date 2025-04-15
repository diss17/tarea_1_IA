import heapq
from algorithms import dfs
from algorithms import ucs
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

        visitados = set()
        caminoMinimo = []
        caminoMinimo.append(1e9)

        # Ejecutar DFS
        print("Buscando el camino más corto hacia el valor final...")
        dfs(matriz, filaInicio, columnaInicio, visitados, filaFinal,columnaFinal, 0, caminoMinimo)

        # Mostrar el resultado
        if caminoMinimo[0] < 1e9:
            print(f"Se llegó a destino en: {caminoMinimo[0]} pasos.")
        else:
            print("No se encontró un camino hacia el valor final.")
        # Ejecutar UCS
        print("\nBuscando el camino más corto hacia el valor final con UCS...")
        pasos, costo = ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal)

        # Mostrar el resultado de UCS
        if pasos != -1:
            print(f"UCS: Se llegó a destino con un total de: {pasos} pasos y el costo acumulado es de: {costo}")
        else:
            print("UCS: No se encontró un camino hacia el valor final.")