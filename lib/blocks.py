import pygame
from pygame.locals import *
from random import randint


def create_grid(width, height, colors):
    column = lambda: [colors['blue']() for _ in range(width)]
    rows = [column() for _ in range(height)]
    return rows


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.width = 3
        self.height = 3
        self.scale = 100
        self.win_width = self.width * self.scale
        self.win_height = self.height * self.scale
        self.size = self.win_width, self.win_height
        rand_color = lambda: randint(0, 255)
        self.grid = create_grid(self.width, self.height, {'blue': lambda: (rand_color(), rand_color(), 255)})

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        scale_for_box = lambda x: int(self.scale / len(x))
        width = scale_for_box(self.grid[0])
        height = scale_for_box(self.grid)
        for i, row in enumerate(self.grid):
            for j, color in enumerate(row):
                x = j * self.scale 
                y = i * self.scale
                pygame.draw.rect(self._display_surf, color, pygame.Rect(x, y, self.scale, self.scale))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
