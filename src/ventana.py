import pygame
import os

# Configuración de colores
COLOR_FONDO = (30, 30, 30)
COLOR_CELDA = (200, 200, 200)
COLOR_VISITADO = (255, 255, 0)
COLOR_CAMINO = (255, 165, 0)
COLOR_INICIO = (0, 255, 0)
COLOR_FINAL = (255, 0, 0)
COLOR_FINAL_CONFIRMACION = (0,255, 0)
COLOR_BOTON_HOVER = (0, 92, 191)    
COLOR_TEXTO_BOTON = (255, 255, 255) 
# Tamaño de la ventana
TAM_CELDA = 40
MARGEN = 2

def dibujarMatriz(pantalla, matriz, visitados, camino, inicio, final, finalAlcanzado):
    filas, columnas = len(matriz), len(matriz[0])
    pantalla.fill(COLOR_FONDO)

    fuente = pygame.font.Font(None, 24)

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
            valorCelda = str(matriz[fila][columna])
            texto = fuente.render(valorCelda, True, (0, 0, 0))
            textRect =  texto.get_rect(center=(
                (MARGEN + TAM_CELDA) * columna + MARGEN + TAM_CELDA // 2,
                (MARGEN + TAM_CELDA) * fila + MARGEN + TAM_CELDA // 2
            ))
            pantalla.blit(texto, textRect)
    pygame.display.flip()

def visualizarCamino(matriz, caminoMinimo, inicio, final):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    filas, columnas = len(matriz), len(matriz[0])
    ancho = columnas * (TAM_CELDA + MARGEN) + MARGEN
    boton = 80
    alto = filas * (TAM_CELDA + MARGEN) + MARGEN + boton
    pantalla = pygame.display.set_mode((ancho, alto))  # Redimensionar la ventana
    pygame.display.set_caption("Visualización del Camino Mínimo")

    botonSiguiente = pygame.Rect((ancho//2) - 75, alto - 50, 150, 30)
    fuenteContador = pygame.font.Font(None, 20)

    # Dibujar el camino paso a paso
    for i in range(len(caminoMinimo)):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

        # Dibujar la matriz con el camino hasta el paso actual
        caminoActual = caminoMinimo[:i + 1]
        finalAlcanzado = (i == len(caminoMinimo)-1)
        dibujarMatriz(pantalla, matriz, set(caminoActual), caminoActual, inicio, final, finalAlcanzado)
        textoPasos = fuenteContador.render(f"Paso {i} de {len(caminoMinimo)-1}", True, (255, 255, 255))
        pantalla.blit(textoPasos, (10, alto - 70))  # Posición del texto en la parte inferior izquierda
        
        pygame.display.flip()
        pygame.time.delay(500)  # Controlar la velocidad de actualización

    # Mantener la ventana abierta hasta que el usuario cierre o presione una tecla
    while True:
        dibujarBoton(pantalla, botonSiguiente, "Siguiente matriz", COLOR_BOTON_HOVER, COLOR_TEXTO_BOTON)
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
    botonDFS = pygame.Rect(100, 80, 200, 50)
    botonUCS = pygame.Rect(100, 160, 200, 50)

    fuente = pygame.font.Font(None, 36)
    while True:
        pantalla.fill(COLOR_FONDO)

        # Dibujar botones
        pygame.draw.rect(pantalla, COLOR_BOTON_HOVER, botonDFS)
        pygame.draw.rect(pantalla, COLOR_BOTON_HOVER, botonUCS)

        textoDFS = fuente.render("DFS", True, COLOR_TEXTO_BOTON)
        textoUCS = fuente.render("UCS", True,COLOR_TEXTO_BOTON)

        pantalla.blit(textoDFS, (botonDFS.x + (botonDFS.width - textoDFS.get_width()) // 2,
                                  botonDFS.y + (botonDFS.height - textoDFS.get_height()) // 2))
        pantalla.blit(textoUCS, (botonUCS.x + (botonUCS.width - textoUCS.get_width()) // 2,
                                  botonUCS.y + (botonUCS.height - textoUCS.get_height()) // 2))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonDFS.collidepoint(evento.pos):
                    return "DFS"
                if botonUCS.collidepoint(evento.pos):
                    return "UCS"
                
def dibujarBoton(pantalla, boton, texto, colorFondo, colorTexto):
    pygame.draw.rect(pantalla, colorFondo, boton)
    fuente = pygame.font.Font(None, 24)
    textoBoton = fuente.render(texto, True, colorTexto)
    pantalla.blit(textoBoton, (boton.x + (boton.width - textoBoton.get_width()) // 2,
                                boton.y + (boton.height - textoBoton.get_height()) // 2))
    