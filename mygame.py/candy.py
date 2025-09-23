import pygame
import random
import sys

# --- setup ---
pygame.init()
WIDTH, HEIGHT = 480, 480
ROWS, COLS = 8, 8
CELL = WIDTH // COLS
COLORS = [
    (255, 0, 0),    # red
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (255, 255, 0),  # yellow
    (255, 0, 255),  # magenta
    (0, 255, 255),  # cyan
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy Crush Mini")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# --- grid ---
grid = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]
selected = None
score = 0

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            color = grid[r][c]
            rect = pygame.Rect(c*CELL, r*CELL, CELL, CELL)
            pygame.draw.rect(screen, color, rect.inflate(-4, -4))
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

def swap(a, b):
    r1, c1 = a
    r2, c2 = b
    grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

def find_matches():
    matched = set()
    # horizontal
    for r in range(ROWS):
        for c in range(COLS-2):
            if grid[r][c] == grid[r][c+1] == grid[r][c+2]:
                matched.update([(r, c), (r, c+1), (r, c+2)])
    # vertical
    for c in range(COLS):
        for r in range(ROWS-2):
            if grid[r][c] == grid[r+1][c] == grid[r+2][c]:
                matched.update([(r, c), (r+1, c), (r+2, c)])
    return matched

def collapse(matched):
    global score
    for r, c in matched:
        grid[r][c] = None
        score += 10
    # drop candies
    for c in range(COLS):
        empty = [r for r in range(ROWS) if grid[r][c] is None]
        if empty:
            for r in reversed(range(ROWS)):
                if grid[r][c] is not None:
                    drop_to = max([e for e in empty if e > r], default=None)
                    if drop_to is not None:
                        grid[drop_to][c], grid[r][c] = grid[r][c], None
                        empty.remove(drop_to)
            # refill top
            for r in range(ROWS):
                if grid[r][c] is None:
                    grid[r][c] = random.choice(COLORS)

# --- main loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            r, c = my // CELL, mx // CELL
            if selected is None:
                selected = (r, c)
            else:
                if abs(selected[0]-r) + abs(selected[1]-c) == 1:
                    swap(selected, (r, c))
                    matched = find_matches()
                    if matched:
                        collapse(matched)
                    else:
                        swap(selected, (r, c))  # undo swap if no match
                selected = None

    # auto clear new matches
    matched = find_matches()
    if matched:
        collapse(matched)

    # --- draw ---
    screen.fill((30, 30, 30))
    draw_grid()
    img = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(img, (10, 10))
    pygame.display.flip()
    clock.tick(30)
