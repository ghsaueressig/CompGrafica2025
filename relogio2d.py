import pygame
import time
import math

# Configuração inicial
pygame.init()
LARGURA, ALTURA = 500, 500
CENTRO = (LARGURA // 2, ALTURA // 2)
RAIO = 200

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Criar tela
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Relógio Analógico")

# Função para desenhar ponteiros
def desenhar_ponteiro(angulo, comprimento, cor):
    x = CENTRO[0] + comprimento * math.cos(math.radians(angulo))
    y = CENTRO[1] - comprimento * math.sin(math.radians(angulo))
    pygame.draw.line(screen, cor, CENTRO, (x, y), 4)

# Loop principal
rodando = True
while rodando:
    screen.fill(BRANCO)
    pygame.draw.circle(screen, PRETO, CENTRO, RAIO, 3)
    
    # Obter tempo atual
    tempo = time.localtime()
    segundos = tempo.tm_sec
    minutos = tempo.tm_min
    horas = tempo.tm_hour % 12
    
    # Calcular ângulos
    angulo_seg = 90 - (segundos * 6)
    angulo_min = 90 - (minutos * 6)
    angulo_hora = 90 - (horas * 30 + minutos * 0.5)
    
    # Desenhar ponteiros
    desenhar_ponteiro(angulo_hora, RAIO * 0.5, VERDE)
    desenhar_ponteiro(angulo_min, RAIO * 0.7, AZUL)
    desenhar_ponteiro(angulo_seg, RAIO * 0.9, VERMELHO)
    
    # Atualizar tela
    pygame.display.flip()
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    time.sleep(1)
    
pygame.quit()
