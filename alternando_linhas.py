import pygame  # Importa a biblioteca Pygame

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
tela_largura, tela_altura = 800, 600
screen = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Modo Traçado e Linhas Independentes")

# Variável de controle do loop principal
rodando = True

# Lista para armazenar os pontos e linhas
pontos = []
linhas = []
tracos = []
ponto_anterior = None  # Armazena o ponto anterior para as linhas independentes

# Define as dimensões e posição do botão de limpar
botao_x, botao_y, botao_largura, botao_altura = 10, 10, 100, 40

# Define a cor do botão e do texto
cor_botao = (200, 0, 0)
cor_texto = (255, 255, 255)

# Inicializa a fonte do pygame
pygame.font.init()
fonte = pygame.font.Font(None, 30)
texto_botao = fonte.render("Limpar", True, cor_texto)

# Modo de desenho (True = Traçado contínuo, False = Linhas independentes)
modo_tracado = True

# Loop principal do jogo
while rodando:
    for evento in pygame.event.get():  # Captura eventos (teclado, mouse, fechamento da janela, etc.)
        if evento.type == pygame.QUIT:  # Se o usuário fechar a janela
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            
            # Verifica se o clique foi dentro do botão
            if botao_x <= x <= botao_x + botao_largura and botao_y <= y <= botao_y + botao_altura:
                pontos.clear()
                linhas.clear()
                tracos.clear()
                ponto_anterior = None
            elif evento.button == 1:  # Botão esquerdo do mouse
                if modo_tracado:
                    pontos.append((x, y))  # Armazena o ponto clicado para traçado contínuo
                    if len(pontos) > 1:
                        tracos.append((pontos[-2], pontos[-1]))  # Adiciona a linha ao traçado contínuo
                else:
                    if ponto_anterior is not None:
                        linhas.append((ponto_anterior, (x, y)))  # Cria uma linha independente
                    ponto_anterior = (x, y)  # Atualiza o ponto anterior para o próximo clique
            elif evento.button == 3:  # Botão direito do mouse
                modo_tracado = not modo_tracado  # Alterna o modo de desenho
                ponto_anterior = None  # Reinicia a referência ao ponto anterior

    # Preenche a tela com a cor preta
    screen.fill((0, 0, 0))

    # Desenha o traçado contínuo
    for traco in tracos:
        pygame.draw.line(screen, (255, 255, 255), traco[0], traco[1], 2)
    
    # Desenha as linhas independentes
    for linha in linhas:
        pygame.draw.line(screen, (255, 255, 255), linha[0], linha[1], 2)
    
    # Desenha o botão de limpar
    pygame.draw.rect(screen, cor_botao, (botao_x, botao_y, botao_largura, botao_altura))
    screen.blit(texto_botao, (botao_x + 20, botao_y + 10))
    
    # Exibe o modo atual na tela
    texto_modo = fonte.render("Modo: " + ("Traçado" if modo_tracado else "Linhas"), True, (0, 255, 0))
    screen.blit(texto_modo, (650, 10))
    
    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
