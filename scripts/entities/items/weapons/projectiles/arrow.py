from scripts.entities.items.weapons.projectiles.projectile import Projectile
import math
import pygame

class Arrow(Projectile):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 8, 10, 'arrow')
        self.max_animation = 0
        self.attack_animation_max = 0
        self.distance_from_player = 0
        
    

    def Set_Attack(self):
        super().Set_Attack()
        if self.attacking == 0 or self.range == 0 or self.attack_animation_time == 0:
            return
        self.attack_animation_time = int(self.attacking / self.range / self.attack_animation_time) 
    
    def Shoot(self):
        self.Initialise_Shooting(self.entity.strength)

        super().Shoot()

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        self.Drop_Weapon_After_Shot()

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.distance_from_player = 0
            self.rotate = 0
            return

        self.Stabbing_Attack_Handler()

    def Stabbing_Attack_Handler(self):
        # if not self.rotate:  
        self.Point_Towards_Mouse()
        self.Set_Attack_Direction()
        self.Stabbing_Attack()


    def Stabbing_Attack(self):
        if not self.return_to_holder:
            self.distance_from_player += 1
            left_offset = 0
            if self.attack_direction[0] < 0:
                left_offset = -3
            new_x_pos = self.pos[0] + self.distance_from_player * self.attack_direction[0] + left_offset
            new_y_pos = self.pos[1] + self.distance_from_player * self.attack_direction[1]
            self.Move((new_x_pos, new_y_pos))
            
            if self.distance_from_player <= self.range:
                return
            elif self.distance_from_player > self.range:
                self.return_to_holder = True
                return
        else:
            self.distance_from_player -= 1


            if self.distance_from_player <= 0:
                self.return_to_holder = False  
        

                
    def Set_Attack_Direction(self):
        super().Set_Attack_Direction()
        if self.attack_direction[0] > 0:
            self.rotate *= -1



    def Attack_Align_Weapon(self):
        left_offset = 0
        if self.attack_direction[0] < 0:
            left_offset = -5

        self.Move((self.pos[0] + left_offset, self.pos[1] + 2))
        return
    
        
    def Arrow_Inventory_Check(self, inventory_slot):
        if not 'arrow' in self.weapon_class:
            return True
        
        if not inventory_slot.inventory_type:
            return True
        if 'arrow' in inventory_slot.inventory_type:
            return True
        else:
            return False