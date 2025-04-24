import heapq

def dfs(matriz, filaInicio, columnaInicio, visitados, filaFinal,columnaFinal, pasos, caminoMinimo, caminoActual):
     #Verificar límites y si ya fue visitado
     if (filaInicio < 0 or filaInicio >= len(matriz) or
        columnaInicio < 0 or columnaInicio >= len(matriz[0]) or
        (filaInicio, columnaInicio) in visitados):
        return False
     
     if pasos >= caminoMinimo[0]:
        return False
     #Marcar la celda como visitada
     visitados.add((filaInicio, columnaInicio))
     caminoActual.append((filaInicio, columnaInicio))
     #Verificar si se encontró el valor final
     if (filaInicio, columnaInicio) == (filaFinal, columnaFinal):
        if pasos < caminoMinimo[0]:
            caminoMinimo[0] = pasos
            caminoMinimo[1] = list(caminoActual)
        visitados.remove((filaInicio,columnaInicio))
        caminoActual.pop()                        
        return True
     
    #Desplazamientos en las direcciones: arriba, abajo, izquierda, derecha
     valorActual = matriz[filaInicio][columnaInicio]
     direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
     for df, dc in direcciones:
         dfs(matriz, filaInicio + df, columnaInicio + dc, visitados, filaFinal, columnaFinal, pasos + 1, caminoMinimo, caminoActual)
 
    #Desmarcar la celda y eliminarla del camino actual al retroceder
     visitados.remove((filaInicio, columnaInicio))
     caminoActual.pop()
     return False  #Retornar False si no se encuentra el valor final en este camino
def ucs(matriz, filaInicio, columnaInicio, filaFinal, columnaFinal):
    filas, columnas = len(matriz), len(matriz[0])
    visitados = {}
    priorityQueue = []
    heapq.heappush(priorityQueue, (0, filaInicio, columnaInicio, []))  #Agregar el camino como lista vacía

    while priorityQueue:
        #Extraer el nodo con el menor costo acumulado
        costoAcumulado, fila, columna, camino = heapq.heappop(priorityQueue)
        
        #Si ya se visitó esta celda con un costo menor o igual, omitirla
        if (fila, columna) in visitados and visitados[(fila, columna)] <= costoAcumulado:
            continue

        visitados[(fila, columna)] = costoAcumulado
        camino = camino + [(fila, columna)]  #Actualizar el camino

        if (fila, columna) == (filaFinal, columnaFinal):
            return len(camino) - 1, costoAcumulado, camino  #Retornar pasos, costo y el camino óptimo
        # Generar vecinos
        valorActual = matriz[fila][columna]
        direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
        for df, dc in direcciones:
            nuevaFila, nuevaColumna = fila + df, columna + dc
            #Verificar si el vecino está dentro de los límites de la matriz
            if 0 <= nuevaFila < filas and 0 <= nuevaColumna < columnas:
                nuevoCosto = costoAcumulado + valorActual
                #Agregar el vecino a la cola si no ha sido visitado o si tiene un costo menor
                if (nuevaFila, nuevaColumna) not in visitados or nuevoCosto < visitados[(nuevaFila, nuevaColumna)]:
                    heapq.heappush(priorityQueue, (nuevoCosto, nuevaFila, nuevaColumna, camino))
    
    return -1, -1, []  #Si no se encuentra un camino