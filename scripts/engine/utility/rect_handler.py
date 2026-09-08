import pygame

class Rect_Handler():
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

    def rect(self, pos):
        pos_x, pos_y = self.Calculate_Rect_Pos(pos)
        return pygame.Rect(pos_x, pos_y, self.size_x, self.size_y)

    def Calculate_Rect_Pos(self, pos):
        pos_x = pos[0] - self.size_x / 2
        pos_y = pos[1] - self.size_y / 2
        return pos_x, pos_y