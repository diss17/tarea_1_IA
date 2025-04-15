import heapq

def dfs(matriz, filaInicio, columnaInicio, visitados, filaFinal,columnaFinal, pasos, caminoMinimo):
    # Verificar límites y si ya fue visitado
    if (filaInicio < 0 or filaInicio >= len(matriz) or
        columnaInicio < 0 or columnaInicio >= len(matriz[0]) or
        (filaInicio, columnaInicio) in visitados):
        return False
    
    if pasos >= caminoMinimo[0]:
        return False
    # Marcar la celda como visitada
    visitados.add((filaInicio, columnaInicio))
    
    # Verificar si se encontró el valor final
    if (filaInicio, columnaInicio) == (filaFinal, columnaFinal):
        if pasos < caminoMinimo[0]:
           caminoMinimo[0] = pasos
        visitados.remove((filaInicio,columnaInicio))                        
        return True
    
    # Desplazamientos en las direcciones: arriba, abajo, izquierda, derecha
    valorActual = matriz[filaInicio][columnaInicio]
    direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
    for df, dc in direcciones:
        dfs(matriz, filaInicio + df, columnaInicio + dc, visitados, filaFinal, columnaFinal, pasos + 1, caminoMinimo)

    visitados.remove((filaInicio, columnaInicio))
    return False  # Retornar False si no se encuentra el valor final en este camino

def ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal):
    filas, columnas = len(matriz), len(matriz[0])
    visitados = {}
    priorityQueue = []
    padres = {}
    pasos = 0
    heapq.heappush(priorityQueue, (0, filaInicio, columnaInicio))

    while priorityQueue:
        costoAcumulado, fila, columna = heapq.heappop(priorityQueue)
        
        if (fila, columna) in visitados and visitados[(fila, columna)] <= costoAcumulado:
            continue

        visitados[(fila, columna)] = costoAcumulado
        
        pasos += 1

        if (fila, columna) == (filaFinal, columnaFinal):
            camino = []
            actual = (fila, columna)
            while actual in padres:
                camino.append(actual)
                actual = padres[actual]
            camino.append((filaInicio, columnaInicio))
            camino.reverse()

            return pasos, costoAcumulado, camino
        
        #generar vecinos
        valorActual = matriz[fila][columna]
        direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
        for df, dc in direcciones:
            nuevaFila, nuevaColumna = fila + df, columna + dc
            if 0 <= nuevaFila < filas and 0 <= nuevaColumna < columnas:
                nuevoCosto = costoAcumulado + matriz[nuevaFila][nuevaColumna]
                if(nuevaFila, nuevaColumna) not in visitados or nuevoCosto < visitados[(nuevaFila, nuevaColumna)]:
                    heapq.heappush(priorityQueue, (nuevoCosto, nuevaFila, nuevaColumna))
                    padres[(nuevaFila, nuevaColumna)] = (fila, columna)
    
    return -1, -1, [] # Si no se encuentra un camino