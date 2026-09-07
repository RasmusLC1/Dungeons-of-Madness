from scripts.entities.entity.entities import PhysicsEntity
from scripts.engine.keys.keys import keys
from scripts.engine.utility.cooldown_handler import Cooldown_Handler

import math
import pygame
import random

DAMAGE_COOLDOWN = 1

class Trap(PhysicsEntity):
    def __init__(self, game, pos, type, size = (32, 32), max_animation = 0,
                 animation_cooldown_max = 0):
        super().__init__(game, type, 'trap', pos, size,
                            max_animation=max_animation,
                            animation_cooldown_max=animation_cooldown_max)
        self.cooldown = 0
        self.Set_Sprite()
        self.entity_check_cooldown = 0
        self.entities = {}
        if self.tile:
            self.tile.Set_Trap(self)
        self.damaged_entities = {}
        self.entity_cooldown_handler = Cooldown_Handler(0.05)



    def Save_Data(self):
        super().Save_Data()
        self.saved_data['Cooldown'] = self.cooldown

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.cooldown = data['Cooldown']

    def Update(self, delta_time):
        if not self.render:
            return False
        super().Update(delta_time)
        self.Update_Damage_Cooldown(delta_time)
        if not self.Update_Cooldown(delta_time):
            return False
        self.Update_Trapped_Entities()
        return True

    def Add_Entity(self, entity):
        # 1. Early exit: Ignore items
        if entity.category == keys.item:
            return False
    
        # 2. Early exit: Already tracked (O(1) dictionary lookup)
        if entity.ID in self.entities:
            return False
        
        # 3. Early exit: Geometric check (call rect() once and cache it)
        if not self.rect().colliderect(entity.rect()):
            return False
        
        # Add to trap tracking
        self.entities[entity.ID] = entity
        return True

    def Remove_Entity(self, entity_ID):
        return self.entities.pop(entity_ID, None) is not None

    def Update_Cooldown(self, delta_time):
        return self.entity_cooldown_handler.Update_Cooldown(delta_time)
    
    # Handle cooldown of entities in the trap seperately to ensure fast trigger on trap
    # but controlled damage
    def Update_Damage_Cooldown(self, delta_time):
        expired = [entity_id for entity_id, handler in self.damaged_entities.items()
                if handler.Tick(delta_time)]
        for entity_id in expired:
            self.damaged_entities.pop(entity_id)

    def Update_Trapped_Entities(self):
        for entity in self.entities.values():
            if not entity.touching_ground:
                continue
            if entity.ID in self.damaged_entities:
                continue
            if entity.ID == self.ID:
                continue
            if not self.rect().colliderect(entity.rect()):
                continue
            self.Apply_Entity_Effect(entity)
            self.damaged_entities[entity.ID] = Cooldown_Handler(DAMAGE_COOLDOWN, DAMAGE_COOLDOWN)


    def Apply_Entity_Effect(self, entity):
        pass

    def Animation_Update(self, delta_time):
        pass


    def Set_Active(self, duration):
        self.active = duration

    def Reduce_Active(self):
        self.active -= 1

