import pygame  # Importa a biblioteca Pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
tela_largura, tela_altura = 800, 600
screen = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Desenhando Linhas com Pygame")

# Variável de controle do loop principal
rodando = True

# Lista para armazenar os pares de pontos dos cliques
linhas = []
ponto_atual = []

# Define as dimensões e posição do botão de limpar
botao_x, botao_y, botao_largura, botao_altura = 10, 10, 100, 40

# Define a cor do botão e do texto
cor_botao = (200, 0, 0)
cor_texto = (255, 255, 255)

# Inicializa a fonte do pygame
pygame.font.init()
fonte = pygame.font.Font(None, 30)
texto_botao = fonte.render("Limpar", True, cor_texto)

# Loop principal do jogo
while rodando:
    for evento in pygame.event.get():  # Captura eventos (teclado, mouse, fechamento da janela, etc.)
        if evento.type == pygame.QUIT:  # Se o usuário fechar a janela
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:  # Se o usuário clicar com o mouse
            x, y = evento.pos
            # Verifica se o clique foi dentro do botão
            if botao_x <= x <= botao_x + botao_largura and botao_y <= y <= botao_y + botao_altura:
                linhas.clear()  # Limpa todas as linhas desenhadas
            else:
                ponto_atual.append((x, y))  # Adiciona a posição do clique
                if len(ponto_atual) == 2:
                    linhas.append(tuple(ponto_atual))  # Armazena o par de pontos
                    ponto_atual.clear()  # Reseta para capturar um novo par de pontos

    # Preenche a tela com a cor preta
    screen.fill((0, 0, 0))

    # Desenha todas as linhas armazenadas
    for linha in linhas:
        pygame.draw.line(screen, (255, 255, 255), linha[0], linha[1], 2)  # Cor branca, espessura 2
    
    # Desenha o botão de limpar
    pygame.draw.rect(screen, cor_botao, (botao_x, botao_y, botao_largura, botao_altura))
    screen.blit(texto_botao, (botao_x + 20, botao_y + 10))
    
    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()