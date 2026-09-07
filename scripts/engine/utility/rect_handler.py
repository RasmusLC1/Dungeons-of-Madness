import pygame

class Rect_Handler():
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def rect(self, pos):
        return pygame.Rect(pos[0] - self.size_x / 2, pos[1] - self.size_y / 2,
                           self.size_x, self.size_y)