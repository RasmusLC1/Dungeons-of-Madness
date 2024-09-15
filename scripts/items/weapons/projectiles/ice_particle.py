from scripts.items.weapons.projectiles.projectile import Projectile
import pygame

class Ice_Particle(Projectile):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, special_attack, direction, entity):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class)
        self.special_attack = special_attack / 4
        self.entity = entity
        self.direction = direction  # Store the direction vector
        self.attack_animation_max = 3
        self.attack_animation_time = range // self.attack_animation_max

    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)

        # Use the stored direction to move the particle
        self.pos = (
            self.pos[0] + self.direction[0] * self.shoot_speed,
            self.pos[1] + self.direction[1] * self.shoot_speed
        )

        entity = super().Shoot()
        if entity:
            self.Set_Special_Attack(0)
            entity.Set_Effect('Freeze', 3)

        self.range = max(0, self.range - 1)
        if self.special_attack <= 0 or not self.range:
            self.game.item_handler.Remove_Item(self, True)
        
        

    
    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):

        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
