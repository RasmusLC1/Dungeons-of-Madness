import random
from ....engine.utility.cooldown_handler import Cooldown_Handler

class Base_Animation_Handler:
    def __init__(self, entity, animation_max, animation_cooldown_max):
        self.entity = entity
        self.animation_enabled = True
        self.sprite = None
        self.animation = 0
        self.min_animation = 0
        self.animation_max = int(animation_max)
        self._Set_Animation_Cooldown_Max(animation_cooldown_max)
        self.animation_cooldown_handler = Cooldown_Handler(self.animation_cooldown_max)

    @property
    def animation_cooldown(self):
        return self.animation_cooldown_handler.value

    @animation_cooldown.setter
    def animation_cooldown(self, new_cooldown):
        self.animation_cooldown_handler.value = new_cooldown


    def Save_Data(self):
        return {
            'animation': self.animation,
            'animation_cooldown': self.animation_cooldown_handler.Save_Data()
        }

    def Load_Data(self, data):
        self.animation = data['animation']
        self.animation_cooldown_handler.Load_Data(data['animation_cooldown'])

    def Set_Sprite(self, key):
        try:
            self.sprite = self.entity.game.assets[key]
        except Exception as e:
            print(f'Setting sprite failed: {e}', getattr(self.entity, 'type', None), key)
            return False
        self.Set_Entity_Image()
        return True

    def Set_Entity_Image(self):
        if not self.sprite:
            return
        try:
            self.entity.entity_image = self.sprite[self.animation].convert_alpha()
            self.entity.render_needs_update = True
        except Exception as e:
            print(f'Set entity image failed: {e}', getattr(self.entity, 'type', None), self.animation, self.sprite)

    def Set_Frame(self, value):
        value = max(self.min_animation, min(int(value), self.animation_max))
        self.animation = value
        self.Set_Entity_Image()

    def Increase_Frame(self):
        next_value = self.animation + 1
        if next_value > self.animation_max:
            next_value = self.min_animation
        self.Set_Frame(next_value)

    def Update_Animation(self, movement, delta_time):
        if not self.entity.render or not self.animation_enabled:
            return False
        if not self.animation_cooldown_handler.Update_Cooldown(delta_time):
            return False
        self.Increase_Frame()
        return True

    def Set_Random_Animation(self):
        if self.animation_max > 0:
            self.animation = random.randint(self.min_animation, self.animation_max)
        else:
            self.animation = 0

    def Set_Min_Animation(self, value):
        self.min_animation = value
        if self.animation < self.min_animation:
            self.animation = self.min_animation

    def Set_Static_Animation(self, value):
        self.aniamtion_cooldown = 0
        self.animation = value
        self.animation_enabled = False

    # Animation and cooldown will autoamtically be set to correct value with min and max animation
    def Enable_Animation(self):
        self.animation_enabled = True

    def _Set_Animation_Cooldown_Max(self, value):
        self.animation_cooldown_max = float(value)
        if self.animation_cooldown_max <= 0:
            self.animation_enabled = False