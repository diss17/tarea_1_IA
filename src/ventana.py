import pygame
import os

# Configuración de colores
COLOR_FONDO = (30, 30, 30)
COLOR_CELDA = (200, 200, 200)
COLOR_VISITADO = (100, 200, 100)
COLOR_CAMINO = (255, 255, 0)
COLOR_INICIO = (0, 255, 0)
COLOR_FINAL = (0, 0, 255)
COLOR_FINAL_CONFIRMACION = (255,0, 0)
# Tamaño de la ventana
TAM_CELDA = 40
MARGEN = 2

def dibujar_matriz(pantalla, matriz, visitados, camino, inicio, final, finalAlcanzado):
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
                color = COLOR_FINAL_CONFIRMACION if finalAlcanzado else COLOR_FINAL
            pygame.draw.rect(
                pantalla,
                color,
                [(MARGEN + TAM_CELDA) * columna + MARGEN,
                 (MARGEN + TAM_CELDA) * fila + MARGEN,
                 TAM_CELDA,
                 TAM_CELDA]
            )

    pygame.display.flip()

def visualizar_camino(matriz, caminoMinimo, inicio, final):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    filas, columnas = len(matriz), len(matriz[0])
    ancho = columnas * (TAM_CELDA + MARGEN) + MARGEN
    boton = 50 
    alto = filas * (TAM_CELDA + MARGEN) + MARGEN + boton
    pantalla = pygame.display.set_mode((ancho, alto))  # Redimensionar la ventana
    pygame.display.set_caption("Visualización del Camino Mínimo")
    botonSiguiente = pygame.Rect((ancho//2) - 75, alto - 40, 150, 30)
    # Dibujar el camino paso a paso
    for i in range(len(caminoMinimo)):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        # Dibujar la matriz con el camino hasta el paso actual
        camino_actual = caminoMinimo[:i + 1]
        finalAlcanzado = (i == len(caminoMinimo)-1)
        dibujar_matriz(pantalla, matriz, set(camino_actual), camino_actual, inicio, final, finalAlcanzado)
        pygame.time.delay(500)  # Controlar la velocidad de actualización

    # Mantener la ventana abierta hasta que el usuario cierre o presione una tecla
    while True:
        pantalla.fill(COLOR_FONDO, botonSiguiente)  # Limpiar el área del botón
        pygame.draw.rect(pantalla, (70, 130, 180), botonSiguiente)  # Dibujar el botón
        texto_boton = pygame.font.Font(None, 24).render("Siguiente", True, (255, 255, 255))
        pantalla.blit(texto_boton, (botonSiguiente.x + (botonSiguiente.width - texto_boton.get_width()) // 2,
                                    botonSiguiente.y + (botonSiguiente.height - texto_boton.get_height()) // 2))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonSiguiente.collidepoint(evento.pos):
                    return # Avanzar al procesar la siguiente matriz

def menuSeleccionAlgoritmo():
    pygame.init()
    ancho, alto = 400, 300
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Seleccionar Algoritmo")

    # Botones
    boton_dfs = pygame.Rect(100, 80, 200, 50)
    boton_ucs = pygame.Rect(100, 160, 200, 50)

    fuente = pygame.font.Font(None, 36)
    while True:
        pantalla.fill(COLOR_FONDO)

        # Dibujar botones
        pygame.draw.rect(pantalla, (70, 130, 180), boton_dfs)
        pygame.draw.rect(pantalla, (70, 130, 180), boton_ucs)

        texto_dfs = fuente.render("DFS", True, (255, 255, 255))
        texto_ucs = fuente.render("UCS", True, (255, 255, 255))

        pantalla.blit(texto_dfs, (boton_dfs.x + (boton_dfs.width - texto_dfs.get_width()) // 2,
                                  boton_dfs.y + (boton_dfs.height - texto_dfs.get_height()) // 2))
        pantalla.blit(texto_ucs, (boton_ucs.x + (boton_ucs.width - texto_ucs.get_width()) // 2,
                                  boton_ucs.y + (boton_ucs.height - texto_ucs.get_height()) // 2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_dfs.collidepoint(evento.pos):
                    return "DFS"
                if boton_ucs.collidepoint(evento.pos):
                    return "UCS"