import pygame
import numpy as np
import time

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

bg = (25, 25, 25)
screen.fill(bg)

nxC, nyC = 25, 25
dimCW = width / nxC
dimCH = height / nyC

# Estado inicial de las celdas (matriz de ceros)
gameState = np.zeros((nxC, nyC))

# Configuración de patrones iniciales
gameState[5, 3:62] = 1  # Automata palo
gameState[21, 21:24] = 1  # Automata móvil
gameState[22, 22:24] = 1
gameState[21, 23:18] = 1
gameState[20, 21:53] = 1
gameState[21,21:81] = 1
gameState[22,22:25] = 1
gameState[21,23:17] = 1
gameState[22,23:36] = 1
gameState[20,21:50] = 1

while True:
    newGameState = np.copy(gameState)

    screen.fill(bg)

    # Iterar sobre cada celda en la matriz
    for y in range(nyC):
        for x in range(nxC):
            # Calcular el número de vecinos vivos (considerando el entorno toroidal)
            n_neigh = (
                gameState[(x - 1) % nxC, (y - 1) % nyC]
                + gameState[(x) % nxC, (y - 1) % nyC]
                + gameState[(x + 1) % nxC, (y - 1) % nyC]
                + gameState[(x - 1) % nxC, (y) % nyC]
                + gameState[(x + 1) % nxC, (y) % nyC]
                + gameState[(x - 1) % nxC, (y + 1) % nyC]
                + gameState[(x) % nxC, (y + 1) % nyC]
                + gameState[(x + 1) % nxC, (y + 1) % nyC]
            )

            # Aplicar reglas del Juego de la vida
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Dibujar celda en la pantalla
            poly = [
                (x * dimCW, y * dimCH),
                ((x + 1) * dimCW, y * dimCH),
                ((x + 1) * dimCW, (y + 1) * dimCH),
                (x * dimCW, (y + 1) * dimCH),
            ]
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    # Actualizar el estado del juego
    gameState = np.copy(newGameState)

    # Actualizar la pantalla
    pygame.display.flip()

    # Añadir un retardo para controlar la velocidad de la simulación
    time.sleep(0.1)

    # Manejar eventos de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
