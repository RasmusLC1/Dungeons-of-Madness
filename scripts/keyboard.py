import pygame

class Keyboard_Handler:
    def keyboard_Input(self, key_press):
        if key_press.type == pygame.KEYDOWN:
            if key_press.key == pygame.K_a:
                self.movement[0] = True
            if key_press.key == pygame.K_d:
                self.movement[1] = True
            if key_press.key == pygame.K_w:
                self.movement[2] = True
            if key_press.key == pygame.K_s:
                self.movement[3] = True
            if key_press.key == pygame.K_SPACE:
                self.player.Dash()
            if key_press.key == pygame.K_x:
                pass
        if key_press.type == pygame.KEYUP:
            if key_press.key == pygame.K_a:
                self.movement[0] = False
            if key_press.key == pygame.K_d:
                self.movement[1] = False
            if key_press.key == pygame.K_w:
                self.movement[2] = False
            if key_press.key == pygame.K_s:
                self.movement[3] = False