from scripts.entities.moving_entities.effects.effect import Effect
from scripts.engine.keys.keys import keys
import random
from scripts.engine.utility.cooldown_handler import Cooldown_Handler
from ..registry import register_effect

@register_effect(keys.electric)
class Electric(Effect):
    def __init__(self, entity):
        description = 'Damage and snare,\nspreads to nearby\nenemy, increased\nby wet'
        super().__init__(entity, keys.electric, 5, 0.2, (1, 1.5), description)
        self.snare_cooldown_handler = Cooldown_Handler()

    def Set_Effect(self, effect_time, permanent=False):
        if self.Get_Entity_Effect_Strength(keys.electric_resistance):
            return False

        if self.Get_Entity_Effect_Strength(keys.wet):
            effect_time *= 2

        self.entity.Damage_Taken(effect_time, (self.effect_type, 0))
        return super().Set_Effect(effect_time, permanent)

    def Update_Effect(self, delta_time):
        if not self.effect_strength:
            return False

        if self.Get_Entity_Effect_Strength(keys.electric_resistance):
            self.Remove_Effect()
            return False

        if self.Update_Cooldown(delta_time):
            damage = 1
            self.entity.Damage_Taken(damage, (self.effect_type, 0))

        self.Effect_Animation_Cooldown(delta_time)
        if not self.snare_cooldown_handler.Tick(delta_time):
            self.entity.frame_movement = (0, 0)

        return True

    def Update_Cooldown(self, delta_time):
        cooldown_state = super().Update_Cooldown(delta_time)
        if cooldown_state:
            if random.randint(1, 4) == 4:
                self.snare_cooldown_handler.Set_Cooldown(self.effect_strength / 10)

        return cooldown_state