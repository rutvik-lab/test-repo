# dodge.py
import pygame
import random
import sys

# --- config ---
WIDTH, HEIGHT = 640, 480
FPS = 60
PLAYER_SIZE = 40
PLAYER_SPEED = 6
BLOCK_SIZE = 30
BLOCK_SPEED_MIN, BLOCK_SPEED_MAX = 3, 7
SPAWN_INTERVAL_MS = 700  # spawn a new block every 700 ms

# --- init ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- game objects ---
player_rect = pygame.Rect((WIDTH//2 - PLAYER_SIZE//2, HEIGHT - PLAYER_SIZE - 10),
                          (PLAYER_SIZE, PLAYER_SIZE))

blocks = []
last_spawn_time = 0
score = 0
game_over = False

# --- helper functions ---
def spawn_block():
    x = random.randint(0, WIDTH - BLOCK_SIZE)
    speed = random.randint(BLOCK_SPEED_MIN, BLOCK_SPEED_MAX)
    rect = pygame.Rect(x, -BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    return {"rect": rect, "speed": speed}

def draw_text(surf, text, x, y):
    img = font.render(text, True, (255, 255, 255))
    surf.blit(img, (x, y))

# --- main loop ---
while True:
    dt = clock.tick(FPS)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # reset
            blocks.clear()
            player_rect.x = WIDTH//2 - PLAYER_SIZE//2
            score = 0
            game_over = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_rect.x += PLAYER_SPEED

    # keep player on screen
    player_rect.x = max(0, min(WIDTH - PLAYER_SIZE, player_rect.x))

    # spawn blocks
    if not game_over and now - last_spawn_time > SPAWN_INTERVAL_MS:
        blocks.append(spawn_block())
        last_spawn_time = now

    # update blocks
    if not game_over:
        for b in blocks[:]:
            b["rect"].y += b["speed"]
            if b["rect"].top > HEIGHT:
                blocks.remove(b)
                score += 1  # survived one block

    # collision?
    for b in blocks:
        if player_rect.colliderect(b["rect"]):
            game_over = True
            break

    # draw
    screen.fill((30, 30, 40))  # background
    # draw player
    pygame.draw.rect(screen, (80, 200, 120), player_rect)
    # draw blocks
    for b in blocks:
        pygame.draw.rect(screen, (200, 80, 80), b["rect"])
    # hud
    draw_text(screen, f"Score: {score}", 10, 10)

    if game_over:
        draw_text(screen, "GAME OVER — Press R to restart", WIDTH//7, HEIGHT//2)

    pygame.display.flip()
