from scripts.traps.trap import Trap
from scripts.items.weapons.projectiles.projectile import Projectile
import random
import math
import pygame


class Spider_Web_Projectile(Projectile):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, special_attack, direction, entity):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class)
        self.special_attack = special_attack / 4
        self.entity = entity
        self.direction = direction  # Store the direction vector
        self.target_hit = 0
        self.attack_animation_max = 3
        self.attack_animation_time = range // self.attack_animation_max



    def Shoot(self):
        if self.target_hit:
            self.target_hit -= 1
            if not self.target_hit:
                self.Set_Special_Attack(0)
            return

        if (self.special_attack <= 0 or not self.range):
            self.game.item_handler.Remove_Item(self, True)
            return

        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)

        # Move the projectile using the stored direction
        self.pos = (
            self.pos[0] + self.direction[0] * self.shoot_speed,
            self.pos[1] + self.direction[1] * self.shoot_speed
        )

        # Custom collision detection
        entity = self.Attack_Collision_Check()
        if entity:
            entity.Set_Effect('Snare', 100)
            self.animation = self.attack_animation_max
            self.pos = entity.pos
            self.target_hit = 100
            return

        self.range = max(0, self.range - 1)
        
