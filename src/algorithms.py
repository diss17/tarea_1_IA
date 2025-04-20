import heapq

def dfs(matriz, filaInicio, columnaInicio, visitados, filaFinal,columnaFinal, pasos, caminoMinimo, caminoActual):
    # Verificar límites y si ya fue visitado
    if (filaInicio < 0 or filaInicio >= len(matriz) or
        columnaInicio < 0 or columnaInicio >= len(matriz[0]) or
        (filaInicio, columnaInicio) in visitados) or matriz[filaInicio][columnaFinal] == 0:
        return False
    
    if pasos >= caminoMinimo[0]:
        return False
    # Marcar la celda como visitada
    visitados.add((filaInicio, columnaInicio))
    caminoActual.append((filaInicio, columnaInicio))
    
    # Verificar si se encontró el valor final
    if (filaInicio, columnaInicio) == (filaFinal, columnaFinal):
        if pasos < caminoMinimo[0]:
           
           #Actualizar camino minimo
           caminoMinimo[0] = pasos
           caminoMinimo[1].clear()
           caminoMinimo[1].extend(caminoActual)
    
        visitados.remove((filaInicio,columnaInicio))                        
        caminoActual.pop()
        return True
    
    # Desplazamientos en las direcciones: arriba, abajo, izquierda, derecha
    valorActual = matriz[filaInicio][columnaInicio]
    direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
    for df, dc in direcciones:
        dfs(matriz, filaInicio + df, columnaInicio + dc, visitados, filaFinal, columnaFinal, pasos + 1, caminoMinimo, caminoActual)

    visitados.remove((filaInicio, columnaInicio))
    caminoActual.pop()
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

            return len(camino), costoAcumulado, camino
        
        #generar vecinos
        valorActual = matriz[fila][columna]
        direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
        for df, dc in direcciones:
            nuevaFila, nuevaColumna = fila + df, columna + dc
             # Si el vecino no ha sido visitado o el nuevo costo es menor, agregarlo a la cola
            if 0 <= nuevaFila < filas and 0 <= nuevaColumna < columnas:
                # Calcular el nuevo costo acumulado al moverse al vecino
                nuevoCosto = costoAcumulado + matriz[nuevaFila][nuevaColumna]

                if(nuevaFila, nuevaColumna) not in visitados or nuevoCosto < visitados[(nuevaFila, nuevaColumna)]:
                    heapq.heappush(priorityQueue, (nuevoCosto, nuevaFila, nuevaColumna))

                    # Registrar la celda actual como el padre del vecino
                    padres[(nuevaFila, nuevaColumna)] = (fila, columna)
    
    return -1, -1, [] # Si no se encuentra un camino