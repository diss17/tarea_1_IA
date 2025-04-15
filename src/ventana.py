import pygame
import time

# Configuración de colores
COLOR_FONDO = (30, 30, 30)
COLOR_CELDA = (200, 200, 200)
COLOR_VISITADO = (100, 200, 100)
COLOR_CAMINO = (255, 255, 0)
COLOR_INICIO = (0, 255, 0)
COLOR_FINAL = (255, 0, 0)

# Tamaño de la ventana
TAM_CELDA = 40
MARGEN = 2

def dibujar_matriz(pantalla, matriz, visitados, camino, inicio, final):
    filas, columnas = len(matriz), len(matriz[0])
    pantalla.fill(COLOR_FONDO)

    for fila in range(filas):
        for columna in range(columnas):
            color = COLOR_CELDA
            if (fila, columna) in visitados:
                color = COLOR_VISITADO
            if (fila, columna) in camino:
                color = COLOR_CAMINO
            if (fila, columna) == inicio:
                color = COLOR_INICIO
            if (fila, columna) == final:
                color = COLOR_FINAL

            pygame.draw.rect(
                pantalla,
                color,
                [(MARGEN + TAM_CELDA) * columna + MARGEN,
                 (MARGEN + TAM_CELDA) * fila + MARGEN,
                 TAM_CELDA,
                 TAM_CELDA]
            )

    pygame.display.flip()

def visualizar(matriz, visitados, camino, inicio, final):
    pygame.init()
    filas, columnas = len(matriz), len(matriz[0])
    ancho = columnas * (TAM_CELDA + MARGEN) + MARGEN
    alto = filas * (TAM_CELDA + MARGEN) + MARGEN
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Visualización de Búsqueda")

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        dibujar_matriz(pantalla, matriz, visitados, camino, inicio, final)
        time.sleep(0.1)  # Controlar la velocidad de actualización

    pygame.quit()