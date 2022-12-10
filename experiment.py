import random
import pygame
from Board import Board


class Sapper(Board):
    def __init__(self, width, height, n):
        super().__init__(width, height)
        self.board = [[-1] * width for i in range(height)]
        i = 0
        while i < n:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == -1:
                self.board[y][x] = 10
                i += 1

    def on_click(self, cell):
        self.open_cell(cell)

    def open_cell(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            return
        s = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
                    continue
                if self.board[new_y][new_x] == 10:
                    s += 1
        self.board[y][x] = s

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.Color("red"), (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                     self.cell_size, self.cell_size))
                if 0 <= self.board[y][x] < 10:
                    font = pygame.font.Font(None, self.cell_size - 6)
                    text = font.render(str(self.board[y][x]), 1, (100, 255, 100))
                    screen.blit(text, (x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3))

                pygame.draw.rect(screen, pygame.Color("white"),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)


def main():
    pygame.init()
    size = 470, 470
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    board = Sapper(10, 10, 10)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == '__main__':
    main()
