import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar dimensões da tela
LARGURA = 800
ALTURA = 600

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Criar a janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Teste Pygame")

# Relógio para controlar FPS
relogio = pygame.time.Clock()

# Loop principal
executando = True
x = LARGURA // 2
y = ALTURA // 2

while executando:
    relogio.tick(60)  # 60 FPS

    # Processar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Capturar teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= 5
    if teclas[pygame.K_RIGHT]:
        x += 5
    if teclas[pygame.K_UP]:
        y -= 5
    if teclas[pygame.K_DOWN]:
        y += 5

    # Limpar tela
    tela.fill(PRETO)

    # Desenhar quadrado (você)
    pygame.draw.rect(tela, AZUL, (x - 15, y - 15, 30, 30))

    # Desenhar alguns círculos
    pygame.draw.circle(tela, VERMELHO, (150, 150), 30)
    pygame.draw.circle(tela, VERDE, (LARGURA - 150, ALTURA - 150), 40)

    # Atualizar tela
    pygame.display.flip()

# Encerrar
pygame.quit()
sys.exit()
