from scripts.traps.trap import Trap

import random
import math
import pygame

class Lava(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = random.randint(0, 2)
        self.light_level = 10
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level)
        

    def Update(self, entity):
        if self.rect().colliderect(entity.rect()):
            self.Cooldown = 20
            if entity.invincible:
                return
            if entity.status_effects.wet:
                entity.Set_Effect('dry', 1)
            if not entity.Set_Effect('fire', 5):
                return
            entity.Set_Effect('slow', 4)
            entity.Damage_Taken(5)

    def Animation_Update(self):
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 2:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)