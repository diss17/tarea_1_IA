import heapq
from algorithms import dfs
from algorithms import ucs
from utilities import leerMatrices
from ventana import visualizar
if __name__ == "__main__":
    with open("input/input.txt", "r") as archivo:
        # Leer todas las matrices del archivo
        matrices = leerMatrices(archivo)

    # Procesar cada matriz
    for i, (filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal, matriz) in enumerate(matrices):
        print(f"\nProcesando matriz {i + 1}:")
        print("Matriz:")
        for fila in matriz:
            print(fila)

        visitados = set()
        caminoMinimo = [1e9, []]
        caminoActual = []
        iteraciones = []
        caminoMinimo.append(1e9)

        # Ejecutar DFS
        print("Buscando el camino más corto hacia el valor final con DFS ...")
        dfs(matriz, filaInicio, columnaInicio, visitados, filaFinal,columnaFinal, 0, caminoMinimo, caminoActual, iteraciones)

        # Mostrar el resultado
        if caminoMinimo[0] < 1e9:
            print(f"Se llegó a destino en: {caminoMinimo[0]} pasos.")
            print("camino minimo:")
            for paso in caminoMinimo[1]:
                print(paso)
            visualizar(matriz, iteraciones, (filaInicio,columnaInicio), (filaFinal, columnaFinal))
        else:
            print("No se encontró un camino hacia el valor final.")

        # Ejecutar UCS
        print("\nBuscando el camino más corto hacia el valor final con UCS...")
        pasos, costo, camino = ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal)

        # Mostrar el resultado de UCS
        if pasos != -1:
            print(f"UCS: Se llegó a destino con un total de: {pasos} pasos y el costo acumulado es de: {costo}")
            print("Camino óptimo:")
            for paso in camino:
                print(paso)
        else:
            print("UCS: No se encontró un camino hacia el valor final.")