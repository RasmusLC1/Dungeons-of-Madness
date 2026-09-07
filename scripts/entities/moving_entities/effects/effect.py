import pygame
import random
from scripts.engine.keys.keys import keys
from scripts.engine.utility.cooldown_handler import Cooldown_Handler

class Effect():
    def __init__(self, entity, effect_type, animation_max, animation_cooldown_max, cooldown_range, description):
        self.entity = entity
        self.effect_type = effect_type
        self.effect_cooldown_handler = Cooldown_Handler(0)  # actual value always set explicitly via Set_Cooldown
        self.animation_cooldown_handler = Cooldown_Handler(animation_cooldown_max)
        self.effect_max = 10
        self.permanent = False
        self.effect_strength = 0
        self.animation = 0
        self.animation_max = animation_max
        self.update_trigged = False
        self.cooldown_range = cooldown_range
        self.description = description
        self.saved_data = None

    def Save_Data(self):
        self.saved_data = {}
        self.saved_data['effect'] = self.effect_strength
        self.saved_data['cooldown'] = self.effect_cooldown_handler.Save_Data()
        self.saved_data['animation'] = self.animation
        self.saved_data['animation_cooldown'] = self.animation_cooldown_handler.Save_Data()
        self.saved_data['permanent'] = self.permanent
        return self.saved_data

    def Load_Data(self, data):
        self.effect_strength = data['effect']
        self.effect_cooldown_handler.Load_Data(data['cooldown'])
        self.animation = data['animation']
        self.animation_cooldown_handler.Load_Data(data['animation_cooldown'])
        self.permanent = data['permanent']

    def Set_Effect(self, effect_time, permanent=False):
        if self.effect_strength >= self.effect_max:
            return False

        if permanent:
            self.Set_Permanent(effect_time)

        self.effect_strength = min(effect_time + self.effect_strength, self.effect_max)
        self.Set_Cooldown()
        return True

    def Update_Effect(self, delta_time):
        if not self.effect_strength:
            return False

        self.Update_Cooldown(delta_time)
        return True

    def Remove_Effect(self, reduce_permanent=0):
        self.Set_Permanent(-reduce_permanent)
        if self.permanent > 0:
            self.effect_strength = max(0, self.effect_strength - reduce_permanent)
            return False
        self.effect_strength = 0
        self.animation = 0
        self.effect_cooldown_handler.Set_Cooldown(0)
        self.animation_cooldown_handler.Set_Cooldown(0)
        return True

    def Set_Permanent(self, amount):
        self.permanent += amount

    def Decrease_Effect(self):
        self.effect_strength = max(self.effect_strength - 1, 0)

    def Update_Cooldown(self, delta_time) -> bool:
        if not self.effect_cooldown_handler.Tick(delta_time):
            return False

        self.Set_Cooldown()
        if self.permanent >= self.effect_strength:
            return False
        self.effect_strength -= 1
        self.entity.Set_Description()
        return True

    def Set_Cooldown(self):
        self.update_trigged = True
        self.effect_cooldown_handler.Set_Cooldown(random.uniform(self.cooldown_range[0], self.cooldown_range[1]))

    def Effect_Animation_Cooldown(self, delta_time):
        if not self.animation_cooldown_handler.Update_Cooldown(delta_time):
            return

        if self.animation >= self.animation_max:
            self.animation = 0
        else:
            self.animation += 1

    def Damage_Dealt(self, damage):
        pass
    
    def Entity_Dead(self):
        pass

    def Damage_Taken(self, damage, attacker = None):
        pass

    def Push(self, direction):
        pass

    def Get_Entity_Effect_Strength(self, effect_name):
        return self.entity.Get_Effect_Strength(effect_name)
    
    def Get_Entity_Effect(self, effect_name):
        return self.entity.Get_Effect(effect_name)
    
    def Decrease_Other_Effect(self, effect_name, amount = None):
        return self.entity.Remove_Effect(effect_name, amount)


    def Render_Effect(self, surf, offset=(0, 0)):
        pass