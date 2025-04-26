from algorithms import dfs, ucs
from utilities import leerMatrices
from ventana import visualizarCamino, menuSeleccionAlgoritmo

if __name__ == "__main__":
    with open("input/input3.txt", "r") as archivo:
        # Leer todas las matrices del archivo
        matrices = leerMatrices(archivo)
    algoritmo = menuSeleccionAlgoritmo()

    if algoritmo is None:
        exit()

    # Procesar cada matriz
    for i, (filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal, matriz) in enumerate(matrices):
        print(f"Procesando matriz {i + 1}:")
        print("Matriz:")
        for fila in matriz:
            print(fila)

        if algoritmo == "DFS":
            visitados = set()
            caminoMinimo = [1e9, []]
            caminoActual = []
            print("Buscando el camino más corto hacia el valor final con DFS ...")
            dfs(matriz, filaInicio, columnaInicio, visitados, filaFinal, columnaFinal, 0, caminoMinimo, caminoActual)
            if caminoMinimo[0] < 1e9:
                print(f"Se llegó a destino en: {caminoMinimo[0]} pasos.")
                print("Camino mínimo:")
                for paso in caminoMinimo[1]:
                    print(paso)
                visualizarCamino(matriz, caminoMinimo[1], (filaInicio, columnaInicio), (filaFinal, columnaFinal))
            else:
                print("No se encontró un camino hacia el valor final.")

        elif algoritmo == "UCS":
            print("Buscando el camino más corto hacia el valor final con UCS...")
            pasos, costo, camino = ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal)

            # Mostrar el resultado de UCS
            if pasos != -1:
                print(f"UCS: Se llegó a destino con un total de: {len(camino)-1} pasos y el costo acumulado es de: {costo}")
                print("Camino óptimo:")
                for paso in camino:
                    print(paso)
                visualizarCamino(matriz, camino, (filaInicio, columnaInicio), (filaFinal, columnaFinal))
            else:
                print("UCS: No se encontró un camino hacia el valor final.")