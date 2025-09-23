import pygame
import sys
import random

# --- setup ---
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- colors ---
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# --- snake setup ---
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL, 0)
food = (200, 200)
score = 0
game_over = False

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, (x, y, CELL, CELL))

def draw_food(x, y):
    pygame.draw.rect(screen, RED, (x, y, CELL, CELL))

def random_food():
    return (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# --- game loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            snake = [(100, 100), (80, 100), (60, 100)]
            direction = (CELL, 0)
            food = random_food()
            score = 0
            game_over = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            if event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            if event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            if event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    if not game_over:
        # move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # check collision with food
        if snake[0] == food:
            score += 1
            food = random_food()
        else:
            snake.pop()  # remove tail

        # check collision with walls or self
        x, y = snake[0]
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or snake[0] in snake[1:]):
            game_over = True

    # --- draw everything ---
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food[0], food[1])
    draw_text(f"Score: {score}", 10, 10)

    if game_over:
        draw_text("GAME OVER — Press R to restart", WIDTH//6, HEIGHT//2)

    pygame.display.flip()
    clock.tick(7)  # control speed (10 frames per second)
