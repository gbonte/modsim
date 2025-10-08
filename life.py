import tkinter as tk
import random

# Grid size
ROWS = 50
COLS = 50
CELL_SIZE =15 
DELAY = 100  # milliseconds

class GameOfLife:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='white')
        self.canvas.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack()

        self.start_btn = tk.Button(self.btn_frame, text="Start", command=self.start)
        self.start_btn.pack(side=tk.LEFT)

        self.stop_btn = tk.Button(self.btn_frame, text="Stop", command=self.stop)
        self.stop_btn.pack(side=tk.LEFT)

        self.random_btn = tk.Button(self.btn_frame, text="Randomize", command=self.randomize)
        self.random_btn.pack(side=tk.LEFT)

        self.clear_btn = tk.Button(self.btn_frame, text="Clear", command=self.clear)
        self.clear_btn.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(ROWS):
            for j in range(COLS):
                color = "black" if self.grid[i][j] else "white"
                self.canvas.create_rectangle(
                    j*CELL_SIZE, i*CELL_SIZE,
                    (j+1)*CELL_SIZE, (i+1)*CELL_SIZE,
                    fill=color, outline="gray"
                )

    def toggle_cell(self, event):
        row = event.y // CELL_SIZE
        col = event.x // CELL_SIZE
        self.grid[row][col] = 1 - self.grid[row][col]
        self.draw_grid()

    def randomize(self):
        self.grid = [[random.randint(0, 1) for _ in range(COLS)] for _ in range(ROWS)]
        self.draw_grid()

    def clear(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.draw_grid()

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def update(self):
        if not self.running:
            return
        new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                live_neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:
                    new_grid[i][j] = 1 if live_neighbors in [2, 3] else 0
                else:
                    new_grid[i][j] = 1 if live_neighbors == 3 else 0
        self.grid = new_grid
        self.draw_grid()
        self.root.after(DELAY, self.update)

    def count_neighbors(self, row, col):
        count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if (i == row and j == col) or i < 0 or j < 0 or i >= ROWS or j >= COLS:
                    continue
                count += self.grid[i][j]
        return count
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Game of Life - macOS")
    game = GameOfLife(root)
    root.mainloop()
import tkinter as tk
import random

# Grid size
ROWS = 100
COLS = 100
CELL_SIZE = 10
DELAY = 100  # milliseconds

class GameOfLife:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='white')
        self.canvas.pack()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack()

        self.start_btn = tk.Button(self.btn_frame, text="Start", command=self.start)
        self.start_btn.pack(side=tk.LEFT)

        self.stop_btn = tk.Button(self.btn_frame, text="Stop", command=self.stop)
        self.stop_btn.pack(side=tk.LEFT)

        self.random_btn = tk.Button(self.btn_frame, text="Randomize", command=self.randomize)
        self.random_btn.pack(side=tk.LEFT)

        self.clear_btn = tk.Button(self.btn_frame, text="Clear", command=self.clear)
        self.clear_btn.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.draw_grid()

    def draw_grid(self):
       import pygame
import numpy as np

# Configuration
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (40, 40, 40)
BUTTON_COLOR = (70, 130, 180)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Initialize grid
grid = np.zeros((ROWS, COLS), dtype=int)

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            total = int(np.sum(grid[max(i-1,0):min(i+2,ROWS), max(j-1,0):min(j+2,COLS)]) - grid[i, j])
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def draw_grid(win, grid):
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, GRID_COLOR, rect, 1)

def draw_button(win, rect, text):
    pygame.draw.rect(win, BUTTON_COLOR, rect)
    font = pygame.font.SysFont(None, 24)
    text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    win.blit(text_surf, text_rect)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT + 50))
    pygame.display.set_caption("Game of Life with Buttons")
    clock = pygame.time.Clock()

    global grid
    running = False

    # Define buttons
    start_stop_btn = pygame.Rect(50, HEIGHT + 10, 100, 30)
    step_btn = pygame.Rect(200, HEIGHT + 10, 100, 30)
    reset_btn = pygame.Rect(350, HEIGHT + 10, 100, 30)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < HEIGHT:
                    i, j = y // CELL_SIZE, x // CELL_SIZE
                    grid[i, j] = 1 - grid[i, j]
                elif start_stop_btn.collidepoint(x, y):
                    running = not running
                elif step_btn.collidepoint(x, y):
                    grid = update_grid(grid)
                elif reset_btn.collidepoint(x, y):
                    grid = np.zeros((ROWS, COLS), dtype=int)

        if running:
            grid = update_grid(grid)

        win.fill(BLACK)
        draw_grid(win, grid)
        draw_button(win, start_stop_btn, "Start" if not running else "Stop")
        draw_button(win, step_btn, "Step")
        draw_button(win, reset_btn, "Reset")
        pygame.display.flip()

if __name__ == "__main__":
    main()
import pygame
import numpy as np

# Configuration
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 100, 100
CELL_SIZE = WIDTH // COLS
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (40, 40, 40)
BUTTON_COLOR = (70, 130, 180)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Initialize grid
grid = np.zeros((ROWS, COLS), dtype=int)

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            total = int(np.sum(grid[max(i-1,0):min(i+2,ROWS), max(j-1,0):min(j+2,COLS)]) - grid[i, j])
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def draw_grid(win, grid):
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, GRID_COLOR, rect, 1)

def draw_button(win, rect, text):
    pygame.draw.rect(win, BUTTON_COLOR, rect)
    font = pygame.font.SysFont(None, 24)
    text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    win.blit(text_surf, text_rect)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT + 50))
    pygame.display.set_caption("Game of Life with Buttons")
    clock = pygame.time.Clock()

    global grid
    running = False

    # Define buttons
    start_stop_btn = pygame.Rect(50, HEIGHT + 10, 100, 30)
    step_btn = pygame.Rect(200, HEIGHT + 10, 100, 30)
    reset_btn = pygame.Rect(350, HEIGHT + 10, 100, 30)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y < HEIGHT:
                    i, j = y // CELL_SIZE, x // CELL_SIZE
                    grid[i, j] = 1 - grid[i, j]
                elif start_stop_btn.collidepoint(x, y):
                    running = not running
                elif step_btn.collidepoint(x, y):
                    grid = update_grid(grid)
                elif reset_btn.collidepoint(x, y):
                    grid = np.zeros((ROWS, COLS), dtype=int)

        if running:
            grid = update_grid(grid)

        win.fill(BLACK)
        draw_grid(win, grid)
        draw_button(win, start_stop_btn, "Start" if not running else "Stop")
        draw_button(win, step_btn, "Step")
        draw_button(win, reset_btn, "Reset")
        pygame.display.flip()

if __name__ == "__main__":
    main()
import pygame
import numpy as np

# Configuration
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 50, 50
CELL_SIZE = WIDTH // COLS
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (40, 40, 40)

# Initialize grid
grid = np.zeros((ROWS, COLS), dtype=int)

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            total = int(np.sum(grid[max(i-1,0):min(i+2,ROWS), max(j-1,0):min(j+2,COLS)]) - grid[i, j])
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

def draw_grid(win, grid):
    win.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if grid[i, j] == 1 else BLACK
            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, GRID_COLOR, rect, 1)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()

    running = False
    global grid

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_c:
                    grid = np.zeros((ROWS, COLS), dtype=int)

            elif pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                i, j = y // CELL_SIZE, x // CELL_SIZE
                grid[i, j] = 1

            elif pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                i, j = y // CELL_SIZE, x // CELL_SIZE
                grid[i, j] = 0

        if running:
            grid = update_grid(grid)

        draw_grid(win, grid)
        pygame.display.flip()

if __name__ == "__main__":
    main()
