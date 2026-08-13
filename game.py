"import"+pygame"
import sys

pygame.init()

WIDTH, HEIGHT = 800, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Android Demo")
clock = pygame.time.Clock()

player = pygame.Rect(100, 190, 60, 60)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 6
    if keys[pygame.K_RIGHT]:
        player.x += 6
    if keys[pygame.K_UP]:
        player.y -= 6
    if keys[pygame.K_DOWN]:
        player.y += 6

    player.clamp_ip(screen.get_rect())

    screen.fill((8, 12, 30))

    pygame.draw.rect(
        screen,
        (0, 220, 255),
        player,
        border_radius=12
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
