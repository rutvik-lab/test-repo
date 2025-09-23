import pygame
import sys
import random

# --- setup ---
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- colors ---
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)

# --- bird setup ---
bird_x, bird_y = 50, HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# --- pipes ---
pipe_width = 60
pipe_gap = 150
pipes = []
pipe_timer = 0
pipe_interval = 1500  # ms

# --- score ---
score = 0
game_over = False

def draw_bird():
    pygame.draw.circle(screen, YELLOW, (bird_x, int(bird_y)), bird_radius)

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe["top"])
        pygame.draw.rect(screen, GREEN, pipe["bottom"])

def random_pipe():
    gap_y = random.randint(100, HEIGHT - 200)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, gap_y)
    bottom_rect = pygame.Rect(WIDTH, gap_y + pipe_gap, pipe_width, HEIGHT)
    return {"top": top_rect, "bottom": bottom_rect}

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# --- game loop ---
while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # reset
            bird_y = HEIGHT // 2
            bird_velocity = 0
            pipes.clear()
            score = 0
            game_over = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = jump_strength

    if not game_over:
        # physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # spawn pipes
        pipe_timer += dt
        if pipe_timer > pipe_interval:
            pipes.append(random_pipe())
            pipe_timer = 0

        # move pipes
        for pipe in pipes:
            pipe["top"].x -= 3
            pipe["bottom"].x -= 3

        # remove off-screen pipes
        pipes = [p for p in pipes if p["top"].right > 0]

        # collision detection
        for pipe in pipes:
            if (pipe["top"].collidepoint(bird_x, bird_y) or
                pipe["bottom"].collidepoint(bird_x, bird_y)):
                game_over = True
        if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
            game_over = True

        # scoring
        for pipe in pipes:
            if pipe["top"].right == bird_x:
                score += 1

    # --- draw everything ---
    screen.fill(BLUE)
    draw_bird()
    draw_pipes()
    draw_text(f"Score: {score}", 10, 10)

    if game_over:
        draw_text("GAME OVER — Press R to restart", 40, HEIGHT//2)

    pygame.display.flip()
