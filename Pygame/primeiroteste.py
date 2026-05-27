import pygame
import sys
import os

# Usar driver de vídeo que funciona sem display
os.environ['SDL_VIDEODRIVER'] = 'dummy'

try:
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

    # Criar a janela (dummy display para teste)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Teste Pygame")

    print("✓ Pygame inicializado com sucesso!")
    print(f"✓ Janela criada: {LARGURA}x{ALTURA}")

    # Relógio para controlar FPS
    relogio = pygame.time.Clock()

    # Loop principal - roda 60 iterações para teste
    print("✓ Iniciando loop de teste (60 frames)...")

    for frame in range(60):
        relogio.tick(60)  # 60 FPS

        # Processar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                break

        # Limpar tela
        tela.fill(PRETO)

        # Desenhar quadrado
        x = LARGURA // 2
        y = ALTURA // 2
        pygame.draw.rect(tela, AZUL, (x - 15, y - 15, 30, 30))

        # Desenhar alguns círculos
        pygame.draw.circle(tela, VERMELHO, (150, 150), 30)
        pygame.draw.circle(tela, VERDE, (LARGURA - 150, ALTURA - 150), 40)

        # Atualizar tela
        pygame.display.flip()

        if (frame + 1) % 20 == 0:
            print(f"  Frame {frame + 1}/60...")

    print("✓ Teste concluído com sucesso!")
    print("✓ Pygame está funcionando corretamente!")

except Exception as e:
    print(f"✗ Erro: {e}")
    import traceback
    traceback.print_exc()

finally:
    # Encerrar
    pygame.quit()
    sys.exit()
