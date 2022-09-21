import sys

import pygame

def run_game():
    pygame.ini()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #Inicia o laço principal do jogo
    while True:
        #observa os eventos do teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Deixa a tela mais recente visivel
        pygame.display.flip()


run_game()