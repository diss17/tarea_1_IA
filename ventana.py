import pygame
import sys
import time

# Función para leer matrices desde el archivo
def leerMatrices(archivo):
    matrices = []
    while True:
        primeraLinea = archivo.readline().strip()
        if not primeraLinea:
            break
        filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal = map(int, primeraLinea.split())
        matriz = []
        for _ in range(filas):
            fila = list(map(int, archivo.readline().strip().split()))
            matriz.append(fila)
        matrices.append((filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal, matriz))
    return matrices

# Inicializamos pygame
pygame.init()

# Configuración de la ventana
ANCHO_VENTANA = 700
ALTO_VENTANA = 400
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Visualización de DFS")

# Colores
COLOR_FONDO = (30, 30, 30)
COLOR_CELDA = (100, 100, 255)
COLOR_TEXTO = (255, 255, 255)
COLOR_INICIO = (0, 255, 0)
COLOR_FINAL = (255, 0, 0)
COLOR_VISITADO = (255, 255, 0)
COLOR_ACTUAL = (255, 165, 0)

# Fuente para los números
fuente = pygame.font.Font(None, 36)

# Función para dibujar una matriz
def dibujar_matriz(matriz, filas, columnas, pos_inicio, pos_final, visitados, actual=None):
    ventana.fill(COLOR_FONDO)
    tamaño_celda = min(ANCHO_VENTANA // columnas, ALTO_VENTANA // filas)
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * tamaño_celda
            y = fila * tamaño_celda

            # Determinar el color de la celda
            if (fila, columna) == pos_inicio:
                color = COLOR_INICIO
            elif (fila, columna) == pos_final:
                color = COLOR_FINAL
            elif (fila, columna) == actual:
                color = COLOR_ACTUAL
            elif (fila, columna) in visitados:
                color = COLOR_VISITADO
            else:
                color = COLOR_CELDA

            # Dibujar el rectángulo de la celda
            pygame.draw.rect(ventana, color, (x, y, tamaño_celda, tamaño_celda))
            pygame.draw.rect(ventana, (0, 0, 0), (x, y, tamaño_celda, tamaño_celda), 2)

            # Dibujar el valor de la celda
            texto = fuente.render(str(matriz[fila][columna]), True, COLOR_TEXTO)
            texto_rect = texto.get_rect(center=(x + tamaño_celda // 2, y + tamaño_celda // 2))
            ventana.blit(texto, texto_rect)

    pygame.display.flip()

# Función DFS con visualización
def dfs_visual(matriz, fila, columna, visitados, valorFinal, pasos, caminoMinimo, filas, columnas, pos_inicio, pos_final):
    # Verificar límites y si ya fue visitado
    if (fila < 0 or fila >= filas or
        columna < 0 or columna >= columnas or
        (fila, columna) in visitados):
        return False

    # Si el camino actual ya es más largo que el camino más corto encontrado, detener la exploración
    if pasos >= caminoMinimo[0]:
        return False

    # Marcar la celda como visitada
    visitados.add((fila, columna))

    # Dibujar la matriz con la celda actual resaltada
    dibujar_matriz(matriz, filas, columnas, pos_inicio, pos_final, visitados, actual=(fila, columna))
    pygame.time.delay(300)  # Agregar un retraso para visualizar el paso

    # Verificar si se encontró el valor final
    if matriz[fila][columna] == valorFinal:
        if pasos < caminoMinimo[0]:
            caminoMinimo[0] = pasos
        visitados.remove((fila, columna))
        return True

    # Desplazamientos en las direcciones: arriba, abajo, izquierda, derecha
    valorActual = matriz[fila][columna]
    direcciones = [(-valorActual, 0), (valorActual, 0), (0, -valorActual), (0, valorActual)]
    for df, dc in direcciones:
        dfs_visual(matriz, fila + df, columna + dc, visitados, valorFinal, pasos + 1, caminoMinimo, filas, columnas, pos_inicio, pos_final)

    # Desmarcar la celda como visitada (retroceso)
    visitados.remove((fila, columna))
    return False

# Leer las matrices desde el archivo
with open("input.txt", "r") as archivo:
    matrices = leerMatrices(archivo)

# Procesar la primera matriz para la visualización
filas, columnas, filaInicio, columnaInicio, filaFinal, columnaFinal, matriz = matrices[0]
visitados = set()
caminoMinimo = [float('inf')]

# Ejecutar DFS con visualización
dfs_visual(matriz, filaInicio, columnaInicio, visitados, matriz[filaFinal][columnaFinal], 0, caminoMinimo, filas, columnas, (filaInicio, columnaInicio), (filaFinal, columnaFinal))

# Mantener la ventana abierta después de la ejecución
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()