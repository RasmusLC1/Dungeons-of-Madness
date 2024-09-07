from scripts.entities.enemies.enemy import Enemy
from scripts.items.weapons.ranged_weapons.bow import Bow
from scripts.items.weapons.projectiles.spear import Spear

from scripts.engine.utility.helper_functions import Helper_Functions

import pygame
import random


class Decrepit_Bones_Ranged(Enemy):
    def __init__(self, game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina):
        super().__init__(game, pos, size, type, health, strength, max_speed, agility, intelligence, stamina)

        self.animation = 'decrepit_bones'
        self.shooting_distance = False
        self.Equip_Weapon()
        

    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement)
        self.Update_Left_Weapon()
        self.Weapon_Cooldown()
        # if self.distance_to_player < 20:
        #     self.Attack()

    




    def Equip_Weapon(self):
        weapon = None

        random_weapon = random.randint(0, 1)

        if random_weapon == 0:
            weapon = Bow(self.game, self.pos, (16,16))

        elif random_weapon == 1:
            weapon = Bow(self.game, self.pos, (16,16))

        

        if not weapon:
            return False

        if not weapon.Check_Inventory_Type('left_hand'):
            return False
        weapon.Pickup_Reset_Weapon(self)
        weapon.Set_Equip(True)
        self.Set_Active_Weapon(weapon)
        

        self.active_weapon.render = False
        del(weapon)
        return True
    
    def Update_Left_Weapon(self, offset=(0, 0)):
        if not self.active_weapon:
            return

        # Set the active and light to match the enemy itself
        self.active_weapon.Set_Active(self.active)
        self.active_weapon.Set_Light_Level(self.light_level)

        self.active_weapon.Set_Equipped_Position(self.direction_y_holder)
        self.active_weapon.Update(offset)
        if not self.active_weapon:
            return
        
        self.active_weapon.Update_Attack()


        return