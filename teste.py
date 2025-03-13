import pygame                                               # Importa a biblioteca Pygame

pygame.init()                                                   # Inicializa todos os módulos do Pygame
screen = pygame.display.set_mode((800, 600)) # Cria a janela do jogo com largura 800px e altura 600px
pygame.display.set_caption("Teste Pygame")     # Define o título da janela

rodando = True                                              # Variável de controle do loop principal

# Loop principal do jogo
while rodando:
    for evento in pygame.event.get():                 # Captura eventos (teclado, mouse, fechamento da janela, etc.)
        if evento.type == pygame.QUIT:             # Verifica se o evento é o fechamento da janela
            rodando = False                                # Sai do loop principal

    screen.fill((0, 0, 0))                                     # Preenche a tela com a cor preta (RGB: 0, 0, 0)  
    pygame.display.flip()                                  # Atualiza a tela com as alterações feitas

pygame.quit()                                                # Encerra o Pygame e libera recursos do sistema
